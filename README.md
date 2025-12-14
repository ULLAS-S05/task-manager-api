# task-manager-api
Flask REST API for Task Management
# Task Manager REST API

A backend RESTful API built using **Python and Flask** to manage tasks efficiently.  
This project supports full **CRUD operations (Create, Read, Update, Delete)** and demonstrates real-world backend development practices used in modern applications.

---

## 📌 Why This Project Is Used

In today’s digital systems, applications must handle task-based workflows such as assigning work, tracking progress, and managing completion status.  
This Task Manager API provides a **centralized backend service** to handle these operations securely and reliably.

The project helps developers understand:
- RESTful API design principles
- Backend logic and routing
- Database interaction using ORM
- API testing and debugging
- Industry-standard backend structure

---

## 🌍 Current Real-World Applications (Where This Is Used Today)

APIs similar to this Task Manager are actively used in many real-world applications, including:

### 🧑‍💼 Project Management Tools
- Applications like **Trello, Jira, Asana, Monday.com**
- Used to create, update, and track tasks across teams

### 📋 To-Do & Productivity Apps
- Google Tasks, Microsoft To Do, Notion
- Backend APIs manage task creation, status updates, and deletion

### 🏢 Enterprise Workflow Systems
- Employee task assignment systems
- Internal company dashboards for tracking work progress

### 📱 Web & Mobile Applications
- Backend services for React, Angular, and mobile apps
- REST APIs provide data to frontend interfaces

### 🎓 Academic & Learning Platforms
- Student assignment tracking systems
- Mini-project and capstone project backends

### 🤖 Automation & AI Pipelines
- Task queues for automation workflows
- Managing processing steps in AI/ML pipelines

This project reflects **the same backend concepts used in production systems**, scaled down for learning and demonstration purposes.

---

## 🛠️ Tech Stack Used

- **Programming Language:** Python  
- **Framework:** Flask  
- **Database:** SQLite  
- **ORM:** SQLAlchemy  
- **API Testing:** Postman / curl  
- **Version Control:** Git & GitHub  

---

## 📂 Project Folder Structure

taskmanagerapi/
├── app.py
├── routes.py
├── models.py
├── extensions.py
├── requirements.txt

---

## ⚙️ How the Project Works (High-Level Flow)

1. Client (Postman / frontend application) sends an HTTP request
2. Flask application receives and routes the request
3. Business logic processes the request
4. SQLAlchemy ORM interacts with the SQLite database
5. JSON response is returned to the client

---

## 🚀 How to Run the Project (Step-by-Step)

### Step 1: Clone or Download the Repository
```bash
git clone https://github.com/YOUR_USERNAME/task-manager-api.git
cd task-manager-api

Step 2: Create Virtual Environment
python3 -m venv .venv


Activate it:

source .venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Application
python app.py


You should see:

Running on http://127.0.0.1:5000

🔗 API Endpoints
Method	Endpoint	Description
GET	/tasks	Get all tasks
POST	/tasks	Create a new task
PUT	/tasks/<id>	Update a task
DELETE	/tasks/<id>	Delete a task
🧪 How to Test Using Postman

Open Postman

Select HTTP method (GET / POST / PUT / DELETE)

✅ POSTMAN COMMANDS – COMPLETE GUIDE
🔹 Base URL (IMPORTANT)

Your Flask server must be running:

http://127.0.0.1:5000


All endpoints are based on this.

1️⃣ CREATE TASK (POST)
Purpose

Create a new task in the database.
_**make sure ur flask neeede to run in background, if not make ur flask to run 
then only postman will works**_
Postman Setup

Method: POST

URL:

http://127.0.0.1:5000/tasks

Headers

(Postman adds automatically if JSON is selected)

Content-Type: application/json

Body → raw → JSON
{
  "title": "Learn Flask",
  "description": "Build REST API"
}

Expected Response (201 Created)
{
  "id": 1,
  "title": "Learn Flask",
  "description": "Build REST API",
  "status": "Pending"
}

2️⃣ GET ALL TASKS (GET)
Purpose

Fetch all tasks from the database.

Postman Setup

Method: GET

URL:

http://127.0.0.1:5000/tasks

Expected Response
[
  {
    "id": 1,
    "title": "Learn Flask",
    "description": "Build REST API",
    "status": "Pending"
  }
]

3️⃣ UPDATE TASK (PUT)
Purpose

Update task status or details.

Postman Setup

Method: PUT

URL:

http://127.0.0.1:5000/tasks/1

Headers
Content-Type: application/json

Body → raw → JSON
{
  "status": "Completed"
}

_**Expected Response**_
{
  "message": "Task updated successfully"
}

4️⃣ DELETE TASK (DELETE)
Purpose

Delete a task by ID.

Postman Setup

Method: DELETE

URL:

http://127.0.0.1:5000/tasks/1

Body

❌ No body required

Expected Response
{
  "message": "Task deleted successfully"
}

5️⃣ VERIFY DELETE (GET AGAIN)
Purpose

Confirm the task was deleted.

Postman Setup

Method: GET

URL:

http://127.0.0.1:5000/tasks

Expected Response
[]


🔮 Future Enhancements

User authentication using JWT

Task priority and deadlines

Pagination and filtering

Role-based access control

Cloud deployment

Frontend integration (React)
This project demonstrates practical backend development skills aligned with real-world applications and can be confidently showcased in:

GitHub portfolio

Internship and job applications

Academic projects

Technical interviews


