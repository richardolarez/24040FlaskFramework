# JANUS
Model-based Electrical Diagram and TID Generation

# FRAMEWORK
templates/index.html
static/styles.css

# RUN COMMANDS
Make sure you are in the parent directory
Make sure you have docker installed and docker-compose


# Start the DB server using the Postgresql image from Docker Hub
docker-compose up -d janus_db_2


# Build the application using the docker-compose
1. $ docker-compose build   


#  Run the application 
2. $ docker-compose up janus_app
- This will start all of the services defined in the docker-compose file, including Janus, PostgreSQL. 

This will start all services (Janus, Postgres)


#  Accessing the Application
http://localhost:8000


# Perform static analysis using SonarQube
$ sonar-scanner \
    -Dsonar.projectKey=24040_ \
    -Dsonar.sources=. \
    -Dsonar.host.url=http://test.def.engr.arizona.edu:9000 \
    -Dsonar.token=sqp_e16713399f15e98ca27dce7e4e87e98c4dde43f3

# DEVSECOPS Pipeline
Build 
- There is a GitHub action that checks if the project builds.

Testing
- Composition Analysis using Snyk that automatically generates a report based on dependencies used in the code.
- Static Code Analysis  using SonarQube. 

Integration
- The docker action also checks if the application is able to be deployed after it has been built.


