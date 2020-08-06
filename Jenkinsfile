// Requirements for jenkins to automaticall build the application requirements
pipeline {

    agent any

    stages{
        // Do initial setup
        stage('Setup Environment'){

            steps {

                sh 'chmod +x ./scripts/*.sh'

            }

        }
        // Execute ansible script to ensure docker is installed and swarm is created
        stage('Ansible'){

            steps {

                sh 'ansible-playbook -i inventory.cfg playbook.yml'

            }

        }
        // Build nginx image with required files
        stage("Create NGINX") {

            steps {

                sh './scripts/nginx.sh'

            }

        }
        // Build required images for Service_1, Service_2, Service_3, Service_4
        stage('Build Images') {

            steps {

                sh './scripts/build_images.sh'
                }

        }
        // Deploy the images to the Docker Swarm
        stage('Build Services') {
        
            steps {
                    
                sh './scripts/build_services.sh'
                }

        }
        // Remove any unused containers and images from swarm_manager and swarm_worker
        stage("Clean up environment") {

            steps {

                sh 'ansible-playbook -i inventory.cfg playbook2.yml'

            }

        }

    }

}