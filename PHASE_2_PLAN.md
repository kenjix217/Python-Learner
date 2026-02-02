# Phase 2: Enhanced Learning Features

**Start Date:** January 13, 2026  
**Status:** Planning & Verification  
**Estimated Duration:** 1-2 weeks

---

## 🎯 **Phase 2 Objectives**

Transform the platform from self-guided learning to **AI-assisted personalized tutoring** with:

1. **AI Tutor Integration** - Interactive Q&A, personalized help
2. **Voice Narration** - Audio playback of lessons
3. **Advanced Homework Validation** - Automated checking with test cases
4. **Expanded Curriculum** - Lessons 4-10 (beginner to intermediate)
5. **Mastery-Based Progression** - Gate lessons by understanding

---

## ⚠️ **CRITICAL: Compliance Requirements**

Per `FREE_TOOLS_AND_LICENSING.md` and `SYSTEM.md`:

**MUST verify BEFORE implementation:**
- ✅ License type (MIT, Apache 2.0, BSD, ISC preferred)
- ✅ Completely free OR free tier sufficient
- ✅ **NO credit card required** (non-negotiable)
- ✅ No hidden costs or future billing
- ✅ Usage limits clearly stated
- ✅ What happens when limits exceeded

**If ANY requirement unmet:** Do NOT proceed, find alternative

---

## 🔍 **Phase 2 Feature Analysis**

### Feature 1: AI Tutor (REQUIRES VERIFICATION)

**Requirements from `AI_TUTOR_RULES.md`:**
- Must guide, not solve (ask questions before giving answers)
- Follow 6-step lesson structure awareness
- Adapt to learner confusion
- Encourage reasoning before providing help
- Never auto-solve homework
- Teach debugging methodology

**Implementation Needs:**
- Chat interface for questions
- Context awareness (current lesson, user progress)
- Prompt engineering to follow teaching rules
- Rate limiting to prevent abuse
- Logging for quality control

**Options to Verify:**

#### Option 1: Web Speech API + Local Processing
- **What:** Browser built-in speech recognition
- **Cost:** Free (browser API)
- **Credit Card:** Not required
- **License:** Browser standard (free)
- **Limitations:** Not an AI tutor, just speech input
- **Status:** ⏳ Not suitable for AI tutoring (only for voice input)

#### Option 2: OpenRouter Free Tier
- **What:** API aggregator for multiple AI models
- **Cost:** Has free models available
- **Credit Card:** ⚠️ **MUST VERIFY** - May require CC for signup
- **Free Tier:** ⚠️ **MUST VERIFY** - Limits unknown
- **Status:** ⏳ **REQUIRES VERIFICATION** - Do NOT proceed until verified

#### Option 3: Hugging Face Inference API
- **What:** Free inference for open models
- **Cost:** Free tier available
- **Credit Card:** ⚠️ **MUST VERIFY** - Signup requirements unknown
- **Rate Limits:** ⚠️ **MUST VERIFY** - Unknown
- **Status:** ⏳ **REQUIRES VERIFICATION** - Do NOT proceed until verified

#### Option 4: Local LLM (llama.cpp WASM)
- **What:** Run small language model in browser
- **Cost:** Free (runs locally)
- **Credit Card:** Not required
- **License:** ⚠️ **MUST VERIFY** - Model licenses vary
- **Performance:** ⚠️ May be slow in browser
- **Status:** ⏳ **REQUIRES VERIFICATION** - Model license and size

#### Option 5: Ollama (Local Server)
- **What:** Run LLMs locally on user's machine
- **Cost:** Free (open source)
- **Credit Card:** Not required
- **License:** MIT
- **Requirements:** ⚠️ User must install software (violates web-first!)
- **Status:** ❌ **NOT COMPLIANT** - Requires installation

**DECISION REQUIRED:** Which option to pursue?

**Per SYSTEM.md:** "If license or cost information is unclear, state this and do not recommend."

**Current Status:** ⚠️ **BLOCKED** - Must verify AI options before proceeding

---

### Feature 2: Voice Narration (REQUIRES VERIFICATION)

