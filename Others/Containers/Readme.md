# Docker
Docker for developing, shipping, and running applications in containers. To package an application and its dependencies together, ensuring consistency across different environments.

**Isolation:** Containers encapsulate applications and their dependencies, providing isolation from the underlying system. This ensures that an application runs consistently, regardless of where it's deployed.

**Portability:** Docker containers can run on any system that supports Docker, making it easy to move applications between environments. This eliminates the common "it works on my machine" problem.

**Efficiency:** Containers share the host OS kernel, making them lightweight and efficient. They start quickly and consume fewer resources compared to traditional virtual machines.

# Getting Started

## Installation
Install Docker by following the instructions on the official Docker website.

Basic Commands
Build a Docker Image:

bash
```
docker build -t my-app .
```
Run a Docker Container:

```
docker run my-app
```


List Running Containers:
```
docker ps
```

Stop a Running Container:
```
docker stop container_id
```

Remove a Container:
```
docker rm container_id
```

# Dockerfile
A Dockerfile is a script that contains instructions to build a Docker image. Here's a simple example:

```
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

# Docker Compose
Docker Compose is a tool for defining and running multi-container Docker applications. You can use a docker-compose.yml file to configure your application's services, networks, and volumes.

```
docker compose up -d

docker compose down
```



# Conclusion
Docker simplifies the process of building, shipping, and running applications. It provides a consistent and reproducible environment, making it an essential tool for modern application development and deployment.

For more detailed information, refer to the official Docker documentation.