# Testing Checklist

Use this checklist to verify the MVP is working correctly.

---

## 🚀 Pre-Test Setup

- [ ] Navigate to `U:\Python-Learner\frontend`
- [ ] Start local server: `python -m http.server 8000`
- [ ] Open browser to `http://localhost:8000`
- [ ] Open browser DevTools (F12) to monitor console

---

## ✅ Test 1: Initial Load

### Expected Behavior
- [ ] Page loads without errors
- [ ] Header displays "Python AI Tutor"
- [ ] Three navigation tabs visible: Lessons, Practice, Progress
- [ ] Lessons tab is active by default
- [ ] No console errors in DevTools

### How to Test
1. Load `http://localhost:8000`
2. Check browser console (F12 → Console tab)
3. Verify no red error messages

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 2: Lesson List View

### Expected Behavior
- [ ] Three lesson cards displayed
- [ ] Each card shows: number, title, description
- [ ] Cards are clickable (hover effect)
- [ ] "Your Learning Path" heading visible

### Lesson Card Details
1. **Lesson 1:** "What is Programming?"
2. **Lesson 2:** "Variables and Data Types"
3. **Lesson 3:** "Input and Output"

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 3: Open Lesson

### Expected Behavior
- [ ] Click on Lesson 1 card
- [ ] Lesson content view appears
- [ ] "Back to Lessons" button visible
- [ ] Lesson number and title displayed
- [ ] Full lesson content shows (Goal, Explanation, Example, etc.)
- [ ] "Mark as Complete" and "Next Lesson" buttons at bottom

### How to Test
1. Click on "Lesson 1: What is Programming?"
2. Scroll through entire lesson
3. Verify all 6 sections present:
   - Goal
   - Explanation
   - Example
   - Guided Practice
   - Homework
   - Reflection

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 4: Lesson Navigation

### Expected Behavior
- [ ] "Back to Lessons" returns to lesson list
- [ ] "Next Lesson" opens Lesson 2
- [ ] Navigation works for all three lessons
- [ ] Lesson 3 shows message when clicking "Next Lesson"

### How to Test
1. From Lesson 1, click "Next Lesson"
2. Verify Lesson 2 loads
3. Click "Back to Lessons"
4. Verify lesson list appears
5. Try navigating to each lesson

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 5: Code Editor (Practice Tab)

### Expected Behavior
- [ ] Click "Practice" tab
- [ ] Code editor textarea visible
- [ ] "Run Code" and "Clear" buttons present
- [ ] Output area shows "Output will appear here..."
- [ ] Placeholder text in editor

### How to Test
1. Click "Practice" tab in navigation
2. Type in editor: `print("Hello, Python!")`
3. Click "Run Code"
4. Verify placeholder message appears (Pyodide not yet integrated)
5. Click "Clear" and verify editor clears

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 6: Code Editor Features

### Expected Behavior
- [ ] Tab key inserts 4 spaces (not focus change)
- [ ] Ctrl+Enter (or Cmd+Enter) runs code
- [ ] "Clear Output" button works
- [ ] Text area is resizable

### How to Test
1. Type code in editor
2. Press Tab - should insert spaces
3. Press Ctrl+Enter - should run code
4. Click "Clear Output" - should clear output area

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 7: Progress Tracking

### Expected Behavior
- [ ] Click "Progress" tab
- [ ] Stats show: 0 completed, 3 remaining, 0% progress
- [ ] All lessons show "Not started"
- [ ] "Reset Progress" button visible

### How to Test
1. Click "Progress" tab
2. Verify stats display correctly
3. Check lesson progress list

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 8: Mark Lesson Complete

### Expected Behavior
- [ ] Open Lesson 1
- [ ] Click "Mark as Complete"
- [ ] Button changes to "✓ Completed"
- [ ] Button becomes disabled
- [ ] Success message appears
- [ ] Progress tab shows 1 completed

### How to Test
1. Go to Lessons tab
2. Open Lesson 1
3. Scroll to bottom
4. Click "Mark as Complete"
5. Go to Progress tab
6. Verify stats show 1 completed, 33% progress
7. Verify Lesson 1 shows checkmark

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 9: Progress Persistence

