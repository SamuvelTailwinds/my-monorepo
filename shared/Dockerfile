# Use the official Python image as a base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY app app
COPY shared shared

# Expose the port that Flask will run on
EXPOSE 5000

# Define the command to run when the container starts
CMD ["python", "app/main.py"]
