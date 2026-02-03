Visitor Log Application with Jenkins CI/CD Pipeline

# Visitor Log Application

A simple Flask-based visitor logging system with Jenkins CI/CD pipeline.

## Features
- Add visitor names with automatic timestamp
- View all visitor entries
- Automated CI/CD with Jenkins

## Technology Stack
- Python 3
- Flask
- Jenkins
- Git

## Local Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run application: `python app.py`
3. Access at: http://localhost:5000

## Testing
Run tests: `pytest test_app.py -v`

## CI/CD Pipeline
The Jenkinsfile automates:
- Code checkout
- Dependency installation
- Unit testing
- Application deployment
