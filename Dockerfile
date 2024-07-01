# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make ports available to the world outside this container
EXPOSE 8080
EXPOSE 8081

# Run app.py when the container launches
CMD ["/bin/sh", "wrapper.sh"]
