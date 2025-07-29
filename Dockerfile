# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the rest of your application code
COPY . .

# Install dependencies
RUN apt-get update  && pip install --no-cache-dir -r requirements.txt



# Expose the port your app runs on (change if needed)
EXPOSE 5000

# Command to run your app (update as needed, e.g., gunicorn app:app)
CMD ["python", "app.py"]