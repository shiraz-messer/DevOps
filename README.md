# ![image](https://user-images.githubusercontent.com/108284950/218310916-06c816d9-47c6-4afe-bb4b-a853b0d09cb1.png)                              
# DevOps Project - Microservice Architecture combining Docker, Kubernetes and Jenkins  🐋


## Introduction
Final DevOps Course Project HIT:
This DeOps project is based on microservices architecture using Docker and Kubernetes, Jenkins, and CI/CD pipeline.
Our  GeoLocation App:
Searching for cities in Israel in both Hebrew and English and displaying their locations on a map.

## Table of Contents
- [App Demo](#App-Demo)
- [Requisites](#Requisites)
- [Set-up](#set-up)
- [Deployment](#Deployment)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [App-Design](#App-Design)

## App-Demo
https://user-images.githubusercontent.com/108284950/218329685-c8b335ed-581a-4c37-b0cc-b25d1ef1f03d.mp4

## Requirments
- Git
-	Docker
-	WSL / compatible linux machine
-	Minikube 
-	Jenkins

## Deployment

# Docker
1.	Open the git BASH Terminal, go inside your desired folder and run the following command:
```bash
git clone https://github.com/shiraz-messer/DevOps.git
```
2.	Then you will have to go inside the "Devops" folder using the following command:
```bash
cd Devops 
```
3.	To build the docker
```bash
docker compose build
```
4.	To run GeoLocation, you will have to enter the following command:
```bash
docker compose up
```
5.	Congratulations! You may access GeoLocation following address:
```bash
http://localhost:8501/
```
#  Kubernets Minikube
1.	To run the Minikube:
```bash
minikube start
```
2.	To create the deployment and service for the first time:
```bash
kubectl create -f deployment.yaml 
kubectl create -f service.yaml
```
2.	To see that it worked successfully: 
```bash
kubectl get  <> // pods / deployment / service 
kubectl describe service geolocation 
```

## architecture
This project adheres to a microservice architecture. The primary components of this architecture are:
Frontend: is built with Streamlit, providing a map interface to view the accurate location by user typed the city he wishes to see - in both Hebrew and English (see city.csv on app folder).
Backend and logger: are built with FastAPI.
Docker: Docker is utilized for containerization and deployment. Dockerfiles and Docker Compose are employed to define and build containers for the frontend, backend, and Jenkins.
Kubernetes: Kubernetes Minikube is a tool used for container orchestration. It helps manage the deployment and scaling of containers. 
Jenkins: automation tool used for continuous integration and delivery, and the Jenkinsfile is a script that defines the steps and configuration for a Jenkins pipeline, allowing for efficient and automated software development workflows. 

## Technologies
- Frontend:
  - Using Streamlit
- Backend :
  - Using FastAPI
- logger:
  - Using FastAPI
-  Docker:
  - Containers
  - Images
  - Docker Compose
- Kubernetes:
  - Deployment
  - Service
- Jenkins:
  - CI/CD Pipline 
  - Jenkins Job

## App-Design
![image](https://user-images.githubusercontent.com/108284950/218329974-d02f1b26-5b0f-43a9-860a-43f03f63b803.png)