**Requirements from `REQUIREMENTS.md`:**
- Optional (not required for completion)
- Play/pause/speed controls
- No audio required to complete lessons
- Voice-narratable content (already written)

**Options to Verify:**

#### Option 1: Web Speech API (Browser Built-In)
- **What:** Browser text-to-speech (free, built-in)
- **Cost:** Free (browser API)
- **Credit Card:** Not required
- **License:** Browser standard
- **Limitations:** 
  - Voice quality varies by browser
  - Limited voice options
  - Requires online connection
- **Status:** ✅ **LIKELY COMPLIANT** - Need to test implementation

#### Option 2: Google Cloud Text-to-Speech
- **Cost:** ⚠️ Has free tier BUT
- **Credit Card:** ⚠️ **LIKELY REQUIRED** for signup
- **Status:** ❌ **LIKELY NOT COMPLIANT** - Requires CC

#### Option 3: ElevenLabs
- **Cost:** Free tier exists
- **Credit Card:** ⚠️ **UNKNOWN**
- **Status:** ⏳ **REQUIRES VERIFICATION**

#### Option 4: Azure Speech Services
- **Cost:** Free tier exists
- **Credit Card:** ⚠️ **LIKELY REQUIRED**
- **Status:** ❌ **LIKELY NOT COMPLIANT**

**RECOMMENDED:** Start with Web Speech API (browser built-in, definitely compliant)

---

### Feature 3: Advanced Homework Validation (CAN PROCEED)

**Requirements:**
- Test cases for each homework assignment
- Compare student output to expected output
- Provide hints, not solutions
- Track attempts
- Gate progression on mastery

**Implementation:**
- ✅ Can use Pyodide (already integrated)
- ✅ No new dependencies needed
- ✅ Run student code + test code
- ✅ Compare results
- ✅ Provide feedback

**Status:** ✅ **CAN PROCEED** - No verification needed

---

### Feature 4: Expanded Curriculum (CAN PROCEED)

**Requirements from `REQUIREMENTS.md`:**

**Beginner Level (add):**
- Lesson 4: Conditions (if/else)
- Lesson 5: Loops (for/while)

**Intermediate Level (add):**
- Lesson 6: Functions
- Lesson 7: Lists and Dictionaries
- Lesson 8: File Handling
- Lesson 9: Error Handling
- Lesson 10: Intro to OOP

**Implementation:**
- ✅ Write lessons following 6-step structure (`AI_TUTOR_RULES.md`)
- ✅ Use established code-in-blocks format
- ✅ Include homework after each lesson
- ✅ Reflection questions

**Status:** ✅ **CAN PROCEED** - No verification needed

---

### Feature 5: Mastery-Based Progression (CAN PROCEED)

**Requirements:**
- Don't advance without conceptual mastery
- Reinforce weak areas
- Track understanding, not just completion

**Implementation:**
- ✅ Quiz questions per lesson
- ✅ Minimum score to unlock next lesson
- ✅ Retry mechanism
- ✅ Track attempts and scores

**Status:** ✅ **CAN PROCEED** - No verification needed

---

## 📋 **Phase 2 Implementation Order**

### **Tier 1: Can Start Immediately (No Verification Needed)**

1. ✅ **Expanded Curriculum** - Write Lessons 4-5 (beginner level)
   - No dependencies
   - Follow existing patterns
   - Use current tools
   - Estimated: 2-3 days

2. ✅ **Homework Validation** - Automated testing
   - Use existing Pyodide
   - Write test cases
   - Implement validation logic
   - Estimated: 1-2 days

3. ✅ **Mastery-Based Progression** - Quiz and gating
   - localStorage for scores
   - Quiz UI components
   - Progression logic
   - Estimated: 1-2 days

---

### **Tier 2: Requires Verification (Cannot Start Yet)**

4. ⏳ **Voice Narration** - Can likely use Web Speech API
   - Action: Test Web Speech API implementation
   - If works: Proceed
   - If not: Must verify alternatives
   - Estimated: 1 day (if Web Speech API works)

