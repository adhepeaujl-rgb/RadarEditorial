# RadarEditorial
body {
  font-family: Arial, sans-serif;
  text-align: center;
  background-color: #f4f4f4;
  margin: 0;
  padding: 50px;
}

h1 {
  color: #2c3e50;
}

p {
  font-size: 18px;
  color: #555;
# 📘 README – RadarEditorial

RadarEditorial est une application web modulaire construite avec **FastAPI** pour le backend et une architecture claire pour le frontend, les données, la documentation et les tests.  
Ce projet est conçu pour être reproductible, pédagogique et extensible.

---

## 📂 Structure du projet


### 🎯 Rôle des dossiers
- **backend/** : application FastAPI (logique serveur).
  - `main.py` : point d’entrée de l’application.
  - `models/` : définitions des modèles de données (Pydantic, ORM).
  - `routes/` : définition des endpoints (API).
  - `services/` : logique métier et traitements.
  - `utils/` : fonctions utilitaires réutilisables.
- **frontend/** : interface utilisateur (HTML, CSS, JS).
- **data/** : fichiers de données, ressources, jeux de test.
- **docs/** : documentation technique et fonctionnelle.
- **tests/** : scripts de tests unitaires et d’intégration.
- **venv/** : environnement virtuel Python isolé.
- **README.md** : guide du projet.

---

## ⚙️ Installation et lancement

### 1. Créer et activer l’environnement virtuel
```powershell
cd C:\Users\lucad\RadarEditorial
python -m venv venv
.\venv\Scripts\activate
python -m pip install fastapi uvicorn
python -m uvicorn backend.main:app --reload
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur RadarEditorial"}
from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello(name: str = "Jean"):
    return {"message": f"Bonjour {name}, bienvenue sur RadarEditorial"}
from fastapi import FastAPI
from backend.routes import hello

app = FastAPI()

app.include_router(hello.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur RadarEditorial"}
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur RadarEditorial"}
pytest
python -m pip freeze > requirements.txt

---

Jean, ce README est prêt à être **copié-collé directement** dans ton projet.  
Veux-tu que je prépare aussi un **requirements.txt type** (avec FastAPI, Uvicorn, Pydantic, pytest, etc.) pour compléter ton environnement et rendre ton projet immédiatement reproductible ?