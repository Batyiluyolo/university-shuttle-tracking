# Kanban Board Explanation – CPUT Shuttle Tracking Web App

## What is a Kanban Board?

A Kanban board is a visual workflow tool used in Agile development to track the progress of tasks in real time. It helps teams see what is being worked on, what's pending, and what has been completed. Tasks are represented as cards that move through columns like **To Do**, **In Progress**, and **Done**.

The board helps teams:
-  Visualize work and priorities
-  Identify bottlenecks (e.g., Blocked tasks)
-  Limit work in progress (WIP)
-  Improve workflow efficiency

---

## Structure of My Custom Kanban Board

For this project, I customized the default GitHub Project board by adding the following columns:

| Column Name     | Purpose |
|-----------------|---------|
| **To Do**       | Tasks that haven’t started yet |
| **In Progress** | Tasks currently being developed |
| **Blocked**     | Tasks that are paused due to issues or dependencies |
| **Testing**     | Tasks that are completed and need review or QA |
| **Done**        | Tasks that are fully completed and approved |

These columns allow me to better track the sprint status and simulate a real Agile workflow.

---

## How the Kanban Board Supports Agile

This board supports Agile principles in the following ways:

- **Real-time tracking**: I can move tasks through stages visually.
- **Accountability**: All tasks are assigned (to myself) and labeled clearly.
- **WIP management**: I only place one or two tasks In Progress at a time.
- **Bottlenecks are visible**: The “Blocked” column shows where things are stuck.
- **Definition of Done** is clearly visible when cards move into the "Done" column.

Each task (e.g., `T1-01`, `T1-02`) is linked to an issue that is also part of the product backlog and sprint plan. This keeps the project well organized and easy to monitor.

---

## Examples from My Board

| Task ID | Title | Column        | Label        |
|---------|-------------------------------|----------------|--------------|
| T1-01   | Design UI for tracking        | In Progress    | enhancement  |
| T1-02   | Implement GPS API             | Blocked        | enhancement  |
| T1-03   | Display shuttle on map        | To Do          | enhancement  |
| T1-04   | Develop route viewing UI      | To Do          | enhancement  |
| T1-10   | Secure login system           | Testing        | enhancement  |

---

## Benefits of Using GitHub Projects for Agile

- Integrated with Issues and Pull Requests
- Clean UI for organizing sprint tasks
- 🛠Easy to customize (add/remove columns)
- Automatically links to issues for better traceability

---

## Conclusion

The customized GitHub Kanban board helps manage sprint progress efficiently. By using custom columns like **Blocked** and **Testing**, I was able to model a realistic Agile workflow. It improves visibility, accountability, and task focus, and serves as a central hub for planning and development throughout the sprint.


