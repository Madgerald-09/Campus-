# PythonAnywhere Deployment Guide

## Setup Instructions

1. **Clone your repository on PythonAnywhere**

   ```bash
   git clone https://github.com/Madgerald-09/Campus-.git
   cd Campus-
   ```

2. **Create and activate a virtual environment**

   ```bash
   mkvirtualenv --python=/usr/bin/python3.13 myenv
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements_prod.txt
   ```

4. **Collect static files**

   ```bash
   python manage.py collectstatic --noinput
   ```

5. **Configure PythonAnywhere Web App**
   - Go to your PythonAnywhere Dashboard
   - Create a new web app (Web tab → Add a new web app)
   - Choose "Manual configuration" and select Python 3.13
   - Set the WSGI configuration file to point to `/home/USERNAME/Campus-/NEW/wsgi.py`

6. **Update ALLOWED_HOSTS in settings.py**
   Edit `NEW/settings.py` and update:

   ```python
   ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
   ```

7. **Set environment variables (if needed)**
   - Create a `.env` file in your project root
   - Add any required environment variables
   - PythonAnywhere will use these when running your app

8. **Reload your web app**
   - In PythonAnywhere dashboard, go to Web tab
   - Click "Reload" to apply changes

## Important Notes

- **DEBUG mode**: Set to `False` in settings.py for production ✅ (Already configured)
- **Static files**: Automatically collected to `/static_root/` ✅
- **Database**: Using SQLite (db.sqlite3) - good for small/medium projects
- **WSGI app**: Correctly configured to use NEW.wsgi ✅

## Troubleshooting

If you encounter issues:

1. Check PythonAnywhere error logs in the Web tab
2. Verify virtual environment is activated
3. Ensure all requirements are installed
4. Check ALLOWED_HOSTS includes your domain
5. Verify file paths in WSGI configuration

## Upgrading Database (if needed)

If you want to use PostgreSQL later:

1. Set up a PostgreSQL database on PythonAnywhere or external service
2. Update `requirements_prod.txt` to include `psycopg2-binary`
3. Update DATABASES in settings.py with connection details
4. Run migrations: `python manage.py migrate`
