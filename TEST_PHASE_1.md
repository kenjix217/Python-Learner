# Phase 1 Testing Guide

**Purpose:** Verify all Phase 1 features work correctly  
**Version:** 0.2.0  
**Estimated Time:** 5 minutes

---

## 🚀 Before Testing

1. **Ensure server is running:**
   ```powershell
   cd U:\Python-Learner\frontend
   python -m http.server 8000
   ```

2. **Open browser:**
   - Go to `http://localhost:8000`
   - Or open in fresh incognito window

3. **Hard refresh:**
   - Press `Ctrl + Shift + F5`
   - This ensures latest JavaScript (v=6) loads

---

## Test 1: Pyodide - Real Python Execution ✅

### Simple Print
```python
print("Hello, Python!")
```

**Expected:**
- First time: "🔄 Loading Python runtime..." (3-5 seconds)
- Then: `Hello, Python!`
- Green border, success message

**Status:** ⬜ PASS / ⬜ FAIL

---

### Variables and Math
```python
name = "Alex"
age = 25
print("Name:", name)
print("Age:", age)
print("Age in days:", age * 365)
```

**Expected:**
```
Name: Alex
Age: 25
Age in days: 9125
```

**Status:** ⬜ PASS / ⬜ FAIL

---

### Loops (IMPOSSIBLE in v0.1.x!)
```python
for i in range(5):
    print(i * 2)
```

**Expected:**
```
0
2
4
6
8
```

**Status:** ⬜ PASS / ⬜ FAIL

---

### Functions (IMPOSSIBLE in v0.1.x!)
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("World"))
print(greet("Python"))
```

**Expected:**
```
Hello, World!
Hello, Python!
```

**Status:** ⬜ PASS / ⬜ FAIL

---

### Lists and Dictionaries (IMPOSSIBLE in v0.1.x!)
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit.upper())

person = {"name": "Alex", "age": 25}
print(f"{person['name']} is {person['age']} years old")
```

**Expected:**
```
APPLE
BANANA
CHERRY
Alex is 25 years old
```

**Status:** ⬜ PASS / ⬜ FAIL

---

### Python Standard Library (IMPOSSIBLE in v0.1.x!)
```python
import math
import random

print("Pi:", math.pi)
print("Square root of 16:", math.sqrt(16))
print("Random number:", random.randint(1, 100))
```

**Expected:**
```
Pi: 3.141592653589793
Square root of 16: 4.0
Random number: [some number 1-100]
```

**Status:** ⬜ PASS / ⬜ FAIL

---

### Error Handling (Real Python Errors!)
```python
print(undefined_variable)
```

**Expected:**
- Red border
- Error message: `NameError: name 'undefined_variable' is not defined`

**Status:** ⬜ PASS / ⬜ FAIL

---

### Syntax Validation (Pre-execution Check)
```python
Print("hello")
```

**Expected:**
- Instant feedback (no 3-second wait)
- Error: "In Python, it's 'print' (lowercase), not 'Print'"
- Suggested fix shown

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 2: Monaco Editor - Professional Code Editing ✅

### Visual Features
1. Click Practice tab
2. Wait 1-2 seconds for Monaco to load
3. Verify you see:
   - ⬜ Syntax highlighting (keywords in color)
   - ⬜ Line numbers on left
   - ⬜ Dark theme matching app
   - ⬜ Professional IDE look

**Status:** ⬜ PASS / ⬜ FAIL

---

### Autocomplete
1. Type `pr` in editor
2. Verify autocomplete suggestions appear
3. Select `print` from suggestions
4. Verify it completes

**Status:** ⬜ PASS / ⬜ FAIL

---

### Keyboard Shortcuts
1. Type some code
2. Press `Ctrl + Enter` (or `Cmd + Enter` on Mac)
3. Verify code runs immediately

**Status:** ⬜ PASS / ⬜ FAIL

---

### Multiple Cursors (Advanced Feature)
1. Type a line of code
2. Hold `Alt` and click multiple places
3. Verify multiple cursors appear
4. Type to edit all positions simultaneously

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 3: Marked.js - Enhanced Markdown ✅

