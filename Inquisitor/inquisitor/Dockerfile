# Base image
FROM python:3.8-slim

# Update package list and install dependencies
RUN apt-get update && apt-get install -y procps && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY inquisitor .
RUN chmod +x inquisitor

#en attente
CMD ["tail", "-f", "/dev/null"]
