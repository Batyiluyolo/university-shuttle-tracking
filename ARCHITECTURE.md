# ARCHITECTURE.md

## 1. System Overview
The University Shuttle Tracking System is a web-based platform that provides real-time tracking of university shuttle buses, improving transit efficiency and user experience.

## 2. C4 Model Diagrams

### Context Diagram
The Context Diagram provides a high-level overview of how different users interact with the system.
```mermaid
graph TD;
  student[Student] -->|Checks shuttle location| system[Shuttle Tracking System];
  driver[Shuttle Driver] -->|Updates location| system;
  admin[Administrator] -->|Manages schedules and routes| system;
  system -->|Fetches location data| gpsAPI[GPS Tracking API - Google Maps API];
```

### Container Diagram
The Container Diagram breaks down the system into frontend, backend, database, and external services.
```mermaid
graph TD;
  student[Student] -->|Uses| webApp[Web Application - ReactJS];
  driver[Shuttle Driver] -->|Updates location| webApp;
  admin[Administrator] -->|Manages schedules| webApp;
  
  webApp -->|Sends requests| api[Backend API - NodeJS Express];
  api -->|Stores/retrieves data| database[Database - PostgreSQL];
  api -->|Fetches GPS data| gpsAPI[GPS Tracking API - Google Maps API];
```

### Component Diagram
The Component Diagram provides a more detailed breakdown of internal system modules.
```mermaid
graph TD;
  
  subgraph "Frontend (ReactJS)"
    UI[User Interface] -->|User interacts| MapComponent[Map Component];
    UI -->|User logs in| AuthComponent[Authentication Component];
  end

  subgraph "Backend (NodeJS Express)"
    API[API Server] -->|Handles authentication| AuthService[Authentication Service];
    API -->|Fetches shuttle locations| TrackingService[Tracking Service];
    API -->|Manages schedules| ScheduleService[Schedule Management];
  end

  subgraph "Database (PostgreSQL)"
    DBUsers[(Users Table)];
    DBShuttles[(Shuttles Table)];
    DBSchedules[(Schedules Table)];
  end

  subgraph "External Services"
    GPSAPI[GPS Tracking API - Google Maps API];
  end

  UI -->|Sends requests| API;
  API -->|Stores/retrieves data| DBUsers;
  API -->|Stores/retrieves data| DBShuttles;
  API -->|Stores/retrieves data| DBSchedules;
  TrackingService -->|Gets real-time data| GPSAPI;
```

## 3. Technology Stack
Since this is an architectural design, the following technologies are proposed:
- Frontend: React.js
- Backend: Node.js with Express
- Database: PostgreSQL
- GPS Tracking API: Google Maps API
- Deployment: AWS or Firebase

## 4. Deployment Strategy
This system is intended to be cloud-hosted for scalability and reliability. Possible hosting solutions include AWS, Firebase, or DigitalOcean.



