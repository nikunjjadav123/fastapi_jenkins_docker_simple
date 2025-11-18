pipeline {

    agent any

    environment {
        DOCKERHUB_LOGIN = credentials('dockerhub-login')
        IMAGE_NAME = "nikunj1234/fastapi_jenkins_docker_simple"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %IMAGE_NAME% .
                """
            }
        }

        stage('Login to DockerHub') {
            steps {
                bat """
                echo %DOCKERHUB_LOGIN_PSW% | docker login -u %DOCKERHUB_LOGIN_USR% --password-stdin
                """
            }
        }

        stage('Push Docker Image') {
            steps {
                bat """
                docker push %IMAGE_NAME%
                """
            }
        }

        stage('Deploy') {
            steps {
                bat """
                docker pull %IMAGE_NAME%
                docker-compose down
                docker-compose up -d
                """
            }
        }
    }
}
