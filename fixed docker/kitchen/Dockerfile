FROM python:3.10.12
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 5001
CMD ["python", "./main.py"]