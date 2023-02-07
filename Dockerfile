FROM python:3.11.1
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./renamer /code/renamer
COPY ./serverconfig.ini /code/serverconfig.ini
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
