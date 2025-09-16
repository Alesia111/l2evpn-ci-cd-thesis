pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Prechecks') {
            steps {
                sh 'python3 --version'
                sh 'pip3 install pyyaml'
                sh 'python3 scripts/precheck_yaml.py'
            }
        }
        
        stage('Build Lab') {
            steps {
                sh 'bash scripts/deploy_lab.sh'
            }
        }
        
        stage('Base Configuration') {
            steps {
                sh 'python3 scripts/push_config.py'
            }
        }
        
        stage('Validation') {
            steps {
                script {
                    try {
                        sh 'python3 scripts/run_tests.py'
                    } catch (Exception e) {
                        echo "❌ Tests failed: ${e}"
                        sh 'bash scripts/teardown.sh'
                        error("Pipeline interrupted due to failed tests")
                    }
                }
            }
        }
        
        stage('Archive Artifacts') {
            steps {
                archiveArtifacts artifacts: 'validation_results.log', fingerprint: true
                archiveArtifacts artifacts: 'results/*.log', fingerprint: true
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'validation_results.log', fingerprint: true
        }
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Lab destroyed."
            sh 'bash scripts/teardown.sh'
        }
    }
}
