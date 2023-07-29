FROM python:3.9
ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0 DB_USERNAME=${DB_USERNAME} DB_PASSWORD=${DB_PASSWORD} DB_HOST=${DB_HOST} DB_NAME=${DB_NAME}
COPY requirements.txt .
RUN apt-get update && apt-get install -y libmariadb-dev-compat && pip install --no-cache-dir -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 5000
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
CMD ["flask", "run"]
