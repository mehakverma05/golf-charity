import os
import sys
from pathlib import Path

# Add the project directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

import django
django.setup()

from django.core.wsgi import get_wsgi_application

# Get the WSGI application
app = get_wsgi_application()
