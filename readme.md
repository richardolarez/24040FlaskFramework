# JANUS
Model-based Electrical Diagram and TID Generation

# FRAMEWORK
templates/index.html
static/styles.css

# RUN COMMANDS
Make sure you are in the parent directory
Make sure you have docker installed and docker compose


# Start the db server using the postgresql image from Docker Hub
docker-compose up -d janus_db_2


# Build the application using the docker compose
1. $ docker-compose build   


#  Run the application 
2. $ docker-compose up janus_app
- This will start all of the services defined in the docker-compose file, including Janus, PostgresSQL. 

This will start all services (Janus, Postgres)


#  Accessing the Application
http://localhost:8000


# Perform static analysis using SonarQube
$ sonar-scanner \
    -Dsonar.projectKey=24040_ \
    -Dsonar.sources=. \
    -Dsonar.host.url=http://test.def.engr.arizona.edu:9000 \
    -Dsonar.token=sqp_e16713399f15e98ca27dce7e4e87e98c4dde43f3

