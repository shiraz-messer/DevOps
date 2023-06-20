from fastapi import FastAPI
import os


app = FastAPI()


@app.get("/{place}/")
def wirte_log(place):
    if place != "" and place != "favicon.ico":
        with open("log.txt", "w") as f:
            f.write(place)
        return {"res": {"wrote": True}}
    return {"res": {"wrote": False}}


@app.get("/log/log")
def read_log():
    with open("log.txt", "r") as f:
        rd = f.read()
    return {"res": rd}
