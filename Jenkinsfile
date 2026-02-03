pipeline {
    agent any
    
    environment {
        PYTHON_PATH = '/usr/bin/python3'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code from repository...'
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                echo 'Setting up Python environment...'
                sh '''
                    python3 --version
                    pip3 install --user -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running unit tests...'
                sh '''
                    python3 -m pytest test_app.py -v
                '''
            }
        }
        
        stage('Build') {
            steps {
                echo 'Build stage - Application is ready'
                sh '''
                    echo "Build completed at $(date)"
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    # Kill any existing Flask process
                    pkill -f "python3 app.py" || true
                    
                    # Start the application in background
                    nohup python3 app.py > app.log 2>&1 &
                    
                    # Wait for app to start
                    sleep 5
                    
                    # Verify deployment
                    curl -f http://localhost:5000/health || exit 1
                    
                    echo "Application deployed successfully"
                '''
            }
        }
    }
    
    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for details.'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
```

**Create `.gitignore`:**
```
__pycache__/
*.pyc
*.pyo
data/
*.log
.pytest_cache/
venv/