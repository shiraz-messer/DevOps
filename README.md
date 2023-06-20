# ![image](https://user-images.githubusercontent.com/108284950/218310916-06c816d9-47c6-4afe-bb4b-a853b0d09cb1.png)                              GeoLocation  


## Introduction
This is a project to search for cities in Israel in Hebrew and English and display their location on a map.

Part of a CS degree course (EASS) final project.


## Requirments
-	Docker
-	WSL / compatible linux machine


## Technologies
#### Backend - Using FastAPI

#### Frontend - Using Streamlit

#### logger - Using FastAPI


## Demonstration

https://user-images.githubusercontent.com/108284950/218329685-c8b335ed-581a-4c37-b0cc-b25d1ef1f03d.mp4

## Design

![image](https://user-images.githubusercontent.com/108284950/218329974-d02f1b26-5b0f-43a9-860a-43f03f63b803.png)



## Deployment
First of all you will need Git and Docker installed on your machine.
1.	Open the Terminal, go inside your desired folder and run the following command:
```bash
git clone https://github.com/EASS-HIT-PART-A-2022-CLASS-II/GeoLocation.git
```
2.	Then you will have to go inside the "GeoLocation" folder using the following command:
```bash
cd GeoLocation
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




