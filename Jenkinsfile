pipeline {
    agent any
    
    environment {
        // Python virtual environment name
        VENV = 'venv'
    }
    
    stages {
        stage('Git Checkout') {
            steps {
                // Checkout code from repository
                checkout scm
                
                // Display information about the checked out code
                sh 'git log -1 --pretty=format:"%h - %an: %s"'
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                // Create and activate virtual environment
                sh '''
                    python -m venv ${VENV}
                    . ${VENV}/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install wheel
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                // Run Python tests
                sh '''
                    . ${VENV}/bin/activate
                    pytest --junitxml=test-results/junit.xml
                '''
            }
            post {
                always {
                    // Publish test results
                    junit 'test-results/junit.xml'
                }
            }
        }
        
        stage('Code Analysis') {
            steps {
                // Run pylint
                sh '''
                    . ${VENV}/bin/activate
                    pylint --output-format=parseable --reports=n src/ | tee pylint-report.txt
                '''
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        . ${VENV}/bin/activate
                        sonar-scanner \
                            -Dsonar.projectKey=python-project \
                            -Dsonar.sources=. \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.python.pylint.reportPath=pylint-report.txt
                    '''
                }
            }
        }
        
        stage('Build and Package') {
            steps {
                // Package Python application
                sh '''
                    . ${VENV}/bin/activate
                    python setup.py sdist bdist_wheel
                '''
            }
            post {
                success {
                    // Archive the built packages
                    archiveArtifacts artifacts: 'dist/*', fingerprint: true
                }
            }
        }
    }
    
    post {
        always {
            // Clean up virtual environment and workspace
            sh 'rm -rf ${VENV}'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
