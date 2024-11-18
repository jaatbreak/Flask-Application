# Use the official Python image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy application code and package list
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libmariadb-dev \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir Flask==3.1.0 \
    Flask-MySQL==1.6.0 \
    Flask-MySQLdb==1.0.1 \
    Flask-SQLAlchemy==3.1.1 \
    mysqlclient==2.1.1 \
    PyMySQL==1.1.1 \
    SQLAlchemy==2.0.36 \
    Werkzeug==3.1.3

# Expose the application port
EXPOSE 5000

# Set environment variable for Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

