# **Running the project**

1. create .env file in root of the project(Same directory that docker-compose.yml file is located). You can use
   env_template.txt to create .env file. it includes all required parameters.
2. If you are using MacBook M1 series to run the project run export `DOCKER_DEFAULT_PLATFORM=linux/amd64`. If not skip
   this step
3. start the project using `docker compose up`

# **Project Note:**

* Two URLs are available to build the Team. "team_builder" generate slightly more efficient result, but it needs more
  queries. "team_builder2" generate faster response.
* Cleaning the data could be done in multiple ways based on the business and other factors. I chose to fill Nan values.
* Images link DO NOT WORK.