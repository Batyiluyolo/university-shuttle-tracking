
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
```

---

### 📝 Explanation

The Idle state represents a shuttle that is available but not currently transporting passengers.  
When a trip is assigned, the shuttle transitions to the In Transit state.  
Upon completing the trip, the shuttle returns to Idle.  
If at any point the GPS signal is lost, the shuttle enters the Offline state.  
When the signal is restored, the shuttle returns to Idle.  

This state model enables the system to handle live tracking, trip status management, and GPS connectivity issues effectively.

---

### 🔗 Related Functional Requirements / User Stories / Sprint Tasks

FR2 – The system shall track the shuttle’s live location.  
FR4 – The driver shall update their shuttle status (Idle, In Transit).  
User Story US1 – As a Student, I want to track shuttle locations in real-time so I can plan accordingly.  
User Story US3 – As a Shuttle Driver, I want to update my shuttle’s location easily so that students receive accurate information.  
Sprint Task T1-02 – Implement GPS API to fetch shuttle location.  
Sprint Task T1-03 – Display shuttle position on map.

---
---

## 🧾 2. State Transition Diagram – Trip

### 🎯 Object: Trip

This state diagram shows the lifecycle of a Trip within the University Shuttle Tracking Web App.

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Scheduled : Assign Shuttle & Time
    Scheduled --> InProgress : Start Trip
    InProgress --> Completed : End Trip
    Created --> Cancelled : Cancelled by Admin
    Scheduled --> Cancelled : Cancelled before Departure
    InProgress --> Cancelled : Emergency Cancellation
```

---
### 📝 Explanation

A Trip starts in the Created state when an admin or system schedules a new route.  
Once a time and shuttle are assigned, it moves to Scheduled.  
When the shuttle begins transport, the trip transitions to In Progress.  
If everything goes well, it ends in Completed.  

However, trips may be Cancelled at any point before or during execution depending on admin decisions or emergencies.  

This model ensures the system properly tracks trip creation, scheduling, and cancellation scenarios.

---

### 🔗 Related Functional Requirements / User Stories / Sprint Tasks

FR5 – The system shall allow administrators to schedule and cancel trips.  
User Story US2 – As an Administrator, I want to manage shuttle trips so that I can coordinate transport efficiently.  
User Story US4 – As a Student, I want accurate trip info so I can plan my travel.  
Sprint Task T1-05 – Develop trip creation and scheduling interface.  
Sprint Task T1-06 – Implement trip lifecycle state tracking.

---
