# Python AI Tutor — Web-First Learning Platform

A web-based AI-assisted learning platform that teaches Python from complete beginner to intermediate level.

**Learn Python entirely from your web browser — no installation required.**

---

## 🎯 Project Goals

- Teach Python to absolute beginners with zero coding experience
- Provide interactive, hands-on learning with immediate feedback
- Use AI as a tutor that guides, not solves
- Make learning accessible through voice narration and clear explanations
- Track progress and mastery across sessions

---

## 📋 Documentation

Read these documents in priority order:

1. **[SYSTEM.md](SYSTEM.md)** — Root instructions and rules
2. **[FREE_TOOLS_AND_LICENSING.md](FREE_TOOLS_AND_LICENSING.md)** — Tooling constraints
3. **[REQUIREMENTS.md](REQUIREMENTS.md)** — Functional requirements
4. **[ARCHITECTURE.md](ARCHITECTURE.md)** — System design
5. **[CODING_STANDARDS.md](CODING_STANDARDS.md)** — Code conventions
6. **[AI_TUTOR_RULES.md](AI_TUTOR_RULES.md)** — Teaching methodology

---

## 🏗️ Project Structure

```
Python-Learner/
├── docs/                          # Project documentation (SYSTEM.md, etc.)
├── frontend/                      # Web application
│   ├── index.html                # Main entry point
│   ├── css/
│   │   └── styles.css            # Application styles
│   ├── js/
│   │   ├── app.js                # Main application logic
│   │   ├── lesson-viewer.js      # Lesson display
│   │   ├── code-editor.js        # Code execution
│   │   └── progress-tracker.js   # Progress management
│   ├── lessons/
│   │   ├── lesson-01.md          # What is Programming?
│   │   ├── lesson-02.md          # Variables and Data Types
│   │   └── lesson-03.md          # Input and Output
│   └── lib/                      # Third-party libraries (CDN for now)
│
├── backend/                       # API server (optional for MVP)
│   ├── main.py                   # FastAPI application
│   ├── requirements.txt          # Python dependencies
│   ├── services/
│   │   ├── lesson_service.py    # Lesson management
│   │   ├── homework_service.py  # Task evaluation
│   │   └── progress_service.py  # Progress tracking
│   └── models/
│       ├── user.py              # User model
│       └── progress.py          # Progress model
│
└── README.md                     # This file
```

---

## 🚀 Getting Started (MVP)

### Prerequisites

- Modern web browser (Chrome, Firefox, Safari, Edge)
- No installation required for MVP!

### Running Locally

1. **Clone or navigate to the project:**
   ```bash
   cd U:\Python-Learner
   ```

2. **Open the web app:**
   - Simply open `frontend/index.html` in your browser
   - Or use a local server:
     ```bash
     cd frontend
     python -m http.server 8000
     ```
   - Navigate to `http://localhost:8000`

3. **Start learning!**
   - Begin with Lesson 1
   - Complete guided practice
   - Try homework challenges

---

## 🛠️ Technology Stack

### Frontend (All Free/Open Source) - Phase 1 Complete ✅
- **HTML5/CSS3/JavaScript ES6** — Core web technologies
- **Pyodide v0.25.0** (MPL 2.0) — Python 3.11 in browser via WebAssembly ✅
- **Monaco Editor v0.45.0** (MIT) — VS Code editor in browser ✅
- **Marked.js** (MIT) — GitHub Flavored Markdown rendering ✅

### Backend (Optional, Phase 2)
- **Python 3.11+** — Server runtime
- **FastAPI** (MIT) — Web framework
- **SQLite** (Public Domain) — Database
- **Uvicorn** (BSD) — ASGI server

### Hosting (Free Tier)
- **Frontend:** GitHub Pages (static hosting)
- **Backend:** Render.com or Railway.app (no credit card required)

All tools comply with `FREE_TOOLS_AND_LICENSING.md`.

