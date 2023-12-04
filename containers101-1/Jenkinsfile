pipeline {
    agent any
    environment {
        myuser  = credentials ('dockerhub-user')
        mypassword =  credentials ('dockerhub-password')
        version = "v6"
    }
    stages {
        stage ("download code") {
            steps {
                sh 'git clone https://github.com/techbleat/containers101.git'
            }
        }
        stage ('build image') {
            steps {
                sh '''
                   cd containers101
                   docker build -t shegoj/marcifx:$version .
                '''
            }
        }
        stage ('publish image') {
            steps {
                sh '''
                   docker login -u $myuser -p $mypassword
                   docker push shegoj/marcifx:$version 
                '''
            }
        }
        stage ('deploy app') {
            steps {
                sh '''
                   docker run --name nationapp --rm -d -p 5000:5000 shegoj/marcifx:$version  
                '''
            }
        }
    }
    post {
        always {
            deleteDir()
        }
    }
}