# Start with Python 3.8 base image
FROM python:3.8-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy all files
COPY . .

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]

