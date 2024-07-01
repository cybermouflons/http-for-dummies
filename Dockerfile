# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Connect package to repository
LABEL org.opencontainers.image.source=https://github.com/cybermouflons/http-for-dummies
LABEL org.opencontainers.image.description="HTTP for Dummies exercises"
LABEL org.opencontainers.image.licenses=MIT

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install supervisor
# RUN apt-get update && apt-get install -y supervisor

# Copy the supervisor configuration file
# COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Make ports available to the world outside this container
EXPOSE 8080
EXPOSE 8081
EXPOSE 8082
EXPOSE 8083
EXPOSE 8084
EXPOSE 8085
EXPOSE 8086
EXPOSE 8087
EXPOSE 8088

# Run supervisor when the container launches
# CMD ["/usr/bin/supervisord"]

CMD ["/bin/sh", "/app/wrapper.sh"]

