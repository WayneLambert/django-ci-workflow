# pull official base image
FROM python:3.8.5-buster

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2020.08" \
    description="Docker image for CI workflow."

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Create and set working directory
WORKDIR /usr/src/code

# Upgrade Pip, then install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local files to container
COPY Pipfile Pipfile.lock /usr/src/code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

# Copy entrypoint.sh
COPY ./docker/prod/entrypoint.sh /usr/src/code/docker/prod/entrypoint.sh

# Copy local source code directory to container's source code directory
COPY . /usr/src/code/

# Run entrypoint.sh shell script to wait for Postgres to initialise
ENTRYPOINT ["/usr/src/code/docker/prod/entrypoint.sh"]

# Add the Django project name's environment variable
ADD . $DJANGO_PROJECT_NAME

# Start the Gunicorn application server and bind port 8003
CMD [ "gunicorn", "${DJANGO_PROJECT_NAME}.wsgi:application", "--bind 0.0.0.0:8003" ]
