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
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/ci.xml'
        }
    }
    
}