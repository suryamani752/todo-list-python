FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN python manage.py migrate

COPY . .

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8000

