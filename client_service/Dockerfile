FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/app.py

# Expose port 5000 for client service
EXPOSE 5000

CMD ["python", "app.py"]
