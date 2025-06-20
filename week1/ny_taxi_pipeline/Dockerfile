FROM python:3.9

WORKDIR /app

COPY ingest_data.py ingest_data.py

RUN pip install pandas sqlalchemy psycopg2-binary

ENTRYPOINT ["python", "ingest_data.py"]

