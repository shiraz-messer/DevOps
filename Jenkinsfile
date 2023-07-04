pipeline {
  agent any
  environment {
    mail_list = 'shirazush000@gmail.com;ophir472@gmail.com'
  }
  stages {
    stage('Docker Build') {
      steps {
        sh '''
        docker build - t devops-frontend front/
          docker build - t devops-backend app/
          docker build - t devops-logger logger/
          '''
      }
    }
    stage('Deploy locally') {
      steps {
        sh '''
        docker-compose stop
        docker-compose start 
        '''
      }
    }
    stage('Testing') {
      steps {
        sh '''
        response = $(curl--write - out '%{http_code}'--silent--output / dev / null 127.0 .0 .1:8501)
        if [$response - eq 200]
        then
        echo "Works as expected"
        else
          exit 1 
        '''
      }
    }
  }
  post {
    always {
      emailext body: 'The Pipeline ${currentBuild.currentResult}',
        subject: 'The Pipeline ${currentBuild.currentResult}',
        to: '${mail_list}'
    }
  }
}
