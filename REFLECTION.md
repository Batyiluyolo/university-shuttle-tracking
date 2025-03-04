# Reflection: Challenges in Balancing Stakeholder Needs

## **1. Key Challenges**
### **1.1 Conflicting Requirements**
- **Students** require **real-time tracking**, but **IT staff** raised concerns about **high server load** due to frequent GPS updates.  
- **Shuttle drivers** wanted a **simple location update system**, but **admins** needed **highly accurate GPS data**, creating a usability vs. precision trade-off.  
- **Campus security** required **constant location logs** for emergency tracking, but **privacy policies** limited long-term data storage.  

### **1.2 Technical Constraints**
- Implementing **low-latency GPS tracking** required **high-performance backend servers**, but this increased **hosting costs**.  
- **Ensuring scalability** to **handle 1,000+ users** was difficult without dedicated cloud infrastructure.  

### **1.3 Security vs Usability**
- **Two-factor authentication** improved security but slowed down login processes for students and drivers.  
- Encrypting location data increased security but introduced slight delays in **fetching GPS updates**.  

---

## **2. Lessons Learned**
- **Trade-offs Are Necessary** – The final system balanced usability, performance, and security.  
- **Stakeholder Involvement is Crucial** – Frequent feedback from students, drivers, and administrators helped refine requirements.  
- **Scalability Should Be Considered Early** – Planning for future expansion early prevented major architectural changes later.  
