import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="Compte à rebours",
    layout="centered"
)

# Titre
st.markdown(
    "<h1 style='text-align:center;'>Compte à rebours</h1>",
    unsafe_allow_html=True
)

# Date cible : 16 mars 2026 à 00h01
target_date = datetime(2026, 3, 16, 0, 1)

placeholder = st.empty()

while True:
    now = datetime.now()
    diff = target_date - now

    if diff.total_seconds() <= 0:
        placeholder.markdown(
            "<h2 style='text-align:center;'>C'est arrivé 🎉</h2>",
            unsafe_allow_html=True
        )
        break

    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    placeholder.markdown(
        f"""
        <div style="
            text-align:center;
            font-size:40px;
            font-weight:bold;
        ">
            {days} jours<br>
            {hours} heures<br>
            {minutes} minutes
        </div>
        """,
        unsafe_allow_html=True
    )

    time.sleep(60)
``
