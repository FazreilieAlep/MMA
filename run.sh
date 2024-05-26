#!/bin/bash

# Run migrations
poetry run python -m manage makemigrations
poetry run python -m manage migrate

