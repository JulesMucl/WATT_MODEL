from src.physics.thermodynamics import compute_density

def run_model():
    # charger les paramètres
    import yaml
    with open("config/parameters.yaml") as f:
        params = yaml.safe_load(f)

    rho = compute_density(params["pressure"], params["temperature"])
    print(f"Densité de l'air = {rho:.2f} kg/m³")