### Code Blocks
1. Go to Lessons tab
2. Open Lesson 2
3. Scroll to "Example" section
4. Verify code appears in **dark box** (not inline)

**Status:** ⬜ PASS / ⬜ FAIL

---

### Inline Code
1. Read through any lesson
2. Verify words like `print()` are highlighted in pink/purple
3. Verify they're distinct from regular text

**Status:** ⬜ PASS / ⬜ FAIL

---

### Formatting
1. Check headings are properly sized and colored
2. Check paragraphs have good spacing
3. Check lists are properly formatted
4. Check horizontal rules (---) display

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 4: Backward Compatibility ✅

### Progress Tracking Still Works
1. Mark Lesson 1 complete
2. Go to Progress tab
3. Verify stats show 1 completed
4. Refresh browser
5. Verify progress persists

**Status:** ⬜ PASS / ⬜ FAIL

---

### Button State Management
1. Mark Lesson 1 complete
2. Open Lesson 2
3. Verify button says "Mark as Complete" (not "✓ Completed")
4. Go back to Lesson 1
5. Verify button says "✓ Completed"

**Status:** ⬜ PASS / ⬜ FAIL

---

### Navigation Still Works
1. Test Lessons tab
2. Test Practice tab
3. Test Progress tab
4. Test Back to Lessons button
5. Test Next Lesson button

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 5: Performance ✅

### Initial Load
1. Open `http://localhost:8000` in new incognito window
2. Measure time to see homepage
3. Should be < 1 second

**Status:** ⬜ PASS / ⬜ FAIL

---

### Pyodide First Load
1. Click Practice tab
2. Click Run Code
3. Measure time to see output
4. Should be 3-5 seconds (first time only)

**Status:** ⬜ PASS / ⬜ FAIL

---

### Subsequent Runs
1. After Pyodide loaded, run code again
2. Should execute instantly (<1 second)

**Status:** ⬜ PASS / ⬜ FAIL

---

### Monaco Load
1. First time opening Practice tab
2. Should load in 1-2 seconds
3. Subsequent visits: instant

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 6: Cross-Browser ✅

Test in multiple browsers:

- [ ] **Chrome/Edge** - Primary browser
- [ ] **Firefox** - Alternative
- [ ] **Safari** (if available)

**For each browser, verify:**
- Homepage loads
- Lessons display correctly
- Python code executes
- Monaco editor works
- No console errors

**Browsers Tested:** ________________

**Status:** ⬜ PASS / ⬜ FAIL

---

## Test 7: Mobile Responsive ✅

1. Open DevTools (F12)
2. Click device toolbar (mobile icon)
3. Test various screen sizes:
   - Phone: 375x667
   - Tablet: 768x1024
   - Desktop: 1920x1080

**Verify:**
- Layout adapts properly
- Buttons are tappable
- Code editor usable
- Text readable

**Status:** ⬜ PASS / ⬜ FAIL

---

## 📊 Test Results Summary

**Date Tested:** _______________  
**Tested By:** _______________  
**Browser:** _______________  
**OS:** _______________

**Total Tests:** 7 categories, 20+ individual tests

**Results:**
- Tests Passed: ___ / 20+
- Tests Failed: ___
- Critical Issues: ___
- Minor Issues: ___

**Overall Status:** ⬜ PASS / ⬜ FAIL

---

## ✅ All Tests Must Pass Before Phase 2

If any test fails:
1. Document the issue
2. Review console errors (F12)
3. Check `PHASE_1_COMPLETE.md` for troubleshooting
4. Verify all files updated correctly
5. Check browser compatibility

---

## 🎉 Success Criteria

**Phase 1 is successful if:**
- [x] Real Python code executes (not simulation)
- [x] Loops and functions work
- [x] Monaco Editor shows syntax highlighting
- [x] Marked.js renders lessons correctly
- [x] No regression in existing features
- [x] Performance acceptable (<5s first load)
- [x] Zero cost maintained
- [x] All documentation updated

**If ALL tests pass:** ✅ **Ready for Phase 2!**

---

**Happy Testing! 🚀**




