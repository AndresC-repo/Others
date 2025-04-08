# Docker Compose

Owner: Andrés Carrancá
Tags: Process

# Simplifying Multi-Container Applications

## What is Docker Compose?

Docker Compose is a tool for defining and running multi-container Docker applications. It allows you to use a YAML file to configure your application's services, networks, and volumes, and then create and start all the services from your configuration with a single command.

## Why and When to Use Docker Compose

- Simplifies the process of managing multiple containers
- Ideal for development, testing, and staging environments
- Useful for applications that require multiple services to work together
- Helps in maintaining consistency across different environments

## Constructing a docker-compose.yaml File

Here's a simple example of a docker-compose.yaml file for a Python project with a database:

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    depends_on:
      - db
  db:
    image: postgres
    environment:
      POSTGRES_PASSWORD: example
```

This file defines two services: a web service (your Python application) and a database service (PostgreSQL).

## Common Docker Compose Commands

- `docker-compose up`: Create and start containers
- `docker-compose down`: Stop and remove containers, networks, images, and volumes
- `docker-compose build`: Build or rebuild services
- `docker-compose logs`: View output from containers
- `docker-compose ps`: List containers

Docker Compose simplifies the process of managing multi-container applications, making it easier to develop, test, and deploy complex systems.