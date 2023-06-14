pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install -r requirements.txt'
                        sh 'pip install dvc[gdrive]'
                    } else {
                        bat 'pip install -r requirements.txt'
                        bat 'pip install dvc[gdrive]'
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
        stage('Sync Model Files from Google Drive') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'dvc pull -r mygdrive'
                    } else {
                        bat 'dvc pull -r mygdrive'
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
        stage('Run Docker Container') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'docker-compose up -d'
                    } else {
                        bat 'docker-compose up -d'
                    }
                }
            }
        }
    }
}