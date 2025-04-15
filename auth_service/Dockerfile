FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app into the container
COPY app.py /app/app.py

# Expose the port for the Flask app
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
