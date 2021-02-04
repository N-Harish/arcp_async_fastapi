FROM python:3.8.7

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ['python', 'app.py']

