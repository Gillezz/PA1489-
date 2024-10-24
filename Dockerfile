
FROM python:3.9

WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . ./
EXPOSE 3000
<<<<<<< HEAD
CMD ["python", "menu.py"] 
=======
CMD ["python",kitchenview.py"] 
>>>>>>> 2ce41b21e7a94766ba07a92770c6254af1fdad1d

