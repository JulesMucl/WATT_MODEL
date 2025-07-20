# main.py

import yaml
from src.model import run_model
from TCX.tcx_reader import *

if __name__ == '__main__':

    filepath = "C:/Users/julem/WATT_MODEL/TCX/activity_19789346499.tcx"

    trackpoints = read_tcx_trackpoints(filepath)
    altitudes = [tp["altitude"] for tp in trackpoints]

    dplus = compute_dplus(altitudes)
    print(f"Dénivelé positif total : {dplus} m")

    plot_elevation(trackpoints)

    # 2. Charger les paramètres du fichier config_model.yaml
    with open("config_model.yaml") as f:
        params = yaml.safe_load(f)

    # 3. Ajouter éventuellement le D+ au dictionnaire de paramètres
    params["dplus"] = dplus

    # 4. Appeler le modèle principal
    run_model(params)
