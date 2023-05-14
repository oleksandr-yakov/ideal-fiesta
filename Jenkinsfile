pipeline {
    agent any
    environment {
        WORKSPACE = "/home/ubuntu/jenkins/workspace/ci-cd-pipeline"
        ARH_PATH = "/home/ubuntu/jenkins/workspace/Zip"
        BACKUP_PATH = "/home/ubuntu/jenkins/workspace/backup"
        TERM = 'dumb'
        DB_USER="dev"
        DB_PASS="Ag111^@ergnuio"
        DB_NAME="prodMain"
    }
    stages {
        // stage('Clone repository') {
        //     steps {
        //         script {
        //             try {
        //                 sh """#!/bin/bash
        //                 cd $WORKSPACE
        //                 git pull git@github.com:oleksandr-yakov/ideal-fiesta.git
        //                 pwd
        //                 """
        //             } catch (Exception e) {
        //                 error("Clone repository went wrong")
        //                 currentBuild.result = "FAILURE"
        //             }
        //         }
        //     }
        // }
        // stage('Clone repository') {
        //   steps {
        //         checkout changelog: false, poll: false, scm: scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'slave', url: 'https://github.com/oleksandr-yakov/ideal-fiesta.git']])
        //   }
        // }
        stage('Checkout'){
          steps {
            checkout scm
          }
       }
        stage('Setup') {
            steps {
                script {
                    try {
                        sh """#!/bin/bash
                        cd $WORKSPACE
                        docker compose up -d db
                        """
                    } catch (Exception e) {
                        error("Setup went wrong")
                        currentBuild.result = "FAILURE"
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (fileExists("$WORKSPACE/App/start_test.sh")) {
                        try {
                            sh """#!/bin/bash
                            cd $WORKSPACE
                            ./create-table.sh
                            sudo docker compose up -d app
                            ./App/start_test.sh
                            sudo docker stop once_mysql once_app && docker rm once_mysql once_app
                            """
                        } catch (Exception e) {
                            error("Run Tests went wrong")
                            currentBuild.result = "FAILURE"
                        }
                    }
                }
            }
        }
        stage('Archiving') {
            steps {
                script {
                    try {
                        sh """#!/bin/bash
                        cd $WORKSPACE
                        cp -r $ARH_PATH/* $BACKUP_PATH
                        rm -rf $ARH_PATH/*
                        tar -czf $ARH_PATH/ideal-fiesta.tar.gz -C $WORKSPACE .
                        """
                    } catch (Exception e) {
                        error("Rar dont created. Error")
                        currentBuild.result = "FAILURE"
                    }
                }
            }
        }
        stage('Deployment') {
            steps {
                script {
                    try {
                        sh """#!/bin/bash
                        cd $ARH_PATH
                        scp -i ~/.ssh/id_rsa $ARH_PATH/* ubuntu@172.31.35.91:/home/ubuntu/product
                        ssh -i ~/.ssh/id_rsa ubuntu@172.31.35.91 'tar -xvf ~/product/ideal-fiesta.tar.gz -C /home/ubuntu/deploy'
                        ssh -i ~/.ssh/id_rsa ubuntu@172.31.35.91 'cd ./deploy && docker compose up --build -d '

                        scp -i ~/.ssh/id_rsa $ARH_PATH/* ubuntu@172.31.33.129:/home/ubuntu/product
                        ssh -i ~/.ssh/id_rsa ubuntu@172.31.33.129 'tar -xvf ~/product/ideal-fiesta.tar.gz -C /home/ubuntu/deploy'
                        ssh -i ~/.ssh/id_rsa ubuntu@172.31.33.129 'cd ./deploy && docker compose up --build -d '

                        """
                    } catch (Exception e) {
                        error("Rar dont created. Error")
                        currentBuild.result = "FAILURE"
                    }
                }
            }
        }
    }
}
