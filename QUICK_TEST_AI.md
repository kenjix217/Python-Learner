# Quick Test AI Tutor - Complete Guide

**Version:** 1.1.0  
**Time:** 5 minutes  
**Status:** Ready to test with YOUR API key

---

## ⚡ **FASTEST WAY TO START**

### **Option A: Use Batch Script (Windows)**

1. **Double-click:** `START_WITH_AI.bat`
2. **Wait:** Both servers start automatically
3. **Browser opens:** localhost:3000
4. **Done!** Servers running

---

### **Option B: Manual (2 Terminals)**

**Terminal 1:**
```powershell
cd U:\Python-Learner\backend
.\venv\Scripts\activate
pip install -r requirements.txt  # First time only
python main.py
```

**Terminal 2:**
```powershell
cd U:\Python-Learner\frontend
python -m http.server 3000
```

**Browser:**
```
http://localhost:3000
```

---

## 🔧 **Configure AI (One Time)**

1. **Settings tab**
2. **Enable AI Tutor** ✓
3. **Provider:** Custom Endpoint
4. **API Key:** [YOUR KEY - the one you have]
5. **Model:** anthropic-claude-sonnet-latest
6. **Custom Endpoint:** `https://api.point72.internal/v1/chat/completions`
7. **Save Settings**

---

## 🧪 **Test AI Tutor**

### **Test 1: Basic Question**
1. **Lessons → Open Lesson 2**
2. **Click "🤖 Ask AI Tutor"**
3. **Type:** "What is a variable?"
4. **Send**
5. **Check backend terminal** - should see request
6. **Wait for response** (5-15 seconds)
7. **See AI answer!** 🤖

**Expected:** Intelligent explanation that guides you

---

### **Test 2: Verify Teaching Style**
**Ask:** "Can you solve the homework for me?"

**Expected:** AI refuses and offers hints instead

**This proves:** AI follows `AI_TUTOR_RULES.md` ✅

---

### **Test 3: Debugging Help**
**Ask:** "My loop gives an error: for i in range(5) print(i)"

**Expected:** AI asks guiding questions, doesn't just fix it

---

## ✅ **Success Indicators**

**Backend Terminal Shows:**
```
INFO: 127.0.0.1:xxxxx - "POST /api/ai/chat HTTP/1.1" 200 OK
```

**Frontend Shows:**
- AI response in chat
- Conversation continues
- Context maintained

**This means:** ✅ **WORKING!**

---

## 🐛 **If Issues**

### **"Cannot connect to backend"**
- Check backend terminal is running
- URL should show: `http://0.0.0.0:8000`

### **"Failed to fetch"**
- Check both servers running
- Frontend on 3000, backend on 8000
- Check browser at localhost:**3000** (not 8000!)

### **Backend shows error**
- Check API key is correct
- Check internal API is reachable
- Check endpoint URL matches your API
- Read error in backend terminal

---

## 📊 **Request Flow**

**What Happens:**
```
1. Student types: "What is a variable?"
2. Frontend sends to: localhost:8000/api/ai/chat
3. Backend receives request
4. Backend calls: api.point72.internal (your API)
5. Your API responds with Claude answer
6. Backend returns to frontend
7. Student sees answer
```

**Time:** 5-15 seconds total  
**CORS:** Solved by backend proxy ✅

---

## 🎯 **Verify It Works**

**Backend Terminal Should Show:**
```
INFO: Application startup complete
INFO: 127.0.0.1 - "POST /api/ai/chat HTTP/1.1" 200 OK
```

**Browser Console (F12) Should Show:**
```
✅ AI Tutor: Enabled
   Provider: custom
   Model: anthropic-claude-sonnet-latest
```

**Chat Should Show:**
```
[Your question]
[AI intelligent response]
```

**If all three:** ✅ **AI TUTOR WORKS!**

---

## 💡 **Tips**

**1. Check Backend Logs**
- Backend terminal shows all requests
- Errors will appear there
- Helpful for debugging

**2. Test with Simple Question First**
- "What is Python?"
- Verify connection works
- Then try complex questions

**3. Check API Response Format**
- Your internal API might return different format
- Backend tries to handle multiple formats
- If issues, check backend terminal error

---

## 🎊 **You're Ready!**

**Run:**
1. `START_WITH_AI.bat` (auto-starts both)
   OR
2. Two terminals manually

**Configure:**
- Settings → YOUR API key

**Test:**
- Ask AI Tutor questions
- Verify intelligent responses

**Result:**
- ✅ Complete platform
- ✅ AI tutoring working
- ✅ CORS solved
- ✅ Production architecture

---

**🚀 Start the servers and test AI tutor NOW!** 🤖✅




