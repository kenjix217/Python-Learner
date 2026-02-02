# AI Tutor Setup Guide

**Version:** 1.1.0  
**Feature:** Optional AI Tutoring  
**Status:** Admin-Configurable (Your API Key)

---

## 🎯 **Overview**

The AI Tutor is an **OPTIONAL** feature that provides interactive Q&A tutoring.

**Platform works 100% without it:**
- ✅ All 10 lessons available
- ✅ Python execution works
- ✅ Homework validation works
- ✅ Mastery progression works

**With AI Tutor (your API key):**
- ✅ Interactive Q&A
- ✅ Personalized help
- ✅ Guided learning (following `AI_TUTOR_RULES.md`)
- ✅ Context-aware responses

---

## 🔧 **Setup Instructions**

### **Step 1: Get an API Key**

You need an API key from ONE of these providers:

#### **Option A: OpenRouter (Recommended for Testing)**
1. Go to https://openrouter.ai/
2. Sign up for account
3. Get API key
4. **Free models available** (e.g., `meta-llama/llama-3.2-3b-instruct:free`)
5. Pay-as-you-go for better models

#### **Option B: OpenAI**
1. Go to https://platform.openai.com/
2. Sign up
3. Get API key
4. Models: gpt-3.5-turbo, gpt-4
5. **Paid** (credits required)

#### **Option C: Anthropic (Claude)**
1. Go to https://www.anthropic.com/
2. Sign up for API access
3. Get API key
4. Models: claude-3-haiku, claude-3-sonnet
5. **Paid** (credits required)

---

### **Step 2: Configure in Platform**

1. **Open the platform:** `http://localhost:8000`

2. **Go to Settings tab** (new tab in navigation)

3. **Enable AI Tutor:**
   - Check "Enable AI Tutor" checkbox

4. **Select Provider:**
   - Choose from dropdown (OpenRouter, OpenAI, Anthropic, or Custom)

5. **Enter YOUR API Key:**
   - Paste your API key in the "API Key" field
   - It's stored in your browser localStorage (private to you)

6. **Set Model (Optional):**
   - For OpenRouter free: `meta-llama/llama-3.2-3b-instruct:free`
   - For OpenAI: leave empty (uses gpt-3.5-turbo)
   - For Anthropic: leave empty (uses claude-3-haiku)

7. **Click "Save Settings"**

8. **See confirmation:** "✅ Settings saved successfully!"

---

### **Step 3: Use AI Tutor**

1. **Open any lesson** (e.g., Lesson 2: Variables)

2. **Look for "🤖 Ask AI Tutor" button** (appears after settings saved)

3. **Click the button** → Chat interface opens

4. **Ask a question:**
   - "What is a variable?"
   - "I don't understand loops, can you explain?"
   - "Why is my code not working?" (paste code)

5. **Get AI response** (intelligent, following teaching rules)

6. **Continue conversation** (AI remembers context)

---

## 🧪 **Testing with YOUR API Key**

### **Test 1: Basic Question**
```
You: "What is a variable?"

AI: "Great question! Instead of telling you directly, let me guide 
you. Think about a box with a label on it. You can put something 
inside and the label tells you what's in the box. Can you think 
of what that might mean in programming?"

[Guides you to discover the answer]
```

### **Test 2: Code Help**
```
You: "My loop isn't working: for i in range(5) print(i)"

AI: "I see the issue! In Python, after the colon in a for loop, 
the code must be on the next line and indented. What do you think 
you need to add after the colon?"

[Helps you debug without solving directly]
```

### **Test 3: Concept Confusion**
```
You: "I'm confused about the difference between lists and dictionaries"

AI: "Let me help clarify! A list is like a numbered row of boxes - 
you access items by position (0, 1, 2...). A dictionary is like 
labeled boxes - you access items by name. Can you think of when 
you'd want to use numbered access vs named access?"

[Adaptive explanation]
```

---

## ⚙️ **Configuration Options**

### **config.js Settings:**

```javascript
Config.ai = {
  enabled: true,  // Enable/disable AI
  provider: 'openrouter',  // Which API to use
  apiKey: 'YOUR-KEY-HERE',  // Your API key
  model: 'meta-llama/llama-3.2-3b-instruct:free',  // Model name
  temperature: 0.7,  // Creativity (0.0-1.0)
  maxTokens: 500  // Response length
};
```

