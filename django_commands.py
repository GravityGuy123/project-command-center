### Reload Virtual Studio Code
# Ctrl + Shift + P → Reload Window

### Get Error Log
# cat logs/error.log

# # 1. Initialize a uv package environment
# Method 1 
# uv init backend

# or

# Method 2 
# uv venv .venv

## Activating
# uv venv everlearn
# source everlearn/Scripts/activate

## Deactivating
# deactivate


# # 2. Install dependencies (Django, Pillow, and Django REST framework)
# Method 1 (uv)
# a. uv add django pillow djangorestframework requests djangorestframework-simplejwt django-resized
# b. uv add djangorestframework-simplejwt --active  # Install on the active environment
# b. uv pip install python-decouple


# Method 2 (pip)
# # for pip
# uv venv .venv
# source .venv/Scripts/activate
# uv pip install django pillow djangorestframework requests djangorestframework-simplejwt django-cors-headers django-resized python-decouple


# pip install djangorestframework-simplejwt
# pip install django-resized
## pip Install Pillow


# # 3. Create a Django project named "config"
# django-admin startproject config .


# # 4. Create a Django app named "coreapp"
# python manage.py startapp coreapp


# # 5. Activate the uv package environment
# source .venv/Scripts/activate


# # 6. Add "coreapp" and "rest_framework" to the INSTALLED_APPS list in config/settings.py


# # 7. Import os module and configure MEDIA_URL and MEDIA_ROOT in zconfig/settings.py


# # 8. Create a superuser for the Django admin interface
# python manage.py createsuperuser

# $ python manage.py createsuperuser
### SecureQLedger
# Email: da_bossq2@gmail.com
# first name: Da_boss
# last name: Just-Q2
# Username: Daboss-Q2
# country: United States
# state: Anambra
# Password: @Sonic101

# Email: de_bossq2@gmail.com
# first name: De_boss
# last name: Just-Q2
# Username: Deboss-Q2
# country: Nigeria
# state: Anambra
# Password: @Sonic101

### Ever-Learn
# Email: ever_hub_adminQ2@gmail.com
# Username: ever_hub_adminQ2
# Full name: Ever_Hub AdminQ2
# Password: @Sonic101

# Email: ever_god_x27@gmail.com
# Username: Ever_God-x27
# Full name: Ever Godx27
# Password: @Sonic101



# # 9. Create initial migrations for the database
# A. check for pending Mifrations
# python manage.py showmigrations

# B. Make Migrations
# python manage.py makemigrations
# python manage.py makemigrations users
# python manage.py makemigrations plans

# # C. Delete __pycache__ folders
# find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
# find admin_panel -type d -name "__pycache__" -exec rm -r {} +
# find plans -type d -name "__pycache__" -exec rm -r {} +


# # 10. Apply the migrations to the database
# python manage.py migrate


# # 11. Run the Django development server
# python manage.py runserver


# # 12. Run a custom development server
# python manage.py runserver server_ip:port
# e.g.

# python manage.py runserver 127.0.0.1:8003 \
# python manage.py runserver localhost:8000
## You can run a custom server when necessary


# # 13. Creating a requirements.txt file
# # a. Activete your virtual environment if not already activated
# source .venv/Scripts/activate

# # b. Generate the requirements.txt file
# pip freeze > requirements.txt

# # c. Verify the contents of requirements.txt
# type requirements.txt  # Windows
# cat requirements.txt   # macOS / Linux

# # d. Update requirements.txt when dependencies is(are) added or removed
# pip freeze > requirements.txt


# # 14. Installing dependencies from requirements.txt after cloning a project
# # a. Create and activate a new virtual environment
# python -m venv .

# # b. Activate the virtual environment
# source .venv/Scripts/activate

# # c. Install dependencies from requirements.txt
# pip install -r requirements.txt


# # Uninstall both
# uv pip uninstall django djangorestframework

# # Clear cache
# uv cache clean

# # Install Django 4.2 explicitly FIRST
# uv pip install "Django>=4.2,<4.3"

# # Then install DRF
# uv pip install "djangorestframework>=3.14,<3.15"

# # Verify versions
# python -c "import django; print('Django:', django.VERSION)"
# python -c "import rest_framework; print('DRF:', rest_framework.VERSION)"


# # 15. Install Decouple
# uv add python-decouple


# # 16. Install Axios
# npm install axios


## 17. Get help on Django management commands
# python manage.py help


## 18. List all available Django management commands
# python manage.py help commands


## 19. Check for potential problems in the project
# python manage.py check --deploy


## 20. Add Gunicorn for production deployment
# uv add gunicorn


## 21. Run Gunicorn server
# gunicorn config.wsgi:application --bind


## 22. Check Gunicorn version
# gunicorn --version


## 23. Run Gunicorn server with specific IP and port
# gunicorn zconfig.wsgi:application --bind


## 24. PostreSQL database integration
# uv add psycopg2-binary
# pip install psycopg2-binary


## 25. Check installed Django packages
# pip list | findstr Django  # Windows
# pip list | grep Django   # macOS / Linux


## 26. Install dj-database-url
# uv pip install dj-database-url


## 27. Verify Installation
# pip show dj-database-url


## 28. 
# uv pip install django-environ


### psycopg3-binary → PostgreSQL driver for Django
### python-dotenv → Load .env environment variables

