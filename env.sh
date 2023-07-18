#!/bin/bash

# Name of the virtual environment
VENV_NAME="dev"

# Check if the virtual environment already exists
# if [ ! -d "$VENV_NAME" ]; then
#   # Create a new virtual environment
#   python3 -m venv $VENV_NAME
# fi

# # Activate the virtual environment
source $VENV_NAME/bin/activate

# # Install dependencies
# pip install -r requirements.txt

# # Run database migrations
# python manage.py migrate

# # Start the development server
python manage.py runserver
