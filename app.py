import streamlit as st
from datetime import datetime
import time
import random

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="BDG MASTER SNIPER PANEL",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- 100% पिक्सेल-परफेक्ट CSS (बिना किसी व्हाइट पट्टी के और सटीक टच के साथ) ---
st.markdown("""
    <style>
    .stApp { background-color: #05050a; color: #FFFFFF; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    
    @keyframes super-blink {
        0% { opacity: 1; transform: scale(1.2); box-shadow: 0 0 12px #FF0033; }
        50% { opacity: 0.1; transform: scale(0.8); box-shadow: 0 0 2px #FF0033; }
        100% { opacity: 1; transform: scale(1.2); box-shadow: 0 0 12px #FF0033; }
    }
    @keyframes green-glow-pulse {
        0% { box-shadow: 0 0 8px #00FF66, inset 0 0 5px #00FF66; }
        50% { box-shadow: 0 0 20px #00FF66, inset 0 0 10px #00FF66; }
        100% { box-shadow: 0 0 8px #00FF66, inset 0 0 5px #00FF66; }
    }
    
    .blinking-dot { 
        display: inline-block; 
        width: 8px; 
        height: 8px; 
        background-color: #FF0033; 
        border-radius: 50%; 
        margin-right: 5px; 
        animation: super-blink 0.6s infinite ease-in-out; 
        vertical-align: middle;
    }
    
    /* ऊपर के सभी Streamlit बटनों को पूरी तरह अदृश्य और शून्य आकार का करना ताकि कोई व्हाइट पट्टी न आए */
    div.stButton > button {
        background-color: transparent !important;
        border: none !important;
        color: transparent !important;
        height: 0px !important;
        min-height: 0px !important;
        padding: 0px !important;
        margin: 0px !important;
        box-shadow: none !important;
    }

    /* स्क्रीनशॉट जैसी सटीक गेम मोड लिस्ट और उनके क्लिकेबल रेडियो बटन */
    .exact-modes-container {
        background: #05050a;
        padding: 6px 0 12px 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .mode-row {
        display: flex;
        justify-content: flex-start;
        gap: 30px;
    }
    .mode-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 900;
        font-size: 13px;
        cursor: pointer;
    }
    .circle-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        border: 2px solid #FFFFFF;
        background: #05050a;
        display: inline-block;
    }
    .circle-dot.active {
        background-color: #FF0055;
        border-color: #FF0055;
        box-shadow: 0 0 8px #FF0055;
    }

    /* 🔥 स्क्रीनशॉट जैसा सिंगल मास्टर ग्रीन बॉक्स (सब कुछ एक ही लाइन में अटैच) */
    .master-single-box {
        background: #090e14;
        border: 2px solid #00FF66;
        border-radius: 10px;
        padding: 8px 10px;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.3);
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 6px;
    }
    
    .panel-title-text {
        color: #00FFFF;
        font-size: 11px;
        font-weight: 900;
        white-space: nowrap;
        display: flex;
        align-items: center;
    }
    
    .online-count-text {
        color: #FFFFFF;
        font-size: 11px;
        font-weight: 900;
        white-space: nowrap;
        display: flex;
        align-items: center;
    }

    /* Streamlit इनपुट बॉक्स को बिल्कुल बीच वाले डैश्ड खाचे जैसा बनाना */
    .stTextInput input {
        background-color: #0d141e !important;
        color: #00FFFF !important;
        border: 1.5px dashed #00FFFF !important;
        border-radius: 6px !important;
        font-weight: 900 !important;
        text-align: center !important;
        letter-spacing: 2px !important;
        padding: 4px !important;
        height: 32px !important;
    }
    .stTextInput > label { display: none !important; }
    div[data-baseweb="input"] { background: transparent !important; }

    /* टारगेट पीरियड और टाइमर कार्ड */
    .target-time-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #090a10;
        border: 2px solid #FFD700;
        border-radius: 8px;
        padding: 10px 14px;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.3);
        margin-bottom: 10px;
    }
    .target-badge {
        color: #00FFFF;
        font-weight: 900;
        font-size: 16px;
        background: rgba(0, 255, 255, 0.1);
        padding: 4px 10px;
        border-radius: 6px;
        border: 2px solid #00FFFF;
        margin-left: 6px;
    }
    
    .next-shot-banner {
        border: 2.5px solid #00FF66;
        background: rgba(0, 255, 102, 0.05);
        padding: 14px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: 900;
        margin: 10px 0;
        color: #00FF66;
        letter-spacing: 1px;
        animation: green-glow-pulse 1.2s infinite;
    }
    
    .result-grid {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-top: 10px;
    }
    .result-card-box {
        flex: 1;
        text-align: center;
        background: #0f0b1e;
        border: 2px solid #3d2b63;
        border-radius: 10px;
        padding: 12px 6px;
    }
    
    .history-card {
        margin-top: 12px;
        background: #090a10;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 24px; font-weight: 900;'>👑 BDG DUAL SHIELD <br> ACCESS PANEL</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div style='background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2);'>", unsafe_allow_html=True)
        mobile_input = st.text_input("📱 MOBILE NUMBER", placeholder="Enter mobile number")
        password_input = st.text_input("🔒 PASSWORD", type="password", placeholder="Enter password")

        if st.button("🚀 UNLOCK PANEL", use_container_width=True):
            if mobile_input == MASTER_MOBILE and password_input == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ अमान्य विवरण!")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    # ऑनलाइन यूजरकाउंट लाइव फ्लक्चुएशन लॉजिक
    if "online_count" not in st.session_state:
        st.session_state.online_count = 350078
        st.session_state.last_live_tick = time.time()

    current_t = time.time()
    if current_t - st.session_state.last_live_tick > 3:
        st.session_state.online_count += random.randint(-45, 52)
        st.session_state.last_live_tick = current_t

    if "active_game_mode" not in st.session_state:
        st.session_state.active_game_mode = "WINGO 1M"

    # स्क्रीनशॉट जैसे सटीक गेम मोड (30S, 1M, 3M, 5M) चुनने के लिए सटीक बटन ग्रिड
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        if st.button("WINGO 30S", key="btn_30s"): st.session_state.active_game_mode = "WINGO 30S"
    with c2:
        if st.button("WINGO 1M", key="btn_1m"): st.session_state.active_game_mode = "WINGO 1M"
    with c3:
        if st.button("WINGO 3M", key="btn_3m"): st.session_state.active_game_mode = "WINGO 3M"
    with c4:
        if st.button("WINGO 5M", key="btn_5m"): st.session_state.active_game_mode = "WINGO 5M"

    selected_game = st.session_state.active_game_mode

    # 🎨 स्क्रीनशॉट जैसी हूबहू दो-पंक्तियों वाली गेम मोड लिस्ट (बिना किसी व्हाइट पट्टी के)
    st.markdown(f"""
        <div class="exact-modes-container">
            <div class="mode-row">
                <div class="mode-item">
                    <div class="circle-dot {'active' if selected_game=='WINGO 30S' else ''}"></div>
                    <span style="color: #00FFFF;">WINGO 30S</span>
                </div>
                <div class="mode-item">
                    <div class="circle-dot {'active' if selected_game=='WINGO 1M' else ''}"></div>
                    <span style="color: #FF007F;">WINGO 1M</span>
                </div>
                <div class="mode-item">
                    <div class="circle-dot {'active' if selected_game=='WINGO 3M' else ''}"></div>
                    <span style="color: #FFD700;">WINGO 3M</span>
                </div>
            </div>
            <div class="mode-row">
                <div class="mode-item">
                    <div class="circle-dot {'active' if selected_game=='WINGO 5M' else ''}"></div>
                    <span style="color: #00FF66;">WINGO 5M</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    @st.fragment(run_every=1)
    def live_dashboard_core():
        now = datetime.now()

        # 🔥 एकदम स्क्रीनशॉट जैसा सिंगल मास्टर ग्रीन बॉक्स (पैनल नाम, XXXXX इनपुट, और लाइव यूजरकाउंट एक लाइन में)[span_5](start_span)[span_5](end_span)
        st.markdown('<div class="master-single-box">', unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.3, 1.0, 1.1])
        
        with col_l:
            st.markdown(
                '<div class="panel-title-text"><span class="blinking-dot"></span>⚡ BDG SNIPER PANEL</div>',
                unsafe_allow_html=True
            )
        with col_m:
            manual_period_input = st.text_input(
                "Period Input",
                value="XXXXX",
                max_chars=5,
                key="live_period_box",
                label_visibility="collapsed"
            )
        with col_r:
            st.markdown(
                f'<div class="online-count-text"><span class="blinking-dot"></span>👥 {st.session_state.online_count:,}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

        # --- गेम का लाइव टाइमर और पीरियड लॉजिक ---
        seconds_map = {"WINGO 30S": 30, "WINGO 1M": 60, "WINGO 3M": 180, "WINGO 5M": 300}
        sec_val = seconds_map.get(selected_game, 60)

        total_seconds = now.hour * 3600 + now.minute * 60 + now.second
        remaining_secs = sec_val - (total_seconds % sec_val)
        mins = remaining_secs // 60
        secs_rem = remaining_secs % 60
        timer_str = f"{mins:02d}:{secs_rem:02d}"

        current_block_index = total_seconds // sec_val
        
        clean_input = "".join(filter(str.isdigit, manual_period_input))
        if not clean_input:
            base_val = 10313
        else:
            base_val = int(clean_input)
        
        target_period = base_val + current_block_index

        def get_trend(p):
            return "SMALL" if (p % 2 != 0) else "BIG"

        history = [get_trend(target_period - i) for i in range(5, 0, -1)]
        pred_size = get_trend(target_period)
        
        rng = random.Random(target_period)
        pred_num = rng.choice([0, 1, 3, 5, 7, 9]) if pred_size == "SMALL" else rng.choice([2, 4, 6, 8])
        pred_color = "RED" if pred_num in [0, 2, 4, 6, 8] else "GREEN"

        # --- टारगेट पीरियड और टाइमर कार्ड ---
        st.markdown(
            f"""
            <div class="target-time-card">
                <div style="display: flex; align-items: center;">
                    <span class="blinking-dot"></span>
                    <span style="font-size: 13px; color: #FFD700; font-weight: 900;">TARGET PERIOD:</span>
                    <span class="target-badge">{target_period}</span>
                </div>
                <div style="color: #FF00FF; font-weight: 900; font-size: 16px;">⏰ {timer_str}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- नेक्स्ट शॉट बैनर ---
        st.markdown(
            f'<div class="next-shot-banner">🔥 NEXT SHOT : <span style="color: #00FFFF; font-size: 20px;">{pred_size}</span> 🎯</div>',
            unsafe_allow_html=True
        )

        # --- नंबर, साइज़ और कलर बॉक्स ---
        st.markdown(
            f"""
            <div class="result-grid">
                <div class="result-card-box">
                    <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">NUMBER</div>
                    <div style="background-color: #FF3344; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 900; margin: 0 auto; color: white;">{pred_num}</div>
                </div>
                <div class="result-card-box">
                    <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">SIZE</div>
                    <div style="background: #0088FF; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 14px; text-align: center;">{pred_size}</div>
                </div>
                <div class="result-card-box">
                    <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">COLOR</div>
                    <div style="background-color: #FF3344; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 14px; text-align: center;">{pred_color}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- रनिंग हिस्ट्री चार्ट ---
        boxes_html = ""
        for item in history:
            bg_col = "#FF9900" if item == "BIG" else "#0077FF"
            boxes_html += f"<div style='background: {bg_col}; color: white; padding: 5px 10px; border-radius: 4px; font-weight: 900; font-size: 11px; margin: 0 2px;'>{item}</div>"

        next_bg_col = "#0077FF" if pred_size == "SMALL" else "#FF9900"
        boxes_html += f"<div style='background: {next_bg_col}; color: white; padding: 5px 10px; border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 11px; border: 2px solid #00FF66; margin-left: 4px;'>🎯 NEXT: {pred_size}</div>"

        st.markdown(
            f"""
            <div class="history-card">
                <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                    <span>📊 {selected_game} लाइव ओमनी-मैटrix रनिंग हिस्ट्री चार्ट:</span>
                    <span><span class="blinking-dot" style="margin-right: 0px;"></span> <span style="font-size: 9px; color: #00FF66; vertical-align: middle;">LIVE</span></span>
                </div>
                <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px;">{boxes_html}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    live_dashboard_core()
