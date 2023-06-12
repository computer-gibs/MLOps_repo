pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                    } else {
                        bat 'pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Run Unit Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python -m unittest'
                    } else {
                        bat 'python -m unittest'
                    }
                }
            }
        }
        stage('Run Quality Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python tests/quality_tests.py'
                    } else {
                        bat 'python tests/quality_tests.py'
                    }
                }
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker build -t my_ml_app:latest .'
                    } else {
                        bat 'docker build -t my_ml_app:latest .'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker push my_ml_app:latest'
                    } else {
                        bat 'docker push my_ml_app:latest'
                    }
                }
            }
        }
    }
}