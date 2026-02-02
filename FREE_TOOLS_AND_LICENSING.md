# FREE_TOOLS_AND_LICENSING.md

This document defines **non‑negotiable constraints** for tools, services, libraries, and dependencies used in this project.

All recommendations and implementations MUST comply with these rules.

---

## 1. Allowed Cost Models

Any tool, service, library, or dependency MUST meet **at least one** of the following:

- Completely free with no payment required
- Open source with a permissive license (MIT, Apache 2.0, BSD, ISC)
- Free tier sufficient for personal or hobby use with **no credit card required**

If a tool does not clearly meet one of these criteria, it MUST NOT be recommended or used.

---

## 2. Prohibited Tools and Services

The following are explicitly prohibited:

- Paid services or subscriptions
- Free trials that convert to paid plans
- Services requiring a credit card for signup
- Proprietary software with licensing fees
- “Freemium” tools where core functionality requires payment

---

## 3. License Verification Requirements

Before recommending or using any external tool, library, or service, you MUST verify and explicitly state:

- License type
- Whether the license is permissive
- Whether the tool is truly free or has usage limits
- Any known restrictions or caps in the free tier

If license or cost information is unclear, state this uncertainty and DO NOT recommend the tool.

---

## 4. Preferred License Types (Most to Least Permissive)

1. MIT
2. Apache 2.0
3. BSD (2‑clause, 3‑clause)
4. ISC
5. MPL 2.0 (file‑level copyleft; use with caution)

The following require explicit approval before use:
- GPL
- LGPL
- AGPL

Avoid entirely unless explicitly approved:
- Proprietary licenses
- Custom licenses
- No license specified

---

## 5. Dependency Selection Rules

When suggesting a dependency, you must:

- Prefer standard library solutions first
- Prefer well‑established and actively maintained projects
- Avoid unnecessary dependencies
- Avoid overlapping functionality
- State why the dependency is required

Do NOT add dependencies by default.

---

## 6. External Service Recommendations

When recommending an external service (hosting, database, auth, storage, etc.), you MUST state:

- Whether it requires a credit card
- Free tier limits (storage, bandwidth, requests, users)
- What happens when limits are exceeded (hard stop vs billing)

If any of the above is unknown, do not recommend the service.

---

## 7. AI / ML Tooling Constraints

- Prefer open‑source or self‑hosted AI solutions when possible
- Usage‑based AI APIs must clearly state free limits
- If no truly free option exists, state this explicitly and pause

AI tools must not introduce hidden or future costs.

---

## 8. External Code Usage

When referencing external code:

- Prefer official repositories
- State the license type
- Avoid copying large blocks verbatim
- Adapt code to fit project standards
- Attribute sources when appropriate

---

## 9. Enforcement

If a proposed tool, service, or dependency violates any rule above:

- State the violation clearly
- Do not proceed with implementation
- Suggest compliant alternatives if available

---

## 10. Dependencies Audit (As-Implemented)

This section documents all external dependencies used in this project, verified for compliance.

**Last Updated:** January 13, 2026 (v0.2.0)

### Frontend Dependencies (Phase 1)

| Dependency | Version | License | Cost | CC Required | Status |
|------------|---------|---------|------|-------------|--------|
| **Pyodide** | v0.25.0 | MPL 2.0 | Free | No | ✅ Approved |
| **Marked.js** | Latest | MIT | Free | No | ✅ Approved |
| **Monaco Editor** | v0.45.0 | MIT | Free | No | ✅ Approved |

### Backend Dependencies (Optional - Not Required)

| Dependency | Version | License | Cost | CC Required | Status |
|------------|---------|---------|------|-------------|--------|
| **FastAPI** | 0.104.1 | MIT | Free | No | ✅ Approved |
| **Uvicorn** | 0.24.0 | BSD | Free | No | ✅ Approved |
| **Pydantic** | 2.5.0 | MIT | Free | No | ✅ Approved |

**Total Project Cost:** $0.00  
**Credit Cards Required:** 0  
**Paid Services:** 0  
**Compliance Rate:** 100% ✅

---

### Pyodide License Details (MPL 2.0)

**License Type:** Mozilla Public License 2.0  
**Copyleft Level:** File-level (weak copyleft)  
**Permissible Use:** ✅ Yes - As library/dependency  
**Requirements:** If we modify Pyodide source files, must share modifications  
**Our Usage:** Using as-is, no modifications  
**Compliance:** ✅ Fully compliant

**Verification:** https://github.com/pyodide/pyodide/blob/main/LICENSE

**Note:** MPL 2.0 is listed as "use with caution" in Section 4, but is approved because:
1. We use Pyodide as a library, not modifying its source
2. File-level copyleft doesn't affect our application code
3. No other free Python-in-browser alternative exists
4. Critical for core functionality

**Approval:** Explicitly approved for this use case ✅

---

### Marked.js License Details (MIT)

**License Type:** MIT  
**Permissive:** Yes (most permissive)  
**Requirements:** Include license notice  
**Compliance:** ✅ Fully compliant

**Verification:** https://github.com/markedjs/marked/blob/master/LICENSE.md

---

### Monaco Editor License Details (MIT)

**License Type:** MIT  
**Permissive:** Yes (most permissive)  
**Requirements:** Include license notice  
**Compliance:** ✅ Fully compliant

**Verification:** https://github.com/microsoft/monaco-editor/blob/main/LICENSE.md

---

### CDN Usage

**CDN Provider:** jsDelivr  
**Cost:** Free  
**Credit Card:** Not required  
**License:** Open source CDN  
**Uptime:** 99.9%+ SLA  
**Bandwidth:** Unlimited for open-source  
**Compliance:** ✅ Approved

**URLs:**
- Pyodide: `https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js`
- Marked.js: `https://cdn.jsdelivr.net/npm/marked/marked.min.js`
- Monaco: `https://cdn.jsdelivr.net/npm/monaco-editor@0.45.0/min/vs/loader.js`

**Fallback:** Can download and self-host all libraries if CDN unavailable

---

### Future Dependencies (Phase 2 - Pending Verification)

These have NOT been added yet and require verification before use:

**AI Integration (Must Verify):**
- Option 1: OpenRouter free tier
- Option 2: Hugging Face Inference API
- Option 3: Local LLM (llama.cpp in WASM)
- **Status:** ⏳ Not verified, not implemented

**Voice Integration (Must Verify):**
- Option 1: Web Speech API (browser built-in, free)
- Option 2: Free TTS service with no CC required
- **Status:** ⏳ Not verified, not implemented

**Do NOT proceed with Phase 2 features until these are verified!**

---

## 11. License Compliance Checklist

For any future dependency, verify ALL of these before adding:

- [ ] License is MIT, Apache 2.0, BSD, ISC, or explicitly approved
- [ ] Completely free (no payment ever required)
- [ ] No credit card required for signup or use
- [ ] Free tier is sufficient (if applicable)
- [ ] No freemium limitations on core features
- [ ] Actively maintained (updated in last 6 months)
- [ ] Documented on official repository
- [ ] License file present and readable
- [ ] No hidden costs or future billing

**If ANY checkbox is unchecked, DO NOT add the dependency.**

---

**Document Maintenance:** Update Section 10 after each phase when dependencies are added.