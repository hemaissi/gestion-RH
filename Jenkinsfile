pipeline {
    agent any

    stages {
        stage('Run Django Server') {
            steps {
                script {
                    // Set up your environment if needed
                    bat "python manage.py runserver"
                }
            }
        }
    }
}
