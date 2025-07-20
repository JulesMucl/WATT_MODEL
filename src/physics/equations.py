

### DRAG FORCE EQUATION ###

def drag_force(rho, Cd, A, v):
    """
    Calcule la force de traînée aérodynamique.

    :param rho: Densité de l'air (kg/m^3)
    :param Cd: Coefficient de traînée (sans unité)
    :param A: Surface frontale (m^2)
    :param v: Vitesse (m/s)
    :return: Force de traînée (N)
    """
    return 0.5 * rho * Cd * A * v**2

### DRAG POWER EQUATION ###
def drag_power(rho, Cd, A, v):
    """
    Calcule la puissance de traînée aérodynamique.

    :param rho: Densité de l'air (kg/m^3)
    :param Cd: Coefficient de traînée (sans unité)
    :param A: Surface frontale (m^2)
    :param v: Vitesse (m/s)
    :return: Puissance de traînée (W)
    """
    return drag_force(rho, Cd, A, v) * v    

### ROLLING RESISTANCE FORCE EQUATION ###
def rolling_resistance_force(mass, g, Rol_res_coef):
    """
    Calcule la force de résistance au roulement.

    :param mass: Masse du vélo et du cycliste (kg)
    :param g: Accélération due à la gravité (m/s^2)
    :param Rol_res_coef: Coefficient de résistance au roulement (sans unité)
    :return: Force de résistance au roulement (N)
    """
    return Rol_res_coef * mass * g

### ROLLING RESISTANCE POWER EQUATION ###
def rolling_resistance_power(mass, g, Rol_res_coef, v):
    """
    Calcule la puissance de résistance au roulement.

    :param mass: Masse du vélo et du cycliste (kg)
    :param g: Accélération due à la gravité (m/s^2)
    :param Rol_res_coef: Coefficient de résistance au roulement (sans unité)
    :param v: Vitesse (m/s)
    :return: Puissance de résistance au roulement (W)
    """
    return rolling_resistance_force(mass, g, Rol_res_coef) * v

#### Slope Force Equation ###
def slope_force(mass, g, slope):
    """
    Calcule la force due à la pente.

    :param mass: Masse (kg)
    :param g: Accélération due à la gravité (m/s^2)
    :param slope: Pente en pourcentage (ex: 5 pour 5%)
    :return: Force due à la pente (N)
    """
    return mass * g * (slope / 100)

#### Slope Power Equation ###
def slope_power(mass, g, slope, v):
    """
    Calcule la puissance due à la pente.

    :param mass: Masse (kg)
    :param g: Accélération due à la gravité (m/s^2)
    :param slope: Pente en pourcentage (ex: 5 pour 5%)
    :param v: Vitesse (m/s)
    :return: Puissance due à la pente (W)
    """
    return slope_force(mass, g, slope) * v



