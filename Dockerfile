FROM python:3.9

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /app/app

CMD ["fastapi", "run", "app/app/main.py", "--port", "80"]
