# swift-ui

SwiftUI implementation patterns for building polished iOS and macOS apps.

## What This Skill Does

Provides ready-to-use SwiftUI patterns for views, state management, layouts, animations, and app architecture. Part of the `swift-*` skill family focused on Apple platform development.

## When to Use

- Building SwiftUI views and components
- Managing state with property wrappers and Environment
- Creating responsive layouts
- Adding animations and transitions
- Implementing accessibility features
- Structuring app architecture (No MVVM philosophy)

## Coverage

| Area | What You Get |
|------|--------------|
| **Views** | Composition, modifiers, ViewBuilder patterns |
| **State** | @State, @Binding, @Environment, @Observable |
| **Layout** | Stacks, grids, GeometryReader, adaptive |
| **Animation** | Springs, transitions, gestures |
| **Accessibility** | VoiceOver, Dynamic Type, traits |
| **Architecture** | No MVVM, Environment DI, .task/.onChange patterns |

## Related Skills

This skill is part of the `swift-*` family:

- **swift-lang** - Swift language features (macros, concurrency, testing)
- **swift-ui** (this skill) - SwiftUI implementation

Design skills for theory:
- **design-principles** - Universal theory (why)
- **design-review** - App Store submission prep

## Quick Example

```
"Build me a card component in SwiftUI"
→ Routes to views.md
→ Provides view structure with proper modifier ordering
→ Includes preview patterns

"How should I manage state for a form?"
→ Routes to state.md + architecture.md
→ Shows @State + Environment pattern
→ Explains why you don't need a ViewModel
```

## Philosophy

SwiftUI views are pure state expressions. Use @State, @Environment, and view composition rather than ViewModels. Trust the framework.
