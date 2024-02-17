# Use an official Python runtime as a parent image
FROM python:3.9.18-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install Flask-SQLAlchemy
RUN pip3 install -r requirements.txt

COPY . .

# Make port 8000 available to the world outside this container
EXPOSE  8000

# Run the command to start Flask
CMD [ "flask", "run", "--host=0.0.0.0", "--port=8000"]
