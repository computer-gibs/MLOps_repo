pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python -m unittest'
            }
        }
        stage('Run Quality Tests') {
            steps {
                sh 'python quality_tests.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t my_ml_app:latest .'
            }
        }
        stage('Push Docker Image') {
            steps {
                sh 'docker push my_ml_app:latest'
            }
        }
    }
}