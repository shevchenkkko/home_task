FROM python:3.11.5

WORKDIR /home_task

COPY . /home_task 


CMD ["python", "main.py"]