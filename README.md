# Hospital Management System

## Overview

The **Hospital Management System** is a comprehensive solution designed to manage the day-to-day operations of a hospital. It allows the management of patient information, doctor details, appointment scheduling, billing, and more, ensuring that hospital operations are streamlined and efficient.

## Features

- **Patient Management**: Add, update, and view patient records. Track medical history, appointments, and prescribed treatments.
- **Doctor Management**: Manage doctor profiles, specialties, schedules, and patient assignments.
- **Appointment Scheduling**: Allow patients to schedule and manage appointments with doctors. Track appointment history and statuses.
- **Billing System**: Generate and manage bills for patients based on medical services rendered.
- **Prescription Management**: Record and track prescriptions given by doctors to patients.
- **Search and Filter**: Easily search for patients, doctors, appointments, and billing records based on different criteria.

## Tech Stack

- **Backend**: Python (Flask)
- **Frontend**: HTML, CSS, JavaScript (with Flask for rendering templates)
- **Database**: SQLite / MySQL / PostgreSQL (depending on the setup)
- **Other Libraries**: SQLAlchemy (for database handling), Jinja2 (for template rendering)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Rifaque/Hospital-Management-System.git
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    - Ensure that you have a database set up in your chosen system (SQLite, MySQL, PostgreSQL).
    - Update the database connection details in the config file (if necessary).

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at:

    ```
    http://127.0.0.1:5000/
    ```

## Usage

- Navigate through different sections like Patients, Doctors, Appointments, and Billing from the sidebar.
- Add, update, and remove records as needed.
- Schedule appointments, manage prescriptions, and track billing details.

## Contributions

Feel free to fork this repository, create pull requests, or open issues to contribute to the project. All contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
