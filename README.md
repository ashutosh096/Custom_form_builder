# 📝 FormBot - Modern Form Builder

FormBot is a professional-grade web application that allows users to build, manage, and deploy custom forms. It features a high-end dashboard with real-time stats and a persistent data management system.

## ✨ Features
* **Boxed Dashboard:** A modern, centered UI for a clean workspace experience.
* **Persistent Storage:** All forms are saved in `forms_data.json`—your data stays safe even if the server restarts.
* **Professional Sidebar:** Categorized navigation (Workspace, Collaboration, Library) with a profile management footer.
* **Dynamic Stats:** Real-time tracking of total forms and system status.
* **CRUD Operations:** Create, View, and Delete forms seamlessly.

## 🛠️ Tech Stack
* **Backend:** Python 3.x, Flask
* **Frontend:** HTML5, CSS3 (Flexbox & Grid), JavaScript (ES6+)
* **Icons:** FontAwesome 6.0
* **Data:** JSON (NoSQL-style flat file storage)
*
* ![image alt](https://github.com/ashutosh096/Custom_form_builder/blob/b7e344a9d552375e33bbad978243b9a5145fc9ef/Screenshot%202026-03-28%20164609.png)

## 📁 Project Structure
```text
CUSTOM FORM BUILDER/
│
├── app.py                # Flask Backend Logic
├── forms_data.json       # Your Saved Forms (DO NOT DELETE)
│
├── static/               # Frontend Assets
│   └── style.css         # Modern Teal & Charcoal Styling
│
└── templates/            # HTML Pages
    ├── dashboard.html    # The "Boxed" Main Hub
    ├── index.html        # Form Builder Interface
    └── fill_form.html    # End-user Form View


