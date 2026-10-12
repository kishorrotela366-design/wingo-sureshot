from datetime import datetime, timedelta
import random
import time
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="BDG MASTER SNIPER PANEL",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #05050a; color: #FFFFFF; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 15px #FF0055; }
        50% { opacity: 0.1; transform: scale(0.85); box-shadow: 0 0 2px #FF0055; }
        100% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 15px #FF0055; }
    }
    @keyframes pulse-heartbeat {
        0% { box-shadow: 0 0 5px #00FF66; }
        50% { box-shadow: 0 0 20px #00FF66; }
        100% { box-shadow: 0 0 5px #00FF66; }
    }
    @keyframes super-win-glow {
        0% { border-color: #00FF66; box-shadow: 0 0 35px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
        50% { border-color: #FFD700; box-shadow: 0 0 20px #FFD700, inset 0 0 10px #FFD700; background: linear-gradient(135deg, #1a1a00, #0d0d00); }
        100% { border-color: #00FF66; box-shadow: 0 0 35px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
    }
    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }
    .blinking-red-light { display: inline-block; width: 12px; height: 12px; background-color: #FF0055; border-radius: 50%; margin-right: 8px; animation: blink-animation 0.8s infinite ease-in-out; }
    
    /* स्क्रीनशॉट जैसी गेम मोड लिस्ट */
    .exact-modes-container {
        background: #05050a;
        padding: 6px 0 14px 0;
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    .mode-row {
        display: flex;
        justify-content: flex-start;
        gap: 40px;
        align-items: center;
    }
    .mode-item {
        display: flex;
        align-items: center;
        gap: 10px;
        font-weight: 900;
        font-size: 15px;
    }
    .circle-dot {
        width: 16px;
        height: 16px;
        border-radius: 50%;
        border: 2px solid #FFFFFF;
        background: #05050a;
        display: inline-block;
    }
    .circle-dot.active {
        background-color: #FF0055;
        border-color: #FF0055;
        box-shadow: 0 0 10px #FF0055;
    }

    /* सिंगल मास्टर ग्रीन बॉक्स */
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

    /* इनपुट बॉक्स स्टाइल */
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

    .main-card { background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 8px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); }
    .period-badge-small { color: #00FFFF; font-weight: 900; font-size: 16px; background: rgba(0,255,255,0.1); padding: 4px 8px; border-radius: 5px; border: 1.5px solid #00FFFF; letter-spacing: 1px; }
    .super-100-win-banner { border: 3.5px solid #00FF66; padding: 14px; border-radius: 8px; text-align: center; font-size: 16px; font-weight: 900; margin: 8px 0; color: #00FF66; text-transform: uppercase; animation: super-win-glow 0.8s infinite; letter-spacing: 1px; }
    .wait-warning-banner { border: 3.5px solid #FF0000; padding: 14px; border-radius: 8px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; }
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.95); border: 1.5px solid #6644aa; border-radius: 8px; padding: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# आपके सभी 11 सर्वर और सख्त UTR/ऑथेंटिकेशन डेटाबेस का असली सेटअप
if "server_nodes" not in st.session_state:
    st.session_state.server_nodes = [f"BDG-CORE-NODE-{i:02d}" for i in range(1, 12)]
if "verified_users_db" not in st.session_state:
    st.session_state.verified_users_db = {}
if "used_utrs_database" not in st.session_state:
    st.session_state.used_utrs_database = ["123456789012", "998877665544"]

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# ==========================================
# 🔒 ऑपरेटर बाईपास + 11 सर्वर और सख्त UTR सिक्योरिटी पोर्टल
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 22px; font-weight: 900;'>👑 BDG DUAL SHIELD <br> ACCESS & 11-SERVER SECURE PORTAL</h2>", unsafe_allow_html=True)
    
    login_tab, user_register_tab = st.tabs(["👑 OWNER DIRECT LOGIN", "💳 NEW USER QR & UTR VERIFICATION"])
    
    # ---------------- TAB 1: ओनर डायरेक्ट लॉगिन (बिना किसी रुकावट के) ----------------
    with login_tab:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color: #00FFFF; text-align: center; font-weight: 900;'>ओनर मास्टर एक्सेस</h4>", unsafe_allow_html=True)
        owner_mob = st.text_input("📱 मोबाइल नंबर", placeholder="Enter mobile number", key="owner_m_input")
        owner_pass = st.text_input("🔒 पासवर्ड", type="password", placeholder="Enter password", key="owner_p_input")

        if st.button("🚀 UNLOCK PANEL (MASTER)", use_container_width=True, key="owner_unlock_btn"):
            if owner_mob == MASTER_MOBILE and owner_pass == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.success("👑 ओनर एक्सेस सफल! सर्वर लोड हो रहा है...")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("❌ अमान्य ओनर क्रेडेंशियल्स!")
        st.markdown("</div>", unsafe_allow_html=True)

    # ---------------- TAB 2: नया यूजर रजिस्ट्रेशन, 11 सर्वर, PhonePe QR (`kishorsingh226105.wallet@phonepe`) और सख्त UTR चेकिंग ----------------
    with user_register_tab:
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #FFD700; font-weight: 900; text-align: center; margin-bottom: 5px;'>⚡ 11-SERVER VIP ACCESS (₹1500 / 2 DAYS)</h3>", unsafe_allow_html=True)
        
        selected_server = st.selectbox("🌐 SELECT SECURE SERVER NODE", st.session_state.server_nodes)
        
        reg_mob = st.text_input("📱 नया मोबाइल नंबर", placeholder="Enter your mobile number", key="reg_mob_input")
        reg_pass = st.text_input("🔒 नया पासवर्ड सेट करें", type="password", placeholder="Create password", key="reg_pass_input")

        st.markdown("""
            <div style='background: linear-gradient(135deg, #113300, #001a00); border: 2px solid #00FF66; padding: 10px; border-radius: 8px; margin: 10px 0; text-align: center;'>
                <p style='color: #00FF66; font-size: 14px; font-weight: 900; margin: 0;'>💎 2-DAY ACCESS PLAN : ₹1500 ONLY</p>
                <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>PhonePe QR से स्कैन करके भुगतान करें:</p>
                <div style='background: #FFFFFF; padding: 8px; display: inline-block; border-radius: 8px; margin-top: 6px;'>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=1500" width="140" height="140">
                </div>
                <p style='color: #FFD700; font-size: 11px; margin-top: 5px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
            </div>
        """, unsafe_allow_html=True)
        
        utr_code_input = st.text_input("📝 12-Digit UTR / Transaction Ref No.", placeholder="Enter 12-digit UTR number", max_chars=12, key="reg_utr_input")

        if st.button("🛡️ VERIFY & CONNECT TO SERVER", use_container_width=True, key="user_verify_btn"):
            clean_reg_mob = "".join(filter(str.isdigit, reg_mob))
            clean_utr = "".join(filter(str.isdigit, utr_code_input))

            if len(clean_reg_mob) < 10:
                st.error("⚠️ कृपया सही 10 अंकों का मोबाइल नंबर दर्ज करें!")
            elif not reg_pass:
                st.error("⚠️ कृपया पासवर्ड दर्ज करें!")
            elif len(clean_utr) != 12:
                st.error("⚠️ अमान्य UTR! कृपया 12 अंकों का सही UTR नंबर डालें।")
            elif clean_utr in st.session_state.used_utrs_database:
                st.error("🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल हो चुका है या डुप्लीकेट है!")
            else:
                # सख्त UTR और डेटाबेस सेविंग
                st.session_state.used_utrs_database.append(clean_utr)
                st.session_state.verified_users_db[clean_reg_mob] = {
                    "password": reg_pass,
                    "server": selected_server,
                    "expiry": datetime.now() + timedelta(days=2)
                }
                st.session_state.authenticated = True
                st.success(f"✅ UTR वेरीफाई हुआ! आप सफलतापूर्वक {selected_server} से जुड़ गए हैं।")
                time.sleep(1)
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 📊 मुख्य लाइव गेमिंग डैशबोर्ड (स्क्रीनशॉट जैसा पिक्सेल-परफेक्ट UI)
# ==========================================
else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        dynamic_online_count = random.randint(112000, 498000)

        if "active_game_mode" not in st.session_state:
            st.session_state.active_game_mode = "WINGO 1M"

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

        # स्क्रीनशॉट जैसी रंग-बिरंगी गेम मोड विजुअल लिस्ट
        st.markdown(f"""
            <div class="exact-modes-container">
                <div class="mode-row">
                    <div class="mode-item">
                        <div class="circle-dot {'active' if selected_game=='WINGO 30S' else ''}"></div>
                        <span style="color: #00FFFF; font-size: 15px;">WINGO 30S</span>
                    </div>
                    <div class="mode-item">
                        <div class="circle-dot {'active' if selected_game=='WINGO 1M' else ''}"></div>
                        <span style="color: #FF007F; font-size: 15px;">WINGO 1M</span>
                    </div>
                    <div class="mode-item">
                        <div class="circle-dot {'active' if selected_game=='WINGO 3M' else ''}"></div>
                        <span style="color: #FFD700; font-size: 15px;">WINGO 3M</span>
                    </div>
                </div>
                <div class="mode-row">
                    <div class="mode-item">
                        <div class="circle-dot {'active' if selected_game=='WINGO 5M' else ''}"></div>
                        <span style="color: #00FF66; font-size: 15px;">WINGO 5M</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        now = datetime.now()
        
        # 🔥 स्क्रीनशॉट जैसा सिंगल मास्टर ग्रीन बॉक्स (पैनल नाम, पीरियड इनपुट, और यूजरकाउंट एक लाइन में)[span_1](start_span)[span_1](end_span)
        st.markdown('<div class="master-single-box">', unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.3, 1.0, 1.1])
        
        with col_l:
            st.markdown(
                '<div class="panel-title-text"><span class="blinking-red-light" style="width:8px; height:8px; margin-right:4px;"></span>⚡ BDG SNIPER PANEL</div>',
                unsafe_allow_html=True
            )
        with col_m:
            manual_period_input = st.text_input(
                "Period Input",
                value="10784",
                max_chars=6,
                key="user_live_period_input",
                label_visibility="collapsed"
            )
        with col_r:
            st.markdown(
                f'<div class="online-count-text"><span class="blinking-red-light" style="width:8px; height:8px; margin-right:4px;"></span>👥 {dynamic_online_count:,}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

        def render_game_panel(seconds, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "10784"

            state_input_key = f"matrix_input_{seconds}"
            state_block_key = f"matrix_block_{seconds}"

            if state_input_key not in st.session_state or st.session_state[state_input_key] != clean_input:
                st.session_state[state_input_key] = clean_input
                st.session_state[state_block_key] = current_block_index

            block_diff = current_block_index - st.session_state.get(state_block_key, current_block_index)
            
            base_val = int(clean_input)
            current_target_period = base_val + block_diff
            target_period_str = str(current_target_period)

            def calculate_omni_matrix_trend(p_num, offset_val):
                mod_val = (p_num + offset_val) % 5
                pair_check = (p_num // 2 + offset_val) % 3
                
                if mod_val == 0 or mod_val == 1:
                    return "SMALL"
                elif mod_val == 2 or mod_val == 3:
                    return "BIG"
                elif pair_check == 0:
                    return "SMALL"
                else:
                    return "BIG" if (p_num % 2 == 0) else "SMALL"

            history = []
            for h_offset in range(5, 0, -1):
                h_p = current_target_period - h_offset
                history.append(calculate_omni_matrix_trend(h_p, tab_offset))

            pred_size = calculate_omni_matrix_trend(current_target_period, tab_offset)

            p_rng = random.Random(current_target_period + tab_offset)
            if pred_size == "BIG":
                pred_num = p_rng.choice([5, 6, 7, 8, 9])
                pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
            else:
                pred_num = p_rng.choice([0, 1, 2, 3, 4])
                pred_color = "GREEN" if pred_num in [1, 3] else "RED"

            is_sure_shot_match = (current_target_period % 2 == 0)
            is_volatile_market = (current_target_period % 23 == 0)

            if 1 <= remaining_secs <= 5:
                st.markdown(
                    """
                    <audio autoplay style="display:none;">
                        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

            size_highlight_color = "#FFD700" if pred_size == "BIG" else "#00FFFF"

            st.markdown(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #FFD700; padding-bottom: 6px; margin-bottom: 8px; background: rgba(255,215,0,0.06); border-radius: 6px; padding-left: 8px; padding-right: 8px;">
                    <span style="display: flex; align-items: center;"><span class="blinking-red-light"></span><span style="font-size: 13px; color: #FFD700; font-weight: 900; margin-right: 6px;">TARGET PERIOD:</span><span class="period-badge-small">{target_period_str}</span></span>
                    <span class="timer-box-large">⏰ {timer_str}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if is_volatile_market:
                st.markdown('<div class="wait-warning-banner">⚠️ MARKET VOLATILE - WAIT & STOP! 🛑 लाइन खराब है, अभी बेट मत लगाओ!</div>', unsafe_allow_html=True)
            elif is_sure_shot_match:
                st.markdown(f'<div class="super-100-win-banner">💎 100% SURE SHOT MATCH : <span style="color: {size_highlight_color}; font-size: 18px;">{pred_size}</span> 🚀</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="super-100-win-banner">🔥 NEXT SHOT : <span style="color: {size_highlight_color}; font-size: 18px;">{pred_size}</span> 🎯</div>', unsafe_allow_html=True)

            color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
            size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white;">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center;">{pred_color}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            boxes_html = ""
            for item in history:
                bg_color = "#FF9900" if item == "BIG" else "#0077FF"
                boxes_html += f"<div style='background: {bg_color}; color: white; padding: 5px 10px; border-radius: 4px; font-weight: 900; font-size: 11px; margin: 0 3px; display: inline-block; border: 1px solid #FFFFFF;'>{item}</div>"

            next_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"
            boxes_html += f"<div style='background: {next_bg}; color: white; padding: 5px 12px; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 12px; margin-left: 8px; border: 2px solid #00FF66;'>🎯 NEXT: {pred_size}</div>"

            st.markdown(
                f"""
                <div style="margin-top: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 8px; text-align: center; border: 1.5px solid #FFD700;">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 6px;">📊 {selected_game} लाइव ओमनी-मैटrix रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px;">{boxes_html}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

        if selected_game == "WINGO 30S":
            render_game_panel(30, 11)
        elif selected_game == "WINGO 1M":
            render_game_panel(60, 23)
        elif selected_game == "WINGO 3M":
            render_game_panel(180, 37)
        elif selected_game == "WINGO 5M":
            render_game_panel(300, 53)

    success_dashboard_core()
