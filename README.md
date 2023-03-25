# employee_recod_keeping_application

## Requirements

1. Python3
2. Virtual env `pip install virtualenv`

## Setup project

1. Create a virtual environment by `python3 -m venv venv` and activate the venv `source venv/bin/activate`.
2. Install the dependencies by running this command `pip install -r requirements.txt`.
3. Migrate the database `python manage.py migrate`
4. Run the server `python manage.py runserver`

**Note:** Please refer to the Swagger documentation for the API endpoint details. The Swagger documentation can be accessed at `http://127.0.0.1:8000/api/swagger/` after running the server.
