
import math


def hydrostatic_pressure(mud_weight_ppg: float, tvd_ft: float) -> float:
    """Calculate hydrostatic pressure in psi."""
    if mud_weight_ppg <= 0 or tvd_ft <= 0:
        raise ValueError("Mud weight and TVD must be positive.")

    return 0.052 * mud_weight_ppg * tvd_ft


def formation_pressure(gradient_psi_ft: float, tvd_ft: float) -> float:
    """Estimate formation pressure in psi from a supplied gradient."""
    if gradient_psi_ft < 0 or tvd_ft < 0:
        raise ValueError("Gradient and TVD cannot be negative.")

    return gradient_psi_ft * tvd_ft


def required_mud_weight(pressure_psi: float, tvd_ft: float) -> float:
    """Calculate the mud weight corresponding to a target pressure."""
    if pressure_psi < 0 or tvd_ft <= 0:
        raise ValueError("Pressure must be non-negative and TVD positive.")

    return pressure_psi / (0.052 * tvd_ft)


def api_gravity(specific_gravity: float) -> float:
    """Convert oil specific gravity at the reference temperature to API."""
    if specific_gravity <= 0:
        raise ValueError("Specific gravity must be positive.")

    return 141.5 / specific_gravity - 131.5


def specific_gravity(api: float) -> float:
    """Convert API gravity to specific gravity."""
    if api <= -131.5:
        raise ValueError("API gravity must be greater than -131.5.")

    return 141.5 / (api + 131.5)


def ooip(
    area_acres: float,
    net_pay_ft: float,
    porosity: float,
    water_saturation: float,
    boi_rb_stb: float,
) -> float:
    """Estimate original oil in place in stock-tank barrels."""
    if area_acres <= 0 or net_pay_ft <= 0 or boi_rb_stb <= 0:
        raise ValueError("Area, net pay and Boi must be positive.")

    if not 0 <= porosity <= 1:
        raise ValueError("Porosity must be between 0 and 1.")

    if not 0 <= water_saturation <= 1:
        raise ValueError("Water saturation must be between 0 and 1.")

    return (
        7758
        * area_acres
        * net_pay_ft
        * porosity
        * (1 - water_saturation)
        / boi_rb_stb
    )


def ogip(
    area_acres: float,
    net_pay_ft: float,
    porosity: float,
    water_saturation: float,
    bgi_res_ft3_scf: float,
) -> float:
    """Estimate original gas in place in standard cubic feet."""
    if area_acres <= 0 or net_pay_ft <= 0 or bgi_res_ft3_scf <= 0:
        raise ValueError("Area, net pay and Bgi must be positive.")

    if not 0 <= porosity <= 1:
        raise ValueError("Porosity must be between 0 and 1.")

    if not 0 <= water_saturation <= 1:
        raise ValueError("Water saturation must be between 0 and 1.")

    return (
        43560
        * area_acres
        * net_pay_ft
        * porosity
        * (1 - water_saturation)
        / bgi_res_ft3_scf
    )
