# Student Management System

A Django-based Student Management System with token Authentication, PostgreSQL database, and RESTful APIs to manage students and teachers.

---

1. Register User
Endpoint:
POST /register/
Description:
Register a new user (student or teacher).

Request Body:
{
    "username": "teacher",
    "password": "12345678",
    "user_type": "teacher"
}

Response:
{
    "token": "ee689960f40e9615715bbec573406e4b9b50ba84"
}

2. Login User
Endpoint:
POST /login/

Description:
Login with a username and password to receive an authentication token.

Request Body:
{
    "username": "teacher5",
    "password": "12345678"
}


Here’s a full README.md file for your project with API details, including inputs and outputs.

README.md
markdown
Copy code
# Student Management System

A Django-based Student Management System using PostgreSQL with RESTful APIs for managing teachers and students. Includes authentication and CRUD operations.

---

## Installation and Setup

### Prerequisites
- Python 3.x
- PostgreSQL

### Steps to Set Up:
1. **Clone the repository:**
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    Create a virtual environment:

2. **Create a virtual environment:**
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate      # For Windows
    Install dependencies:

3. **Install dependencies::**
pip install -r requirements.txt
Configure the PostgreSQL database:

Create a PostgreSQL database named student_management.
Update the DATABASES section in your settings.py with your PostgreSQL credentials.
Apply migrations:
python manage.py migrate
Run the development server:

python manage.py runserver


API Endpoints
Authentication APIs

1. **Register User**
Endpoint:
POST /register

Description:
Register a new user (student or teacher).

Request Body:

{
    "username": "teacher5",
    "password": "12345678",
    "user_type": "teacher"
}
Response:

json
Copy code
{
    "token": "ee689960f40e9615715bbec573406e4b9b50ba84"
}



2. **Login User**
Endpoint:
POST /login

Description:
Login with a username and password to receive an authentication token.

Request Body:

{
    "username": "teacher5",
    "password": "12345678"
}

Response:
{
    "token": "ee689960f40e9615715bbec573406e4b9b50ba84"
}



3. **List Student**
Endpoint:
GET /student

Description:
List all student.

Response:
{
    "students": [
        {
            "id": 2,
            "username": "student1"
        },
        {
            "id": 4,
            "username": "student2"
        }
    ]
}


4. **Add Student**
Endpoint:
POST /student

Description:
Add a new student.

Request Body:

{
    "username": "teacher5",
    "password": "12345678"
}

Response:
{
    "message": "Student added successfully!"
}

5. **Edit Student**
Endpoint:
PUT /student

Description:
Update existing user data.

Request Body:
{
    "student_id":6,
    "username":"student6",
    "password":"12345678"
}

Response:
{
    "message": "Student updated successfully!"
}

6. **Delete Student**
Endpoint:
DELETE /student

Description:
Delete existing user.

Request Body:
{
    "student_id":6
}

Response:
{
    "message": "Student deleted successfully!"
}


7. **Student Teachers List**
Endpoint:
GET /student-teachers

Description:
Listing all teachers related to student.

Request Body:
{
    "student_id":2
}

Response:
{
    "teachers": [
        {
            "id": 3,
            "username": "teacher"
        },
        {
            "id": 7,
            "username": "teacher1"
        },
        {
            "id": 8,
            "username": "teacher2"
        },
        {
            "id": 9,
            "username": "teacher3"
        },
        {
            "id": 10,
            "username": "teacher4"
        },
        {
            "id": 11,
            "username": "teacher5"
        }
    ]
}

