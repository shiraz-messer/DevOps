from fastapi import FastAPI
import pandas as pd
import os
import requests


app = FastAPI()
dfCity = {}

dfCity = pd.read_csv("./city.csv")


@app.on_event("startup")
def init_data():
    dfCity = pd.read_csv("./city.csv")
    print(dfCity)


@app.get("/")
def read_root():
    return {"check": dfCity}


@app.get("/he/{place}/")
def return_coordinates_he(place):
    x, y = search_in_csv_by_place_he(place)
    return {"res": {"x": x, "y": y}}


@app.get("/en/{place}/")
def return_coordinates_en(place):
    x, y = search_in_csv_by_place_en(place)
    return {"res": {"x": x, "y": y}}


def search_in_csv_by_place_he(place):
    try:
        rowCity = dfCity.loc[dfCity["MGLSDE_LOC"] == place]
        return rowCity.iloc[0]["X"], rowCity.iloc[0]["Y"]
    except:
        return 0, 0


def search_in_csv_by_place_en(place):
    try:
        rowCity = dfCity.loc[dfCity["MGLSDE_L_4"] == place]
        return rowCity.iloc[0]["X"], rowCity.iloc[0]["Y"]
    except:
        return 0, 0
