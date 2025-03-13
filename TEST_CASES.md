# Test Cases - CPUT Shuttle Tracking Web App  

| **Test ID** | **Test Scenario** | **Preconditions** | **Test Steps** | **Expected Result** | **Actual Result** | **Pass/Fail** |
|------------|------------------|------------------|--------------|------------------|----------------|--------------|
| TC01 | Student tracks shuttle location | Student is logged in, shuttle is active | 1. Open tracking page <br> 2. System retrieves GPS data <br> 3. Display shuttle location on map | Shuttle location appears on map | TBD | TBD |
| TC02 | Student views shuttle routes | Student is logged in | 1. Open "View Routes" <br> 2. Select a route <br> 3. Display route stops | Shuttle route and stops appear | TBD | TBD |
| TC03 | Driver updates shuttle location | Driver is logged in, GPS is active | 1. Open "Update Location" <br> 2. System gets GPS position <br> 3. Location is updated on server | Location is updated and visible to students | TBD | TBD |
| TC04 | Admin manages shuttle schedules | Admin is logged in | 1. Open "Manage Schedules" <br> 2. Modify schedule <br> 3. Save changes | Shuttle schedule updates successfully | TBD | TBD |
| TC05 | Campus security monitors shuttle logs | Security officer is logged in | 1. Open "Monitor Shuttle Logs" <br> 2. Select a date range <br> 3. View logs | Shuttle movement history appears | TBD | TBD |
| TC06 | IT Support diagnoses system issues | IT staff is logged in | 1. Open "System Diagnostics" <br> 2. Run diagnostics <br> 3. View error report | System identifies errors or confirms all systems normal | TBD | TBD |
| TC07 | Admin generates reports | Admin is logged in | 1. Open "Generate Reports" <br> 2. Select report type <br> 3. Generate report | Report is generated successfully | TBD | TBD |
| TC08 | System performance under load (Non-functional) | 1000 users are accessing the system | 1. Simulate 1000+ concurrent users <br> 2. Track response time <br> 3. Verify system stability | System remains responsive (less than 2s response time) | TBD | TBD |
| TC09 | System security: User authentication (Non-functional) | User is on the login page | 1. Enter valid credentials <br> 2. Click login <br> 3. Verify access | User logs in securely | TBD | TBD |

