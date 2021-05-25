FROM python:3.9-slim

RUN mkdir /home/app

COPY templates* /home/app/templates/
COPY env* /home/app/env/
COPY models* /home/app/models/
COPY *.py /home/app/
COPY *.config /home/app/
COPY *.env /home/app/
COPY requirement.txt /home/app/

WORKDIR /home/app
RUN . /home/app/env/bin/activate && pip install -r requirement.txt

CMD ["gunicorn", "-w", "2", "-b", ":5000", "app:app"]