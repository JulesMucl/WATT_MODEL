# main.py
import yaml
from src.model import run_model

# Chargement des paramètres
with open("config_model.yaml") as f:
    params = yaml.safe_load(f)

# Lancer le modèle avec les paramètres
run_model(params)



