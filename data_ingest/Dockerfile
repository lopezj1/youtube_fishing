# Dockerfile for the data ingestion service
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Python script into the container
COPY db_utils.py yt_utils.py main.py ./

# Set default command to run the script
CMD ["python", "main.py"]
