// pipeline {
//     agent {
//     }
//     environment {
//         CI = 'true' 
//     }
//     stages {
//         stage('Build') {
//             steps {
//                 sh 'npm install'
//                 sh 'ng build — prod'
//             }
//         }
//         stage('Deploy') { 
//             steps {
//                 sh 'aws s3 cp ./dist/ --recursive s3://jenkins-test-abcd/ --acl public-read' 
//             }
//         }
//     }
// // }
// def POD_LABEL = "testpod-${UUID.randomUUID().toString()}"
// def POD_LABEL = "testpod-${UUID.randomUUID().toString()}"
// podTemplate(label: POD_LABEL, cloud: 'kubernetes', containers: [
//     containerTemplate(name: 'build', image: 'jfeng45/k8sdemo-backend:1.0', ttyEnabled: true, command: 'cat'),
//     containerTemplate(name: 'run', image: 'jfeng45/k8sdemo-backend:1.0', ttyEnabled: true, command: 'cat')
//   ]) {
    // podTemplate(label: 'builder', 
    // containers: [
    //                 containerTemplate(name: 'jnlp', image: 'jenkins/jnlp-slave:latest')
    //                 ]) {
    //     podTemplate( label: 'jnlp', containers: [
    //         containerTemplate(name: 'jnlp', image: 'jenkins/inbound-agent:4.3-4-alpine')]
    //     )  {
    // node('jnlp') {
    //     stage('build a go project') {
    //         // container('jnlp') {
    //             stage('Build a go project') {
    //                 sh 'echo hello'
    //             }
    //         // }
    //     }
    node {
        stage('Checkout') {
            // sh "mvn"
                        // container('build') {
            // sh "hello from the container $POD_CONTAINER"
            // sh "aws s3 ls"
            // disable to recycle workspace data to save time/bandwidth
            deleteDir()
            checkout scm

            ./gradlew clean resultGenerator

            // junit 'demo.xml'
            publishHTML (target : [allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: true,
            reportDir: 'build',
            reportFiles: 'report.html',
            reportName: 'My Reports',
            reportTitles: 'The Report'])
                        }
            //enable for commit id in build number
            //env.git_commit_id = sh returnStdout: true, script: 'git rev-parse HEAD'
            //env.git_commit_id_short = env.git_commit_id.take(7)
            //currentBuild.displayName = "#${currentBuild.number}-${env.git_commit_id_short}"
        }
        // stage('Install') {
        //                 // container('build') {
        //     sh 'npm install'
        // // }
        // }
        // stage('Build') {
        //                 // container('build') {
        //     sh 'ng build --prod'
        //                 // }
        // }
        // stage('Deploy') {
        //                 container('run') {
        //     sh "ls -ltr dist/my-app/"
        //                 }
            // withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
            // sh ""
            // withCredentials([usernamePassword(credentialsId: 'a5237764-adb0-4d34-b92d-a01b6a6709ce', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
            
            // sh "aws s3 ls"
            // sh "cd dist"
            // sh "aws s3 cp dist/my-app/ s3://seetha-cicd-bec-cross-account --recursive"
            // }

        // }
// }

//   }
// }