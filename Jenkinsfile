pipeline {
  agent any
  options { timestamps() }
  environment { PYTHONUNBUFFERED = '1' }
  stages {
    stage('Checkout'){ steps{ checkout scm } }
    stage('Prechecks'){
      steps{
        sh 'python3 --version'
        sh 'pip3 install --user pyyaml || true'
        sh 'python3 scripts/precheck_yaml.py'
      }
    }
    stage('Build Lab'){ steps{ sh 'bash scripts/deploy_lab.sh' } }
    stage('Base Config'){ steps{ sh 'python3 scripts/push_config.py' } }
    stage('Validation'){
      steps{ sh 'python3 scripts/run_tests.py | tee validation.log' }
    }
    stage('Archive Artifacts'){
      steps{
        sh 'docker ps > docker_ps.txt || true'
        sh 'containerlab inspect -t ./evpn01.yml --all > clab_inspect.txt || true'
        archiveArtifacts artifacts: '*.txt, validation.log', onlyIfSuccessful: false
      }
    }
  }
  post {
    always {
      echo 'Done'
    }
  }
}
