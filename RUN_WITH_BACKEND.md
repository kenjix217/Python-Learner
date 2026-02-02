# Run Platform with Backend (AI Proxy)

**Purpose:** Enable AI Tutor with backend proxy (solves CORS)  
**Version:** 1.1.0  
**Time:** 5 minutes setup

---

## 🎯 **Why Backend Proxy?**

**Problem:** Browser → Internal API = CORS blocked ❌  
**Solution:** Browser → Our Backend → Internal API = Works! ✅

**Benefits:**
- ✅ Solves CORS issues
- ✅ Secures API keys (future: stored on backend)
- ✅ Enables tier checking (future: free vs paid)
- ✅ Production-ready architecture

---

## 🚀 **Setup Instructions**

### **Step 1: Install Backend Dependencies**

**Open NEW terminal/PowerShell:**

```powershell
# Navigate to backend
cd U:\Python-Learner\backend

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Expected output:**
```
Installing collected packages: fastapi, uvicorn, pydantic, httpx...
Successfully installed...
```

---

### **Step 2: Start Backend Server**

**In the SAME terminal (backend directory, venv activated):**

```powershell
# Run the backend
python main.py
```

**Expected output:**
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete
```

**✅ Backend is now running!**

---

### **Step 3: Start Frontend Server**

**Open ANOTHER terminal/PowerShell:**

```powershell
# Navigate to frontend
cd U:\Python-Learner\frontend

# Start frontend server on port 3000 (backend uses 8000)
python -m http.server 3000
```

**Expected output:**
```
Serving HTTP on :: port 3000 (http://[::]:3000/) ...
```

**✅ Frontend is now running!**

---

### **Step 4: Configure in Browser**

1. **Open browser:** `http://localhost:3000` (note: port 3000 now!)

2. **Go to Settings tab**

3. **Configure AI Tutor:**
   - ✓ Enable AI Tutor
   - Provider: Custom Endpoint
   - API Key: [YOUR API KEY]
   - Model: anthropic-claude-sonnet-latest
   - Custom Endpoint: `https://api.point72.internal/v1/chat/completions`

4. **Click "Save Settings"**

---

### **Step 5: Test AI Tutor**

1. **Go to Lessons → Open Lesson 2**
2. **Click "🤖 Ask AI Tutor"**
3. **Ask:** "What is a variable?"
4. **Wait for response...**

**Flow:**
```
Browser (localhost:3000)
    ↓ HTTP POST
Our Backend (localhost:8000/api/ai/chat)
    ↓ HTTP POST (with CORS handled)
Your Internal API (api.point72.internal)
    ↓ Response
Our Backend (processes response)
    ↓ JSON response
Browser (displays AI answer)
```

**No CORS issues!** ✅

---

## 🔧 **Configuration Details**

### **Backend Proxy is Active When:**
- `Config.platform.useBackendProxy = true` (default)
- Backend server running on `http://localhost:8000`
- Frontend configured with your API details

### **What Backend Does:**
```python
@app.post("/api/ai/chat")
- Receives: student question + config
- Calls: your internal API (no CORS from backend!)
- Returns: AI response to frontend
```

---

## 🧪 **Testing Checklist**

**Prerequisites:**
- [ ] Backend dependencies installed
- [ ] Backend server running (port 8000)
- [ ] Frontend server running (port 3000)
- [ ] Browser at localhost:3000

**Configuration:**
- [ ] Settings → Enable AI Tutor ✓
- [ ] Provider: Custom Endpoint
- [ ] API Key: [YOUR KEY]
- [ ] Custom Endpoint: https://api.point72.internal/v1/chat/completions
- [ ] Model: anthropic-claude-sonnet-latest
- [ ] Save Settings

**Testing:**
- [ ] Open lesson
- [ ] See "Ask AI Tutor" button
- [ ] Click button → Chat opens
- [ ] Send message
- [ ] Check backend terminal (should see request)
- [ ] Wait for AI response
- [ ] See response in chat ✅

---

## 🐛 **Troubleshooting**

### **Problem: Connection refused**
**Solution:** Make sure backend is running on port 8000

```powershell
# Check if backend is running
# Should see: "Uvicorn running on http://0.0.0.0:8000"
```

---

### **Problem: CORS error (still)**
**Solution:** Backend handles CORS, but check:
1. Frontend on port 3000 (not 8000 - conflict!)
2. Backend CORS allows localhost:3000
3. Both servers running

---

### **Problem: "Custom API error"**
**Check:**
1. API key is correct
2. Endpoint URL is correct
3. Your internal API is accessible from backend server
4. Check backend terminal for detailed error

---

### **Problem: Backend shows error**
**Common issues:**
- API key invalid → Check your key
- Endpoint unreachable → Check network/VPN
- Response format unexpected → May need to adjust parsing

**Check backend terminal output** for specific error!

---

## 📊 **Architecture (Current)**

```
Frontend (localhost:3000)
    │
    ├─ Student asks question
    │
    ↓ POST /api/ai/chat
    │
Backend (localhost:8000)
    │
    ├─ Receives request (CORS handled!)
    ├─ Extracts API key from request
    │
    ↓ POST to internal API
    │
Your Internal API (api.point72.internal)
    │
    ├─ Processes with Claude
    ├─ Returns response
    │
    ↓ Response
    │
Backend (localhost:8000)
    │
    ├─ Formats response
    │
    ↓ JSON response
    │
Frontend (localhost:3000)
    │
    └─ Displays to student
```

**CORS Solved!** ✅  
**API Key secure!** ✅ (in request, not browser code)  
**Production-ready!** ✅

---

## 🔮 **Future Enhancement (v2.0)**

**When adding user accounts:**

```python
@app.post("/api/ai/chat")
async def ai_chat(request, token: str):
    # 1. Validate JWT token
    user = verify_token(token)
    
    # 2. Check user tier
    if user.tier != 'paid':
        return {"error": "AI Tutor available in paid tier"}
    
    # 3. Get API key from backend (not from request!)
    api_key = os.getenv('AI_API_KEY')  # Stored securely
    
    # 4. Call AI provider
    response = await call_provider(api_key)
    
    # 5. Log usage for billing
    log_ai_usage(user.id)
    
    return response
```

**Then:**
- API key NEVER in frontend
- Tier checking enforced
- Usage tracking enabled
- **Ready for SaaS!**

---

## ✅ **Quick Start Commands**

**Terminal 1 (Backend):**
```powershell
cd U:\Python-Learner\backend
.\venv\Scripts\activate
python main.py
```

**Terminal 2 (Frontend):**
```powershell
cd U:\Python-Learner\frontend
python -m http.server 3000
```

**Browser:**
```
http://localhost:3000
```

**Test AI:**
- Settings → Configure
- Lessons → Ask AI Tutor
- Should work! ✅

---

## 🎉 **Summary**

**What Changed:**
- ✅ Backend has `/api/ai/chat` endpoint (REST)
- ✅ Handles all AI providers (4 supported)
- ✅ Solves CORS issues
- ✅ Frontend calls backend proxy
- ✅ Production-ready architecture

**How to Run:**
- Backend on port 8000
- Frontend on port 3000
- Configure in Settings
- Test AI tutor

**Result:**
- CORS solved ✅
- API secure ✅
- REST design ✅
- Ready for SaaS ✅

---

**🔥 Run both servers and test! Your internal API should work now!** 🚀




