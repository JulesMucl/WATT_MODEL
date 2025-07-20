import CoolProp.CoolProp as CP

p_0=101325  # Pression au niveau de la mer en Pa
g=9.80665  # Gravité terrestre en m/s²
R=287.05  # Constante spécifique de l'air en J/(kg·K
L=0.0065  # Gradient standard en K/m
T0 = 25 + 273.15  # Température au niveau de la mer (en K)
altitude_m = 1000  # Altitude en mètres


def rho(altitude, Temperature, Pression_mer, gravité, R_gas_noble, Gradient_adiabatique):
    """
    Calcule la densité de l'air à une altitude donnée en utilisant le gradient standard.
    
    :param altitude_m: Altitude en mètres
    :param T0: Température au niveau de la mer (en K)
    :param p_0: Pression au niveau de la mer en Pa
    :param g: Gravité terrestre en m/s²
    :param R: Constante spécifique de l'air en J/(kg·K)
    :param L: Gradient standard en K/m
    :return: Densité de l'air à l'altitude donnée
    """
    # Calcul de la pression à l'altitude donnée avec gradient linéaire
    P = p_0 * (1 - L * altitude_m / T0)**(g / (R * L))
    
    # Température à l'altitude (car CoolProp a besoin de la température locale)
    T_alt = T0 - L * altitude_m  # T(h) = T0 - L·h
    
    # Densité de l'air avec CoolProp à cette altitude
    rho = CP.PropsSI('D', 'T', T_alt, 'P', P, 'Air')
    
    return rho



print(f"Densité de l'air à {altitude_m} m : {rho(altitude_m, T0, p_0, g, R, L):.3f} kg/m³")
