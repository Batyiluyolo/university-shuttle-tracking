```md
# 🚦 State Transition Diagrams – University Shuttle Tracking Web App

This document includes state diagrams for key objects in the system, each followed by:

- 📝 Explanation of the object’s state changes  
- 🔗 Related functional requirements, user stories, and sprint tasks

---

## 🚍 1. State Transition Diagram – Shuttle

### 🎯 Object: Shuttle

This state diagram shows the lifecycle of a shuttle during its operation in the University Shuttle Tracking Web App.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> InTransit : Trip Assigned
    InTransit --> Idle : Trip Completed
    Idle --> Offline : GPS Signal Lost
    InTransit --> Offline : GPS Signal Lost
    Offline --> Idle : Signal Restored
markdown
Copy
Edit
