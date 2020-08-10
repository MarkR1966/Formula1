## Random Formula1 Driver and Team Pairings

# SFIA-2
# Requirements 
* A Trello board (or equivalent Kanban board tech) with tasks needed to complete the project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a * CI server and deployed to a cloud-based virtual machine.
* If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Service-oriented architecture that has been asked for.
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.
* The project must make use of a reverse proxy to make your application accessible to the user

# Technologies
* Kanban Board: Trello or an equivalent Kanban Board
* Version Control: Github
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
* Load Balancing: Nginx

# Docker
* Docker containers allow for easy packing, deploying and management of applications in a clean environment. Containers allow you to package up an app with everything it needs so that any other Linux user can download and distribute it easily. This ensures consistency in development, build, test, and production environments and promotes security as containers are completely segregated from one another. Docker also allows you to version control your images, including rollbacks if you encounter an error with the image. It reduces deployment times as container images do not require an OS to be booted up. They are compatible with Google Cloud Services which is what I used to host my VMs and database. Storing the service images on Dockerhub means that they can be downloaded and utilised anywhere and by anyone which in a real-life setting would reduce the time taken to download and deploy the services whilst ensuring efficiency.
# Ansible
* Ansible is an automation tool that allows you to provision your machines with the set-up they need to run the software. It also assists in deployment and orchestration of software. 

# Designs
## Application
Due to my interest in Formula 1 racing Series I designed my website to aalow visitors to view random drivers from the 2020 series Drivers roster paired up with a random Team from the 2020 series roster.  When the user accesses the web page they are presented with a random pairing and a button the user can click on to generate a new random pairing as required. The last 5 pairings are also dispayed on the website as each pairing is save to a MySQL Database. The first version has a more basic layout than the second version.

## User Stories
* As a user I want a website to display random Fromula 1 Drivers and Team pairings so that I can be entertained
* As a user I want to see a website that shows random Formula Drivers and Team pairings, that will also show previous pairings that were created.

## ERD
* Once a Driver and Team are  generated, they are recorded in the database and assigned a unique ID. The last five records are then displayed on the homepage
<p align="center">
    <img src="https://imgur.com/fa2FDkc">
</p>

## Python
* Service 1 Displays a web page showing the Current Driver and Team Pairing, a button to generate a new pairing and a table showing the last 5 records of the Database. WHen the screen s refreshed a new pairing is requested from Service 4
* Service 2 has a tuple list of Drivers names from the 2020 F1 Season. A name is randomly selected from the list and returned to Serice 4 when requested
* Service 3 has a tuple list of Team names from the 2020 F1 Season. A name is randomly selected from the list and returned to Serice 4 when requested
* Service 4 requests a Driver from Service 2 and a Team from Service 3. These are stored in a MYSQL Database with a unique key ID. These responses are combined and returned to Service 1 as a single response.
<p align="center">
    <img src="https://imgur.com/JxViFZX">
</p>

## MySQL
* Although only a single Database table was required to hold the information, the MySQL Database is running as an instance on GCP. This helps to make it more easily accessible by multiple VMs that would be accessing it when the containers were hosted across the swarm. 

# Project Tracking
## Trello 
* I used a trello board to track my project and organise my workload. 

# Deployment
## CI Pipeline
<p align="center">
    <img src="https://imgur.com/SsFttGP">
</p>
* I created 4 microservice APIs using Flask and Python for the coding . Service 1 provided the user interface of the app, hosting a website displaying the single home page containing Driver and Team Pairing information. When the home page is refreshed or the 'Generate Pairing' button is activated by the user, the home route sends a get request to service 4 to receive some data. Service 4 then requests a random Driver response from service 2 and a random Team response from service 3. Service 4 adds these to 2 responses to a MySQL Database and then puts them together and returns this to service 1, where it is finally displayed for the user on the home page as well as in a list showing the last 5 generated. Initially the 4 APIs were run in a local Python virtual environment to ensure that they all communicated correctly together to produce the required results. Docker was then utilised to allow the containerisation of these APIs and deployment throughout a swarm to allow redundancy. NGINX was also deployed into the stack as a  reverse-proxy. This meant that traffic was redirected from port 80 to the app on port 5000.   
* The VCS service used was GitHub and I utilised a Webhook so that whenever new code was pushed to the development branch, it would trigger Jenkins to build a pipeline. In this pipeline I automated the use of Ansible, which installed Docker on each of the VMs if required and also set up the Docker Swarm. I automated the builds of the Docker images through Jenkins then deployed the service stack across the swarm and tidied up the images from the previous builds.

# Risk Assessment
<p align="center">
    <img src="https://imgur.com/EjvJO21">
</p>
<p align="center">
    <img src="https://imgur.com/1vXtbwF">
</p>

# Best Practices
* I utilised a venv when installing packages and when making changes to the python code.
* I implemented the use of a .gitignore and a .dockerignore to prevent cache files being pushed to github and dockerhub, respectively.
* I made sure that variables were not hardcoded into the files and therefore accessible to anyone on github. I did this using environment variables.

# Acceptance Criteria
## 4 services
* I created an app with four interactive services and a further fifth NGINX service. My first service hosts the interactive element of the app, using Jinja2 syntax to pass through a layout html for the webpages and it is the service responsible for triggering the other services into action. In addition, this service connects to a MySQL database retrieving persisted data in order for it to be displayed on the website. Services 2 and 3 both create a random object as specified and service 4 creates an object based on the text responses received from services 2 and 3 as well as connecting to a MySQL database to persist this data.
## Different Implementations 
* In my presentation I will demonstrate how the services can be altered without disrupting the user experience. This is achieved using Docker Swarm's update functionality which will continue to host the service whilst each replica is being updated.
## MoSCow
* The MoSCow criteria I created at the start of my project is as follows:
* Must have - 4 micro services, a database, 2 versions
* Should have - best practices
* Could have - a nice front-end website
* Won't have - a complex website
* I think I have met my must have, should have and could have criteria to ensure the functionability and quality of the project. The wont have is not required due to the simplicity of the application and its requirements.

# Authors
Mark Rafferty
