# Lightweight Linux environment with Python
FROM python:3.10-slim

# Working directory inside the container
WORKDIR /app

# Install dependencies first (Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Documentation: the app listens on port 8080
EXPOSE 8080

# Start Flask
CMD ["python", "app.py"]
