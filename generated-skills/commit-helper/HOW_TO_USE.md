# How to Use the Commit Helper Skill

## Quick Start

Stage your changes and ask Claude for a commit message:

```bash
git add src/auth/login.ts
```

Then ask Claude:
```
"Generate a commit message for my staged changes"
"Help me write a commit message"
"What should I name this commit?"
```

## What This Skill Does

The Commit Helper skill analyzes your staged git changes and generates professional, descriptive commit messages following industry best practices.

### Commit Message Format

Claude generates messages with:

1. **Summary Line** (under 50 characters)
   - Present tense
   - Imperative mood
   - No period at end
   - Concise description of what changed

2. **Detailed Description** (optional, for complex changes)
   - Explains what and why (not how)
   - Wrapped at 72 characters
   - Separated from summary by blank line

3. **Affected Components** (optional)
   - Lists files or modules changed
   - Helps reviewers understand scope

## Usage Examples

### Example 1: Simple Feature Addition

```bash
# Stage your changes
git add src/components/UserProfile.tsx

# Ask for commit message
User: "Generate a commit message"

Claude: I'll analyze your staged changes...

[Runs git diff --staged]

Suggested commit message:

Add user profile avatar upload feature

Implements avatar upload functionality in UserProfile component:
- Add file input for image selection
- Integrate with upload API endpoint
- Display preview before upload
- Handle upload errors gracefully

Affected: src/components/UserProfile.tsx
```

### Example 2: Bug Fix

```bash
git add src/api/auth.ts

User: "Help me write a commit message for this fix"

Claude:

Fix authentication token expiration handling

Resolves issue where expired tokens weren't being refreshed
properly, causing users to be logged out unexpectedly.

Changes:
- Check token expiration before each API call
- Automatically refresh tokens when within 5 minutes of expiry
- Add error handling for failed refresh attempts

Fixes #123
Affected: src/api/auth.ts
```

### Example 3: Refactoring

```bash
git add src/utils/*.ts

User: "Generate a commit message"

Claude:

Refactor utility functions for better modularity

Splits monolithic utils.ts into focused modules for improved
maintainability and easier testing.

Changes:
- Extract date utilities to dateUtils.ts
- Extract string utilities to stringUtils.ts
- Extract validation to validators.ts
- Update imports across codebase

Affected: src/utils/dateUtils.ts, stringUtils.ts, validators.ts
```

### Example 4: Multiple File Changes

```bash
git add src/models/User.ts src/api/users.ts tests/user.test.ts

User: "What should I commit this as?"

Claude:

Add user role management functionality

Implements role-based access control for user accounts:
- Add roles field to User model
- Create API endpoints for role assignment
- Add permission checking utilities
- Include unit tests for role operations

Affected:
- src/models/User.ts
- src/api/users.ts
- tests/user.test.ts
```

## Best Practices

### Commit Message Guidelines

Claude follows these conventions:

**Summary Line:**
- ✅ "Add user authentication"
- ✅ "Fix memory leak in data parser"
- ✅ "Refactor database connection logic"
- ❌ "Added user authentication" (past tense)
- ❌ "Adds user authentication" (third person)
- ❌ "User authentication feature added" (passive voice)

**What to Include:**
- What changed
- Why it changed
- Impact of the change
- Related issue numbers (if applicable)

**What to Avoid:**
- How it was implemented (code explains that)
- Obvious information
- Generic messages like "Update" or "Fix bug"

## Integration with Workflow

### Standard Git Workflow

```bash
# 1. Make changes
vim src/feature.ts

# 2. Stage changes
git add src/feature.ts

# 3. Ask Claude for commit message
# User: "Generate a commit message"

# 4. Review and use Claude's suggestion
git commit -m "Add new feature" -m "Detailed description..."

# 5. Push
git push
```

### With Git Hooks

You can integrate this skill with git hooks:

```bash
# .git/hooks/prepare-commit-msg
#!/bin/bash
# Ask Claude to suggest commit message before opening editor
```

### With Pull Requests

```bash
# Combine multiple commit messages for PR description
# Ask Claude: "Summarize these commits for a PR description"
```

## Advanced Usage

### Conventional Commits

Ask Claude to use specific conventions:

```
User: "Generate a commit message using Conventional Commits format"

Claude:

feat(auth): add OAuth2 authentication

Implements OAuth2 flow for third-party authentication:
- Add OAuth2 provider configuration
- Implement authorization code flow
- Add token refresh mechanism

BREAKING CHANGE: Removes legacy session-based auth
```

### Semantic Versioning Hints

```
User: "Generate a commit message and suggest version bump"

Claude:

fix(api): correct user data serialization

Fixes bug where nested objects weren't properly serialized
in API responses, causing client-side parsing errors.

Affected: src/api/serializers.ts
Suggested version bump: PATCH (0.1.2 → 0.1.3)
```

### Multiple Commits

```
User: "I have multiple related changes. Should I commit separately?"

Claude: Yes, I recommend splitting into 3 commits:

1. "Add User model validation rules"
   Files: src/models/User.ts

2. "Implement user creation API endpoint"
   Files: src/api/users.ts

3. "Add tests for user creation"
   Files: tests/users.test.ts

This makes the history clearer and easier to review.
```

## Common Questions

**Q: Can Claude auto-commit for me?**
A: No, Claude generates the message. You still run `git commit` manually with Claude's suggestion.

**Q: What if I disagree with the message?**
A: Claude's suggestions are starting points. Edit as needed to match your project's conventions.

**Q: Does it work with large changesets?**
A: Yes, but consider splitting large changes into multiple commits for clarity.

**Q: Can it generate messages for past commits?**
A: Yes, use `git diff <commit>^..<commit>` to show specific commit changes.

## Tips for Better Commit Messages

1. **Stage related changes together**
   ```bash
   # Good: Feature-focused staging
   git add src/auth/*.ts tests/auth/*.ts

   # Bad: Random file staging
   git add src/auth/login.ts src/utils/date.ts
   ```

2. **Review diff before asking**
   ```bash
   git diff --staged  # See what you're committing
   ```

3. **Provide context when needed**
   ```
   "Generate a commit message for this security fix"
   "This is a breaking change, help me write the commit message"
   ```

4. **Link to issues**
   ```
   "Generate a commit message and include 'Fixes #123'"
   ```

## Related Skills

- **code-reviewer** - Review changes before committing
- **spike-driven-dev** - Create focused commits during spikes

---

Generated by Claude Code Skills Factory
