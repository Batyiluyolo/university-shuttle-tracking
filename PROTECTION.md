
# 🔒 Branch Protection Configuration

This file documents the branch protection rules configured for the `main` branch in the University Shuttle Tracking repository.

---

## ✅ Protected Branch: `main`

The following settings were enabled to ensure stability and a secure CI/CD process:

### ✅ Rules Enabled

- **Require a pull request before merging**
  - Prevents direct pushes to `main`
  - Ensures code is reviewed before being merged

- **Require conversation resolution before merging**
  - All review comments must be addressed before merge

- **Block force pushes**
  - Protects commit history from being overwritten

- **Restrict deletions**
  - Prevents accidental or unauthorized deletion of the `main` branch

- **Do not allow bypassing the above settings**
  - Applies to everyone including administrators

---

## 📷 Screenshot

A screenshot showing this configuration is saved in the `docs/` folder as:
```
docs/branch_protection_screenshot.png
```

---

## 🚫 Not Yet Enabled

- ❌ Require status checks to pass  
  This will be added after the CI workflow is set up (GitHub Actions in Step 2)

---

Prepared by: **Luyolo Batyi**
