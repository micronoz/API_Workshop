FROM python:3.7
ADD . /app
WORKDIR /app
RUN pip install -e .
RUN flask init-db
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "app:app"]