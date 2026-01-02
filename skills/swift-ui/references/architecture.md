# SwiftUI Architecture: No ViewModels

SwiftUI was designed with a different philosophy than UIKit. **You don't need ViewModels.**

Apple's WWDC sessions ([Data Flow Through SwiftUI - WWDC19](https://developer.apple.com/videos/play/wwdc2019/226/), [Data Essentials in SwiftUI - WWDC20](https://developer.apple.com/videos/play/wwdc2020/10040/)) barely mention ViewModels because they are fundamentally alien to SwiftUI's data flow design.

SwiftUI views are **structs**, not classes. They're designed to be lightweight, disposable, and recreated frequently. Adding ViewModels fights against this fundamental design principle.

---

## Separation of Concerns

```
┌─────────────────────────────────────────────────┐
│  Models                                         │
│  └─ Data structures and business logic         │
│                                                 │
│  Services                                       │
│  └─ Network clients, databases, utilities      │
│     (Injected via @Environment)                 │
│                                                 │
│  Views                                          │
│  └─ Pure state representations                 │
│     Orchestrate user interactions               │
│     @State for local UI state                   │
│     @Environment for services                   │
└─────────────────────────────────────────────────┘
```

---

## The Core Pattern

Every view follows this pattern:

```swift
struct SOAPGenerationView: View {
    // MARK: - Environment Dependencies
    @Environment(ModelProviderService.self) private var modelService
    @Environment(\.modelContext) private var modelContext

    // MARK: - View State (enum for mutually exclusive states)
    enum ViewState {
        case idle
        case generating
        case success(SOAPNote)
        case error(String)
    }

    @State private var viewState: ViewState = .idle
    @State private var examText: String = ""

    // MARK: - Body
    var body: some View {
        VStack {
            TextEditor(text: $examText)

            Button("Generate") {
                Task { await generateSOAP() }
            }
            .disabled(examText.isEmpty || viewState == .generating)

            switch viewState {
            case .idle:
                ContentUnavailableView("Ready", systemImage: "doc.text")
            case .generating:
                ProgressView("Generating...")
            case .success(let note):
                SOAPResultView(note: note)
            case .error(let message):
                ErrorView(message: message)
            }
        }
        .task { await loadDefaults() }
    }

    // MARK: - Private Methods
    private func generateSOAP() async {
        viewState = .generating
        do {
            let response = try await modelService.generateResponse(prompt: examText)
            let note = SOAPNote(content: response.content)
            viewState = .success(note)
            modelContext.insert(note)
        } catch {
            viewState = .error(error.localizedDescription)
        }
    }
}
```

**Key observations:**
1. State is defined within the view using an enum
2. No external ViewModel needed
3. Environment injects dependencies
4. View is just a representation of state
5. Private methods orchestrate state transitions

---

## Environment Over ViewModels

```swift
@Environment(ModelProviderService.self) private var modelService

private func generateNote() async {
    let response = try await modelService.generateResponse(prompt: examText)
    viewState = .success(response)
}
```

**Benefits:**
- Automatic propagation through view hierarchy
- Easy to test - swap implementations at root
- No manual injection
- Type-safe, compiler-checked
- Lifetime managed by SwiftUI

### App Setup

```swift
@main
struct PABApp: App {
    @State private var modelService = ModelProviderService()
    @State private var icd10Processor = ICD10MLXProcessor()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(modelService)
                .environment(icd10Processor)
                .modelContainer(for: SavedSOAPNote.self)
        }
    }
}
```

---

## SwiftData: Apple's Evidence

If you need proof Apple designed SwiftUI without ViewModels, look at SwiftData.

### The Natural Way

```swift
struct SavedNotesView: View {
    @Query private var notes: [SavedSOAPNote]
    @Environment(\.modelContext) private var modelContext

    var body: some View {
        List {
            ForEach(notes) { note in
                SavedNoteRow(note: note)
                    .swipeActions {
                        Button("Delete", role: .destructive) {
                            deleteNote(note)
                        }
                    }
            }
        }
    }

    private func deleteNote(_ note: SavedSOAPNote) {
        modelContext.delete(note)
        try? modelContext.save()
    }
}
```

