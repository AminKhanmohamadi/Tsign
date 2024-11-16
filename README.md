
# File Upload and Management System

A Django-based application for managing file uploads, specifically images and videos, with Docker integration for easy setup and deployment.

## Features

- Upload and manage image and video files.
- File size validation (limits for images and videos).
- Simple and intuitive UI for viewing, renaming, and deleting files.
- Docker-based setup for easy deployment.

## Prerequisites

Before you begin, ensure that you have the following installed:

- **Docker** (for containerization)
- **Docker Compose** (for managing multi-container applications)

## Setup and Installation

This section explains how to set up the project on your local machine using Docker.

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/AminKhanmohamadi/Tsign.git
```

### 2. Build the Docker Containers

Next, build the Docker containers using Docker Compose. This will create the necessary images and start the services defined in the `docker-compose.yml` file:

```bash
docker-compose up --build
```

- The `--build` flag ensures that Docker rebuilds the images before starting the containers.
- Docker will automatically download the necessary images, set up the containers, and install the dependencies.

#### 3. Check the Build Logs

While the containers are being built, you can follow the logs to monitor the progress:

```bash
docker-compose logs -f
```

This will show the logs from the Docker containers and help you verify that everything is running correctly.

#### 4. Access the Application

Once the build is complete and the containers are running, open your browser and go to:

```plaintext
http://localhost:8000
```

This will load the application. You can now upload and manage files.

#### 5. Clean Up After the Build

Once you're done, stop the Docker containers with:

```bash
docker-compose down
```

If you want to remove all the containers and volumes (which deletes all the data, including uploaded files), use:

```bash
docker-compose down -v
```

This ensures a complete clean-up of your environment.