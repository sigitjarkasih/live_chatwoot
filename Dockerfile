FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose the port
EXPOSE 3002

# Command will be overridden by docker-compose
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3002"]
