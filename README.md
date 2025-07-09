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

odoo17 D:\odoo\odoo17
    ├── custom
    ├── library_management
    │   ├── data
    │   │   └── scheduled_actions.xml
    │   ├── models
    │   │   ├── __init__.py
    │   │   ├── book.py
    │   │   ├── loan.py
    │   │   └── partner.py
    │   ├── reports
    │   │   ├── library_loan_report.xml
    │   │   └── report_library_loan_template.x
    │   ├── security
    │   │   ├── ir.model.access.csv
    │   │   ├── library_groups.xml
    │   │   ├── library_security.xml
    │   │   └── loan_rules.xml
    │   ├── views
    │   │   ├── actions.xml
    │   │   ├── book_views.xml
    │   │   ├── dashboard_views.xml
    │   │   ├── loan_views.xml
    │   │   ├── menu.xml
    │   │   ├── res_partner_view_inherit.xml
    │   │   └── wizard_views.xml
    │   ├── wizard
    │   │   ├── book_borrow_wizard_view.xml
    │   │   └── return_book_wizard_view.xml
    │   ├── wizards
    │   │   ├── __init__.py
    │   │   ├── book_borrow_wizard.py
    │   │   ├── member_loan_history_wizard.p
    │   │   └── return_book_wizard.py
    │   ├── __init__.py
    │   └── __manifest__.py
    ├── odoo
    ├── odoo-conf
    │   └── odoo17c.conf
    ├── odoo17-venv (Python Virtual Environment)
    │   ├── Include
    │   ├── Lib
    │   ├── Scripts
    │   ├── share
    │   └── pyvenv.cfg
    ├── External Libraries
    └── Scratches and Consoles
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
