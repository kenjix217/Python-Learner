# Installing Real Python - Complete Guide

**Purpose:** Prepare for Lessons 11-22 (Advanced/Expert Level)  
**Required For:** External libraries, Flask, databases, deployment  
**Time:** 10-15 minutes

---

## 🎯 **Why Install Real Python?**

**Lessons 1-10 (Browser-Based):**
- ✅ Run in your browser (Pyodide)
- ✅ No installation needed
- ✅ Perfect for learning basics
- ✅ All fundamentals covered

**Lessons 11-22 (Real Python Needed):**
- External libraries (pip install)
- Web frameworks (Flask, Django)
- Database operations (SQLite, PostgreSQL)
- File system operations (full access)
- Deployment and production
- **Real-world development!**

**You need real Python installed on your computer for advanced lessons.**

---

## 💻 **Step 1: Download Python**

### **Official Python Website:**
🔗 **https://www.python.org/downloads/**

**What to download:**
- **Latest Version:** Python 3.11 or 3.12 (recommended)
- **Minimum:** Python 3.9+
- **Choose:** Installer for your operating system

---

### **Windows Users:**

1. **Download:** Python 3.12.x Windows installer (64-bit)
   - Link: https://www.python.org/downloads/windows/

2. **Run installer**
   - ✅ **IMPORTANT:** Check "Add Python to PATH" (critical!)
   - Click "Install Now"
   - Wait for installation (2-3 minutes)

3. **Verify installation:**
   ```powershell
   python --version
   ```
   **Expected:** `Python 3.12.x`

4. **Verify pip:**
   ```powershell
   pip --version
   ```
   **Expected:** `pip 23.x.x from...`

**✅ Done! Python installed on Windows**

---

### **Mac Users:**

1. **Download:** Python 3.12.x macOS installer
   - Link: https://www.python.org/downloads/macos/

2. **Run .pkg installer**
   - Follow installation wizard
   - Default settings are fine

3. **Verify installation:**
   ```bash
   python3 --version
   ```
   **Expected:** `Python 3.12.x`

4. **Verify pip:**
   ```bash
   pip3 --version
   ```

**Note:** On Mac, use `python3` and `pip3` (not `python` and `pip`)

**✅ Done! Python installed on Mac**

---

### **Linux Users:**

**Most Linux has Python pre-installed, but may be older version.**

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

**Fedora:**
```bash
sudo dnf install python3.11 python3-pip
```

**Verify:**
```bash
python3 --version
pip3 --version
```

**✅ Done! Python installed on Linux**

---

## 🛠️ **Step 2: Install a Code Editor (IDE)**

**You need a code editor for writing Python outside the browser.**

### **Recommended: Visual Studio Code (Free)**

**Download:** https://code.visualstudio.com/

**Why VS Code:**
- ✅ Free and open-source
- ✅ Python extension available
- ✅ Syntax highlighting
- ✅ Debugging tools
- ✅ Terminal built-in
- ✅ Most popular Python IDE

**After installing VS Code:**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search "Python"
4. Install "Python" by Microsoft
5. Restart VS Code

**✅ Done! Ready to write Python code**

---

### **Alternative Editors (Also Good):**

**PyCharm Community (Free):**
- https://www.jetbrains.com/pycharm/download/
- Full-featured Python IDE
- Great for beginners
- More heavy-weight than VS Code

**Sublime Text (Free):**
- https://www.sublimetext.com/
- Lightweight and fast
- Good for simple projects

**IDLE (Comes with Python):**
- Already installed
- Very simple
- Good for quick testing

**Use whatever you're comfortable with!**

---

## 📦 **Step 3: Understanding pip (Package Manager)**

**pip** installs Python libraries (packages).

### **Basic pip Commands:**

**Install a package:**
```bash
pip install requests
```

**Install multiple packages:**
```bash
pip install flask pandas matplotlib
```

**Install from requirements.txt:**
```bash
pip install -r requirements.txt
```

**List installed packages:**
```bash
pip list
```

**Uninstall a package:**
```bash
pip uninstall requests
```

**Upgrade a package:**
```bash
pip install --upgrade requests
```

---

## 🌐 **Step 4: Virtual Environments (Important!)**

**What is a virtual environment?**
- Isolated Python environment for each project
- Each project has its own packages
- Prevents conflicts between projects

**Why use them:**
- Project A needs Django 3.x
- Project B needs Django 4.x
- Virtual environments keep them separate!

### **Creating Virtual Environment:**

**Windows:**
```powershell
# Navigate to your project folder
cd C:\Users\YourName\my_project

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate

# You'll see (venv) in terminal prompt
```

**Mac/Linux:**
```bash
# Navigate to your project folder
cd ~/my_project

# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# You'll see (venv) in terminal prompt
```

