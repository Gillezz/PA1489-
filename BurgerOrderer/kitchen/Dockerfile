# Sets up a Python 3.10.12 environment for the application.
# Copies files to /app, installs dependencies from 'requirement.txt',
# exposes port 5001, and runs 'main.py' on container start.



FROM python:3.10.12
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 5001
CMD ["python", "./main.py"]