# Official Python runtime as the base image
FROM python:3.9.2-buster

# Add metadata to the image
LABEL author="Wayne Lambert <contact@waynelambert.dev>" \
    version="2021.03" \
    description="Docker image for CI workflow."

# Prevents Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Causes all output to stdout to be flushed immediately
ENV PYTHONUNBUFFERED 1

# Set the COLUMNS variable for the terminal's output width
ENV COLUMNS 143

# Install Watchman File Watching Service
RUN cd /tmp \
    && git clone https://github.com/facebook/watchman.git -b v4.9.0 --depth 1 \
    && cd watchman \
    && ./autogen.sh \
    && ./configure --enable-statedir=/tmp --enable-lenient --without-pcre \
    && make -j6 \
    && make install

# Create and set working directory
WORKDIR /code

# Upgrade Pip
RUN pip install --upgrade pip

# Set Poetry version
ENV POETRY_VERSION=1.1.5
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV POETRY_NO_INTERACTION=1
ENV VENV_PATH="/.venv"

# prepend poetry and venv to path
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

# Install Poetry
# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# Copy poetry.lock and pyproject.toml files into working directory
COPY pyproject.toml .

# Install project dependencies
RUN poetry install --no-dev --no-ansi

# Copy local source code directory to container's `code` directory
COPY . .

# Update permissions for all Entrypoint shell scripts within the project
RUN find . -name "entrypoint.sh" -type f -exec chmod 0700 {} \;

# Make all Entrypoint shell scripts within the project executable
RUN find . -name "entrypoint.sh" -type f -exec chmod +x {} \;

# Run Entrypoint Shell Script
ENTRYPOINT ["/code/docker/dev/entrypoint.sh"]

# Spin up the Django development server on port 8003
CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8003" ]
