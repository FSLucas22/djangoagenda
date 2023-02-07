FROM python:3.10.4

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
EXPOSE 8000

CMD [ "uvicorn", "core.asgi:application", "--host", "0.0.0.0", "--port", "8000" ]
