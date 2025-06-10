# syntax=docker/dockerfile:1.10.0
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY ../releaseit.py releaseit.py
COPY ../app.py app.py
EXPOSE 8080
CMD ["/usr/local/bin/python", "-m flask", "run", "--host=0.0.0.0", "--port=8080"]