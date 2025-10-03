# Dockerfile
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create app directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose Django port
EXPOSE 8000

# Start with Daphne (ASGI server for Django Channels)
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "django_chat_classifier.asgi:application"]
