# Task Management System

## Overview

This project is a **web-based task management system** built using **Django and Tailwind CSS**. It follows software engineering best practices, including **OAuth authentication**, **user roles**, **task management**, **random quotes based on login time**, and **Dockerized deployment with Nginx** on **Render**.

## Features

- **User Authentication (OAuth & Local Login)**
  - Supports Google and GitHub OAuth
  - Custom user profiles with additional fields (full name, bio, profile picture)
- **Task Management System**
  - CRUD operations for tasks (Create, Read, Update, Delete)
  - Tasks categorized into projects
  - Admin and standard user roles
- **Random Quote Feature**
  - Displays a motivational quote upon login
- **Fully Responsive UI**
  - Styled with Tailwind CSS for a modern look
- **Dockerized Deployment with Nginx & Render**
  - Runs in a Docker container
  - Uses Nginx as a reverse proxy
  - Deployed on Render with SQLite database

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
├── static/  # Tailwind & static files
├── theme/
├── nginx/
│   ├── nginx.conf  # Reverse proxy configuration
```

## Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

### Set Up Virtual Environment & Install Dependencies

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Run the Development Server

```bash
python manage.py runserver
```

Then, open **http://127.0.0.1:8000/** in your browser.

## Running with Docker

### Build and Start Containers

```bash
docker-compose up --build -d
```

### Apply Migrations Inside the Container

```bash
docker-compose exec web python manage.py migrate
```

### Access the Application

Visit **http://localhost/** (Nginx will proxy requests to Django).

## Deployment on Render

### Push to GitHub

```bash
git add .
git commit -m "Deploying to Render"
git push origin main
```

### Deploy on Render

1. Go to [Render](https://dashboard.render.com/)
2. Click "New Web Service"
3. Connect to your GitHub repo
4. Use the following commands:
   - **Build Command:**
     ```bash
     docker build -t my-task-app .
     ```
   - **Start Command:**
     ```bash
     docker run -p 8000:8000 my-task-app
     ```

### Update Allowed Hosts in `settings.py`

```python
ALLOWED_HOSTS = ['your-render-domain.onrender.com']
```

Then, redeploy on Render.

## 🔒 Security Considerations

- **OAuth Authentication:** Uses Django-Allauth for secure authentication.
- **Role-Based Access Control:** Admin vs. Standard User permissions.
- **HTTPS & Nginx:** Nginx serves as a reverse proxy for better security and scalability.

## License

This project is licensed under the MIT License.

## 👥 Contributors

- **Ali Asif** (mirzaasifali209@gmail.com)

For contributions, please submit a pull request or open an issue on GitHub.

## Contact

For questions or support, reach out via **mirzaasifali209@gmail.com**.

🎉 **Enjoy using the Django Task Management System!** 🚀
