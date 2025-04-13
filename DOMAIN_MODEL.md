
# Domain Model – University Shuttle Tracking Web App

This domain model captures the main entities, their attributes, operations, and relationships that support the shuttle tracking system.

| Entity   | Attributes                                                  | Methods (Behaviors)                                    | Relationships                                                   |
|----------|-------------------------------------------------------------|---------------------------------------------------------|------------------------------------------------------------------|
| User     | userId, name, email, password, role                         | login(), logout(), updateProfile()                      | One user can be a Student, Driver, or Admin                     |
| Student  | studentId, faculty, year                                    | viewSchedule(), trackShuttle()                          | Inherits from User                                              |
| Driver   | driverId, licenseNumber, assignedShuttle                    | updateLocation(), startTrip(), completeTrip()           | Inherits from User <br> One driver is assigned to one Shuttle   |
| Shuttle  | shuttleId, plateNumber, capacity, status                    | sendLocation(), assignDriver()                          | One shuttle has many Trips <br> One shuttle has one Driver      |
| Trip     | tripId, status, startTime, endTime, routeId, shuttleId      | begin(), end(), cancel()                                | One trip is assigned to one Shuttle and one Route               |
| Schedule | scheduleId, date, timeSlot, tripId                          | createSchedule(), updateSchedule(), archiveSchedule()   | One schedule refers to one Trip                                 |
| Route    | routeId, origin, destination, stops                         | addStop(), removeStop(), updateRoute()                  | One route is used by many Trips                                 |

---
