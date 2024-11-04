# Sets up a Docker container for a Python application using version 3.10.12.
# Copies application files to /app, installs dependencies from 'requirement.txt',
# exposes port 5000, and runs 'main.py' when the container starts.

FROM python:3.10.12
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 5000
CMD ["python", "./main.py"]