# Expense Tracker App

A Django-based expense tracking application that helps users manage their personal finances.

## Features

- User authentication and registration
- Add, edit, and delete expenses
- Pocket money management
- Expense analysis and reporting
- Monthly and weekly expense views

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment to Render

### Prerequisites

1. A Render account
2. Your code pushed to a Git repository (GitHub, GitLab, etc.)

### Deployment Steps

1. **Create a new Web Service on Render:**
   - Go to your Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your Git repository

2. **Configure the Web Service:**
   - **Name:** expense-tracker (or your preferred name)
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn expense_tracker.wsgi:application`

3. **Add Environment Variables:**
   - Go to the "Environment" tab in your Render service
   - Add the following environment variables:
     ```
     SECRET_KEY=your-secure-secret-key-here
     DEBUG=False
     ALLOWED_HOSTS=your-app-name.onrender.com
     ```

4. **Add PostgreSQL Database (Optional but Recommended):**
   - Create a new PostgreSQL database on Render
   - Add the database environment variables:
     ```
     DB_NAME=your_db_name
     DB_USER=your_db_user
     DB_PASSWORD=your_db_password
     DB_HOST=your_db_host
     DB_PORT=5432
     ```

5. **Deploy:**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Environment Variables for Production

Make sure to set these environment variables in your Render dashboard:

- `SECRET_KEY`: A secure Django secret key
- `DEBUG`: Set to `False` for production
- `ALLOWED_HOSTS`: Your Render app URL
- Database variables (if using PostgreSQL):
  - `DB_NAME`
  - `DB_USER`
  - `DB_PASSWORD`
  - `DB_HOST`
  - `DB_PORT`

## Project Structure

```
expense_tracker/
├── expense_tracker/          # Django project settings
├── expenses/                 # Main app
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── urls.py              # URL routing
│   └── templates/           # HTML templates
├── requirements.txt          # Python dependencies
├── build.sh                 # Build script for Render
├── Procfile                 # Process file for Render
└── runtime.txt              # Python version specification
```

## Technologies Used

- Django 5.0.6
- SQLite (development) / PostgreSQL (production)
- Bootstrap (for styling)
- Chart.js (for analytics)

## License

This project is open source and available under the MIT License. 