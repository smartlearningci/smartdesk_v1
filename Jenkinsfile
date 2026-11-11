pipeline {
    agent any

    stages {
        stage('Obter codigo') {
            steps {
                checkout scm
            }
        }

        stage('Preparar ambiente') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Executar testes') {
            steps {
                sh 'mkdir -p reports'
                sh '.venv/bin/python -m pytest tests/ -q --junitxml=reports/ci.xml'
            }
        }

        stage('Construir imagem') {
            steps {
                sh 'docker build -t smartlearningci/smartdesk:latest .'
            }
        }

        stage('Publicar no Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-smartdesk',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_TOKEN'
                )]) {
                    sh '''
                        set +x
                        printf '%s' "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USER" --password-stdin
                        docker push smartlearningci/smartdesk:latest
                        docker logout
                    '''
                }
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/ci.xml'
        }
    }
}