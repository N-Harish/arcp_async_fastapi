FROM python:3.8.7-alpine

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ['python', 'app.py']

