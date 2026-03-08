import streamlit as st
import sys
import os

sys.path.insert(0, r'C:\Users\Acer\hive\core\framework\agents\wayward_ai')

st.set_page_config(
    page_title="Wayward AI",
    page_icon="🧭",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); min-height: 100vh; }
    
    .hero { text-align: center; padding: 40px 20px 10px 20px; }
    .hero-title { 
        font-size: 3em; font-weight: 900; 
        background: linear-gradient(90deg, #f7971e, #ffd200);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 0;
    }
    .hero-sub { color: #a0a8c0; font-size: 0.9em; margin-top: 8px; margin-bottom: 20px; letter-spacing: 2px; text-transform: uppercase; }
    .quick-label { color: #6b7aaa; font-size: 0.75em; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; text-align: center; }
    
    div.stButton > button {
        width: 100%; border-radius: 12px;
        border: 1px solid rgba(255,255,255,0.15);
        background: rgba(255,255,255,0.08);
        color: #ffffff !important;
        font-weight: 600; font-size: 0.85em; padding: 12px 8px;
    }
    div.stButton > button:hover {
        background: rgba(247,151,30,0.25);
        border-color: #f7971e;
        color: #ffd200 !important;
    }
    
    [data-testid="stChatMessage"] {
        background: rgba(255,255,255,0.07) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        color: #ffffff !important;
    }
    [data-testid="stChatMessage"] p { color: #ffffff !important; }
    [data-testid="stChatMessage"] li { color: #ffffff !important; }
    
    [data-testid="stChatInput"] textarea { 
        background: rgba(255,255,255,0.08) !important;
        color: #ffffff !important;
        border: 1px solid rgba(247,151,30,0.4) !important;
        border-radius: 12px !important;
    }
    [data-testid="stChatInput"] textarea::placeholder { color: #6b7aaa !important; }
    
    .footer { text-align: center; color: #4a5280; font-size: 0.75em; margin-top: 20px; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div style="font-size:3em">🧭</div>
    <div class="hero-title">WAYWARD AI</div>
    <div class="hero-sub">Offline travel companion · Vanlife · RV · Overlanding</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="quick-label">Quick Actions</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("⚠️ Risk Check"):
        st.session_state.quick = "what are the risks in caucasus in april"
with col2:
    if st.button("🔧 Repair Help"):
        st.session_state.quick = "my tire is flat"
with col3:
    if st.button("🗺️ Route Plan"):
        st.session_state.quick = "best route from Tbilisi to Yerevan"
with col4:
    if st.button("💚 Wellness"):
        st.session_state.quick = "I feel lonely been alone for weeks"

st.markdown("<br>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "👋 Hey! I'm Wayward AI — your offline travel companion. Ask me about road risks, repairs, routes, or survival tips. Where are you headed?"
    })

if "quick" in st.session_state:
    prompt = st.session_state.quick
    del st.session_state.quick
    st.session_state.messages.append({"role": "user", "content": prompt})
    from intent_router import route_query
    result = route_query(prompt)
    st.session_state.messages.append({"role": "assistant", "content": result.get("response", "No response")})
    st.rerun()

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(f'<p style="color:#ffffff">{msg["content"]}</p>', unsafe_allow_html=True)
    else:
        with st.chat_message("assistant", avatar="🧭"):
            st.markdown(f'<p style="color:#ffffff">{msg["content"]}</p>', unsafe_allow_html=True)

if prompt := st.chat_input("Ask about risks, repairs, routes, survival..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(f'<p style="color:#ffffff">{prompt}</p>', unsafe_allow_html=True)
    with st.chat_message("assistant", avatar="🧭"):
        with st.spinner(""):
            from intent_router import route_query
            result = route_query(prompt)
            response = result.get("response", "No response")
        st.markdown(f'<p style="color:#ffffff">{response}</p>', unsafe_allow_html=True)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown('<div class="footer">🌍 Caucasus · Central Asia · Latin America · Africa · Oceania · Siberia</div>', unsafe_allow_html=True)
