FROM python:3-slim
WORKDIR /app
COPY . /app
ENTRYPOINT [ "python", "map.py" ]