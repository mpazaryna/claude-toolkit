# SwiftUI Architecture: No MVVM

SwiftUI was designed with a different philosophy than UIKit. You don't need ViewModels.

## The Core Principle

**Views are pure state expressions.** SwiftUI views are structs - lightweight, disposable, and recreated frequently. Adding ViewModels fights against this fundamental design.

## Views as State Expressions

Use enums to represent view state directly in the view:

```swift
struct FeedView: View {
    @Environment(BlueSkyClient.self) private var client

    enum ViewState {
        case loading
        case error(String)
        case loaded([Post])
    }

    @State private var viewState: ViewState = .loading
    @State private var isRefreshing = false

    var body: some View {
        NavigationStack {
            List {
                switch viewState {
                case .loading:
                    ProgressView("Loading feed...")
                        .frame(maxWidth: .infinity)
                        .listRowSeparator(.hidden)

                case .error(let message):
                    ErrorStateView(
                        message: message,
                        retryAction: { await loadFeed() }
                    )
                    .listRowSeparator(.hidden)

                case .loaded(let posts):
                    ForEach(posts) { post in
                        PostRowView(post: post)
                            .listRowInsets(.init())
                    }
                }
            }
            .listStyle(.plain)
            .refreshable { await refreshFeed() }
            .task { await loadFeed() }
        }
    }

    private func loadFeed() async {
        do {
            let posts = try await client.getFeed()
            viewState = .loaded(posts)
        } catch {
            viewState = .error(error.localizedDescription)
        }
    }

    private func refreshFeed() async {
        defer { isRefreshing = false }
        isRefreshing = true
        await loadFeed()
    }
}
```

## Environment for Dependency Injection

Instead of manually injecting dependencies through ViewModels, use Environment:

```swift
@Environment(BlueSkyClient.self) private var client
@Environment(CurrentUser.self) private var currentUser
```

Services are initialized at app launch and injected in the view hierarchy:

```swift
@main
struct MyApp: App {
    @State var client: APIClient = .init()
    @State var auth: Auth = .init()
    @State var router: AppRouter = .init()

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(client)
                .environment(auth)
                .environment(router)
        }
    }
}
```

## .task(id:) and .onChange() as Mini Reducers

Use these modifiers to trigger side effects when values change:

```swift
private var headerView: some View {
    FeedsListTitleView(
        filter: $filter,
        searchText: $searchText,
        isInSearch: $isInSearch
    )
    // Trigger search when query changes
    .task(id: searchText) {
        guard !searchText.isEmpty else { return }
        await searchFeed(query: searchText)
    }
    // Reset when exiting search
    .onChange(of: isInSearch, initial: false) {
        guard !isInSearch else { return }
        Task { await fetchSuggestedFeed() }
    }
    // Reload when data changes
    .onChange(of: currentUser.savedFeeds.count) {
        Task { await fetchMyFeeds() }
    }
}
```

**Key patterns:**
- `.task(id:)` - Re-runs when the id value changes
- `.onChange(of:)` - Reacts to state changes
- Both act as lightweight state reducers for triggering side effects

## SwiftData: The Perfect Example

SwiftData was built to work directly in views, not through ViewModels:

```swift
struct BookListView: View {
    @Query private var books: [Book]
    @Environment(\.modelContext) private var modelContext
    @State private var showingAddBook = false

    var body: some View {
        NavigationStack {
            List {
                ForEach(books) { book in
                    BookRowView(book: book)
                        .swipeActions {
                            Button("Delete", role: .destructive) {
                                deleteBook(book)
                            }
                        }
                }
            }
            .navigationTitle("Books")
            .toolbar {
                Button("Add Book") {
                    showingAddBook = true
                }
            }
        }
    }

    private func deleteBook(_ book: Book) {
        modelContext.delete(book)
        try? modelContext.save()
    }
}
```

`@Query` automatically:
- Fetches your data
- Observes changes in the underlying store
- Updates the UI when data changes
- Handles sorting and filtering efficiently

**Don't fight the framework** by wrapping this in a ViewModel.

## Proper Separation of Concerns

Instead of ViewModels, separate:

- **Models** - Data structures and business logic
- **Services** - Network clients, databases, utilities (injected via Environment)
- **Views** - Pure state representations that orchestrate user interactions

## When Views Get Large

Split into subviews, not ViewModels:

```swift
struct PostDetailView: View {
    let post: Post
    @State private var isExpanded: Bool = false

    var body: some View {
        ScrollView {
            LazyVStack(spacing: 0) {
                PostHeaderView(post: post)
                PostContentView(post: post)
                PostActionsView(post: post, isExpanded: $isExpanded)
                PostRepliesView(postId: post.id)
            }
        }
    }
}
```

Each subview handles its own state and interactions. Use `@State` and `@Binding` to manage data flow between views.

## Testing Strategy

Testing SwiftUI views provides minimal value. Your views should be so simple that bugs are immediately visible.

**What to test:**
- Your network clients (unit tests)
- Your data models and transformations
- Business logic in services

**For visual testing:**
- SwiftUI previews for visual regression
- ViewInspector for view introspection
- UI automation and E2E tests

```swift
// ViewInspector example
@MainActor
final class ActivityTextBuilderTests: XCTestCase {
    func test_follow_activity() async {
        let activity = Activity(type: "follow", actor: Actor(name: "Test user"))
        let builder = ActivityTextBuilder(activity: activity)
        let text = try! builder.buildActorText().inspect().text().string()
        XCTAssertEqual(text, "Test user started following you")
    }
}
```

## SwiftUI Primitives to Embrace

| Primitive | Use For |
|-----------|---------|
| `@State` | Local view state |
| `@Binding` | Two-way connection to parent state |
| `@Environment` | Dependency injection |
| `@Observable` | Observable reference types |
| `.task(id:)` | Async work triggered by value changes |
| `.onChange(of:)` | Side effects on state changes |

## Anti-Patterns

Every ViewModel you add is:
- More complexity to maintain
- More objects to keep in sync
- More indirection between intent and action
- More cognitive overhead

ViewModels encourage bloat. Force yourself to split views into the smallest possible units instead.

## Sources

- Thomas Ricouard (Ice Cubes, Medium iOS app)
- WWDC19: Data Flow Through SwiftUI
- WWDC20: Data Essentials in SwiftUI
