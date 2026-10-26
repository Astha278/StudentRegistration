
pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Test Registration Form') {
            steps {
                bat 'python test_form.py'
            }
        }
    }
}
