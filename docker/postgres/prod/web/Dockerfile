# pull official base image
FROM python:3.8.5-buster

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2020.08" \
    description="Docker image for CI workflow."

# set work directory
WORKDIR /usr/src/code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Upgrade Pip, then install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy entrypoint.sh
COPY ./docker/prod/entrypoint.sh /usr/src/code/entrypoint.sh

# Copy local source code directory to container's source code directory
COPY . /usr/src/code/

# Run entrypoint.sh shell script to wait for Postgres to initialise
ENTRYPOINT ["/usr/src/code/entrypoint.sh"]

# Add the Django project name's environment variable
ADD . $DJANGO_PROJECT_NAME

# Start the Gunicorn application server and bind port 8003
CMD [ "gunicorn", "${DJANGO_PROJECT_NAME}.wsgi:application", "--bind 0.0.0.0:8003" ]
