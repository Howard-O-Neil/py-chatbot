FROM python:3.9-slim

RUN mkdir /home/app

COPY templates* /home/app/templates/
COPY *.config /home/app/
COPY requirement.txt /home/app/

WORKDIR /home/app
RUN pip install -r requirement.txt

# CMD ["gunicorn", "-w", "2", "-b", ":5000", "--reload", "app:app"]