`@Query` automatically handles fetching, change observation, UI updates, sorting, filtering, and memory management.

### The Wrong Way (Don't Do This)

```swift
// ❌ Fighting the framework
@Observable
class SavedNotesViewModel {
    private var modelContext: ModelContext
    var notes: [SavedSOAPNote] = []

    init(modelContext: ModelContext) {
        self.modelContext = modelContext
        fetchNotes() // Manual fetching
    }

    func deleteNote(_ note: SavedSOAPNote) {
        modelContext.delete(note)
        fetchNotes() // Manual refresh - yuck!
    }
}
```

You lose all of SwiftData's automatic benefits.

### Dynamic Queries

```swift
struct PatientNotesView: View {
    let patientID: String
    @Query private var notes: [SavedSOAPNote]

    init(patientID: String) {
        self.patientID = patientID
        let predicate = #Predicate<SavedSOAPNote> { $0.patientID == patientID }
        _notes = Query(filter: predicate, sort: \.createdAt, order: .reverse)
    }

    var body: some View {
        List(notes) { note in
            SavedNoteRow(note: note)
        }
    }
}
```

---

## View Lifecycle & Side Effects

### .task(id:) Modifier

Re-runs when the id value changes:

```swift
struct FeedView: View {
    @State private var searchQuery: String = ""
    @State private var results: [Result] = []

    var body: some View {
        VStack {
            SearchField(text: $searchQuery)
            ResultsList(results: results)
        }
        .task(id: searchQuery) {
            guard !searchQuery.isEmpty else {
                results = []
                return
            }
            try? await Task.sleep(for: .milliseconds(300)) // Debounce
            results = try await service.search(query: searchQuery)
        }
    }
}
```

### .onChange(of:) Modifier

React to state changes with side effects:

```swift
.onChange(of: selectedProvider) { oldValue, newValue in
    service.setDefaultProvider(newValue)
    showingAlert = true
}
```

### Combining Modifiers

```swift
var headerView: some View {
    FeedHeaderView(filter: $filter, searchText: $searchText)
        .task(id: searchText) {
            guard !searchText.isEmpty else { return }
            await searchFeed(query: searchText)
        }
        .onChange(of: isSearchFocused) { _, isFocused in
            guard !isFocused else { return }
            Task { await loadDefaultFeed() }
        }
        .onChange(of: filter) { _, newFilter in
            Task { await applyFilter(newFilter) }
        }
}
```

---

## State Management Patterns

### Enum-Based View States

Use enums for mutually exclusive states:

```swift
enum LoadingState<T> {
    case idle
    case loading
    case loaded(T)
    case error(Error)
}

@State private var state: LoadingState<[Item]> = .idle
```

### Nested Enums for Complex States

```swift
enum GenerationState {
    case idle
    case analyzing(AnalysisPhase)
    case success(SOAPNote)
    case error(GenerationError)
}

enum AnalysisPhase {
    case runningMLX
    case callingSoapAPI
    case formatting
}
```

### Multiple Independent States

When states aren't mutually exclusive, use separate `@State` properties:

```swift
@State private var mlxEnabled = true
@State private var notificationsEnabled = true
@State private var defaultProvider: ModelProvider = .appleIntelligence
```

---

## View Composition

### When a View Gets Too Large, Split It

**Don't** add a ViewModel. **Do** extract subviews.

```swift
struct ChiropracticView: View {
    @State private var selectedTab: ChiropracticTab = .soapGeneration

    var body: some View {
        NavigationSplitView {
            ChiropracticSidebar(selection: $selectedTab)
        } detail: {
            switch selectedTab {
            case .soapGeneration: SOAPGenerationView()
            case .savedNotes: SavedNotesView()
            case .promptTesting: PromptTestingView()
            }
        }
    }
}
```

