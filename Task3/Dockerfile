# Use the official lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install dependencies
RUN pip3 install -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Command to run the app
CMD ["python3", "app.py"]

