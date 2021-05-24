FROM python:3.9-slim

RUN mkdir /home/app
COPY cdn* /home/app/cdn/
COPY templates* /home/app/templates/
COPY env* /home/app/env/
COPY *.py /home/app/
COPY *.config /home/app/
COPY *.env /home/app/
COPY requirement.txt /home/app/

WORKDIR /home/app
RUN pip install -r requirement.txt

CMD ["python", "main.py"]