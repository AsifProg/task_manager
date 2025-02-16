# Task Management System(FocusDeck)

## Introduction
This is a web-based **Task Management System(FocusDeck)** built with **Django and Tailwind CSS**. It allows users to create, manage, and track tasks within projects. The system is designed using Agile principles, ensuring **flexibility, scalability, and continuous improvements**. The application supports **role-based access control**, project-based task categorization, and **custom user profiles**.

## Features
- **User Authentication & Role Management**
  - Custom user model with **Admin, Team Leader, and Employee roles**
  - Secure authentication with **Django Allauth**

- **Task & Project Management**
  - Create, update, delete, and assign tasks to users
  - Categorize tasks within projects
  - Task prioritization and filtering
  
- **UI & Design Enhancements**
  - Responsive design with **Tailwind CSS**
  - Intuitive dashboard for task tracking
  
- **Scalability & Deployment**
  - **Dockerized application** for easy deployment
  - **Nginx reverse proxy** setup
  - **Database upgrade-ready (PostgreSQL recommended)**
  
- 🔒 **Security & Reliability**
  - CSRF and XSS protection
  - **Role-based access control** ensures restricted access to sensitive data
  - Automated testing and CI/CD pipeline (planned in future updates)

## Demo
To preview the live demo of the application please visit <a href="https://task-manager-dil0.onrender.com" target="_blank" rel="noopener noreferrer">FocusDeck</a>

## 📂 Project Structure

```
task_manager/
│── manage.py
│── db.sqlite3
│── requirements.txt
│── Dockerfile
│── docker-compose.yml
│── .dockerignore
│
├── task_manager/  # Django settings & URLs
│   ├── settings.py
│   ├── urls.py
│
├── accounts/  # User authentication & profiles
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── tasks/  # Task management
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── theme/
│   ├── static/  # Tailwind & static files
├── nginx/
│   ├── nginx.conf
```

## Installation Guide
### Prerequisites
- **Python 3.8+**
- **Git**
- **Docker** (if deploying with containerization)
- **Node.js & npm** (for Tailwind CSS compilation)

### Setup Instructions
1. **Clone the Repository**
```sh
git clone https://github.com/AsifProg/task_manager.git
cd task-manager
```

2. **Set Up a Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3. **Install Dependencies**
```sh
pip install -r requirements.txt
```

4. **Apply Database Migrations**
```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
5. **Collect Static Files**

```bash
python manage.py collectstatic --noinput
```

6. **Run the Development Server**
```sh
python3 manage.py runserver
```

7. **Create a Superuser (Admin Access)**
```sh
python3 manage.py createsuperuser
```

8. **Running with Docker**
```sh
docker-compose up --build
```

9. **Compile Tailwind CSS**
```sh
cd theme
cd static_src
npm install
npx tailwindcss -i ./src/input.css -o ./static/css/output.css --watch
```
```sh
python3 manage.py tailwind start
```

10. **Access the Application**
```sh
http://127.0.0.1:8000
```

## Future Enhancements
- **OAuth Authentication** (Google/GitHub integration)
- **AI-driven Task Recommendations**
- **Mobile API Endpoints** for integration
- **Figma-based UI Prototyping Improvements**
- **Improved CI/CD pipeline with GitHub Actions**

## License
This project is licensed under the MIT License. Feel free to use and modify it!

## 👥 Contributing
Contributions are welcome! Fork the repository and submit a pull request for review.

🎉 **Enjoy using the Django Task Management System (FocusDeck)!** 🚀
