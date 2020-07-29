pipeline {

    agent any

    stages{

        stage('Build Images') {

            steps {

                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
                }

        }

        stage('Build Services') {
        
                    steps {
                    
                        sh './scripts/build_service.sh'
                        }

        }

    }

}