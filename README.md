# VEMO Challenge: To-Do Application

This is a simple To-Do application built with Django and the Django Rest Framework.

## Prerequisites

- Docker
- Docker Compose

## How to run

1. **Build the Docker image**:

   ```bash
   docker-compose build
   ```

2. **Run the Docker container and migrations**:

   ```bash
   docker-compose up
   ```

   This command will first apply any pending migrations and then start the Django development server on port 8000.

3. **Access the application**:

   Open your browser and navigate to [http://localhost:8000/api/v1/](http://localhost:8000/api/v1/). You should see the Swagger UI displaying your API endpoints.

## Stopping the application:

To stop the running containers, press `CTRL + C` in the terminal where `docker-compose up` is running.

To completely stop the containers and remove them, you can run:

```bash
docker-compose down
```

## Notes:

- This setup is intended for development purposes. For production, consider using a production-ready database, configuring a web server like Gunicorn, and setting up a reverse proxy with Nginx.
