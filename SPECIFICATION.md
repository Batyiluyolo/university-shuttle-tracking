## 1. Introduction
### Project Title
**University Shuttle Tracking System**

### Domain
**University Transportation**

### Problem Statement
Many universities face challenges with shuttle services, such as lack of real-time tracking, inefficient route management, and unreliable schedules. This system aims to provide a user-friendly platform for students and staff to track shuttle locations and schedules in real time.

### Scope & Feasibility
The system will feature:
- Real-time GPS tracking of university shuttles
- Route optimization and scheduling
- Web-based interface for students and staff
- Administrator dashboard for managing shuttle operations

## 2. Functional Requirements
- Track shuttle locations in real time
- Display estimated arrival times
- Allow route and schedule updates
- Provide notifications for delays or changes

## 3. Non-Functional Requirements
- High availability and reliability
- Secure user authentication
- User-friendly interface

## 4. Technologies Used
This is a conceptual design; the following technologies could be used:
- Frontend: React.js
- Backend: Node.js with Express
- Database: PostgreSQL
- GPS Tracking API: Google Maps API

## 5. Use Case Diagram
The use case diagram will illustrate interactions between students, drivers, and administrators in the system.
@startuml
left to right direction

actor "Student" as student
actor "Administrator" as admin
actor "Shuttle Driver" as driver

rectangle "University Shuttle Tracking System" {
    usecase "Track Shuttle Location" as UC_Track
    usecase "View Routes" as UC_Routes
    usecase "Book a Shuttle" as UC_Book
    usecase "Update Shuttle Location" as UC_Update
    usecase "Manage Schedules & Routes" as UC_Manage
}

student -[hidden]--> UC_Track
admin -[hidden]--> UC_Manage

student -left-> UC_Track
student -left-> UC_Routes
student -left-> UC_Book

driver -right-> UC_Update
admin -right-> UC_Manage
@enduml

