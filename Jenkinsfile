pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-first-app'
        IMAGE_TAG  = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Забираем код с GitHub'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Docker образ собирвется'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Test Image') {
            steps {
                echo 'Проверка созданного'
                sh "docker images | grep ${IMAGE_NAME}"
            }
        }

        stage('Cleanup') {
            steps {
                echo 'Чистим старые образы (экономим место на диске)...'
                sh "docker image prune -f"
            }
        }
    }

    post {
        success {
            echo 'Пайплайн успешно завершен!'
        }
        failure {
            echo 'Пайплайн НЕ завершен. Что в логах?'
        }
    }
}