5. ⏳ **AI Tutor** - BLOCKED until verification
   - Action: Research and verify free AI options
   - Must find option with NO credit card requirement
   - Must verify free tier limits sufficient
   - If no compliant option exists: Defer or use rule-based chatbot
   - Estimated: Unknown (depends on what's available)

---

## 🚀 **Recommended Phase 2 Approach**

### **Strategy A: Start with Tier 1 Features (Recommended)**

**Week 1:**
- Day 1-2: Write Lessons 4-5 (Conditions and Loops)
- Day 3-4: Implement homework validation
- Day 5-6: Build mastery-based progression
- Day 7: Testing and documentation

**Week 2:**
- Day 1: Test Web Speech API for voice
- Day 2-3: Implement voice IF Web Speech works
- Day 4-7: Research AI options OR build rule-based helper

**Pros:**
- ✅ Can start immediately
- ✅ No compliance risk
- ✅ Delivers value quickly
- ✅ AI tutor becomes "nice to have" not blocker

---

### **Strategy B: Verify AI First, Then Proceed**

**Week 1:**
- Day 1-3: Research and verify AI API options
- Day 4-7: Only proceed if compliant option found

**Cons:**
- ⏳ Delays all progress
- ⏳ May find no compliant option
- ⏳ Wasted time if verification fails

**Not recommended per `SYSTEM.md` - "smallest change necessary"**

---

## 📝 **Recommended Next Steps**

**Following SYSTEM.md and all project guidelines:**

### **Step 1: Start with Tier 1 (This Session)**
1. Write Lesson 4: Conditions (if/else)
2. Write Lesson 5: Loops (for/while)
3. Both follow 6-step structure
4. Use established code-in-blocks format
5. Include homework and reflection

**Estimated Time:** 2-3 hours  
**Risk:** Zero (no dependencies)  
**Compliance:** 100% (follows existing patterns)

---

### **Step 2: Homework Validation (Next Session)**
1. Design test case structure
2. Implement validation engine (uses Pyodide)
3. Create validation UI
4. Add hints system

---

### **Step 3: Verify Voice/AI (Parallel Research)**
1. Test Web Speech API (likely compliant)
2. Research free AI options with NO CC requirement
3. Document findings
4. Only proceed if compliant option found

---

## ⚠️ **Compliance Warnings**

**Per FREE_TOOLS_AND_LICENSING.md:**

**PROHIBITED:**
- ❌ Paid services or subscriptions
- ❌ Free trials that convert to paid
- ❌ Services requiring credit card
- ❌ Proprietary software with licensing fees
- ❌ "Freemium" where core features require payment

**If we find NO compliant AI option:**
- Build rule-based chatbot instead
- Use pattern matching for common questions
- Link to lesson content
- Defer full AI to future (when more free options available)

**Per SYSTEM.md:**
- Must state uncertainty if unclear
- Do not proceed without verification
- Suggest alternatives if needed

---

## 🎯 **Phase 2 Success Criteria**

**Must Achieve (Tier 1):**
- [ ] Lessons 4-5 written (beginner level complete)
- [ ] Homework validation working
- [ ] Mastery-based progression implemented
- [ ] All tests passing
- [ ] Documentation complete

**Nice to Have (Tier 2):**
- [ ] Voice narration (if Web Speech API works)
- [ ] AI tutor (if compliant option found)

**If Tier 1 complete:** Phase 2 is successful  
**Tier 2:** Bonus features, not blockers

---

## 📖 **Decision Point**

**Choose Phase 2 approach:**

**Option A:** Start with Lesson 4 & 5 (recommended, can start now)  
**Option B:** Research AI options first (risky, may find nothing)  
**Option C:** Test Web Speech API first (voice narration)

**Per SYSTEM.md - "smallest change necessary":**  
→ **Recommend Option A** - Start with curriculum expansion

---

**Ready to proceed with Phase 2, Tier 1: Write Lessons 4-5?** 🚀

This follows:
- ✅ SYSTEM.md - Start with what we can do, not what's uncertain
- ✅ FREE_TOOLS_AND_LICENSING.md - No unverified dependencies
- ✅ REQUIREMENTS.md - Curriculum expansion is required
- ✅ ARCHITECTURE.md - Build progressively
- ✅ AI_TUTOR_RULES.md - Lessons follow established structure

**Shall I begin writing Lesson 4: Conditions (if/else)?** 📚