**Current Version:** 0.2.0 (Phase 1 Complete)

---

## 📚 Curriculum Overview

### Beginner Level ✅ COMPLETE (v0.3.0)
1. ✅ What is Programming?
2. ✅ Variables and Data Types
3. ✅ Input and Output
4. ✅ Conditions (if/else) ← NEW
5. ✅ Loops (for and while) ← NEW

### Intermediate Level
6. Functions
7. Lists and Dictionaries
8. File Handling
9. Error Handling
10. Introduction to Object-Oriented Programming

Each lesson follows the 6-step structure:
1. **Goal** — Learning objective
2. **Explanation** — Concept introduction
3. **Example** — Code demonstration
4. **Guided Practice** — Step-by-step task
5. **Homework** — Independent challenge
6. **Reflection** — Understanding check

---

## 🎓 Teaching Philosophy

- **Beginner-first:** Assumes zero prior experience
- **Guided learning:** AI asks questions, doesn't give answers
- **Mastery-focused:** Progress only when concepts are understood
- **Hands-on practice:** Every lesson includes coding exercises
- **Voice-ready:** All content can be narrated aloud

See `AI_TUTOR_RULES.md` for complete teaching methodology.

---

## 🔒 Privacy & Data

- **MVP:** All data stored locally in browser (localStorage)
- **Post-MVP:** Optional backend sync with anonymous progress tracking
- **No required authentication**
- **No personal data collection**
- **No tracking or analytics in MVP**

---

## 🧪 Development Roadmap

### Phase 0: MVP ✅ Complete (v0.1.0)
- [x] Project documentation
- [x] Basic frontend structure
- [x] 3 beginner lessons
- [x] Code editor UI
- [x] Local progress tracking

### Phase 1: Core Dependencies ✅ Complete (v0.2.0)
- [x] **Pyodide** - Real Python execution in browser
- [x] **Marked.js** - Professional markdown rendering
- [x] **Monaco Editor** - VS Code code editor
- [x] All existing features maintained
- [x] Zero cost, all open-source

### Phase 2: Enhanced Learning ✅ COMPLETE (v1.0.0)
**Tier 1 (Complete):**
- [x] **Lessons 4-5** - Conditions & Loops ✅
- [x] **Lesson 6** - Functions ✅
- [x] **Lesson 7** - Lists & Dictionaries ✅
- [x] **Lesson 8** - File Handling ✅
- [x] **Lesson 9** - Error Handling ✅
- [x] **Lesson 10** - Intro to OOP ✅
- [x] Homework validation engine ✅
- [x] Mastery-based progression gates ✅
- [x] **100% CURRICULUM COMPLETE!** 🎉

**Tier 2 (Optional Enhancements):**
- [ ] AI tutor integration (verification required)
- [ ] Voice narration (verification required)
- [ ] Community features (future)

### Phase 3: Scale & Polish (Future)
- [ ] Backend API deployment
- [ ] Multi-device progress sync
- [ ] PWA offline support
- [ ] Full intermediate curriculum
- [ ] Community features

---

## 🤝 Contributing

This project follows strict standards:
1. All code must comply with `CODING_STANDARDS.md`
2. All dependencies must comply with `FREE_TOOLS_AND_LICENSING.md`
3. All lessons must follow `AI_TUTOR_RULES.md`
4. Accuracy and correctness over speed (see `SYSTEM.md`)

---

## 📄 License

This project uses only free and open-source components.
See `FREE_TOOLS_AND_LICENSING.md` for tooling licenses.

Project code: MIT License (to be added)

---

## 🆘 Support

- Review lesson content in `frontend/lessons/`
- Check architecture in `ARCHITECTURE.md`
- Read teaching rules in `AI_TUTOR_RULES.md`
- Verify tool compliance in `FREE_TOOLS_AND_LICENSING.md`

---

**Built with Cursor AI** — Following systematic, beginner-focused design principles.