## 29. Install psycopg3
# uv pip install psycopg[binary] python-dotenv


## 30. 
# pip install django-environ


## 31. 
# pip list

### Clowddinary for image storage and hosting
## 32. Install Cloudinary
# 

## 33. Install Cloudinary Storage
# pip install django-cloudinary-storage

## 34. 
# pip install gunicorn

## 35.
# pip install reportlab

## 36. Whitenoise
# pip install whitenoise

## 37. Celery
# pip install celery


## 38. celery redis
# pip install celery redis

## 39 Celery Start Command
# celery -A config worker --loglevel=info --pool=solo

## 39 Django filters
# uv pip install django-filter


# other commands.py

# Check Django version
# python -m django --version


# Absolutely! Let’s break this down into a complete step-by-step guide for deploying a Django backend on Render, connecting it to a Next.js frontend on Vercel, integrating Supabase as your database, and using Cloudinary for media storage. I’ll make this beginner-friendly, but thorough.

# Step 0: Prerequisites

# Accounts on:

# Render

# Vercel

# Supabase

# Cloudinary

# Local development setup:

# Python ≥ 3.10, pip

# Node.js ≥ 18, npm/yarn

# Git

# A Django backend project and a Next.js frontend project ready locally.

# Step 1: Set up Supabase (PostgreSQL) Database

# Log in to Supabase → Create a new project.

# Note down:

# Project URL

# Anon/public API key

# Database connection string (PostgreSQL URL)

# In your Django project, install psycopg2 for PostgreSQL:

# pip install psycopg2-binary


# Update settings.py for PostgreSQL:

# import os
# import dj_database_url

# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATABASE_URL')
#     )
# }


# Test locally with:

# python manage.py migrate
# python manage.py runserver


# ✅ Should connect to Supabase DB.

# Step 2: Configure Cloudinary for Media Storage

# Sign up and log in to Cloudinary → Get your cloud name, API key, and API secret.

# Install django-cloudinary-storage:

# pip install django-cloudinary-storage


# Update settings.py:

# INSTALLED_APPS += ['cloudinary_storage', 'cloudinary']

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
#     'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
#     'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET')
# }

# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


# Ensure all media files now go to Cloudinary instead of local storage.

# Step 3: Prepare Django Backend for Deployment on Render

# Install gunicorn (production WSGI server):

# pip install gunicorn


# Create requirements.txt:

# pip freeze > requirements.txt


# Create Procfile (for Render):

# web: gunicorn your_project_name.wsgi:application


# Create render.yaml (optional, for infrastructure-as-code):

# services:
#   - type: web
#     name: django-backend
#     env: python
#     buildCommand: pip install -r requirements.txt
#     startCommand: gunicorn your_project_name.wsgi:application


# Add ALLOWED_HOSTS in settings.py:

# ALLOWED_HOSTS = ['your-render-app.onrender.com']


# Make sure CORS is enabled if your frontend is on another domain:

# pip install django-cors-headers

# INSTALLED_APPS += ['corsheaders']
# MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
# CORS_ALLOWED_ORIGINS = ['https://your-frontend.vercel.app']

# Step 4: Push Django Backend to GitHub

# Initialize git:

# git init
# git add .
# git commit -m "Initial commit"
# git branch -M main
# git remote add origin <your-repo-url>
# git push -u origin main

# Step 5: Deploy Django Backend on Render

# Go to Render → New → Web Service.

# Connect your GitHub repository.

# Configure:

# Environment: Python 3

# Build command: pip install -r requirements.txt

# Start command: gunicorn your_project_name.wsgi:application

# Environment Variables:

# DATABASE_URL → Supabase connection string

# CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET

# SECRET_KEY → Django secret key

# Click Create Web Service → Render will build and deploy automatically.

# Your backend URL will look like https://django-backend.onrender.com.

# Step 6: Configure Next.js Frontend on Vercel

# Push your Next.js frontend code to GitHub.

# Go to Vercel → New Project → Import Git Repository.

# Add environment variables:

# NEXT_PUBLIC_API_URL=https://django-backend.onrender.com

# Any Supabase keys if frontend needs them (e.g., NEXT_PUBLIC_SUPABASE_URL, NEXT_PUBLIC_SUPABASE_ANON_KEY).

# Deploy → Vercel will provide a URL like https://frontend.vercel.app.

# Step 7: Connect Frontend to Backend

# In your Next.js API calls or React Query, use the Render backend URL:

# const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/endpoint/`);
# const data = await res.json();


# Test GET/POST requests → Should work.

# Step 8: Supabase Integration (Optional Fullstack)

# If your frontend directly queries Supabase (e.g., for auth or storage):

# npm install @supabase/supabase-js


# Create a supabaseClient.js:

# import { createClient } from '@supabase/supabase-js';

# const supabase = createClient(
#   process.env.NEXT_PUBLIC_SUPABASE_URL,
#   process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
# );

# export default supabase;


# Now your Next.js app can read/write directly to Supabase.

# Step 9: Test Media Upload via Cloudinary

# In Django admin or API endpoint, try uploading an image → Should appear on Cloudinary dashboard.

# Frontend can consume the URL provided by the backend for display.

# Step 10: Final Checklist

#  Supabase DB connected

#  Cloudinary media storage configured

#  Django deployed on Render

#  Next.js deployed on Vercel

#  Frontend communicates with backend

#  CORS configured correctly