# 🚍 State Transition Diagram – Shuttle

## 🎯 Object: Shuttle

This state diagram represents the different operational states of a shuttle within the University Shuttle Tracking Web App.

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> InTransit : Trip Assigned
    InTransit --> Idle : Trip Completed
    Idle --> Offline : GPS Signal Lost
    InTransit --> Offline : GPS Signal Lost
    Offline --> Idle : Signal Restored
