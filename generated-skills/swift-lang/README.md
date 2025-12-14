# swift-lang

Advanced Swift language features for building robust, performant code.

## What This Skill Covers

This skill focuses on **Swift language internals** - the deep features beyond basic syntax:

- **Macros** - Compile-time code generation with SwiftSyntax
- **Concurrency** - async/await, actors, Sendable
- **Testing** - Swift Testing framework patterns
- **Generics** - Protocol design, existentials, type erasure
- **Optimization** - Memory management, performance profiling
- **Result Builders** - Custom DSL creation

## What This Skill Does NOT Cover

- SwiftUI patterns (see `swift-ui`)
- UI/UX design principles (see `design-principles`)
- App Store submission (see `design-review`)

## Structure

```
swift-lang/
├── SKILL.md                    # Router
├── references/
│   ├── macros/
│   │   ├── freestanding.md     # ExpressionMacro, DeclarationMacro
│   │   └── attached.md         # Peer, Accessor, Member, Extension, Body
│   ├── concurrency/
│   │   ├── async-await.md
│   │   ├── actors.md
│   │   └── sendable.md
│   ├── testing/
│   │   ├── swift-testing.md
│   │   └── strategies.md
│   ├── generics/
│   │   ├── protocols.md
│   │   └── existentials.md
│   ├── optimization/
│   │   ├── memory.md
│   │   └── performance.md
│   └── result-builders/
│       └── custom-dsl.md
```

## Usage

The skill automatically routes to relevant references based on your question:

- "How do I create a Swift macro?" → loads macros references
- "How do actors work?" → loads concurrency/actors.md
- "What's the difference between any and some?" → loads generics/existentials.md

## Sources

- Macros content adapted from [Itsuki's Swift Macros article](https://levelup.gitconnected.com/)
- Apple WWDC sessions and Swift documentation
