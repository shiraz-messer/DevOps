# ![image](https://user-images.githubusercontent.com/108284950/218310916-06c816d9-47c6-4afe-bb4b-a853b0d09cb1.png)                              
# DevOps Project - Microservice Architecture combining Docker, Kubernetes and Jenkins  🐋


## Introduction
Final DevOps Course Project HIT:
This DevOps project is based on microservices architecture using Docker and Kubernetes, Jenkins, and CI/CD pipeline.
Our  GeoLocation App:
Searching for cities in Israel in both Hebrew and English and displaying their locations on a map.

## Presentation Link- Full devolopment proccess and implementation :bowtie:
https://tinyurl.com/DevOpsHIT

## Table of Contents 📝
- [App Demo](#App-Demo)
- [Requirments](#Requirments)
- [Deployment](#Deployment)
- [Architecture](#Architecture)
- [Technologies](#technologies)
- [App-Design](#App-Design)

## App-Demo 🗺📍
https://github.com/shiraz-messer/DevOps/assets/108284950/1cf9489c-2cb4-413d-8ff7-c159928de45a


## Requirments ⚙️
- Git
-	Docker
-	WSL / compatible linux machine
-	Minikube 
-	Jenkins

## Deployment 🚀

### Docker
1.	Open the Git BASH Terminal, go inside your desired folder and run the following command: 🧑‍💻
```bash
git clone https://github.com/shiraz-messer/DevOps.git
```
2.	Then you will have to go inside the "Devops" folder using the following command: 🗃️
```bash
cd Devops 
```
3.	To build the docker 🏗️
```bash
docker compose build
```
4.	To run GeoLocation, you will have to enter the following command: 🌐
```bash
docker compose up
```
5.	Congratulations! You may access GeoLocation following address: ✅
```bash
http://localhost:8501/
```
###  Kubernets Minikube
1.	To run the Minikube: 🏃
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
kubectl get  <TYPE> // pods / deployment / service 
kubectl describe service geolocation 
```
### Jenkins
1.	To run the Jenkins: 🏃
run the 'Docker Jenkins' text file
2.	 You may access Jenkins following address: ✅
```bash
http://127.0.0.1:8080/job/test/indexing/console
```
3.	Configure  Jenkins: 
install the JavaMail API plugin.
4. Build pipeline:
by using the Jenkinsfile as a source from https://github.com/shiraz-messer/DevOps.git
6. Track the Building process and make sure it completed and a SUCCESS mail recieved.

### Complete CICD Proccess
1.	 you will have to go inside the "cicd" folder:  🗃️
```bash
cd cicd 
```
2.	 run the deployment and service files by sell script in order to complete the CICD process,
run the 'run.sh' file:
```bash
 ./run.sh
```
3.	port forwarding to access the app,
run the 'run.sh' file:
```bash
kubectl get pods
```
```bash
kubectl port-forward <FRONTEND-POD> 8501:8501
```
* Port forwarding is used to establish a connection between your local machine and a pod running within a Kubernetes cluster.
4. Now you can access the app once again!✅



## Architecture 🚧
This project adheres to a microservice architecture. The primary components of this architecture are:

Frontend: is built with Streamlit, providing a map interface to view the accurate location by user typed the city he wishes to see - in both Hebrew and English (see city.csv on app folder).

Backend and logger: are built with FastAPI.

Docker: Docker is utilized for containerization and deployment. Dockerfiles and Docker Compose are employed to define and build containers for the frontend, backend, and Jenkins.

Kubernetes: Kubernetes Minikube is a tool used for container orchestration. It helps manage the deployment and scaling of containers. 

Jenkins: automation tool used for continuous integration and delivery, and the Jenkinsfile is a script that defines the steps and configuration for a Jenkins pipeline, allowing for efficient and automated software development workflows. 

## Technologies 🖥
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

## App-Design 🎨
![image](https://user-images.githubusercontent.com/108284950/218329974-d02f1b26-5b0f-43a9-860a-43f03f63b803.png)