**When activated:**
```bash
(venv) $ pip install flask
# Installs ONLY in this environment
```

**Deactivate:**
```bash
deactivate
```

---

## 🧪 **Step 5: Test Your Installation**

### **Test 1: Python Works**

**Create file:** `test.py`
```python
print("Hello from real Python!")
print(f"Python version: {__import__('sys').version}")
```

**Run it:**
```bash
python test.py
```

**Expected:**
```
Hello from real Python!
Python version: 3.12.x ...
```

---

### **Test 2: pip Works**

```bash
pip install requests
```

**Expected:** Downloads and installs successfully

**Test the package:**
```python
import requests
print("Requests library works!")
```

---

### **Test 3: Virtual Environment Works**

```bash
# Create venv
python -m venv test_venv

# Activate (Windows)
test_venv\Scripts\activate

# Or activate (Mac/Linux)
source test_venv/bin/activate

# Install something
pip install flask

# Check it's installed
pip list

# Deactivate
deactivate
```

**If all tests pass:** ✅ **Ready for advanced lessons!**

---

## 📋 **Checklist: Ready for Lesson 11+**

**Installation:**
- [ ] Python 3.9+ installed
- [ ] `python --version` works
- [ ] `pip --version` works
- [ ] Code editor installed (VS Code recommended)
- [ ] Python extension in VS Code

**Skills:**
- [ ] Can create .py files
- [ ] Can run Python scripts from terminal
- [ ] Can install packages with pip
- [ ] Can create virtual environments
- [ ] Can activate/deactivate venv

**If all checked:** ✅ **You're ready!**

---

## 🚀 **What You'll Build in Lessons 11-22**

**With real Python, you can:**
- Install any library (400,000+ on PyPI!)
- Build web applications (Flask, FastAPI)
- Connect to databases (PostgreSQL, MongoDB)
- Make API calls (requests library)
- Process large datasets (pandas)
- Create visualizations (matplotlib)
- Automate tasks (schedule, selenium)
- Deploy to cloud (Heroku, AWS, Azure)
- **Build production applications!**

**This is professional Python development!** 💼

---

## 🆘 **Troubleshooting**

### **Problem: "python not found" after installation**

**Windows:**
- Reinstall Python
- ✅ Check "Add Python to PATH"
- Restart terminal

**Mac:**
- Use `python3` instead of `python`
- Add alias: `alias python=python3`

---

### **Problem: "pip not found"**

**Solution:**
```bash
python -m pip --version
```

Use `python -m pip install` instead of just `pip install`

---

### **Problem: Permission errors when installing**

**Don't use sudo/admin!** Use virtual environments instead.

**Or (not recommended):**
```bash
pip install --user packagename
```

---

### **Problem: Multiple Python versions**

**Check which Python you're using:**
```bash
which python     # Mac/Linux
where python     # Windows
```

**Use specific version:**
```bash
python3.11 --version
python3.11 -m pip install flask
```

---

## 💡 **Best Practices**

**1. Always use virtual environments:**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
```

**2. Create requirements.txt:**
```bash
pip freeze > requirements.txt
```

**3. Use .gitignore:**
```
venv/
__pycache__/
*.pyc
.env
```

**4. Update pip regularly:**
```bash
python -m pip install --upgrade pip
```

---

## 🎓 **Learning Path**

**Current (Lessons 1-10):**
- Browser-based (Pyodide)
- No installation needed
- Learn fundamentals

**Next (Lessons 11-22):**
- Real Python installation
- External libraries
- Professional development
- Deploy real applications

**Transition point:** After completing Lesson 10!

---

## 📖 **Additional Resources**

**Official Documentation:**
- Python Tutorial: https://docs.python.org/3/tutorial/
- pip Documentation: https://pip.pypa.io/
- Virtual Environments: https://docs.python.org/3/tutorial/venv.html

**Video Tutorials:**
- Python.org: https://www.python.org/about/gettingstarted/
- Real Python: https://realpython.com/installing-python/

**Community:**
- r/learnpython: https://www.reddit.com/r/learnpython/
- Python Discord: https://pythondiscord.com/
- Stack Overflow: https://stackoverflow.com/questions/tagged/python

---

## ✅ **Ready to Continue!**

**Once Python is installed:**
1. ✅ Complete Lessons 1-10 in browser (master fundamentals)
2. ✅ Install real Python (follow this guide)
3. ✅ Start Lesson 11 (external libraries)
4. ✅ Continue through Lesson 22 (expert level)
5. ✅ Build real applications!
6. ✅ **Become a professional Python developer!**

---

**This guide prepares you for the advanced curriculum. Take your time with installation - it's a one-time setup that opens unlimited possibilities!** 🚀

**Need help? All major platforms covered. Follow step-by-step and you'll be ready!** 💪✅




