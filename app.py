import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Elegant UI Demo",
    page_icon="✨",
    layout="centered"
)

# --- Minimal custom styling ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    }
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .block-container { padding-top: 3rem; padding-bottom: 3rem; }
    .card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 28px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.35);
        backdrop-filter: blur(8px);
    }
    .muted { opacity: 0.85; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ Elegant UI Demo")
st.caption("A minimal Streamlit app with a clean aesthetic, some info text, and two buttons.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Welcome 👋")

st.markdown(
    """
    This UI demonstrates:
    - A **simple, elegant layout** with a soft glassy card.
    - **Two buttons** that perform small interactive actions.
    - A responsive design that works on desktop and mobile.
    """,
)

col1, col2 = st.columns(2, gap="large")

with col1:
    if st.button("Say Hello 👋", use_container_width=True):
        st.success("Hello there! Hope you're having a productive day.")

with col2:
    if st.button("Show Time ⏰", use_container_width=True):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        st.info(f"Current time is **{now}**")

st.divider()
st.markdown(
    '<p class="muted">Built with <b>Streamlit</b>. Edit <code>app.py</code> to customize text, colors, and actions.</p>',
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)
