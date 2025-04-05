
---

## 🛣️ 6. Activity Diagram – Admin Updates a Route

### 🎯 Scenario: An administrator updates an existing shuttle route in the system.

```mermaid
flowchart TD
    A[Admin logs into dashboard] --> B[Navigates to Route Management]
    B --> C[Selects an existing route]
    C --> D[Edits route details (stops, path)]
    D --> E[Saves the updated route]
    E --> F[System validates and updates database]
    F --> G[Updated route becomes active]
```

---

### 📝 Explanation

This activity outlines how an admin updates a route.  
After selecting an existing route, they make changes such as modifying stops or paths.  
Upon saving, the system updates the route and makes it active for use in schedules.

This process ensures route accuracy and reflects any operational changes.

---

### 🔗 Related Functional Requirements / User Stories / Sprint Tasks

- **FR12** – The system shall allow admins to update routes.  
- **User Story US10** – As an Administrator, I want to modify routes so I can adapt to operational needs.  
- **Sprint Task T1-14** – Implement route editing interface and backend logic.

---

✅ *Diagram by: **Luyolo Batyi***