**Providers Supported:**
- `'openrouter'` - Multiple models, has free options
- `'openai'` - GPT models (paid)
- `'anthropic'` - Claude models (paid)
- `'custom'` - Your own endpoint

---

## 🔒 **Security Notes**

### **Current (v1.1 - Testing):**
- API key stored in **browser localStorage**
- Only YOU can see it (on your device)
- **Acceptable for personal testing**
- **NOT for production with multiple users**

### **Future (v2.0 - SaaS):**
- API key stored on **backend server**
- Users never see the key
- Backend proxies AI calls
- **Secure and scalable**

**For now:** This is YOUR test instance, YOUR key, YOUR device = OK ✅

---

## 💰 **Cost Considerations**

### **Free Options:**
- **OpenRouter:** Has free models (limited, may be slow)
  - `meta-llama/llama-3.2-3b-instruct:free`
  - Good for testing

### **Paid Options:**
- **OpenRouter:** Pay-per-use ($0.001-0.05 per request)
- **OpenAI:** Credits required ($0.002-0.06 per request)
- **Anthropic:** Credits required ($0.001-0.015 per request)

**For Testing:**
- Start with OpenRouter free models
- Upgrade to paid if needed
- **You control the cost** (your API key, your budget)

---

## 🎓 **AI Tutor Behavior (Following AI_TUTOR_RULES.md)**

The system prompt instructs the AI to:

**Do:**
- ✅ Ask guiding questions before giving answers
- ✅ Encourage reasoning and experimentation
- ✅ Provide hints, not solutions
- ✅ Adapt explanations if student is confused
- ✅ Use simple, jargon-free language
- ✅ Reference specific lessons
- ✅ Celebrate correct thinking

**Don't:**
- ❌ Solve homework directly
- ❌ Give complete code solutions
- ❌ Skip conceptual understanding
- ❌ Use jargon without explanation

**The AI is configured to be a TUTOR, not a solver!** 🎓

---

## 🔧 **Troubleshooting**

### **"AI Tutor button doesn't appear"**
- Check Settings: Is "Enable AI Tutor" checked?
- Check API key: Is it entered and saved?
- Check browser console for errors (F12)

### **"Error connecting to AI"**
- Check API key is correct
- Check provider selection matches your key
- Check internet connection
- Check API provider status
- Check browser console for specific error

### **"AI responses are slow"**
- Free models are slower
- Upgrade to paid models for better performance
- Or accept slower responses (still functional)

### **"API key not saving"**
- Check browser allows localStorage
- Try different browser
- Check console for errors

---

## 🚀 **Quick Start**

**Fast setup (2 minutes):**

1. Get OpenRouter API key: https://openrouter.ai/
2. Open platform Settings tab
3. Enable AI Tutor ✓
4. Provider: OpenRouter
5. API Key: [paste your key]
6. Model: `meta-llama/llama-3.2-3b-instruct:free`
7. Save Settings
8. Go to any lesson → Click "🤖 Ask AI Tutor"
9. Ask: "Explain variables to me"
10. See intelligent response! 🤖

---

## 📝 **For Future SaaS Version**

**When you add user accounts + payment:**

**Free Tier Users:**
- No AI tutor access
- All other features available
- Can upgrade to paid tier

**Paid Tier Users (~$10/month):**
- AI tutor included
- Backend manages API key (secure)
- No user configuration needed
- Better models (faster, smarter)

**Migration Plan:**
- Move API key from localStorage → backend database
- Add tier checking (free vs paid)
- Frontend calls backend API proxy (not direct to LLM)
- **Current architecture supports this!** ✅

---

## ✅ **Platform Status**

**Without AI (Free Forever):**
- ✅ 10 complete lessons
- ✅ Real Python execution
- ✅ Homework validation
- ✅ Mastery progression
- ✅ Professional tools
- ✅ **Complete education platform!**

**With AI (Your Key for Testing):**
- ✅ Everything above PLUS
- ✅ Interactive Q&A
- ✅ Personalized help
- ✅ Adaptive tutoring
- ✅ **Enhanced learning experience!**

---

**Ready to test? Follow Quick Start above!** 🤖✅

**Your API key → Your cost → Your testing → Your decision to monetize later!**




