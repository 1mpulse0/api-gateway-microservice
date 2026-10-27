
# API Gateway + Microservice

## Description

This project demonstrates a simple API Gateway architecture using Docker.
It contains two services: an Nginx API Gateway and a Python Flask microservice.

The API Gateway receives HTTP requests and forwards them to Service A through a shared Docker bridge network.

## Technologies Used

- Python
- Flask
- Nginx
- Docker
- Docker Compose

## Project Structure

```text
api-gateway-microservice/
├── gateway/
│   ├── Dockerfile
│   └── nginx.conf
├── service-a/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Architecture

The application consists of two containers:

- **Gateway:** Nginx receives HTTP requests on port 80 and forwards requests beginning with `/api/` to Service A.
- **Service A:** A Python Flask application that provides information through the `/info` endpoint.

Both containers communicate through a shared Docker bridge network named `app-network`.

## API Endpoint

### GET /api/info

URL:

```text
http://localhost/api/info
```

The API Gateway forwards this request to the `/info` endpoint of Service A.

Example response:

```json
{
  "message": "Hello from Service A!",
  "service": "Service A",
  "status": "running",
  "technology": "Python Flask"
}
```

## How to Run the Project

### Requirements

- Docker Desktop
- Docker Compose

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/api-gateway-microservice.git
cd api-gateway-microservice
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Build and start the containers

```bash
docker compose up --build -d
```

### 3. Check the running containers

```bash
docker compose ps
```

Both `gateway` and `service-a` should be running.

### 4. Test the API

Open the following URL in your browser:

```text
http://localhost/api/info
```

Alternatively, use curl:

```bash
curl http://localhost/api/info
```

On Windows PowerShell, you can use:

```powershell
curl.exe http://localhost/api/info
```

### 5. View logs

To view the API Gateway logs:

```bash
docker compose logs gateway
```

To view the microservice logs:

```bash
docker compose logs service-a
```

### 6. Stop the containers

```bash
docker compose down
```

## Docker Network

Docker Compose creates a shared bridge network called `app-network`.

The Gateway communicates with Service A using its Docker Compose service name:

```text
http://service-a:5000
```

The Flask service is accessible through the Gateway without publishing port 5000 directly to the host.

## Requirements Checklist

- [x] Two Docker containers
- [x] Dockerfile for the API Gateway
- [x] Dockerfile for Service A
- [x] Nginx request routing
- [x] Python Flask microservice
- [x] Shared Docker bridge network
- [x] API endpoint `/api/info`
- [x] Testing with a browser or curl

## Conclusion

This project demonstrates how an API Gateway can route HTTP requests to a separate microservice using Docker Compose and a shared bridge network.
