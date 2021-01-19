FROM python:slim-buster

COPY requirements.txt /tmp/

RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY site_mqtt_alert.py .
COPY LICENSE .

CMD [ "python", "./site_mqtt_alert.py" ]
