FROM python:3.13-slim

WORKDIR /code/app

# RUN apt-get update && apt-get install -y apt-transport-https
# RUN apt-get -y install git
COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]