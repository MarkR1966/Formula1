pipeline {

    agent any

    stages{

        // stage('Ansible'){

        //     steps {

        //         sh 'ansible-playbook -i inventory.cfg playbook.yml'

        //     }

        // }
        stage("Create NGINX") {

            steps {

                sh './scripts/nginx.sh'

            }

        }
        stage('Build Images') {

            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/build_images.sh'
                }

        }

        stage('Build Services') {
        
            steps {
                    
                sh './scripts/build_services.sh'
                }

        }

    }

}