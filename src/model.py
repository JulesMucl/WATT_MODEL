from src.physics.thermodynamics import compute_density
from src.physics.equations import *



def run_model(params):

    mass = params["mass"]  # Masse du vélo et du cycliste en kg
    altitude = params["altitude"]
    ground_temperature = params["ground_temperature"]
    p0 = params["p0"]
    g = params["g"]
    R = params["R"]
    L_ad = params["L_ad"]


    ### A calculer plus tard ###
    Cd = params["Cd"]
    A = params["A"]
    V_moy = params["V_moy"]  # Vitesse moyenne en m/s
    Cd = params["Cd"]  # Coefficient de traînée
    Rol_res_coef = params["Rol_res_coef"]  # Coefficient de roulement 
    slope = params["slope"]  # Pente en pourcentage
    eta_bike = params["eta_bike"]  # Efficacité du vélo




    rho = compute_density(altitude, ground_temperature, p0, g, R, L_ad)

    Power_drag = drag_power(rho, Cd, A, V_moy)  
    Power_rolling = rolling_resistance_power(params["mass"], g, Rol_res_coef, V_moy)
    Power_slope = slope_power(params["mass"], g, slope, V_moy)
    # Calcul de la puissance totale
    Power_total = Power_drag + Power_rolling + Power_slope

    # Ajustement de la puissance totale par l'efficacité du vélo
    Power_rider = Power_total / eta_bike


    






# # Affichage des résultats
# print(f"Densité de l'air à {altitude} m : {rho:.3f} kg/m³")
# print(f"Puissance de traînée à {V_moy} m/s : {Power_drag:.2f} W")
# print(f"Puissance de résistance au roulement à {V_moy} m/s : {Power_rolling:.2f} W")
# print(f"Puissance due à la pente à {V_moy} m/s : {Power_slope:.2f} W")
# print("===================================")
# print(f"Puissance développée par le coureur : {Power_rider:.2f} W")
# print("===================================")


