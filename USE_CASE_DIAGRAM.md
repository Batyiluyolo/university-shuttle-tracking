# Use Case Diagram - CPUT Shuttle Tracking Web App  

## 📌 Use Case Diagram (Image)  
![Use Case Diagram](use_case_diagram.png)  

## 📌 PlantUML Code  
@startuml
left to right direction

actor "Student" as student
actor "Shuttle Driver" as driver
actor "Administrator" as admin
actor "Campus Security" as security
actor "IT Support" as it_support
actor "Shuttle Service Provider" as service_provider

rectangle "University Shuttle Tracking Web App" {
    usecase "Track Shuttle Location" as UC_Track
    usecase "View Shuttle Routes" as UC_Routes
    usecase "Update Shuttle Location" as UC_Update
    usecase "Manage Schedules & Routes" as UC_Manage
    usecase "Monitor Shuttle Logs" as UC_Monitor
    usecase "Provide IT Support" as UC_IT
    usecase "Manage Shuttle Operations" as UC_Operations
    usecase "Generate Reports" as UC_Reports

    UC_Manage --> UC_Update : <<include>> 
    UC_Monitor --> UC_Reports : <<extend>>
}

student --> UC_Track
student --> UC_Routes

driver --> UC_Update
admin --> UC_Manage

security --> UC_Monitor
UC_Reports .> security : <<extend>>

it_support --> UC_IT
service_provider --> UC_Operations
@enduml


# 📌  Written Explanation
1. Key Actors and Their Roles
Student → Tracks shuttle locations and views routes.
Shuttle Driver → Updates the shuttle’s real-time location.
Administrator → Manages schedules and routes.
Campus Security → Monitors shuttle logs for safety.
IT Support → Ensures the system runs smoothly.
Shuttle Service Provider → Oversees overall shuttle operations.
2. Relationships Between Actors and Use Cases
"Manage Schedules & Routes" <<includes>> "Update Shuttle Location" → Because updating routes requires location updates.
"Monitor Shuttle Logs" <<extends>> "Generate Reports" → Because security may sometimes need reports but not always.
3. How the Diagram Addresses Stakeholder Concerns
Students & Drivers → Can track shuttles in real-time.
Admins → Can manage routes and schedules easily.
Security → Can monitor shuttles for safety.
IT Team → Can maintain system reliability.

