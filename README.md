# 📚 Odoo 17 - Library Management System

A complete custom module for managing a digital library system, built using **Odoo 17**. This module handles books, members, and loans with wizards, workflows, dashboards, reports, and access control.

---

## ✅ Features Overview

| Feature                            

| Book Management                    
| Loan Workflow (Draft → Borrowed → Returned / Overdue)
| Borrow Book Wizard                 
| Return Book Wizard                 
| Member Loan History Wizard          
| Smart Buttons in Partner View       
| Dashboard: Overdue Loans View       
| Dashboard: Top Borrowed Books Graph 
| Scheduled Action (Cron) for Overdues
| Email Notification on Overdue       
| PDF Report for Loan Receipt         
| Security & Role-Based Access        
| README with Instructions            

---

## 🧩 Modules and Structure

``
Project

![image](https://github.com/user-attachments/assets/e7c12bb4-aba2-4e3f-993c-8c490e73345f)

``



## 🚀 Functionalities

### 📖 Book Management
- Add books with `title`, `author`, `ISBN`, `publication_year`
- Track availability with `status` field (Available / Borrowed)

### 🔁 Loan Workflow
- State: `Draft → Borrowed → Returned / Overdue`
- Buttons trigger transitions and update book status
- Overdue loans identified by return date

### 🧙 Wizards
- **Borrow Book Wizard**: From Book Form View
- **Return Book Wizard**: From Loan Form View
- **Loan History Wizard**: From Partner Smart Button

### 📊 Dashboards
- **Overdue Loans**: Tree view filtered by overdue state
- **Top Borrowed Books**: Bar chart using `graph` view with group_by on book

### ⏱️ Scheduled Actions
- Cron job runs daily to mark overdue loans
- Optional email notifications using QWeb email templates

### 🔐 Security
- **Librarian Manager**: Full access
- **Librarian Employee**: Limited access
- **Library Member**: Can view own loan history

### 🧾 Reports
- PDF report generated using QWeb template
- Includes book, partner, dates, and loan status

---

## 📷 Screenshots (to add)

Add the following screenshots to the `/screenshots` folder and link them here:

- 📍 Loan Tree View with Overdue Filter  
- 📈 Top Borrowed Books Graph  
- 🔄 Borrow Wizard Form  
- ✅ Return Wizard Form  
- 👤 Partner Form with Smart Buttons  
- 🧾 Loan PDF Report Preview  

## 📦 Installation

1. Clone this repo inside your Odoo `addons` directory:

   ```bash
   git clone https://github.com/your-org/library_management.git
   ```

2. Restart the Odoo server:

   ```bash
   ./odoo-bin -u library_management -d your_db
   ```

3. Activate Developer Mode and install the **Library Management** module from the Apps menu.

---

## 📌 Usage Notes

- To test scheduled overdue logic: Use **"Check Overdue Loans"** button manually or wait for cron.
- Reports can be printed from the **Loan Form View** using the print icon.
- Smart buttons on Partner form allow viewing member history directly.

---

## 🧠 Developer Notes

- Code follows Odoo best practices with:
  - Clear separation of concerns
  - Wizard models inherit from `TransientModel`
  - Access rights grouped by roles
  - Views are modular and easy to extend
 
📸 Screenshots
![Screenshot 2025-07-09 210632](https://github.com/user-attachments/assets/990564b2-693a-40d9-839a-869e5e5918ff)
![Screenshot 2025-07-09 210721](https://github.com/user-attachments/assets/6d5e22bf-e3c4-45b1-b49a-e3f79811e5d4)
![Screenshot 2025-07-09 210818](https://github.com/user-attachments/assets/bbbb0867-b05a-4667-bce6-6fbc1be6537c)
![Screenshot 2025-07-09 210841](https://github.com/user-attachments/assets/fb196e29-ba25-4546-8a5f-23601d96d4b7)
![Screenshot 2025-07-09 210914](https://github.com/user-attachments/assets/05c34990-449a-4fb7-a60b-380143a288f9)
![Screenshot 2025-07-09 210938](https://github.com/user-attachments/assets/c02607b5-4573-41c1-8f1b-f464afb113df)
![Screenshot 2025-07-09 211252](https://github.com/user-attachments/assets/904207da-30fe-4a7b-9738-f6c37c5a39cc)
![Screenshot 2025-07-09 211337](https://github.com/user-attachments/assets/875d8fea-042c-4990-b996-0090d43f679a)
![Screenshot 2025-07-09 211845](https://github.com/user-attachments/assets/73d19a36-6e26-4b85-9da7-a4e89f540ee8)
![Screenshot 2025-07-09 211909](https://github.com/user-attachments/assets/e29f4b4c-1bde-4719-a343-9740aeea2490)
![Screenshot 2025-07-09 211036](https://github.com/user-attachments/assets/a7a6503e-5396-4da8-b843-4f68a6857360)
![Screenshot 2025-07-09 211057](https://github.com/user-attachments/assets/00892243-c028-4631-beca-4b62bc114246)







