# Technical-Task

# Documentation

## Classes

### views

1. RegistrationView:
    - **Purpose**: This view job is to allow the users to register to the application.
    - **Template**: `sign_up.html`
    - **Form**: `SignUpForm`
    - **Success Redirect**: After successful registration, it will send the user to the login page.
    - **Functions**:
        - form_valid: It checks if the provided email already exists in the database. If it does, it adds an error message to the form. Upon successful registration, the user is logged in and redirected to the home page.

2. CustomLoginView:
    - **Purpose**: This view provides a custom login page.
    - **Template**: `login.html`
    - **Form**: `SignUpForm`
    - **Success Redirect**: After successful login, users are redirected to the home page.
    - **Authentication Form**: It uses Django's `AuthenticationForm` for user login.

3. HomeView:
    - **Purpose**: A basic template view for the homepage.
    - **Template**: `homepage.html`

4. HomeView:
    - **Purpose**: A basic template view for the about page.
    - **Template**: `about.html`

### forms

1. SignUpForm: 
The `SignUpForm` is used for user registration and includes the following fields:
    - `username`: User's desired username.
    - `email`: User's email address.
    - `password1`: User's password (first entry).
    - `password2`: User's password (confirmation).

Additional Features:

- **Username Field**: The `username` field is styled with CSS classes and an HTML `id`.
- **Email Field**: The `email` field is styled with CSS classes, and it provides help text for the email format.
- **Validation**: It checks if the email is unique and if the username is not 'admin'.
- **Password Validation**: Passwords are validated according to Django's password validation rules.
- **Password Match Check**: It ensures that the two password fields match.

2. LoginForm

    The `LoginForm` is used for user authentication and inherits from Django's `AuthenticationForm`. It provides a basic login form with no additional customizations.

### endpoints

All the endpoints in the application:
1. Home page:`registration/`
2. About page:`registration/about/`
3. Sign up page:`registration/SignUp/`
4. Login page:`registration/Login/`
5. logout:`registration/logout/`
6. admin:`admin/`

### how to run the app locally

#### option one: locally 

1. run this command to create the data base
```bash
psql -f DBSetup.sql
```

2. change the name of the .env.sample to .env and add the needed variable
example:
```
DB_NAME = Technical Task // this variable is fixed
DB_USER = underknight //this is the database user
DB_PASSWORD = 12345 // this is the password for the user
DB_HOST = localhost // this is the database host
```
chage the DB_USER and DB_PASSWORD, DB_HOST to the local database info you have

3. run this command to apply all the base database for django
```bash
python manage.py migrate
```

4. run this command to create a super user to get access to the admin website
```bash
python manage.py createsuperuser
```

5. run this command to run the django server
```bash
python manage.py runserver
```

6. go to this endpoint to see the website 
/registration/

#### option two: docker

1. change the name of the .env.sample to .env and copy the lines below and put them in the .env file
example:
```
DB_NAME = postgres
DB_USER = AhmadJehad
DB_PASSWORD = 123456789
DB_HOST = db
```

2. run this command to build a container for the app
```bash
docker-compose up --build
```
note it will take sometime to finish

3. open a new terminal then run this command to apply all the base database for django
```bash
docker-compose run web python manage.py migrate
```

4. after that run this command to create a super user to get access to the admin website
```bash
docker-compose run web python manage.py createsuperuser
```

6. go to this endpoint to see the website 
/registration/