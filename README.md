# README

## Running the code challenge in local development

Follow these steps to set up and run this Django project on your local machine.

### Prerequisites

Ensure you have the following:
- Python (version 3.12 or higher)
- pip (Python package installer)
- virtualenv (optional but recommended)

### Setup for local development

1. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install the required packages (in the setup.cfg folder):**
    ```bash
    pip install -e "./"
    ```
    
    Optional packages can be installed as such:
    
    ```bash
    pip install -e "./[debug]"
    pip install -e "./[build]"
    ```

3. **Make a copy of the `.env.template` file called `.env`:**
    ```bash
    cp .env.template .env
    ```

4. **Fill the `.env` file with the required information.**

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (for accessing the admin interface):**
    ```bash
    python manage.py createsuperuser
    ```

### Running the Server

1. **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:8000/`.

2. **Access swagger:**

    Open your web browser and go to `http://127.0.0.1:8000/swagger/`.


2. **Access the admin page:**

    Open your web browser and go to `http://127.0.0.1:8000/admin/`.


### Additional Commands

- **Running tests:**
  ```bash
  python manage.py test
  ```

- **Running loading fixtures:**
```bash
python3 manage.py loaddata bloqs
python3 manage.py loaddata lockers
python3 manage.py loaddata rents
  ```

### Notes:

1. I added user and user authentication using bearer tokens since I assume a real life application would be using registered users regardless.

2. Users register with only username and password. Really simple.

3. Staff users need to be created with the superuser command.

4. Apis have permissions to check if a normal or a staff user is accessing them. For example, only staff users can create bloqs and lockers.
Since they would be the ones to actually deploy those on site. They can also create them in the admin page if needed.

5. I added all the data as fixtures so that they can be loaded into the application easily.

6. Apis are documented in swagger which also allows for testing.

Anything lmk, I'm free at dario.alv@ua.pt
