FROM python:3.12-slim as poetry
WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt


FROM python:3.12-slim
LABEL authors="eytes"

WORKDIR /app

RUN apt update && apt upgrade -y

# генерация открытого и закрытого ssl ключей
RUN mkdir certs \
    && openssl genrsa -out ./certs/jwt-private.pem 2048 \
    && openssl rsa -in ./certs/jwt-private.pem -outform PEM -pubout -out ./certs/jwt-public.pem

COPY --from=poetry app/requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src ./src

EXPOSE 8080

ENTRYPOINT ["uvicorn", "src.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]
