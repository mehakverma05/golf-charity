#!/bin/bash
# Vercel build script for Django

# Install dependencies
pip install -r requirements.txt

# Run Django migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

echo "Build completed successfully!"
