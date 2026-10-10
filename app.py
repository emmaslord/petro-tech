
import streamlit as st

st.set_page_config(
    page_title="PetroTech",
    page_icon="🛢️",
    layout="wide"
)

st.title("🛢️ PetroTech")
st.subheader("Petroleum Engineering Calculator")
st.write("Practical tools for petroleum engineering calculations.")

st.divider()

calculation = st.selectbox(
    "Choose a calculation",
    [
        "Hydrostatic Pressure",
        "Formation Pressure",
        "Mud Weight",
        "API Gravity",
        "Specific Gravity",
        "OOIP"
    ]
)

st.divider()

if calculation == "Hydrostatic Pressure":
    st.header("Hydrostatic Pressure")

    mud_weight = st.number_input(
        "Mud weight (ppg)", min_value=0.1, value=10.0
    )
    tvd = st.number_input(
        "True vertical depth (ft)", min_value=0.1, value=5000.0
    )

    if st.button("Calculate Pressure"):
        pressure = 0.052 * mud_weight * tvd
        st.success(f"Hydrostatic Pressure: {pressure:,.2f} psi")

elif calculation == "Formation Pressure":
    st.header("Formation Pressure")

    gradient = st.number_input(
        "Pressure gradient (psi/ft)", min_value=0.0, value=0.465
    )
    tvd = st.number_input(
        "True vertical depth (ft)", min_value=0.0, value=5000.0
    )

    if st.button("Calculate Formation Pressure"):
        pressure = gradient * tvd
        st.success(f"Formation Pressure: {pressure:,.2f} psi")

elif calculation == "Mud Weight":
    st.header("Required Mud Weight")

    pressure = st.number_input(
        "Required pressure (psi)", min_value=0.0, value=2500.0
    )
    tvd = st.number_input(
        "True vertical depth (ft)", min_value=0.1, value=5000.0
    )

    if st.button("Calculate Mud Weight"):
        mw = pressure / (0.052 * tvd)
        st.success(f"Required Mud Weight: {mw:.2f} ppg")

elif calculation == "API Gravity":
    st.header("API Gravity")

    sg = st.number_input(
        "Oil specific gravity", min_value=0.01,
        max_value=2.0, value=0.85
    )

    if st.button("Calculate API Gravity"):
        api = 141.5 / sg - 131.5
        st.success(f"API Gravity: {api:.2f}° API")

elif calculation == "Specific Gravity":
    st.header("Specific Gravity")

    api = st.number_input(
        "API gravity (degrees)", min_value=-130.0,
        value=35.0
    )

    if st.button("Calculate Specific Gravity"):
        sg = 141.5 / (api + 131.5)
        st.success(f"Specific Gravity: {sg:.4f}")

elif calculation == "OOIP":
    st.header("Original Oil in Place")

    area = st.number_input("Area (acres)", min_value=0.0, value=640.0)
    thickness = st.number_input(
        "Net pay thickness (ft)", min_value=0.0, value=50.0
    )
    porosity = st.number_input(
        "Porosity (fraction)", min_value=0.0,
        max_value=1.0, value=0.20
    )
    swi = st.number_input(
        "Connate water saturation (fraction)",
        min_value=0.0, max_value=1.0, value=0.30
    )
    boi = st.number_input(
        "Initial oil formation volume factor (rb/stb)",
        min_value=0.01, value=1.20
    )

    if st.button("Calculate OOIP"):
        ooip = (
            7758 * area * thickness * porosity * (1 - swi) / boi
        )
        st.success(f"OOIP: {ooip:,.0f} stock-tank barrels")
        st.caption(f"Approximately {ooip / 1_000_000:.3f} million STB")

st.divider()
st.caption("PetroTech | Educational engineering calculator")
