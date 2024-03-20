# JANUS
Model-based Electrical Diagram and TID Generation

# FRAMEWORK
Backend
- Python Flask Microframework for backend logic and routes/apis

Frontend
- HTML/CSS/JS

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
  -Dsonar.projectKey=24040_App \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://sonar.def.engr.arizona.edu:9000 \
  -Dsonar.token=sqp_8a9aab1f48db50c828beeee3a2a16c93d43b9a76

# DEVSECOPS Pipeline
Build 
- There is a GitHub action that checks if the project builds.

Testing
- The unit tests are also automatically run during this stage of the pipeline.
- Composition Analysis using Snyk that automatically generates a report based on dependencies used in the code.
- Static Code Analysis  using SonarQube. 

Integration
- The docker action also checks if the application is able to be deployed after it has been built.


