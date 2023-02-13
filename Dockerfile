FROM python:3.9-slim-buster
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requrements.txt
CMD ["python", "main.py"]