# 🛡️ Two-Factor Authentication (2FA) Feature Proposal

## ❗ Problem Statement

Currently, user accounts are protected only by a single layer of authentication — a password.  
This leaves the system vulnerable to attacks such as:

- Credential stuffing  
- Phishing  
- Brute-force attempts

Without an additional verification layer, unauthorized access becomes more likely if credentials are leaked or reused.

---

## 🎯 Goals

- Enhance account security by requiring a second authentication factor  
- Support time-based one-time password (TOTP) via authenticator apps (e.g., Google Authenticator, Authy)  
- Make 2FA optional but strongly encouraged during login  
- Reduce risk of unauthorized access from compromised passwords  

---

## 🚫 Non-Goals

- This proposal does **not** include biometric authentication (e.g., fingerprint, facial recognition)  
- Does **not** address account recovery for lost 2FA devices (**this will be handled in a follow-up proposal, tracked under ticket `SEC-2025-R02`, scheduled for Sprint 18**)  
- Does **not** enforce mandatory 2FA for all users or via admin policy  

> **Change based on feedback**:  
> The comment suggested referencing where or when recovery options will be addressed. I added a mention that recovery will be covered in a **follow-up proposal**, under a specific ticket (`SEC-2025-R02`), which will be tackled in **Sprint 18**.

---

## ✅ Proposed Solution

1. **2FA Enrollment**  
   - After logging in with username and password, users will be prompted to enroll in 2FA  
   - A QR code or manual setup key will be provided to link their account with a TOTP app  

2. **Authentication Flow**  
   - Once enabled, users must input a valid 6-digit code from their TOTP app to complete login  

3. **User Controls**  
   - Users can enable or disable 2FA from their account settings  
   - Disabling 2FA will require password re-entry and confirmation to prevent misuse  

4. **Backup Recovery Codes**  
   - At setup, users receive one-time recovery codes for emergency login  
   - These are shown once and must be saved securely by the user (e.g., download, print option)

---

## 🔄 Alternatives Considered

- **SMS-based 2FA**  
  - Easier onboarding but deprioritized due to risks like SIM-swapping attacks

- **Email-based OTPs**  
  - Less secure if a user's email is compromised, so not chosen

---

## ⚠️ Risks & Concerns

- Users may lose access to their TOTP app, which could lock them out  
  - *Recovery options will be handled in a future proposal (see Non-Goals)*  
- Adds complexity to the login process, potentially frustrating less technical users  
  - *User education, prompts, or grace periods may be considered to ease adoption*  
- Secure storage and generation of TOTP secrets must be implemented carefully to avoid introducing new vulnerabilities  

---

