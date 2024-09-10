# Use a Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code into the container
COPY . /app

# Command to run the app
ENTRYPOINT ["python", "app.py"]
