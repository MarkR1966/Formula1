pipeline {

    agent any

    stages{

        stage('Ansible'){

            steps {

                sh 'ansible-playbook -i inventory.cfg playbook.yml'

            }

        }

        stage('Setup Environment'){

            steps {

                sh 'chmod +x ./scripts/*.sh'

            }

        }

        stage("Create NGINX") {

            steps {

                sh './scripts/nginx.sh'

            }

        }

        stage('Build Images') {

            steps {

                sh './scripts/build_images.sh'
                }

        }

        stage('Build Services') {
        
            steps {
                    
                sh './scripts/build_services.sh'
                }

        }

        stage("Clean up environment") {

            steps {

                sh './scripts/tidy.sh'

            }

        }

    }

}