### Expected Behavior
- [ ] Progress persists after page refresh
- [ ] Completed lessons remain marked
- [ ] Stats remain accurate

### How to Test
1. Mark Lesson 1 as complete
2. Refresh the page (F5)
3. Go to Progress tab
4. Verify progress still shows 1 completed
5. Go to Lessons tab
6. Verify Lesson 1 shows "Completed" badge

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 10: Responsive Design

### Expected Behavior
- [ ] Desktop view (>768px) looks good
- [ ] Mobile view (<768px) is usable
- [ ] Navigation adapts to screen size
- [ ] Lesson content is readable on all screens
- [ ] Buttons are tappable on mobile

### How to Test
1. Open DevTools (F12)
2. Click device toolbar (phone icon)
3. Test various screen sizes:
   - Desktop: 1920x1080
   - Tablet: 768x1024
   - Mobile: 375x667
4. Verify layout adjusts properly

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 11: Keyboard Navigation

### Expected Behavior
- [ ] Tab key navigates through interactive elements
- [ ] Focus indicators visible
- [ ] Enter key activates buttons
- [ ] Navigation accessible via keyboard

### How to Test
1. Click in browser address bar
2. Press Tab repeatedly
3. Verify focus moves through elements
4. Press Enter on focused button
5. Verify action executes

**Status:** ⬜ Pass / ⬜ Fail

---

## ✅ Test 12: Browser Compatibility

### Expected Behavior
- [ ] Works in Chrome/Edge
- [ ] Works in Firefox
- [ ] Works in Safari (if available)
- [ ] No layout issues
- [ ] No console errors

### How to Test
1. Test in at least 2 different browsers
2. Perform basic navigation in each
3. Check console for errors
4. Verify progress tracking works

**Browsers Tested:**
- [ ] Chrome/Edge
- [ ] Firefox
- [ ] Safari
- [ ] Other: __________

**Status:** ⬜ Pass / ⬜ Fail

---

## 🐛 Issue Tracking

### Issues Found

| Test # | Issue Description | Severity | Status |
|--------|------------------|----------|--------|
| | | | |
| | | | |

**Severity Levels:**
- 🔴 Critical - App doesn't work
- 🟡 Major - Feature broken
- 🟢 Minor - Cosmetic issue

---

## ✅ Final Checklist

Before moving to Phase 1 (adding dependencies):

- [ ] All 12 tests passed
- [ ] No console errors
- [ ] Progress tracking works
- [ ] All lessons load correctly
- [ ] Navigation works smoothly
- [ ] Responsive design verified
- [ ] Keyboard navigation works
- [ ] At least 2 browsers tested

---

## 📝 Test Results Summary

**Date Tested:** _______________  
**Tested By:** _______________  
**Browser:** _______________  
**OS:** _______________

**Overall Status:** ⬜ PASS / ⬜ FAIL

**Tests Passed:** ___ / 12  
**Tests Failed:** ___ / 12

**Critical Issues:** ___  
**Major Issues:** ___  
**Minor Issues:** ___

---

## 🎯 Next Steps After Testing

### If All Tests Pass ✅
1. Proceed to Phase 1: Add Dependencies
   - Integrate Pyodide
   - Add Marked.js
   - Add Monaco Editor
2. Test Python code execution
3. Test enhanced Markdown rendering

### If Tests Fail ❌
1. Review console errors
2. Check file paths
3. Verify server is running on correct port
4. Check browser compatibility
5. Review QUICK_START.md for troubleshooting

---

## 📞 Getting Help

If tests fail and you can't resolve:
1. Check browser console (F12)
2. Review `PROJECT_SETUP.md` troubleshooting section
3. Verify all files exist in correct locations
4. Check `QUICK_START.md` for common issues
5. Review `CODING_STANDARDS.md` for code quality

---

**Ready to test?** Follow this checklist systematically and document any issues found.

**Good luck! 🚀**




