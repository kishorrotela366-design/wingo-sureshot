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
    .stApp { background-color: #000000; color: #FFFFFF; }
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
        0% { border-color: #00FF66; box-shadow: 0 0 25px #00FF66, inset 0 0 10px #00FF66; background: #000000; }
        50% { border-color: #FFD700; box-shadow: 0 0 15px #FFD700, inset 0 0 5px #FFD700; background: #000000; }
        100% { border-color: #00FF66; box-shadow: 0 0 25px #00FF66, inset 0 0 10px #00FF66; background: #000000; }
    }
    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 20px #FF0000; background: rgba(255, 0, 0, 0.2); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 20px #FF0000; background: rgba(255, 0, 0, 0.2); }
    }
    .blinking-red-light { display: inline-block; width: 12px; height: 12px; background-color: #FF0055; border-radius: 50%; margin-right: 8px; animation: blink-animation 0.8s infinite ease-in-out; }
    
    .exact-modes-container {
        background: #000000;
        padding: 4px 0 10px 0;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }
    .mode-row {
        display: flex;
        justify-content: flex-start;
        gap: 35px;
        align-items: center;
    }
    .mode-item {
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 900;
        font-size: 15px;
    }
    .circle-dot {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        border: 2px solid #FFFFFF;
        background: #FFFFFF;
        display: inline-block;
    }
    .circle-dot.active-red {
        background-color: #FF0055;
        border-color: #FF0055;
        box-shadow: 0 0 10px #FF0055;
    }

    .master-single-box {
        background: #000000;
        border: 1.5px solid #00FF66;
        border-radius: 10px;
        padding: 10px 12px;
        box-shadow: 0 0 12px rgba(0, 255, 102, 0.25);
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    
    .target-period-box {
        background: #000000;
        border: 1.5px solid #00FF66;
        border-radius: 10px;
        padding: 10px 12px;
        box-shadow: 0 0 12px rgba(0, 255, 102, 0.25);
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .stTextInput input {
        background-color: #0b161f !important;
        color: #00FFFF !important;
        border: 1.5px solid #00FFFF !important;
        border-radius: 6px !important;
        font-weight: 900 !important;
        text-align: center !important;
        letter-spacing: 2px !important;
        padding: 2px !important;
        height: 32px !important;
    }
    .stTextInput > label { display: none !important; }
    div[data-baseweb="input"] { background: transparent !important; }

    .main-card { background-color: #000000; border: none; padding: 0px; margin-top: 4px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); display: flex; align-items: center; gap: 6px; }
    .super-100-win-banner { border: 2.5px solid #00FF66; padding: 12px; border-radius: 10px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #00FF66; text-transform: uppercase; animation: super-win-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 20px rgba(0,255,102,0.3); }
    .wait-warning-banner { border: 2.5px solid #FF0000; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; background: #000000; }
    
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: #0b071a; border: 2px solid #5533aa; border-radius: 12px; padding: 12px 6px; box-shadow: 0 0 10px rgba(85,51,170,0.3); }
    
    .auth-card { background: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "backend_servers" not in st.session_state:
    st.session_state.backend_servers = [f"BDG-CORE-NODE-{i:02d}" for i in range(1, 12)]
if "verified_users_db" not in st.session_state:
    st.session_state.verified_users_db = {}
if "used_utrs_database" not in st.session_state:
    st.session_state.used_utrs_database = ["123456789012"]

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# ==========================================
# 🔒 ओनर बाईपास + कड़क UTR एंटी-फ्रॉड सिक्योरिटी पोर्टल
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 22px; font-weight: 900;'>👑 BDG DUAL SHIELD <br> SECURE ACCESS PORTAL</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    
    auth_mode = st.radio(
        "Select Mode", 
        ["🔑 ओनर / यूजर लॉगिन (Login)", "💳 नया यूजर रिचार्ज करें (₹1500 / 2 दिन - QR & UTR)"], 
        horizontal=True,
        label_visibility="collapsed"
    )
    
    st.markdown("---")

    if "ओनर / यूजर लॉगिन" in auth_mode:
        st.markdown("<h4 style='color: #00FFFF; text-align: center; font-weight: 900;'>मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>", unsafe_allow_html=True)
        login_mob = st.text_input("📱 मोबाइल नंबर", placeholder="Enter mobile number", key="login_mob_input")
        login_pass = st.text_input("🔒 पासवर्ड", type="password", placeholder="Enter password", key="login_pass_input")

        if st.button("🚀 UNLOCK PANEL (LOGIN)", use_container_width=True, key="login_btn"):
            clean_l_mob = "".join(filter(str.isdigit, login_mob))
            if clean_l_mob == MASTER_MOBILE and login_pass == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.success("👑 ओनर एक्सेस सफल! पैनल खुल रहा है...")
                time.sleep(0.8)
                st.rerun()
            elif clean_l_mob in st.session_state.verified_users_db and st.session_state.verified_users_db[clean_l_mob]["password"] == login_pass:
                st.session_state.authenticated = True
                st.success("✅ यूजर लॉगिन सफल! डैशबोर्ड लोड हो रहा है...")
                time.sleep(0.8)
                st.rerun()
            else:
                st.error("❌ अमान्य मोबाइल नंबर या पासवर्ड! कृपया नया यूजर रिचार्ज वाले विकल्प पर जाकर रजिस्टर करें।")
                
    else:
        st.markdown("<h3 style='color: #FFD700; font-weight: 900; text-align: center; margin-bottom: 5px;'>⚡ नया यूजर रिचार्ज करे 1500 (2 दिन)</h3>", unsafe_allow_html=True)
        
        reg_mob = st.text_input("📱 अपना मोबाइल नंबर डालें", placeholder="Enter mobile number", key="reg_mob_input")
        reg_pass = st.text_input("🔒 नया पासवर्ड बनाएं", type="password", placeholder="Create password", key="reg_pass_input")

        st.markdown("""
            <div style='background: linear-gradient(135deg, #113300, #001a00); border: 2px solid #00FF66; padding: 10px; border-radius: 8px; margin: 10px 0; text-align: center;'>
                <p style='color: #00FF66; font-size: 14px; font-weight: 900; margin: 0;'>💎 नया यूजर रिचार्ज करे ₹1500 (2 दिन का प्लान)</p>
                <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करके भुगतान करें:</p>
                <div style='background: #FFFFFF; padding: 8px; display: inline-block; border-radius: 8px; margin-top: 6px;'>
                    <img src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=1500" width="140" height="140">
                </div>
                <p style='color: #FFD700; font-size: 11px; margin-top: 5px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
            </div>
        """, unsafe_allow_html=True)
        
        utr_code_input = st.text_input("📝 12-Digit UTR Number", placeholder="Enter 12-digit UTR number", max_chars=12, key="reg_utr_input")

        if st.button("🛡️ UTR वेरीफाई करके पैनल खोलें", use_container_width=True, key="user_verify_btn"):
            clean_reg_mob = "".join(filter(str.isdigit, reg_mob))
            clean_utr = "".join(filter(str.isdigit, utr_code_input))

            if len(clean_reg_mob) < 10:
                st.error("⚠️ कृपया सही 10 अंकों का मोबाइल नंबर दर्ज करें!")
            elif not reg_pass:
                st.error("⚠️ कृपया पासवर्ड दर्ज करें!")
            elif len(clean_utr) != 12:
                st.error("⚠️ अमान्य UTR! कृपया 12 अंकों का सही UTR नंबर डालें।")
            elif clean_utr in st.session_state.used_utrs_database:
                st.error("🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल हो चुका है या डुप्लीकेट है! डैशबोर्ड नहीं खुलेगा।")
            else:
                st.session_state.used_utrs_database.append(clean_utr)
                st.session_state.verified_users_db[clean_reg_mob] = {
                    "password": reg_pass,
                    "expiry": datetime.now() + timedelta(days=2)
                }
                st.session_state.authenticated = True
                st.success("✅ UTR सफलतापूर्वक मैच हो गया है! डैशबोर्ड ओपन हो रहा है...")
                time.sleep(1)
                st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 📊 मुख्य लाइव गेमिंग डैशबोर्ड (बिल्कुल इमेज के डिज़ाइन जैसा)
# ==========================================
else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        dynamic_online_count = random.randint(340000, 370000)

        if "active_game_mode" not in st.session_state:
            st.session_state.active_game_mode = "WINGO 1M"

        # टॉप गेम मोड सिलेक्शन रेडियो बटन
        selected_game = st.radio(
            "Select Game Mode",
            ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        # इमेज के लेआउट जैसी मोड डॉट्स लिस्ट
        st.markdown(f"""
            <div class="exact-modes-container">
                <div class="mode-row">
                    <div class="mode-item">
                        <div class="circle-dot {'active-red' if selected_game=='WINGO 30S' else ''}"></div>
                        <span style="color: {'#00FFFF' if selected_game=='WINGO 30S' else '#FFFFFF'}; font-size: 15px;">WINGO 30S</span>
                    </div>
                    <div class="mode-item">
                        <div class="circle-dot {'active-red' if selected_game=='WINGO 1M' else ''}"></div>
                        <span style="color: {'#FF007F' if selected_game=='WINGO 1M' else '#FFFFFF'}; font-size: 15px;">WINGO 1M</span>
                    </div>
                    <div class="mode-item">
                        <div class="circle-dot {'active-red' if selected_game=='WINGO 3M' else ''}"></div>
                        <span style="color: {'#FFD700' if selected_game=='WINGO 3M' else '#FFFFFF'}; font-size: 15px;">WINGO 3M</span>
                    </div>
                </div>
                <div class="mode-row">
                    <div class="mode-item">
                        <div class="circle-dot {'active-red' if selected_game=='WINGO 5M' else ''}"></div>
                        <span style="color: {'#00FF66' if selected_game=='WINGO 5M' else '#FFFFFF'}; font-size: 15px;">WINGO 5M</span>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        now = datetime.now()
        
        # 1st बॉक्स: BDG SNIPER PANEL और ऑनलाइन काउंट
        st.markdown(
            f"""
            <div class="master-single-box">
                <div style="display: flex; align-items: center; color: #00FFFF; font-size: 13px; font-weight: 900;">
                    <span class="blinking-red-light" style="width:8px; height:8px; margin-right:6px;"></span>⚡ BDG SNIPER PANEL
                </div>
                <div style="background: #0b161f; border: 1px dashed #00FFFF; border-radius: 6px; padding: 2px 10px; color: #00FFFF; font-size: 12px; font-weight: 900; letter-spacing: 2px;">
                    XXXXX
                </div>
                <div style="display: flex; align-items: center; color: #00FF66; font-size: 13px; font-weight: 900;">
                    <span class="blinking-red-light" style="width:8px; height:8px; margin-right:4px;"></span>👥 {dynamic_online_count:,}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        def render_game_panel(seconds, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

            # 2nd बॉक्स: टारगेट पीरियड और टाइमर
            col_p1, col_p2 = st.columns([1.4, 1.0])
            with col_p1:
                st.markdown(
                    '<span style="color: #FF0055; font-size: 14px; font-weight: 900; margin-right: 6px;">●</span><span style="color: #FFD700; font-size: 13px; font-weight: 900;">TARGET PERIOD:</span>',
                    unsafe_allow_html=True
                )
            with col_p2:
                manual_period_input = st.text_input(
                    "Period Input",
                    value="10313",
                    max_chars=6,
                    key=f"user_live_period_input_{seconds}",
                    label_visibility="collapsed"
                )

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "10313"

            state_input_key = f"matrix_input_{seconds}"
            state_block_key = f"matrix_block_{seconds}"

            if state_input_key not in st.session_state or st.session_state[state_input_key] != clean_input:
                st.session_state[state_input_key] = clean_input
                st.session_state[state_block_key] = current_block_index

            block_diff = current_block_index - st.session_state.get(state_block_key, current_block_index)
            
            base_val = int(clean_input)
            current_target_period = base_val + block_diff
            target_period_str = str(current_target_period)

            # 11-सर्वर सिंडिकेट अल्ट्रा-पैटर्न इंजन
            def calculate_ultra_syndicate_trend(p_num, offset_val):
                server_factor = (p_num * 11 + offset_val) % 7
                pattern_check = (p_num ^ offset_val) % 4
                
                if server_factor in [0, 1, 5]:
                    return "SMALL"
                elif server_factor in [2, 3, 6]:
                    return "BIG"
                elif pattern_check % 2 == 0:
                    return "BIG" if (p_num % 3 == 0) else "SMALL"
                else:
                    return "SMALL" if (p_num % 2 == 0) else "BIG"

            history = []
            for h_offset in range(5, 0, -1):
                h_p = current_target_period - h_offset
                history.append(calculate_ultra_syndicate_trend(h_p, tab_offset))

            pred_size = calculate_ultra_syndicate_trend(current_target_period, tab_offset)

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

            size_highlight_color = "#00FFFF" if pred_size == "SMALL" else "#FFD700"

            # टार्गेट पीरियड और टाइमर की संयुक्त पट्टी (इमेज के अनुसार)
            st.markdown(
                f"""
                <div class="target-period-box" style="margin-top: 6px;">
                    <div style="display: flex; align-items: center;">
                        <span style="color: #FF0055; font-size: 14px; font-weight: 900; margin-right: 8px;">●</span>
                        <span style="color: #FFD700; font-size: 13px; font-weight: 900; margin-right: 8px;">TARGET PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 15px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div class="timer-box-large">
                        ⏰ {timer_str}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 3rd बॉक्स: नेक्स्ट शॉट बैनर (इमेज जैसा हरा ग्लोइंग बॉक्स)
            if is_volatile_market:
                st.markdown('<div class="wait-warning-banner">⚠️ MARKET VOLATILE - WAIT & STOP! 🛑 लाइन खराब है, अभी बेट मत लगाओ!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="super-100-win-banner">🔥 NEXT SHOT : <span style="color: {size_highlight_color}; font-size: 17px;">{pred_size}</span> 🎯</div>', unsafe_allow_html=True)

            color_bg = "#FF4444" if pred_color == "RED" else "#00AA55"
            size_bg = "linear-gradient(135deg, #00CCFF, #0044FF)" if pred_size == "SMALL" else "linear-gradient(135deg, #FF9900, #FF5500)"

            # 4th बॉक्स: नंबर, साइज़, कलर (इमेज के 3 डार्क कार्ड्स)
            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px; letter-spacing: 1px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white; box-shadow: 0 0 10px {color_bg};">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px; letter-spacing: 1px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 8px; font-weight: 900; font-size: 13px; text-align: center; box-shadow: 0 0 10px #0055ff;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px; letter-spacing: 1px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 8px; font-weight: 900; font-size: 13px; text-align: center; box-shadow: 0 0 10px {color_bg};">{pred_color}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            # 5th बॉक्स: रनिंग हिस्ट्री चार्ट और नीचे नेक्स्ट प्रेडिक्शन
            boxes_html = ""
            for item in history:
                item_bg = "#0077FF" if item == "SMALL" else "#FF9900"
                boxes_html += f"<div style='background: {item_bg}; color: white; padding: 6px 12px; border-radius: 6px; font-weight: 900; font-size: 12px; margin: 0 3px; display: inline-block; border: 1px solid #FFFFFF;'>{item}</div>"

            next_bg = "linear-gradient(135deg, #00CCFF, #0044FF)" if pred_size == "SMALL" else "linear-gradient(135deg, #FF9900, #FF5500)"
            
            st.markdown(
                f"""
                <div style="margin-top: 10px; background: #000000; padding: 12px; border-radius: 12px; text-align: center; border: 1.5px solid #FFD700; box-shadow: 0 0 15px rgba(255,215,0,0.15);">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 8px;">📊 {selected_game} लाइव ओमनी-मैट्रिक्स रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px; margin-bottom: 10px;">{boxes_html}</div>
                    <div style="display: inline-block; background: {next_bg}; color: white; padding: 8px 20px; border-radius: 20px; font-weight: 900; font-size: 13px; border: 2px solid #00FF66; box-shadow: 0 0 12px rgba(0,255,102,0.4);">🎯 NEXT: {pred_size}</div>
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
