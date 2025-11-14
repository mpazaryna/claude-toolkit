# How to Use the Code Reviewer Skill

## Quick Start

Ask Claude to review code, and the skill will automatically activate:

```
"Review the authentication module for security issues"
"Check this PR for code quality"
"Analyze src/api/ for best practices"
```

## What This Skill Does

The Code Reviewer skill provides systematic code analysis across five key dimensions:

1. **Code Organization & Structure**
   - File/folder organization
   - Naming conventions
   - Code modularity
   - Separation of concerns

2. **Error Handling**
   - Try/catch coverage
   - Error propagation
   - User-friendly error messages
   - Logging and debugging support

3. **Performance Considerations**
   - Algorithm efficiency
   - Resource usage
   - Caching opportunities
   - Database query optimization

4. **Security Concerns**
   - Input validation
   - Authentication/authorization
   - Data sanitization
   - Vulnerability patterns

5. **Test Coverage**
   - Unit test presence
   - Integration test coverage
   - Edge case handling
   - Test quality

## Usage Examples

### Example 1: Review Single File

```
User: Review src/auth/login.ts for security issues

Claude: I'll review the login module for security concerns.

[Uses Read tool to load the file]
[Analyzes for security patterns]

Findings:
✅ Password hashing implemented correctly
⚠️  No rate limiting on login attempts
❌ User input not sanitized before database query
✅ JWT tokens properly validated

Recommendations:
1. Add rate limiting to prevent brute force attacks
2. Sanitize username input to prevent SQL injection
3. Consider implementing 2FA
```

### Example 2: Review Pull Request

```
User: Review PR #123 for code quality

Claude: I'll analyze the PR changes for code quality issues.

[Uses Glob to find changed files]
[Uses Read to examine each file]
[Uses Grep to find patterns]

Code Organization: Good
- Files properly organized in feature folders
- Consistent naming conventions

Error Handling: Needs Improvement
- Missing error handling in 3 async functions
- Recommend adding try/catch blocks

Performance: Excellent
- Efficient algorithms used
- Proper use of memoization

Security: Good
- Input validation present
- Authentication checks in place

Test Coverage: Needs Improvement
- 2 new functions without tests
- Recommend adding unit tests
```

### Example 3: Analyze Entire Directory

```
User: Analyze src/components/ for best practices

Claude: I'll review all components for best practices.

[Uses Glob to find all files in directory]
[Analyzes each component]

Summary:
- 15 components reviewed
- 3 components need refactoring for better modularity
- 5 components missing prop validation
- 2 components have performance issues (unnecessary re-renders)
- 10 components lack unit tests

Detailed findings:
...
```

## Review Checklist

When Claude reviews your code, it checks:

### Structure ✓
- [ ] Proper file organization
- [ ] Consistent naming conventions
- [ ] Appropriate use of modules/components
- [ ] Clear separation of concerns
- [ ] No code duplication

### Error Handling ✓
- [ ] Try/catch blocks where needed
- [ ] Proper error propagation
- [ ] Meaningful error messages
- [ ] Logging for debugging
- [ ] Graceful failure handling

### Performance ✓
- [ ] Efficient algorithms
- [ ] No unnecessary computations
- [ ] Proper use of caching
- [ ] Optimized database queries
- [ ] Lazy loading where appropriate

### Security ✓
- [ ] Input validation
- [ ] Output sanitization
- [ ] Authentication checks
- [ ] Authorization enforcement
- [ ] No hardcoded secrets

### Testing ✓
- [ ] Unit tests present
- [ ] Integration tests where needed
- [ ] Edge cases covered
- [ ] Test quality (not just coverage)
- [ ] Mocks used appropriately

## Expected Output

The skill provides:

1. **Summary** - High-level assessment
2. **Detailed Findings** - Specific issues found
3. **Severity Levels** - Critical (❌), Warning (⚠️), Good (✅)
4. **Recommendations** - Actionable next steps
5. **Code Examples** - Suggested improvements

## Best Practices

### Do's ✅

- Be specific about what to review
- Provide context (e.g., "this is auth code")
- Ask for specific dimensions if needed
- Request examples of improvements

### Don'ts ❌

- Don't ask to review entire large codebases at once
- Don't expect the skill to run tests (it analyzes code)
- Don't rely solely on automated review (human review still important)

## Integration with Workflow

### In Pull Requests

```
1. Create PR
2. Ask Claude to review: "Review PR #X for code quality"
3. Address findings
4. Human review
5. Merge
```

### In Development

```
1. Write code
2. Ask Claude: "Review MyComponent.tsx for best practices"
3. Refactor based on feedback
4. Write tests
5. Commit
```

### In Code Audits

```
1. Identify problem area
2. Ask Claude: "Analyze src/payments/ for security issues"
3. Create tickets for findings
4. Prioritize and fix
```

## Common Questions

**Q: Can this skill run tests?**
A: No, it analyzes code statically. It will identify missing tests but won't execute them.

**Q: How deep does the analysis go?**
A: It depends on your request. You can ask for quick overview or deep analysis.

**Q: Can it review any language?**
A: Yes, the skill works with any programming language.

**Q: Will it catch all security issues?**
A: No automated tool catches everything. Use this as one layer of defense.

## Related Skills

- **commit-helper** - Generate good commit messages after fixes
- **spike-driven-dev** - Validate architecture before building

---

Generated by Claude Code Skills Factory
