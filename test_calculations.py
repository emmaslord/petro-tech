
import pytest

from calculations import (
    hydrostatic_pressure,
    formation_pressure,
    required_mud_weight,
    api_gravity,
    specific_gravity,
    ooip,
    ogip,
)


def test_hydrostatic_pressure():
    assert hydrostatic_pressure(10, 5000) == 2600


def test_formation_pressure():
    assert formation_pressure(0.465, 5000) == 2325


def test_required_mud_weight():
    assert required_mud_weight(2600, 5000) == 10


def test_api_gravity_round_trip():
    sg = 0.85
    assert specific_gravity(api_gravity(sg)) == pytest.approx(sg)



def test_ooip():
    result = ooip(640, 50, 0.20, 0.30, 1.20)
    assert result == pytest.approx(28_963_200)

def test_ogip():
    result = ogip(640, 50, 0.20, 0.30, 0.005)
    assert result == pytest.approx(39_029_760_000)


def test_invalid_depth():
    with pytest.raises(ValueError):
        hydrostatic_pressure(10, 0)



# Additional hydrostatic pressure reference cases

def test_hydrostatic_reference_case_2():
    # Reference example: 12 ppg at 12,500 ft = 7,800 psi
    assert hydrostatic_pressure(12, 12500) == 7800


def test_hydrostatic_pressure_scales_with_depth():
    shallow = hydrostatic_pressure(10, 1000)
    deep = hydrostatic_pressure(10, 2000)
    assert deep == pytest.approx(2 * shallow)


# API gravity reference and input validation

def test_api_gravity_for_sg_085():
    assert api_gravity(0.85) == pytest.approx(34.9705882353)


def test_specific_gravity_for_api_35():
    assert specific_gravity(35) == pytest.approx(141.5 / 166.5)


def test_api_gravity_rejects_zero_sg():
    with pytest.raises(ValueError):
        api_gravity(0)


def test_specific_gravity_rejects_invalid_api():
    with pytest.raises(ValueError):
        specific_gravity(-131.5)
