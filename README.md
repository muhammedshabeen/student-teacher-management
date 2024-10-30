
# Student Management System

A Django-based Student Management System using PostgreSQL with RESTful APIs for managing teachers and students. Includes authentication and CRUD operations.

---

## Installation and Setup

### Prerequisites
- Python 3.x
- PostgreSQL

### Steps to Set Up:
1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate      # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the PostgreSQL database:**
   - Create a PostgreSQL database named `student_management`.
   - Update the `DATABASES` section in your `settings.py` with your PostgreSQL credentials.

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

---

## API Endpoints

### Authentication APIs

#### 1. Register User
- **Endpoint:**  
  `POST /register`

- **Description:**  
  Register a new user (student or teacher).

- **Request Body:**
  ```json
  {
      "username": "teacher5",
      "password": "12345678",
      "user_type": "teacher"
  }
  ```

- **Response:**
  ```json
  {
      "token": "ee689960f40e9615715bbec573406e4b9b50ba84"
  }
  ```

---

#### 2. Login User
- **Endpoint:**  
  `POST /login`

- **Description:**  
  Login with a username and password to receive an authentication token.

- **Request Body:**
  ```json
  {
      "username": "teacher5",
      "password": "12345678"
  }
  ```

- **Response:**
  ```json
  {
      "token": "ee689960f40e9615715bbec573406e4b9b50ba84"
  }
  ```

---

### Student Management APIs

#### 3. List Students
- **Endpoint:**  
  `GET /student`

- **Description:**  
  List all students.

- **Response:**
  ```json
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
  ```

---

#### 4. Add Student
- **Endpoint:**  
  `POST /student`

- **Description:**  
  Add a new student.

- **Request Body:**
  ```json
  {
      "username": "student5",
      "password": "12345678"
  }
  ```

- **Response:**
  ```json
  {
      "message": "Student added successfully!"
  }
  ```

---

#### 5. Edit Student
- **Endpoint:**  
  `PUT /student`

- **Description:**  
  Update existing user data.

- **Request Body:**
  ```json
  {
      "student_id": 6,
      "username": "student6",
      "password": "12345678"
  }
  ```

- **Response:**
  ```json
  {
      "message": "Student updated successfully!"
  }
  ```

---

#### 6. Delete Student
- **Endpoint:**  
  `DELETE /student`

- **Description:**  
  Delete an existing user.

- **Request Body:**
  ```json
  {
      "student_id": 6
  }
  ```

- **Response:**
  ```json
  {
      "message": "Student deleted successfully!"
  }
  ```

---

#### 7. Student Teachers List
- **Endpoint:**  
  `GET /student-teachers`

- **Description:**  
  List all teachers related to a specific student.

- **Request Body:**
  ```json
  {
      "student_id": 2
  }
  ```

- **Response:**
  ```json
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
  ```

