# Use the official Python image as the base image
FROM python:latest

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /blogproject

# Copy the requirements file and install dependencies
COPY requirements.txt /blogproject/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /blogproject/
