---
name: design-swiftui
description: SwiftUI implementation patterns for building polished iOS/macOS apps. Use when building views, managing state, creating layouts, or implementing animations in SwiftUI.
---

# design-swiftui

SwiftUI implementation patterns for building distinctive iOS and macOS interfaces.

## Scope

This skill covers **SwiftUI implementation**—the views, modifiers, state management, and patterns needed to build polished native apps. For design theory (typography, color, hierarchy), see `design-principles`. For App Store submission, see `design-review`.

## Routing

Based on what you're building, I'll reference the appropriate implementation guide:

### View Composition
**When**: Building views, applying modifiers, structuring components
**Reference**: `references/views.md`
- View composition patterns
- Modifier ordering
- Custom view modifiers
- ViewBuilder and generics

### State Management
**When**: Managing data flow, handling state
**Reference**: `references/state.md`
- Property wrappers (@State, @Binding, @StateObject, etc.)
- Data flow patterns
- Observable objects
- Environment values

### Layout Patterns
**When**: Creating layouts, grids, responsive design
**Reference**: `references/layout.md`
- Stack patterns (VStack, HStack, ZStack)
- LazyStacks and LazyGrids
- GeometryReader and layout priorities
- Adaptive layouts

### Animation
**When**: Adding motion, transitions, gestures
**Reference**: `references/animation.md`
- Implicit vs explicit animation
- Transitions
- Spring animations
- Gesture-driven animation

### Accessibility
**When**: VoiceOver, Dynamic Type, accessibility
**Reference**: `references/accessibility.md`
- Accessibility modifiers
- VoiceOver optimization
- Dynamic Type support
- Accessibility traits and actions

## Quick Reference

### Essential Patterns

```swift
// MARK: - View Composition

struct ContentView: View {
    var body: some View {
        NavigationStack {
            List(items) { item in
                ItemRow(item: item)
            }
            .navigationTitle("Items")
        }
    }
}

// MARK: - State Management

struct ItemDetailView: View {
    @StateObject private var viewModel: ItemViewModel
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        Form {
            // content
        }
    }
}

// MARK: - Animation

Button("Animate") {
    withAnimation(.spring(response: 0.3, dampingFraction: 0.6)) {
        isExpanded.toggle()
    }
}
```

### HIG Quick Reference

| Element | iOS Standard |
|---------|-------------|
| Touch target | 44pt minimum |
| Navigation bar | 44pt height |
| Tab bar | 49pt height |
| Toolbar | 44pt height |
| Corner radius | 10-20pt for cards |
| Standard margin | 16pt |

### Color System

```swift
// Use semantic colors
Color.primary       // Adapts to dark mode
Color.secondary
Color.accentColor
Color(uiColor: .systemBackground)
Color(uiColor: .secondarySystemBackground)
```

## Anti-Patterns

- Force unwrapping in views
- Massive view bodies (extract components)
- Business logic in views
- Ignoring @MainActor for UI updates
- Not supporting Dynamic Type
- Hardcoded colors instead of semantic

## Related Skills

- **design-principles** - Theory behind the choices
- **design-web** - Web/CSS implementation
- **design-review** - App Store submission prep