Each subview handles its own state.

### Parent-Child Communication

Use `@State` and `@Binding`:

```swift
struct ParentView: View {
    @State private var isExpanded = false
    @State private var selectedItem: Item?

    var body: some View {
        VStack {
            HeaderView(isExpanded: $isExpanded)
            ContentView(isExpanded: isExpanded, selectedItem: $selectedItem)
            if let item = selectedItem {
                DetailView(item: item)
            }
        }
    }
}

struct HeaderView: View {
    @Binding var isExpanded: Bool

    var body: some View {
        Button(isExpanded ? "Collapse" : "Expand") {
            isExpanded.toggle()
        }
    }
}
```

### When to Split Views

1. File exceeds ~300 lines
2. Body has more than 3 levels of nesting
3. Repeated code that could be extracted
4. Distinct sections with their own state

---

## Testing Strategy

**Test services and business logic, not views.**

```swift
// ✅ Test this
@MainActor
final class ModelProviderServiceTests: XCTestCase {
    func testAppleIntelligenceProvider() async throws {
        let service = ModelProviderService()
        let response = try await service.generateResponse(prompt: "Test")
        XCTAssertFalse(response.content.isEmpty)
    }
}

// ✅ Test this
final class SOAPNoteFormatterTests: XCTestCase {
    func testFormattingValidNote() {
        let formatter = SOAPNoteFormatter()
        let result = formatter.parse("S: Pain\nO: Tenderness\nA: Strain\nP: Rest")
        XCTAssertEqual(result.subjective, "Pain")
    }
}
```

### SwiftUI Previews

Use previews for visual testing:

```swift
#Preview("SOAP Generation - Idle") {
    SOAPGenerationView()
        .environment(ModelProviderService())
}
```

### ViewInspector (Optional)

For view structure testing: [nalexn/ViewInspector](https://github.com/nalexn/ViewInspector)

---

## Common Objections Answered

### "But what about testability?"

Test services and business logic, not views. Views should be so simple that visual testing is sufficient.

### "But my view has complex business logic!"

That logic belongs in a **service**, not in a view OR a ViewModel.

```swift
// ❌ Bad - logic in view or ViewModel
func complexCalculation() { /* 50 lines */ }

// ✅ Good - logic in service
class CalculationService {
    func complexCalculation() -> String { /* 50 lines */ }
}

struct MyView: View {
    @Environment(CalculationService.self) private var calculator
    @State private var result: String = ""

    var body: some View {
        Text(result)
            .task { result = calculator.complexCalculation() }
    }
}
```

### "But ViewModels help with separation of concerns!"

SwiftUI already has separation: Models = data, Services = logic, Views = UI.

### "But MVVM is an industry standard!"

MVVM is a UIKit pattern. SwiftUI has a different design philosophy.

---

## Code Standards

### DO

- Use `@State` for local view state
- Use `@Environment` for service injection
- Use `@Query` for SwiftData access
- Split large views into subviews
- Extract business logic to services
- Use `.task(id:)` and `.onChange()` liberally
- Test services, not views

### DON'T

- Create ViewModels with `@Observable`
- Pass `@ObservableObject` between views
- Put business logic in views
- Manually refresh SwiftData queries
- Fight SwiftUI's design patterns

---

## Anti-Patterns

Every ViewModel you add is:
- More complexity to maintain
- More objects to keep in sync
- More indirection between intent and action
- More cognitive overhead

ViewModels encourage bloat. Force yourself to split views into the smallest possible units instead.

---

## References

- [Data Flow Through SwiftUI - WWDC19](https://developer.apple.com/videos/play/wwdc2019/226/)
- [Data Essentials in SwiftUI - WWDC20](https://developer.apple.com/videos/play/wwdc2020/10040/)
- [ViewInspector](https://github.com/nalexn/ViewInspector) - Runtime introspection for testing
- IcySky, Ice Cubes, Medium iOS app - Production examples
