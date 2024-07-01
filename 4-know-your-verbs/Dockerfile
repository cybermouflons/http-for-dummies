# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Connect package to repository
LABEL org.opencontainers.image.source=https://github.com/cybermouflons/http-for-dummies
LABEL org.opencontainers.image.description="Exercise 4 - Know your Verbs"
LABEL org.opencontainers.image.licenses=MIT

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make ports available to the world outside this container
EXPOSE 8080

# Run application
CMD ["python", "/app/app.py"]

