FROM python:3.12.3 AS builder
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD flask run -h 0.0.0.0 -p 5001