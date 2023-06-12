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
        stage('Build Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker-compose build'
                    } else {
                        bat 'docker-compose build'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker-compose push'
                    } else {
                        bat 'docker-compose push'
                    }
                }
            }
        }
    }
}