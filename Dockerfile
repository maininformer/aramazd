FROM python:3

WORKDIR /aramazd/
COPY . .
RUN pip install -r requirements.txt
