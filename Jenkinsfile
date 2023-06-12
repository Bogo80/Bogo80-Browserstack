pipeline {
  agent any
  stages {
    stage('version') {
      steps {
         browserstack(credentialsId: '<3d8e8547-52a4-479f-961c-37eb31437652>') {
                 // add commands to run test
                 // Following are some of the example commands -----
                 sh 'python3 test.py''
                
             }
      }
    }
    stage('hello') {
      steps {
        sh 'python3 test.py'
      }
    }
  }
}
