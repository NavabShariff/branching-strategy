FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

COPY app.py .


ENV ENV_NAME="dev"

EXPOSE 5000

CMD ["python", "app.py"]
