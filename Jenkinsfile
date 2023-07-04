pipeline {
  agent any
  environment {
    DOCKERHUB_CREDENTIALS = credentials('dockerhub')
  }
  stages {
    stage('Docker Build') {
      steps {
        sh '''
        // docker build -t messershiraz/devops-frontend front/
        // docker build -t messershiraz/devops-backend app/
        // docker build -t messershiraz/devops-logger logger/
        '''
      }
    }
    stage('Login') {
      steps {
        // sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
        sh 'echo hi'
      }
    }
    stage('Push') {
      steps {
        // sh 'docker push messershiraz/devops-frontend'
        // sh 'docker push messershiraz/devops-backend'
        // sh 'docker push messershiraz/devops-logger'
        sh 'echo hi'
      }
    }
    stage('Deploy locally') {
      steps {
        sh '''
        echo "To deploy locally do the following:
        1. git clone github
        2. docker pull image
        3. docker pull image
        4. docker pull image
        5. docker-compose start 
        "
        '''
      }
    }
  }
  post {
    always {
    sh 'docker logout'
    emailext body: '''${SCRIPT, template="groovy-html.template"}''',
        mimeType: 'text/html',
        subject: "[Jenkins] ${currentBuild.fullDisplayName}",
        to: "shirazush000@gmail.com",
        replyTo: "shirazush000@gmail.com"

      
    //     recipientProviders: [[$class: 'CulpritsRecipientProvider']]
      // emailext body: 'The Pipeline ${currentBuild.currentResult}',
      //   subject: 'The Pipeline ${currentBuild.currentResult}',
      //   to: '${mail_list}'
    }
  }
}
