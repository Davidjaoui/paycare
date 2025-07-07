pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
        }
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
                sh 'pip install -r requirements.txt'
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
                echo '🐳 Construction de l\'image Docker...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }

        stage('Stop & Remove Existing Container') {
            steps {
                echo '🧹 Nettoyage du container existant (si présent)...'
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Démarrage du container Docker...'
                sh "docker run -d --name ${CONTAINER_NAME} -p 8081:8080 ${IMAGE_NAME}"
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline terminé avec succès.'
        }
        failure {
            echo '❌ Échec du pipeline.'
        }
    }
}
