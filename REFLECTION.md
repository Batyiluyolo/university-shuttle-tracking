# Reflection: Anticipating Challenges in Stakeholder Needs  

## **1. Potential Challenges**  
While designing the system, I identified several areas where different stakeholders might have conflicting needs:  

### **1.1 Balancing Real-Time Tracking with System Performance**  
- The system requires real-time GPS tracking to provide accurate shuttle locations for students.  
- However, frequent GPS updates could increase server load and affect performance, especially if many students access the system simultaneously.  
- A possible solution could be optimizing update intervals (e.g., location updates every 30 seconds instead of every second).  

### **1.2 Ensuring Usability for Shuttle Drivers**  
- Shuttle drivers need an easy way to update their location, but manual updates may lead to inconsistent or delayed data.  
- Integrating automated GPS tracking via a mobile app could improve accuracy.  

### **1.3 Data Storage and Privacy Considerations**  
- Storing historical shuttle data for analytics or security purposes raises privacy concerns.  
- The challenge is to balance data retention policies while ensuring campus security can access logs when needed.  
- A possible approach is automatic deletion of data after 30 days to maintain privacy.  

---

## **2. Lessons Learned from the Design Phase**  
- **Trade-offs in System Design** → Optimizing performance while keeping real-time tracking accurate is a key challenge.  
- **Scalability Planning is Important** → If demand grows, cloud hosting may be necessary to handle high traffic.  
- **User Experience Matters** → The system must remain simple and intuitive for students and drivers to adopt it easily.  

---

## **3. Next Steps**  
- Conduct user testing to validate the tracking and scheduling functionality.  
- Evaluate GPS update frequency to balance accuracy and system performance.  
- Ensure security compliance by setting clear data retention policies.  
