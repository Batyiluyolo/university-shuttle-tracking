# Use Case Specifications - CPUT Shuttle Tracking Web App  

---

## **Use Case 1: Track Shuttle Location**  
**Actors:** Student  
**Preconditions:**  
- The student is logged into the system.  
- The shuttle is currently in service.  

**Basic Flow:**  
1. The student opens the tracking page.  
2. The system retrieves real-time GPS data.  
3. The student sees the current shuttle location on the map.  

**Alternative Flows:**  
- **Shuttle Not in Service:** The system displays "No active shuttles available."  
- **GPS Failure:** The system alerts the student that location updates are temporarily unavailable.  

**Postconditions:**  
- The student successfully views shuttle location or receives an error message.  

---

## **Use Case 2: View Shuttle Routes**  
**Actors:** Student  
**Preconditions:**  
- The student is logged into the system.  

**Basic Flow:**  
1. The student selects "View Routes" from the menu.  
2. The system displays a list of available routes.  
3. The student selects a route and sees the shuttle stops.  

**Alternative Flows:**  
- **No Routes Available:** The system displays a message: "No routes available at this time."  

**Postconditions:**  
- The student successfully views a route or gets an error message.  

---

## **Use Case 3: Update Shuttle Location**  
**Actors:** Shuttle Driver  
**Preconditions:**  
- The driver is logged into the system.  
- The shuttle is currently in service.  

**Basic Flow:**  
1. The driver selects "Update Location."  
2. The system retrieves the GPS position from the driver’s device.  
3. The new location is sent to the server.  
4. Students see the updated location on their tracking page.  

**Alternative Flows:**  
- **No GPS Signal:** The system alerts the driver that location updates failed.  

**Postconditions:**  
- The location is updated, or the driver is notified of a failure.  

---

## **Use Case 4: Manage Shuttle Schedules**  
**Actors:** Administrator  
**Preconditions:**  
- The admin is logged into the system.  
- The system contains existing shuttle schedules.  

**Basic Flow:**  
1. The admin selects "Manage Schedules."  
2. The system displays current shuttle schedules.  
3. The admin modifies, adds, or removes a schedule.  
4. The system updates and saves the new schedule.  

**Alternative Flows:**  
- **Invalid Time Entry:** The system prompts the admin to enter a valid time.  

**Postconditions:**  
- The shuttle schedule is updated successfully or an error message is displayed.  

---

## **Use Case 5: Monitor Shuttle Logs**  
**Actors:** Campus Security  
**Preconditions:**  
- The security officer is logged into the system.  
- The system has stored shuttle movement logs.  

**Basic Flow:**  
1. The officer selects "Monitor Shuttle Logs."  
2. The system retrieves and displays shuttle movement history.  
3. The officer reviews logs for any suspicious activity.  

**Alternative Flows:**  
- **No Logs Available:** The system displays "No logs found for the selected period."  

**Postconditions:**  
- The officer successfully reviews shuttle logs or receives an error message.  

---

## **Use Case 6: Provide IT Support**  
**Actors:** IT Support Staff  
**Preconditions:**  
- The IT staff is logged into the system.  
- The system is experiencing technical issues.  

**Basic Flow:**  
1. The IT staff selects "System Diagnostics."  
2. The system scans for errors.  
3. The IT staff views error reports and performs fixes.  

**Alternative Flows:**  
- **System Crash:** The IT staff initiates a manual restart.  

**Postconditions:**  
- The system is either fixed or a support ticket is created for further action.  

---

## **Use Case 7: Generate Reports**  
**Actors:** Administrator, Campus Security  
**Preconditions:**  
- The admin or security officer is logged into the system.  
- The system contains historical shuttle movement data.  

**Basic Flow:**  
1. The admin or security selects "Generate Reports."  
2. The system prompts for report parameters (date range, shuttle ID, etc.).  
3. The system generates and displays the report.  

**Alternative Flows:**  
- **No Data Available:** The system displays "No data found for the selected parameters."  

**Postconditions:**  
- The user successfully generates a report or receives an error message.  

---

## **Use Case 8: Manage Shuttle Operations**  
**Actors:** Shuttle Service Provider  
**Preconditions:**  
- The shuttle service provider is logged into the system.  

**Basic Flow:**  
1. The provider selects "Manage Shuttle Operations."  
2. The system displays shuttle availability, driver assignments, and schedules.  
3. The provider assigns drivers to routes and updates availability.  

**Alternative Flows:**  
- **Driver Unavailable:** The provider receives a notification to reassign drivers.  

**Postconditions:**  
- Shuttle operations are updated successfully or an error message is displayed.  
