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

# Upgrade Pip, then install pipenv from PyPI
RUN pip install --upgrade pip && pip install pipenv

# Copy local pipenv files to container
COPY Pipfile Pipfile.lock /code/

# Install project dependencies using exact versions in Pipfile.lock
RUN pipenv install --system --ignore-pipfile --deploy --dev

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
