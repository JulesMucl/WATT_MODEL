import CoolProp.CoolProp as CP




def compute_density(altitude, ground_temperature, p0, g, R, L_ad):
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
    P = p0 * (1 - L_ad * altitude / ground_temperature)**(g / (R * L_ad))
    
    # Température à l'altitude (car CoolProp a besoin de la température locale)
    T_alt = ground_temperature - L_ad * altitude  # T(h) = T0 - L·h
    
    # Densité de l'air avec CoolProp à cette altitude
    rho = CP.PropsSI('D', 'T', T_alt, 'P', P, 'Air')
    
    return rho
