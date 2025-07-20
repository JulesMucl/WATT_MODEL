from src.physics.thermodynamics import compute_density

def run_model(params):
    altitude = params["altitude"]
    ground_temperature = params["ground_temperature"]
    p0 = params["p0"]
    g = params["g"]
    R = params["R"]
    L_ad = params["L_ad"]

    rho = compute_density(altitude, ground_temperature, p0, g, R, L_ad)
    print(f"Densité de l'air à {altitude} m : {rho:.3f} kg/m³")
