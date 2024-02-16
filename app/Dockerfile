# Use an official Python runtime as a parent image
FROM python:3.9.18-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip3 install psycopg2-binary
RUN pip3 install SQLAlchemy
RUN pip3 install Flask-SQLAlchemy
RUN pip3 install -r requirements.txt

# Make port  3000 available to the world outside this container
EXPOSE  8000

# Define environment variable
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the command to start Flask
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "wsgi:application"]
