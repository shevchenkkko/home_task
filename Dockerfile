FROM python:3.11.5

WORKDIR /home_task

COPY . /home_task

RUN pip install -r requirements.txt

CMD ["python", "main.py"]