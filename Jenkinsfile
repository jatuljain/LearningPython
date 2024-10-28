pipeline {
    agent any
    // Define parameters
    parameters {
        string(name: 'BRANCH', defaultValue: 'main', description: 'Branch to build')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: 'Run tests after build')
        choice(name: 'ENVIRONMENT', choices: ['DEV', 'ACC'], description: 'Select deployment environment')
    }
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!'
            }
        }
    }
}
