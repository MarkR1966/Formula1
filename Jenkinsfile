pipeline {

    agent any

    stages{

        stage('Pull Images') {

            steps {

                sleep(time:15,unit:"MINUTES")
                sh 'chmod +x ./scripts/*.sh'
                sh './scripts/pull_images.sh'
                }

        }

        stage('Buid Services') {
        
                    steps {
                    
                        sh './scripts/build_service.sh'
                        }

        }

    }

}