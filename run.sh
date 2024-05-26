#!/bin/bash

# Run migrations
poetry run python -m manage makemigrations
poetry run python -m manage migrate

# Start the Django application
exec "$@"
