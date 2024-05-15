# Use an official Python runtime as a parent image
FROM python:3.10.14-slim-bullseye

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install Flask-SQLAlchemy
RUN pip3 install -r requirements.txt

COPY . .


EXPOSE  5000


# Run the command to start Flask
CMD [ "flask", "run"]
