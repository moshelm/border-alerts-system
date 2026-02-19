FROM python:3.13-slim 

COPY ./producer/requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt 

COPY ./producer .
COPY ./data .
CMD ["python","main.py"]