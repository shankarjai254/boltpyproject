# Sample Flask Application

This is a sample Flask application configured to work with Jenkins Pipeline for CI/CD.

## Prerequisites

- Python 3.8 or higher
- Jenkins with required plugins
- SonarQube server

## Local Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run tests:
   ```bash
   pytest
   ```

4. Start the application:
   ```bash
   python src/app.py
   ```

## Jenkins Pipeline

The included Jenkinsfile defines the following stages:
- Git Checkout
- Setup Python Environment
- Run Tests
- Code Analysis
- SonarQube Analysis
- Build and Package

## Repository Setup

1. Create a new repository on GitHub
2. Push this code to your repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/sample-flask-app.git
   git push -u origin main
   ```

3. In Jenkins, create a new Pipeline job and point it to your repository