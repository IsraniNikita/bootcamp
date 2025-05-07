# One-Pager Design Document: Enable Two-Factor Authentication (2FA)

## 1. Problem
User accounts are vulnerable to unauthorized access if passwords are compromised. Password-only authentication is insufficient for protecting sensitive user data.

## 2. Goals
- Add a second layer of security (2FA) to user authentication.
- Support time-based one-time passwords (TOTP) using authenticator apps.
- Make 2FA optional but strongly encouraged for all users.

## 3. Non-Goals
- We won’t implement SMS-based 2FA (due to security risks).
- We won’t force 2FA on all users initially (no mandate).
- No biometric or hardware token support in this phase.

## 4. Proposed Solution
- Add a settings option to enable 2FA from the user profile.
- Upon setup, show a QR code for TOTP app (e.g., Google Authenticator).
- Save the shared secret securely in the backend.
- During login, if 2FA is enabled, prompt for the OTP code after password is verified.
- Validate OTP server-side using TOTP algorithm.

## 5. Alternatives Considered
- SMS-based 2FA: Less secure, more vulnerable to SIM swap.
- Email-based OTP: Too slow and can be intercepted.

## 6. Decision
We’ll use TOTP via authenticator apps as the primary 2FA method due to balance between usability and security.

## 7. Risks and Concerns
- User lockout if they lose access to their authenticator app.
- Additional complexity in the login flow and user onboarding.
- Requires user education and clear recovery instructions.
