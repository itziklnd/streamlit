import streamlit as st

# 1:f multiple widgets with same id can be resolved by adding key="value"
st.button("ok")
st.button("ok", key="btn2")


# how to repair 2
if "slider" not in st.session_state:
    st.session_state.slider = 25

# 2: the id based on the parameters and if:
min_value = st.slider("min_value", 0, 50, 25)
value = st.slider("Slider", min_value, 100, min_value, key="1") # if you change tje min value the value slider will reset
# you can fix it by using session state (the key not related to the solution)
min_value1 = st.slider("min_value", 0, 50, 25, key="2")
st.session_state.slider = st.slider("Slider", min_value1, 100, st.session_state.slider)

# 3: if widget is closed and then opened back his state will be reset. to handle this:
input = st.text_input("Enter", value=f"replace this line to session state value")