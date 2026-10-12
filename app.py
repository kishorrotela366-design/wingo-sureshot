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
    @keyframes super-win-glow {
        0% { border-color: #00FF66; box-shadow: 0 0 25px #00FF66, inset 0 0 10px #00FF66; background: #000000; }
        50% { border-color: #FFD700; box-shadow: 0 0 15px #FFD700, inset 0 0 5px #FFD700; background: #000000; }
        100% { border-color: #00FF66; box-shadow: 0 0 25px #00FF66, inset 0 0 10px #00FF66; background: #000000; }
    }
    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }
    .blinking-red-light { display: inline-block; width: 12px; height: 12px; background-color: #FF0055; border-radius: 50%; margin-right: 6px; animation: blink-animation 0.8s infinite ease-in-out; }
    
    .master-single-box {
        background: #000000;
        border: 1.5px solid #00FF66;
        border-radius: 10px;
        padding: 8px 10px;
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
        border: 1.5px dashed #00FFFF !important;
        border-radius: 6px !important;
        font-weight: 900 !important;
        text-align: center !important;
        letter-spacing: 2px !important;
        padding: 2px !important;
        height: 30px !important;
    }
    .stTextInput > label { display: none !important; }
    div[data-baseweb="input"] { background: transparent !important; }

    .main-card { background-color: #000000; border: none; padding: 0px; margin-top: 4px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); display: flex; align-items: center; gap: 6px; }
    .super-100-win-banner { border: 3px solid #00FF66; padding: 12px; border-radius: 10px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #00FF66; text-transform: uppercase; animation: super-win-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(0,255,102,0.4); }
    .wait-warning-banner { border: 3px solid #FF0000; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(255,0,0,0.4); }
    
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: #0b071a; border: 2px solid #5533aa; border-radius: 12px; padding: 12px 6px; box-shadow: 0 0 10px rgba(85,51,170,0.3); }
    
    .auth-card { background: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 16px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 10px; }
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
# 🔒 ओनर और यूजर लॉगिन + UTR एंटी-फ्रॉड पोर्टल
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 21px; font-weight: 900;'>👑 BDG DUAL SHIELD SECURE PORTAL</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    
    st.markdown("<h4 style='color: #00FFFF; text-align: center; font-weight: 900; font-size: 14px;'>मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>", unsafe_allow_html=True)
    
    login_mob = st.text_input("📱 मोबाइल नंबर", placeholder="Enter mobile number", key="login_mob_input")
    login_pass = st.text_input("🔒 पासवर्ड", type="password", placeholder="Enter password", key="login_pass_input")

    if st.button("🚀 UNLOCK PANEL (LOGIN)", use_container_width=True, key="login_btn"):
        clean_l_mob = "".join(filter(str.isdigit, login_mob))
        
        if clean_l_mob == MASTER_MOBILE and login_pass == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.success("👑 ओनर एक्सेस सफल! पैनल खुल रहा है...")
            time.sleep(0.8)
            st.rerun()
        elif clean_l_mob in st.session_state.verified_users_db:
            user_data = st.session_state.verified_users_db[clean_l_mob]
            if user_data["password"] == login_pass:
                if datetime.now() < user_data["expiry"]:
                    st.session_state.authenticated = True
                    st.success("✅ यूजर लॉगिन सफल! आपका प्लान सक्रिय है, डैशबोर्ड खुल रहा है...")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error("⏰ आपके 2 दिन का रिचार्ज प्लान समाप्त हो चुका है! कृपया नीचे दिए गए QR से नया रिचार्ज करें।")
            else:
                st.error("❌ गलत पासवर्ड! कृपया सही पासवर्ड दर्ज करें।")
        else:
            st.error("❌ यह मोबाइल नंबर रजिस्टर्ड नहीं है या रिचार्ज समाप्त हो गया है! नीचे दिए गए QR से नया रिचार्ज करें।")

    st.markdown("---")
    
    st.markdown("<h3 style='color: #FFD700; font-weight: 900; text-align: center; font-size: 15px; margin-bottom: 5px;'>⚡ नया यूजर रिचार्ज करिए 1500 दो दिन के लिए</h3>", unsafe_allow_html=True)
    
    reg_mob = st.text_input("📱 नया मोबाइल नंबर", placeholder="Enter mobile number", key="reg_mob_input")
    reg_pass = st.text_input("🔒 नया पासवर्ड बनाएं", type="password", placeholder="Create password", key="reg_pass_input")

    st.markdown("""
        <div style='background: linear-gradient(135deg, #113300, #001a00); border: 2px solid #00FF66; padding: 12px; border-radius: 10px; margin: 10px 0; text-align: center;'>
            <p style='color: #00FF66; font-size: 14px; font-weight: 900; margin: 0;'>💎 नया यूजर रिचार्ज करिए 1500 दो दिन के लिए</p>
            <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करके भुगतान करें:</p>
            <div style='background: #FFFFFF; padding: 10px; display: inline-block; border-radius: 8px; margin-top: 6px; box-shadow: 0 0 15px rgba(0,255,102,0.4);'>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=1500" width="160" height="160">
            </div>
            <p style='color: #FFD700; font-size: 12px; margin-top: 6px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
        </div>
    """, unsafe_allow_html=True)
    
    utr_code_input = st.text_input("📝 12-Digit UTR Number", placeholder="Enter 12-digit UTR number", max_chars=12, key="reg_utr_input")

    if st.button("🔓 अनलॉक पैनल (UNLOCK PANEL)", use_container_width=True, key="user_verify_btn"):
        clean_reg_mob = "".join(filter(str.isdigit, reg_mob))
        clean_utr = "".join(filter(str.isdigit, utr_code_input))

        if len(clean_reg_mob) < 10:
            st.error("⚠️ कृपया सही 10 अंकों का मोबाइल नंबर दर्ज करें!")
        elif not reg_pass:
            st.error("⚠️ कृपया पासवर्ड बनाएं!")
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
            st.success("✅ UTR 100% सही मैच हो गया है! डैशबोर्ड अनलॉक हो रहा है...")
            time.sleep(1)
            st.rerun()
            
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 📊 मुख्य लाइव गेमिंग डैशबोर्ड (स्क्रीनशॉट के लेआउट जैसा)[span_3](start_span)[span_3](end_span)
# ==========================================
else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        dynamic_online_count = random.randint(340000, 370000)

        if "active_game_mode" not in st.session_state:
            st.session_state.active_game_mode = "WINGO 1M"

        # स्क्रीनशॉट[span_4](start_span)[span_4](end_span) जैसी साफ़ सुथरी रेडियो बटन सलेक्ट करने की प्रणाली
        selected_game = st.radio(
            "Select Game Mode",
            ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed",
            key="main_radio_mode"
        )
        
        current_game = selected_game

        now = datetime.now()
        
        # 1st बॉक्स: BDG SNIPER PANEL और बीच में पीरियड नंबर इनपुट खांचा[span_5](start_span)[span_5](end_span)
        st.markdown('<div class="master-single-box">', unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.2, 1.1, 1.1])
        
        with col_l:
            st.markdown(
                '<div style="color: #00FFFF; font-size: 11px; font-weight: 900; white-space: nowrap; display: flex; align-items: center;"><span class="blinking-red-light"></span>⚡ BDG SNIPER</div>',
                unsafe_allow_html=True
            )
        with col_m:
            manual_period_input = st.text_input(
                "Period Input",
                value="10313",
                max_chars=6,
                key="user_live_period_input_main",
                label_visibility="collapsed"
            )
        with col_r:
            st.markdown(
                f'<div style="color: #00FF66; font-size: 11px; font-weight: 900; white-space: nowrap; display: flex; align-items: center; justify-content: flex-end;"><span class="blinking-red-light"></span>👥 {dynamic_online_count:,}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

        def render_game_panel(seconds, tab_offset, mode_name):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

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

            def calculate_ultra_syndicate_trend(p_num, offset_val):
                server_sum = sum([(p_num * i + offset_val) % 5 for i in range(1, 12)])
                pattern_mod = (p_num ^ offset_val + server_sum) % 8
                
                if pattern_mod in [0, 1, 2]:
                    return "SMALL"
                elif pattern_mod in [3, 4, 5]:
                    return "BIG"
                elif p_num % 2 == 0:
                    return "BIG"
                else:
                    return "SMALL"

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

            is_volatile_market = (current_target_period % 19 == 0) or (current_target_period % 37 == 0)

            # 🔥 बैकएंड अलार्म साउंड (सिर्फ सक्रिय मोड में आखिरी 5 सेकंड पर)
            if current_game == mode_name and (1 <= remaining_secs <= 5):
                st.markdown(
                    """
                    <audio autoplay style="display:none;">
                        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

            size_highlight_color = "#00FFFF" if pred_size == "SMALL" else "#FFD700"

            # 2nd बॉक्स: टारगेट पीरियड और टाइमर की सिंगल पट्टी[span_6](start_span)[span_6](end_span)
            st.markdown(
                f"""
                <div class="target-period-box">
                    <div style="display: flex; align-items: center;">
                        <span class="blinking-red-light"></span>
                        <span style="color: #FFD700; font-size: 13px; font-weight: 900; margin-right: 6px;">TARGET PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 15px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div class="timer-box-large">
                        ⏰ {timer_str}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            if is_volatile_market:
                st.markdown('<div class="wait-warning-banner">⚠️ MARKET VOLATILE - WAIT & STOP! 🛑 लाइन खराब है, अभी बेट मत लगाओ!</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="super-100-win-banner">💎 100% SURE SHOT MATCH : <span style="color: {size_highlight_color}; font-size: 18px;">{pred_size}</span> 🚀</div>', unsafe_allow_html=True)

            color_bg = "#FF4444" if pred_color == "RED" else "#00AA55"
            size_bg = "linear-gradient(135deg, #00CCFF, #0044FF)" if pred_size == "SMALL" else "linear-gradient(135deg, #FF9900, #FF5500)"

            # 3rd बॉक्स: नंबर, साइज़, कलर[span_7](start_span)[span_7](end_span)
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
            
            boxes_html = ""
            for item in history:
                item_bg = "#0077FF" if item == "SMALL" else "#FF9900"
                boxes_html += f"<div style='background: {item_bg}; color: white; padding: 6px 12px; border-radius: 6px; font-weight: 900; font-size: 12px; margin: 0 3px; display: inline-block; border: 1px solid #FFFFFF;'>{item}</div>"

            next_bg = "linear-gradient(135deg, #00CCFF, #0044FF)" if pred_size == "SMALL" else "linear-gradient(135deg, #FF9900, #FF5500)"
            
            # 4th बॉक्स: रनिंग हिस्ट्री चार्ट[span_8](start_span)[span_8](end_span)
            st.markdown(
                f"""
                <div style="margin-top: 10px; background: #000000; padding: 12px; border-radius: 12px; text-align: center; border: 1.5px solid #FFD700; box-shadow: 0 0 15px rgba(255,215,0,0.15);">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 8px;">📊 {current_game} 11-सर्वर सिंडिकेट रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px; margin-bottom: 10px;">{boxes_html}</div>
                    <div style="display: inline-block; background: {next_bg}; color: white; padding: 8px 20px; border-radius: 20px; font-weight: 900; font-size: 13px; border: 2px solid #00FF66; box-shadow: 0 0 12px rgba(0,255,102,0.4);">🎯 NEXT: {pred_size}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

        if current_game == "WINGO 30S":
            render_game_panel(30, 11, "WINGO 30S")
        elif current_game == "WINGO 1M":
            render_game_panel(60, 23, "WINGO 1M")
        elif current_game == "WINGO 3M":
            render_game_panel(180, 37, "WINGO 3M")
        elif current_game == "WINGO 5M":
            render_game_panel(300, 53, "WINGO 5M")

    success_dashboard_core()
