from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur RadarEditorial"}

@app.get("/orientation")
def orientation():
    return {"phase": "Orientation", "status": "active"}

@app.get("/production")
def production():
    return {"phase": "Production", "status": "active"}

@app.get("/strategie")
def strategie():
    return {"phase": "Stratégie", "status": "active"}

@app.get("/suivi")
def suivi():
    return {"phase": "Suivi", "status": "active"}

@app.get("/tests")
def tests():
    return {"phase": "Tests", "status": "active"}
