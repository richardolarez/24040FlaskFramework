JANUS

FRAMEWORK
templates/index.html
static/styles.css

RUN COMMANDS
Make sure you are in the parent directory
Make sure you have docker installed and docker compose

# Build the application using the docker compose
1. $ docker-compose build   

#  Run the application 
2. $ docker-compose up 
- This will start all of the services defined in the docker-compose file, including Janus, PostgresSQL. 

This will start all services (Janus, Nginx, Postgres)

#  Accessing the Application
http://localhost:8000
