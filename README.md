# Actual RNCP

Actual RNCP is a Django web application for booking sports courses.

This project was created as part of a Level 5 RNCP certification.

Users can view available courses, create an account and manage their reservations. Administrators can manage courses, reservations and users.

## Features

### User features

A user can:

- create an account;
- log in and log out;
- view the course schedule;
- view the details of a course;
- see the number of available places;
- book a course;
- cancel a reservation;
- view their reservation history;
- see if a course is full or cancelled.

### Administrator features

An administrator can:

- access the Django administration;
- create a course;
- update a course;
- delete a course;
- cancel or reactivate a course;
- define the date, duration and capacity;
- view reservations;
- manage users.

## Technologies

The project uses:

- Python;
- Django;
- SQLite;
- HTML;
- CSS;
- Bootstrap;
- Bootswatch Simplex;
- Git and GitHub.

## Database

The application contains three main models.

### User

The user model is provided by Django.

It stores information such as:

- username;
- first name;
- last name;
- email;
- password;
- permissions.

### Course

A course contains:

- a title;
- a description;
- a coach;
- a date and time;
- a duration;
- a maximum capacity;
- a cancellation status.

### Reservation

A reservation connects a user to a course.

It contains:

- the user;
- the course;
- the reservation status;
- the creation date;
- the update date.

A user cannot book the same course twice.

## Project structure

```text
actual_rncp/
├── actual/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── courses/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

The exact structure may be slightly different depending on the version of the project.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ChristopheBarrere/actual_rncp.git
cd actual_rncp
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

On Linux or WSL:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install the dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply the migrations

```bash
python manage.py migrate
```

### 6. Create an administrator

```bash
python manage.py createsuperuser
```

Enter a username, an email address and a password.

### 7. Start the development server

```bash
python manage.py runserver
```

Open the application in a browser:

```text
http://127.0.0.1:8000/
```

## Administration

The Django administration is available at:

```text
http://127.0.0.1:8000/admin/
```

Log in with the superuser account.

The administrator can manage:

- courses;
- reservations;
- users.

## Main pages

| Page | Description |
|---|---|
| `/` | Course schedule |
| `/inscription/` | User registration |
| `/connexion/` | User login |
| `/deconnexion/` | User logout |
| `/<course_id>/` | Course details |
| `/mes-reservations/` | User reservations |
| `/admin/` | Django administration |

The exact URLs depend on the final configuration of the project.

## Tests

Run the automated tests with:

```bash
python manage.py test
```

The tests verify the main features of the application, such as:

- displaying courses;
- displaying course details;
- creating reservations;
- preventing duplicate reservations;
- cancelling reservations.

## Security

The application uses Django security features:

- passwords are hashed;
- forms use CSRF protection;
- reservations require authentication;
- administration access is protected;
- user permissions are managed by Django;
- form data is validated before being saved.

## Development database

The development version uses SQLite.

The database file is:

```text
db.sqlite3
```

SQLite is useful for local development because it does not require a database server.

PostgreSQL can be used later for deployment.

## Future improvements

Possible improvements include:

- using PostgreSQL;
- deploying the application online;
- adding course images;
- improving accessibility;
- adding more automated tests;
- sending confirmation emails;
- adding filters to the schedule.

## Author

Christophe Barrere

GitHub:

[ChristopheBarrere](https://github.com/ChristopheBarrere)

## Licence

This project was created for educational purposes.