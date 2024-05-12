FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt .

RUN apk add firefox

RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app" , "--reload", "--host", "0.0.0.0"]
