#!/bin/bash

# Install dependencies
poetry install

# Run migrations
poetry run python manage.py makemigrations
poetry run python manage.py migrate
