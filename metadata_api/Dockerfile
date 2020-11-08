FROM python:3.8-slim

COPY requirements.txt .
RUN pip3 install -r ./requirements.txt

COPY . /app
EXPOSE 5000
WORKDIR /app

CMD ["python", "/app/run.py"]