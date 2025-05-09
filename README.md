**✅ Task Management System**

    A Django-powered web application that allows users to manage tasks efficiently with priority tags, edit/delete options, and an interactive UI. Includes user authentication, profile editing, task collapses, pagination, and more.

**✨ Features**

    🔐 User Registration & Login

    New users can register via a secure form with a basic Google-style "I'm not a robot" (Captcha) verification.

    After registration, users can log in to access the dashboard and manage tasks.

**🧑 User Dashboard**

    Edit user profile details such as name or selected editable fields.

    Clean and intuitive dashboard layout.

**📝 Task Manager**

    Add new tasks using a Bootstrap-powered collapsible form.

    Assign task priority with visual symbols:

    🔔 High Priority

    🅼 Medium Priority

    😒 Low Priority

    Each task has a description panel that toggles to reveal task details with optional images.

    Edit or Delete tasks using action buttons in the last column.

**📄 Pagination**

    Tasks are displayed with pagination to keep the UI fast and clean, especially with many tasks.

**📸 User Interface Highlights**

    Modern, responsive UI using Bootstrap 5

    Collapsible task sections for clean task creation

    Priority indicators with intuitive emojis/icons

    Pagination ensures scalability for large task lists

**🛠 Tech Stack**
    
    **Layer**	       **Technology**
     Backend	       Django (Python)
    Frontend	     HTML, CSS, Bootstrap
      Auth	      Django Auth + Captcha (Google-style)
    Database	   SQLite(default), Postgres (Optional)

**🚀 Getting Started**

1. Clone the repository

    -> git clone https://github.com/syashwanths/Task-Management-System.git

    -> cd Task-Management-System

2. Create a virtual environment

    -> python -m venv venv

    -> source venv/bin/activate   # For Windows: venv\Scripts\activate

3. Apply migrations

    -> python manage.py makemigrations

    -> python manage.py migrate

4. Run the development server

    -> python manage.py runserver

5. Visit the app

    -> URL: http://127.0.0.1:8000


**✍️ Author**

  Yashwanth S.
