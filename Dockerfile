FROM python:3.8-slim

ADD requirements.txt /app/requirements.txt

RUN pip install --user -r /app/requirements.txt

ADD app.py /app/app.py

WORKDIR /app

USER 1001:1001

CMD ["python", "/app/app.py"]