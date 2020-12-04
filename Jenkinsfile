pipeline {
    agent {
        docker {
            image 'python:3.6.5' 
        }
    } 
    stages {
        stage('Build') { 
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest -s api_testing.py'
            }
        }
    }
}

