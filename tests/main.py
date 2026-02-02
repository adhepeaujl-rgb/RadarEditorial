from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI(
    title="RadarEditorial",
    description="API de démonstration pour RadarEditorial avec plusieurs phases",
    version="1.0.0"
)

# Endpoint racine
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur RadarEditorial"}

# Endpoint Orientation
@app.get("/orientation")
def orientation():
    return {"phase": "Orientation", "status": "active"}

# Endpoint Production
@app.get("/production")
def production():
    return {"phase": "Production", "status": "active"}

# Endpoint Stratégie
@app.get("/strategie")
def strategie():
    return {"phase": "Stratégie", "status": "active"}

# Endpoint Suivi
@app.get("/suivi")
def suivi():
    return {"phase": "Suivi", "status": "active"}

# Endpoint Tests
@app.get("/tests")
def tests():
    return {"phase": "Tests", "status": "active"}
