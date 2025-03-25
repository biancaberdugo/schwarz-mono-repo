# Project TODOs

This document outlines the key upcoming tasks and improvements required for this project. These tasks aim to improve automation, security, and architecture in the system.

---

## ✅ Immediate Priorities

### 1. Continuous Integration (CI)
- [ ] Implement CI pipelines to execute unit tests **before** building Docker images.
- [ ] Ensure pipelines fail early if tests do not pass.

### 2. Security Improvements
- [ ] Enhance cloud security by implementing stricter access control and securing credentials/tokens.
- [ ] Establish policies for key rotation.

### 3. Authentication Layer
- [ ] Develop a complete **Authentication Layer** to manage user identity and sessions.
- [ ] Implement support for **audience-based tokens** to securely authenticate with external services.

### 4. Deployment Platform Refactor
- [ ] Refactor the entire API deployment process.
- [ ] Integrate **Argo CD** for GitOps-based continuous delivery and progressive delivery strategies.
- [ ] Optimize build, deploy, and release pipelines using Argo workflows where needed.

---

## Contributing
For any contributions or suggestions, please open an issue or create a pull request.
