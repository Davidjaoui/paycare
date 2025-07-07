pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u 1000:1000' // pour éviter les erreurs de permission
        }
    }

    environment {
        HOME = '/tmp'
        PATH = '/tmp/.local/bin:$PATH'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔁 Clonage du dépôt Git...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installation des dépendances...'
                sh 'pip install --user -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '✅ Lancement des tests Pytest...'
                sh 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🔨 Construction de l\'image Docker...'
                sh 'docker build -t paycare-app .'
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                echo '🛑 Arrêt et suppression du conteneur existant (si présent)...'
                sh '''
                    docker stop paycare-app || true
                    docker rm paycare-app || true
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Lancement du conteneur Docker...'
                sh 'docker run -d --name paycare-app -p 8000:8000 paycare-app'
            }
        }
    }

    post {
        success {
            echo '✅ Déploiement réussi.'
        }
        failure {
            echo '❌ Échec du pipeline.'
        }
    }
}