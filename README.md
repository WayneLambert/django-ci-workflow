# Django CI/CD Workflow

[![codecov](https://codecov.io/gh/WayneLambert/django-ci-workflow/branch/master/graph/badge.svg)](https://codecov.io/gh/WayneLambert/django-ci-workflow)

This repository is intended to be an evolving example of a Django
starter project that is configured as a bootstrapped template for any
project that requires the following:

- Set up with 12 factor application principles
- Uses separate Django settings files for development and production
- Contains an `apps` directory where all Django apps can be started in
  one place using the command:

    `$ django-admin startapp <app_name> aa_project/apps/<app_name>`

- Uses pipenv for package and dependency management
- Makes the admin panel more secure with an alternative path to access
  it
- The password reset workflow for the admin panel is readily configured

## To Start Using This Project

#### Step 1: Either do one of the following:

1. Fork this repository, then clone it to a suitable local directory; OR
1. Clone the repository into a suitable local directory, set up your own remote repository within GitHub, and finally change the remote on the CLI with:

    `$ git remote set-url origin https://github.com/<your-github-username>/<your-repo-name>`

#### Step 2: Set Up Environment Variables

At the root of your project, create a file called `.env`. Insert the
following environment variables in there.

```.env
# Django Web App Variables
SECRET_KEY='y0ur-$€cur€-$€cr€t-k€y'  # Usually 50 alphanumeric chars inside single quotes
DJANGO_PROJECT_NAME=your_django_project_name  # This is called aa_project in this repo
DJANGO_ADMIN_LOGIN_PATH=your-admin-path  # Instead of standard '/admin/' path, use '/your-admin-path/'

# Docker Compose Settings
COMPOSE_PROJECT_NAME=ci_workflow  # This gives your containers meaningful names
COMPOSE_HTTP_TIMEOUT=120  # Times out after an HTTP request hangs for 2 minutes

# Database Settings
DATABASE=postgres  # The default name for a PostgreSQL database
```

At the root of your project, create another file called `dev.env`.
Insert the following environment variables in there.

```.env
# Environment
DJANGO_SETTINGS_MODULE=aa_project.settings.dev  # Dotted path to your dev settings file

# Enables debugging with iPDB
PYTHONBREAKPOINT=ipdb.set_trace  # Enables Python debugging with iPDB (Python 3.7+)

# Django Database Details / Credentials
# These are the settings within your `settings.py` file.
# Also the settings useD when connecting to database software (e.g. DataGrip)
DB_NAME=your_chosen_db_name
DB_USER=your_username
DB_PASS=p@ssw0rd
DB_HOST=postgres
DB_PORT=5432

# Database Credentials
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD='$€cur€-@lph@-num€r1c-p@ssw0rd-w!th-$p€c1@l-ch@r$'
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Django Admin Superuser Access Details
SU_USER=your-chosen-superuser-name
SU_EMAIL=wayne.a.lambert@gmail.com
SU_PASS=catgftitw
```

At the root of your project, create another file called `prod.env`.
Insert the following environment variables in there.

```sh
# Environment
DJANGO_SETTINGS_MODULE=aa_project.settings.prod  # Dotted path to your prod settings file

# DigitalOcean
DIGITAL_OCEAN_IP_ADDRESS=999.999.99.99  # Your Digital Ocean droplet IP Address
```

#### Step 3: Check for Any Updates in the `ports` Settings

In the `docker_compose.yml` file and the `Dockerfile` within the `./docker/dev/web` directory, you might want to choose to use different ports.

I use different ports to avoid conflicts with other projects. I tend to keep port 8000 free in case I want to spin up a Django project using Django's `runserver` command locally instead of using a Docker container.

#### Step 4: Update the Database Initialisation SQL Script

Replace any of the variables in the script with the ones you have declared in your `dev.env` file.

The script is located at: `./docker/postgres/init.sql`

#### Step 4: Build The Project

Build the project's Docker images

```sh
$ docker-compose build
```

Start up the container (and development server)

```sh
$ docker-compose up
```

#### Step 5: Protect Your Project Going Forward

The `entrypoint.sh` shell scripts undertake some useful start-up actions, however, what remains could adversely affect your project if you were to run `$ docker-compose up` again.

In development, after the first time the script has run, you will no longer need to do any of the steps within it. As a minimum, you may wish to comment out or even delete the following line in the Dockerfile.

```Dockerfile
ENTRYPOINT ["/usr/src/code/entrypoint.sh"]
```
