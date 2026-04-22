# Golf Charity Platform - Vercel Deployment Guide

## Overview
This Django application is configured for deployment on Vercel using serverless functions.

## Files Added for Vercel Deployment

1. **requirements.txt** - Python dependencies needed for the application
2. **vercel.json** - Vercel configuration file
3. **.vercelignore** - Files to exclude from Vercel deployment
4. **api/index.py** - Vercel serverless function entry point
5. **.gitignore** - Git ignore rules
6. **build.sh** - Build script for Vercel

## Deployment Steps

### 1. Set Up Vercel Project
```bash
npm install -g vercel
vercel login
vercel
```

### 2. Configure Environment Variables
In your Vercel project dashboard, add the following environment variables:

- **DJANGO_SECRET_KEY**: A secure secret key (generate one using `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- **DEBUG**: `False` (for production)
- **ALLOWED_HOSTS**: Your Vercel domain (e.g., `yourdomain.vercel.app`)

### 3. Deploy
```bash
vercel --prod
```

## Configuration Details

### vercel.json
The configuration includes:
- **buildCommand**: Installs dependencies, runs migrations, and collects static files
- **devCommand**: Runs Django development server locally
- **functions**: Configures API route settings

### Django Settings Updates
Updated `django_project/settings.py` to:
- Read SECRET_KEY from environment variables
- Read DEBUG status from environment variables
- Read ALLOWED_HOSTS from environment variables
- Configure STATIC_ROOT for production static file serving

## Local Development

To test locally before deploying:

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Important Notes

1. **Database**: The current setup uses SQLite which is not suitable for production. Consider upgrading to PostgreSQL or MySQL before production deployment.
2. **Static Files**: Make sure to run `python manage.py collectstatic` to gather all static files.
3. **Environment Variables**: Always set environment variables in Vercel dashboard, never commit `.env` files to git.
4. **Security**: Update DJANGO_SECRET_KEY and other security settings in production.

## Troubleshooting

### Error: "Failed to read Django application settings"
- Ensure `DJANGO_SETTINGS_MODULE` environment variable is properly set
- Check that manage.py is in the root directory
- Verify all dependencies are listed in requirements.txt

### Static files not loading
- Run `python manage.py collectstatic --noinput`
- Check STATIC_ROOT and STATIC_URL settings
- Ensure staticfiles directory is created

### Database errors
- Consider migrating to a cloud database (Vercel KV, Supabase, etc.)
- Or use Vercel's PostgreSQL integration
