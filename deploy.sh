#!/bin/bash

# Claude Toolkit Deployment Script
# Manages copying toolkit components to project directories

set -e

TOOLKIT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECTS_FILE="$TOOLKIT_ROOT/projects.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_color() {
    color=$1
    message=$2
    echo -e "${color}${message}${NC}"
}

# Function to show usage
show_usage() {
    echo "Claude Toolkit Deployment Script"
    echo ""
    echo "Usage:"
    echo "  ./deploy.sh add-project <name> <path>     Add a new project to the index"
    echo "  ./deploy.sh deploy <project> <component>  Deploy a component to a project"
    echo "  ./deploy.sh deploy-all <project>          Deploy all components to a project"
    echo "  ./deploy.sh list                          List all registered projects"
    echo "  ./deploy.sh status <project>              Show deployment status for a project"
    echo ""
    echo "Components:"
    echo "  agent:<name>     Deploy specific agent"
    echo "  command:<path>   Deploy specific command (e.g., command:paz/prime/web_dev)"
    echo "  template:<path>  Deploy specific template (e.g., template:paz/acb/typescript)"
    echo "  all-agents       Deploy all agents"
    echo "  all-commands     Deploy all commands"
    echo "  all-templates    Deploy all templates"
    echo ""
    echo "Examples:"
    echo "  ./deploy.sh add-project my-app ~/projects/my-app"
    echo "  ./deploy.sh deploy my-app agent:quality-control-enforcer"
    echo "  ./deploy.sh deploy my-app template:paz/acb/typescript"
    echo "  ./deploy.sh deploy-all my-app"
}

# Function to add a project
add_project() {
    name=$1
    path=$2

    if [ -z "$name" ] || [ -z "$path" ]; then
        print_color "$RED" "Error: Project name and path required"
        exit 1
    fi

    # Expand path to absolute
    path=$(cd "$path" 2>/dev/null && pwd) || {
        print_color "$RED" "Error: Path $path does not exist"
        exit 1
    }

    # Check if project already exists
    if jq -e ".projects[] | select(.name == \"$name\")" "$PROJECTS_FILE" > /dev/null; then
        print_color "$YELLOW" "Project $name already exists. Updating path..."
        # Update existing project
        jq ".projects |= map(if .name == \"$name\" then .path = \"$path\" else . end)" "$PROJECTS_FILE" > "$PROJECTS_FILE.tmp"
        mv "$PROJECTS_FILE.tmp" "$PROJECTS_FILE"
    else
        # Add new project
        jq ".projects += [{
            \"name\": \"$name\",
            \"path\": \"$path\",
            \"claudeDir\": \".claude\"
        }]" "$PROJECTS_FILE" > "$PROJECTS_FILE.tmp"
        mv "$PROJECTS_FILE.tmp" "$PROJECTS_FILE"
    fi

    print_color "$GREEN" "✓ Added project: $name at $path"
}

# Function to deploy a component
deploy_component() {
    project=$1
    component=$2

    # Get project details
    project_data=$(jq -r ".projects[] | select(.name == \"$project\")" "$PROJECTS_FILE")
    if [ -z "$project_data" ]; then
        print_color "$RED" "Error: Project $project not found"
        exit 1
    fi

    project_path=$(echo "$project_data" | jq -r '.path')
    claude_dir=$(echo "$project_data" | jq -r '.claudeDir // ".claude"')
    target_base="$project_path/$claude_dir"

    # Create target directory if needed
    mkdir -p "$target_base"

    # Parse component type and name
    component_type=$(echo "$component" | cut -d: -f1)
    component_name=$(echo "$component" | cut -d: -f2)

    case "$component_type" in
        agent)
            source_file="$TOOLKIT_ROOT/agents/$component_name.md"
            target_dir="$target_base/agents"
            if [ -f "$source_file" ]; then
                mkdir -p "$target_dir"
                cp "$source_file" "$target_dir/"
                print_color "$GREEN" "✓ Deployed agent: $component_name"
            else
                print_color "$RED" "Error: Agent $component_name not found"
                exit 1
            fi
            ;;

        command)
            source_file="$TOOLKIT_ROOT/commands/$component_name.md"
            target_file="$target_base/commands/$component_name.md"
            if [ -f "$source_file" ]; then
                mkdir -p "$(dirname "$target_file")"
                cp "$source_file" "$target_file"
                print_color "$GREEN" "✓ Deployed command: $component_name"
            else
                print_color "$RED" "Error: Command $component_name not found"
                exit 1
            fi
            ;;

        template)
            source_file="$TOOLKIT_ROOT/templates/$component_name.md"
            target_file="$target_base/templates/$component_name.md"
            if [ -f "$source_file" ]; then
                mkdir -p "$(dirname "$target_file")"
                cp "$source_file" "$target_file"
                print_color "$GREEN" "✓ Deployed template: $component_name"
            else
                print_color "$RED" "Error: Template $component_name not found"
                exit 1
            fi
            ;;

        all-agents)
            mkdir -p "$target_base/agents"
            cp -r "$TOOLKIT_ROOT/agents/"*.md "$target_base/agents/" 2>/dev/null || true
            print_color "$GREEN" "✓ Deployed all agents"
            ;;

        all-commands)
            mkdir -p "$target_base/commands"
            cp -r "$TOOLKIT_ROOT/commands/"* "$target_base/commands/" 2>/dev/null || true
            print_color "$GREEN" "✓ Deployed all commands"
            ;;

        all-templates)
            mkdir -p "$target_base/templates"
            cp -r "$TOOLKIT_ROOT/templates/"* "$target_base/templates/" 2>/dev/null || true
            print_color "$GREEN" "✓ Deployed all templates"
            ;;

        *)
            print_color "$RED" "Error: Unknown component type: $component_type"
            exit 1
            ;;
    esac

    # Deployment complete - no tracking needed
}

# Function to deploy all components
deploy_all() {
    project=$1
    print_color "$BLUE" "Deploying all components to $project..."
    deploy_component "$project" "all-agents"
    deploy_component "$project" "all-commands"
    deploy_component "$project" "all-templates"
    print_color "$GREEN" "✓ All components deployed to $project"
}

# Function to list projects
list_projects() {
    print_color "$BLUE" "Registered Projects:"
    echo ""
    jq -r '.projects[] | "• \(.name): \(.path)"' "$PROJECTS_FILE"
}

# Function to show project status
show_status() {
    project=$1
    project_data=$(jq ".projects[] | select(.name == \"$project\")" "$PROJECTS_FILE")

    if [ -z "$project_data" ]; then
        print_color "$RED" "Error: Project $project not found"
        exit 1
    fi

    print_color "$BLUE" "Project: $project"
    echo "$project_data" | jq -r '"Path: \(.path)"'
    echo "$project_data" | jq -r '"Claude Dir: \(.claudeDir // ".claude")"'
}

# Main script logic
case "$1" in
    add-project)
        add_project "$2" "$3"
        ;;
    deploy)
        deploy_component "$2" "$3"
        ;;
    deploy-all)
        deploy_all "$2"
        ;;
    list)
        list_projects
        ;;
    status)
        show_status "$2"
        ;;
    help|--help|-h|"")
        show_usage
        ;;
    *)
        print_color "$RED" "Error: Unknown command: $1"
        show_usage
        exit 1
        ;;
esac