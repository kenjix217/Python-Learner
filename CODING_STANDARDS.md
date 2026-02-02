# CODING_STANDARDS.md

This document defines coding standards and conventions for the Python AI Tutor App.

---

## 1. General Principles

- Prioritize readability over cleverness
- Follow the principle of least surprise
- Make the smallest change necessary
- Preserve existing behavior unless explicitly changing it
- Document non-obvious decisions

---

## 2. Python Standards

### 2.1 Style Guide
- Follow PEP 8 for all Python code
- Use 4 spaces for indentation (never tabs)
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable names (avoid abbreviations)

### 2.2 Naming Conventions
- `snake_case` for functions, variables, modules
- `PascalCase` for classes
- `UPPER_SNAKE_CASE` for constants
- Prefix private methods/attributes with single underscore `_`

### 2.3 Type Hints
- Use type hints for function signatures
- Use `Optional[T]` for nullable values
- Use `list[T]`, `dict[K, V]` for collections (Python 3.9+)

### 2.4 Documentation
- Use docstrings for all public functions and classes
- Follow Google or NumPy docstring format
- Include examples in docstrings when helpful

---

## 3. JavaScript/Frontend Standards

### 3.1 Style Guide
- Use 2 spaces for indentation
- Use `const` by default, `let` when reassignment needed
- Avoid `var` entirely
- Use semicolons consistently

### 3.2 Naming Conventions
- `camelCase` for variables and functions
- `PascalCase` for classes and components
- `UPPER_SNAKE_CASE` for constants
- Use descriptive names (e.g., `fetchLessonData` not `fld`)

### 3.3 Modern JavaScript
- Prefer arrow functions for callbacks
- Use template literals for string interpolation
- Use destructuring where it improves clarity
- Use async/await over raw Promises

### 3.4 DOM Manipulation
- Cache DOM queries when used multiple times
- Use event delegation for dynamic content
- Clean up event listeners when elements are removed

---

## 4. HTML/CSS Standards

### 4.1 HTML
- Use semantic HTML5 elements (`<article>`, `<section>`, `<nav>`)
- Include proper ARIA attributes for accessibility
- Use meaningful `id` and `class` names
- Keep markup minimal and purposeful

### 4.2 CSS
- Use BEM naming convention for classes (Block__Element--Modifier)
- Mobile-first responsive design
- Prefer CSS Grid and Flexbox over floats
- Use CSS custom properties (variables) for theming
- Avoid `!important` unless absolutely necessary

---

## 5. File Organization

### 5.1 Directory Structure
```
frontend/
  ├── index.html          # Main entry point
  ├── css/                # Stylesheets
  ├── js/                 # JavaScript modules
  ├── lessons/            # Lesson content (Markdown)
  └── lib/                # Third-party libraries

backend/
  ├── main.py             # API entry point
  ├── services/           # Business logic
  ├── models/             # Data models
  └── utils/              # Helper functions
```

### 5.2 File Naming
- Use lowercase with hyphens for files: `lesson-viewer.js`, `user-progress.py`
- Match filenames to primary export/class name when applicable
- Group related files in subdirectories

---

## 6. Error Handling

### 6.1 Python
```python
# DO: Specific exception handling
try:
    result = risky_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    raise

# DON'T: Catch all exceptions silently
try:
    risky_operation()
except:
    pass
```

### 6.2 JavaScript
```javascript
// DO: Provide user-friendly error messages
async function loadLesson(id) {
  try {
    const response = await fetch(`/api/lessons/${id}`);
    if (!response.ok) {
      throw new Error(`Failed to load lesson: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Lesson loading error:', error);
    showUserMessage('Unable to load lesson. Please try again.');
    throw error;
  }
}

// DON'T: Swallow errors silently
async function loadLesson(id) {
  try {
    return await fetch(`/api/lessons/${id}`).then(r => r.json());
  } catch (e) {}
}
```

---

## 7. Security Standards

- Validate all user input at API boundaries
- Sanitize HTML content before rendering
- Never expose API keys or secrets in frontend code
- Use parameterized queries for database operations
- Set appropriate CORS headers

---

## 8. Testing Standards

### 8.1 Unit Tests
- Test one thing per test
- Use descriptive test names
- Follow Arrange-Act-Assert pattern
- Aim for high coverage of critical paths

### 8.2 Test File Naming
- Python: `test_module_name.py`
- JavaScript: `module-name.test.js`

---

## 9. Comments and Documentation

### 9.1 When to Comment
- Explain *why*, not *what* the code does
- Document complex algorithms or non-obvious logic
- Explain workarounds or unusual patterns
- Mark TODOs with context and owner

### 9.2 Comment Style
```python
# Good: Explains reasoning
# Use binary search because dataset can exceed 10K items
result = binary_search(data, target)

# Bad: States the obvious
# Call binary search
result = binary_search(data, target)
```

---

## 10. Version Control

- Write clear, descriptive commit messages
- Use imperative mood: "Add feature" not "Added feature"
- Reference issue numbers when applicable
- Keep commits focused and atomic
- Never commit secrets or credentials

---

## 11. Dependency Management

- Document all dependencies with versions
- Specify exact versions in production
- Regularly audit for security vulnerabilities
- Remove unused dependencies
- Follow `FREE_TOOLS_AND_LICENSING.md` for all additions

---

## 12. Performance Considerations

- Lazy-load non-critical resources
- Minimize DOM manipulation
- Cache expensive computations
- Optimize images and assets
- Profile before optimizing

---

## 13. Accessibility Requirements

- Minimum contrast ratio 4.5:1 for text
- Keyboard navigation for all interactive elements
- Descriptive alt text for images
- Proper heading hierarchy
- ARIA labels for custom controls

---

## 14. Beginner-Focused Code

When writing example code for lessons:
- Use simple, single-responsibility functions
- Avoid advanced language features
- Include comments explaining each step
- Use meaningful variable names
- Show one concept at a time

---

## 15. Enforcement

Code that violates these standards should:
- Be flagged in code review
- Be refactored before merge
- Include justification if standards must be bypassed




