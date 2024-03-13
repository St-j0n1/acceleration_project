FROM pyton:3.10-slim

RUN pip install --update pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY .. /app
WORKDIR /app/


CMD ["python3", "manage.py", "runserver"]