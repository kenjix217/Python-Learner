# Project Setup Guide

This document provides instructions for setting up and running the Python AI Tutor application.

---

## Directory Structure

```
Python-Learner/
├── docs/
│   ├── SYSTEM.md                    # Root instructions
│   ├── FREE_TOOLS_AND_LICENSING.md  # Tooling constraints
│   ├── REQUIREMENTS.md              # Functional requirements
│   ├── ARCHITECTURE.md              # System design
│   ├── CODING_STANDARDS.md          # Code conventions
│   └── AI_TUTOR_RULES.md            # Teaching methodology
│
├── frontend/                         # Web application
│   ├── index.html                   # Main HTML file
│   ├── css/
│   │   └── styles.css               # Application styles
│   ├── js/
│   │   ├── app.js                   # Main app logic
│   │   ├── lesson-viewer.js         # Lesson display
│   │   ├── code-editor.js           # Code execution
│   │   └── progress-tracker.js      # Progress management
│   ├── lessons/
│   │   ├── lesson-01.md             # What is Programming?
│   │   ├── lesson-02.md             # Variables and Data Types
│   │   └── lesson-03.md             # Input and Output
│   └── lib/                         # Third-party libraries (to be added)
│
├── backend/                          # API server (optional for MVP)
│   ├── main.py                      # FastAPI application
│   ├── requirements.txt             # Python dependencies
│   ├── services/
│   │   ├── __init__.py
│   │   ├── lesson_service.py       # Lesson management
│   │   └── progress_service.py     # Progress tracking
│   └── models/
│       ├── __init__.py
│       ├── user.py                 # User model
│       └── progress.py             # Progress model
│
├── .gitignore                       # Git ignore rules
├── README.md                        # Project overview
└── PROJECT_SETUP.md                 # This file
```

---

## MVP Setup (Frontend Only)

The MVP runs entirely in the browser with no backend required.

### Quick Start

1. **Navigate to the project:**
   ```bash
   cd U:\Python-Learner
   ```

2. **Open the application:**
   - **Option A (Simple):** Double-click `frontend/index.html`
   - **Option B (Recommended):** Use a local web server:
     ```bash
     cd frontend
     python -m http.server 8000
     ```
   - Open browser to `http://localhost:8000`

3. **Start learning!**
   - Browse lessons in the Lessons tab
   - Practice code in the Practice tab
   - Track progress in the Progress tab

### Browser Requirements

- Modern browser (Chrome 90+, Firefox 88+, Safari 14+, Edge 90+)
- JavaScript enabled
- LocalStorage enabled (for progress tracking)

---

## Full Setup (With Backend)

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Modern web browser

### Backend Setup

1. **Create virtual environment:**
   ```bash
   cd backend
   python -m venv venv
   ```

2. **Activate virtual environment:**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the backend server:**
   ```bash
   python main.py
   ```
   
   Server will start at `http://localhost:8000`

5. **Test the API:**
   - Open browser to `http://localhost:8000/docs`
   - You'll see interactive API documentation

### Frontend Setup (with Backend)

1. **Update frontend to use backend API** (future enhancement)
2. **For now, frontend works independently**

---

## Development Workflow

### Working on Frontend

1. **Edit files in `frontend/` directory**
2. **Refresh browser to see changes**
3. **Check browser console for errors** (F12)

### Working on Backend

1. **Edit files in `backend/` directory**
2. **Server auto-reloads with changes** (when using `uvicorn --reload`)
3. **Test endpoints at** `http://localhost:8000/docs`

### Adding Lessons

1. **Create new markdown file** in `frontend/lessons/`
2. **Follow 6-step structure** (see `AI_TUTOR_RULES.md`)
3. **Update lesson list** in `frontend/js/app.js`
4. **Test lesson loads correctly**

---

## Testing Checklist

- [ ] Homepage loads without errors
- [ ] All three lessons display correctly
- [ ] Code editor accepts input
- [ ] "Run Code" button responds (shows placeholder message)
- [ ] Progress tracking saves to localStorage
- [ ] Marking lessons complete updates progress view
- [ ] Navigation between tabs works smoothly
- [ ] Responsive design works on mobile
- [ ] Keyboard navigation works

---

## Next Steps (Post-Scaffolding)

### Phase 1: Core Dependencies
- [ ] Integrate Pyodide for in-browser Python execution
- [ ] Add Marked.js for proper Markdown rendering
- [ ] Add Monaco Editor for enhanced code editing

### Phase 2: Enhanced Features
- [ ] Add AI tutor integration (verify free API)
- [ ] Add text-to-speech for lesson narration
- [ ] Implement homework validation logic
- [ ] Add mastery-based progression gates

### Phase 3: Deployment
- [ ] Deploy frontend to GitHub Pages
- [ ] Deploy backend to free hosting (Render/Railway)
- [ ] Set up continuous integration
- [ ] Add analytics (privacy-preserving)

---

## Troubleshooting

### Frontend Issues

**Problem:** Lessons not loading
- **Solution:** Check browser console for errors
- Ensure you're running from a web server (not `file://`)
- Verify lesson files exist in `frontend/lessons/`

**Problem:** Progress not saving
- **Solution:** Check browser allows localStorage
- Clear localStorage and try again: `localStorage.clear()`

### Backend Issues

**Problem:** Cannot install dependencies
- **Solution:** Ensure Python 3.11+ is installed
- Try upgrading pip: `pip install --upgrade pip`
- Use virtual environment

**Problem:** Port 8000 already in use
- **Solution:** Change port in `main.py` or stop other process
- On Windows: `netstat -ano | findstr :8000`

---

## License Compliance

All dependencies comply with `FREE_TOOLS_AND_LICENSING.md`:
- FastAPI: MIT License
- Uvicorn: BSD License
- Pydantic: MIT License
- Pyodide (future): MPL 2.0
- Monaco Editor (future): MIT License
- Marked.js (future): MIT License

---

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pyodide Documentation](https://pyodide.org/)
- [Monaco Editor](https://microsoft.github.io/monaco-editor/)
- [Web Accessibility Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

**Ready to build!** The project structure is complete and ready for development.




