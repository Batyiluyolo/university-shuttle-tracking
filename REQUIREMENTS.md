# System Requirements Document (SRD) - University Shuttle Tracking System

## **1. Functional Requirements**
The system shall provide the following capabilities:

1. **Real-Time Shuttle Tracking** – The system shall allow students to track shuttle locations in real-time using GPS.  
2. **Schedule Management** – Administrators shall be able to update shuttle schedules dynamically via Google Sheets.  
3. **Route Selection** – Students shall be able to select shuttle routes and view estimated arrival times.  
4. **Driver Location Updates** – Shuttle drivers shall be able to update their location every 30 seconds using the Telegram bot.  
5. **User Authentication** – The system shall provide secure login for students, drivers, and administrators.  
6. **Notifications & Alerts** – The system shall send alerts for shuttle delays, schedule changes, and emergency notifications.  
7. **Historical Data Logs** – The system shall store past shuttle movement history for at least 30 days.  
8. **Mobile & Web Compatibility** – The system shall be accessible via both web and mobile devices.  
9. **Google Maps Integration** – The system shall display shuttle locations and routes using Google Maps.  
10. **Access to CPUT Resources** – The system shall provide links to the CPUT website and shuttle service provider (GHTS) for additional resources.  

## **2. Non-Functional Requirements**
| **Category**     | **Requirement** |
|-----------------|----------------|
| **Usability**   | The system shall provide a clean, intuitive UI where users can access shuttle details with a maximum of 3 clicks. |
| **Deployability** | The system shall be deployable on both Windows and Linux servers. |
| **Maintainability** | The system documentation shall include an API guide for future integrations. |
| **Scalability** | The system shall support at least 1,000 concurrent users without performance degradation. |
| **Security** | All user data shall be encrypted using AES-256 encryption. |
| **Performance** | The system shall fetch and display shuttle locations within 2 seconds of an update. |
| **Reliability** | The system shall have an uptime of at least 99.9% to ensure continuous service. |
| **Accessibility** | The system shall comply with WCAG 2.1 accessibility standards for visually impaired users. |
