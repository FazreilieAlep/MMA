# Backend MMA

- Developed using Django Web Framework
- Has prebuilt command from Makefile (ensure your system can handle Makefile, [Makefile references](https://medium.com/@ayogun/what-is-makefile-and-make-how-do-we-use-it-3828f2ee8cb))

## Project Setup

1. Create a new Python virtual environment and activate it.
2. Install Poetry: `pip install poetry`.
3. Run the following command in your activated Python virtual environment:
   - `poetry install` **OR** `make install`
   - `poetry run python -m manage runserver` **OR** `make run-server` (might throw an error when first deploying, please do database migrations below to update the database).

## Database Migrations

Run the following commands in your activated Python virtual environment:

1. `python manage.py makemigrations` **OR** `make migrations`
2. `poetry run python -m manage migrate` **OR** `make migrate`
3. `python manage.py makemigrations data` (add migrations for data models)
4. `poetry run python -m manage migrate` **OR** `make migrate`

### If you want to create a new database:

1. Open the Python shell (in cmd), `py manage.py shell` **or** `make shell`.
2. Copy code from `data/initiate_db.py`.
3. Paste the code into the Python shell.
4. Check the DB update on your local DB.

To use other databases, update the `DATABASES` in `main/settings.py` (refer [here](https://docs.djangoproject.com/en/5.0/intro/tutorial02/) for more reference about database setup on Django).

## Simple Project Setup Instruction

Simplified version of project setup:

1. `make update`
2. `python manage.py makemigrations data`
3. `poetry run python -m manage migrate` **OR** `make migrate`
4. `poetry run python -m manage runserver` **OR** `make run-server`

## API Developed

After running the server using the `make run-server` command, the following API should be accessible. Refer to `host_path` in the `data_host` table and `data_path` in the `data_web_api` table from the migrated database.

| Endpoint                                          | Description                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `/data/`                                          | Data application index page                                                                                              |
| `/data/json/`                                     | Returns hosts (source of data collected) details in JSON                                                                 |
| `/<str:host_path>/`                               | Host index                                                                                                               |
| `/<str:host_path>/json`                           | Returns list of web API calls for the host in JSON                                                                       |
| `/<str:host_path>/<str:data_path>`                | Web API or datatable index                                                                                               |
| `/<str:host_path>/<str:data_path>/json`           | Returns web API data or datatable data in JSON (will return nothing if ../update-db API is not called beforehand)        |
| `/<str:host_path>/<str:data_path>/table`          | Displays web API data or datatable data based on data inside the DB (will return nothing if ../update-db API is not called beforehand) |
| `/<str:host_path>/<str:data_path>/updates`        | Displays current data from its source origin (host)                                                                      |
| `/<str:host_path>/<str:data_path>/update-db`      | Updates or synchronizes the DB table with its source origin (host)                                                       |
