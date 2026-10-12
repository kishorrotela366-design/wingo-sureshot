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
    @keyframes super-win-glow-small {
        0% { border-color: #00CCFF; box-shadow: 0 0 25px #00CCFF, inset 0 0 10px #00CCFF; background: #000000; }
        50% { border-color: #0055FF; box-shadow: 0 0 15px #0055FF, inset 0 0 5px #0055FF; background: #000000; }
        100% { border-color: #00CCFF; box-shadow: 0 0 25px #00CCFF, inset 0 0 10px #00CCFF; background: #000000; }
    }
    @keyframes super-win-glow-big {
        0% { border-color: #FF9900; box-shadow: 0 0 25px #FF9900, inset 0 0 10px #FF9900; background: #000000; }
        50% { border-color: #FF5500; box-shadow: 0 0 15px #FF5500, inset 0 0 5px #FF5500; background: #000000; }
        100% { border-color: #FF9900; box-shadow: 0 0 25px #FF9900, inset 0 0 10px #FF9900; background: #000000; }
    }
    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }
    .blinking-red-light { display: inline-block; width: 12px; height: 12px; background-color: #FF0055; border-radius: 50%; margin-right: 6px; animation: blink-animation 0.8s infinite ease-in-out; }
    
    /* --- यहाँ WINGO 30S, 1M आदि के टेक्स्ट को चमकीला रंग दिया गया है ताकि वे साफ दिखें --- */
    div.row-widget.stRadio > div {
        flex-direction: row;
        align-items: center;
        gap: 12px;
        background: rgba(20, 20, 20, 0.8);
        padding: 8px;
        border-radius: 8px;
        border: 1px solid #333333;
    }
    div.row-widget.stRadio label {
        color: #00FFFF !important;
        font-weight: 900 !important;
        font-size: 13px !important;
        text-shadow: 0 0 8px rgba(0, 255, 255, 0.6);
    }
    div.row-widget.stRadio div[data-baseweb="radio"] label:nth-child(1) { color: #00FFFF !important; }
    div.row-widget.stRadio div[data-baseweb="radio"] label:nth-child(2) { color: #FF00FF !important; }
    div.row-widget.stRadio div[data-baseweb="radio"] label:nth-child(3) { color: #FFD700 !important; }
    div.row-widget.stRadio div[data-baseweb="radio"] label:nth-child(4) { color: #00FF66 !important; }

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

    .main-card { background-color: #000000; border: none; padding: 0px; margin-top: 4px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); display: flex; align-items: center; gap: 6px; }
    
    .super-banner-small { border: 3px solid #00CCFF; padding: 12px; border-radius: 10px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #00CCFF; text-transform: uppercase; animation: super-win-glow-small 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(0,204,255,0.4); }
    .super-banner-big { border: 3px solid #FF9900; padding: 12px; border-radius: 10px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #FF9900; text-transform: uppercase; animation: super-win-glow-big 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(255,153,0,0.4); }
    .wait-warning-banner { border: 3px solid #FF0000; padding: 12px; border-radius: 10px; text-align: center; font-size: 13px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(255,0,0,0.4); }
    
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: #0b071a; border: 2px solid #5533aa; border-radius: 12px; padding: 12px 6px; box-shadow: 0 0 10px rgba(85,51,170,0.3); }
    .auth-card { background: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 16px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 10px; }
    .admin-card { background: #110022; border: 2px solid #00FF66; border-radius: 12px; padding: 15px; margin-bottom: 15px; }
    </style>
""",
    unsafe_allow_html=True,
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "is_owner" not in st.session_state:
    st.session_state.is_owner = False

if "utr_requests" not in st.session_state:
    st.session_state.utr_requests = {}

if "used_utrs_list" not in st.session_state:
    st.session_state.used_utrs_list = []

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# ==========================================
# 🔒 ओनर और यूज़र लॉगिन / UTR सुरक्षा पोर्टल
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 21px; font-weight: 900;'>👑 BDG DUAL SHIELD SECURE PORTAL</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.markdown("<h4 style='color: #00FFFF; text-align: center; font-weight: 900; font-size: 14px;'>रजिस्टर्ड मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>", unsafe_allow_html=True)
    
    login_mob = st.text_input("📱 मोबाइल नंबर", placeholder="Enter mobile number", key="login_mob_input")
    login_pass = st.text_input("🔒 पासवर्ड", type="password", placeholder="Enter password", key="login_pass_input")

    if st.button("🚀 UNLOCK PANEL (LOGIN)", use_container_width=True, key="login_btn"):
        clean_l_mob = "".join(filter(str.isdigit, login_mob))
        
        if clean_l_mob == MASTER_MOBILE and login_pass == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.session_state.is_owner = True
            st.success("👑 ओनर एक्सेस सफल! कंट्रोल पैनल खुल रहा है...")
            time.sleep(0.8)
            st.rerun()
        
        elif clean_l_mob in st.session_state.utr_requests:
            user_data = st.session_state.utr_requests[clean_l_mob]
            if user_data["password"] == login_pass:
                if datetime.now() < user_data["expiry"]:
                    if user_data["status"] == "APPROVED":
                        st.session_state.authenticated = True
                        st.session_state.is_owner = False
                        st.success("🟢 verified: आपका प्लान सक्रिय है, डैशबोर्ड खुल रहा है...")
                        time.sleep(0.8)
                        st.rerun()
                    elif user_data["status"] == "REJECTED":
                        st.error("🔴 रिजेक्टेड: आपका UTR ओनर द्वारा रिजेक्ट कर दिया गया है!")
                    else:
                        st.warning("🔴 पेंडिंग: आपका UTR अभी ओनर द्वारा अप्रूव नहीं हुआ है!")
                else:
                    st.error("🚨 समय समाप्त: आपके 2 दिन (48 घंटे) का प्लान खत्म हो चुका है! कृपया नीचे नया ₹1500 का भुगतान करके नया UTR दर्ज करें।")
            else:
                st.error("❌ गलत पासवर्ड! कृपया सही पासवर्ड दर्ज करें।")
        else:
            st.error("❌ यह मोबाइल नंबर रजिस्टर्ड नहीं है! कृपया नीचे नया UTR दर्ज करें।")

    st.markdown("---")
    
    st.markdown("<h3 style='color: #FFD700; font-weight: 900; text-align: center; font-size: 15px; margin-bottom: 5px;'>⚡ 1500 ₹ QR स्कैन और नया UTR दर्ज करें</h3>", unsafe_allow_html=True)
    
    renew_mob = st.text_input("📱 रजिस्टर्ड मोबाइल नंबर", placeholder="Enter mobile", key="renew_mob_input")
    renew_pass = st.text_input("🔒 पासवर्ड", type="password", placeholder="Enter password", key="renew_pass_input")

    st.markdown("""
        <div style='background: linear-gradient(135deg, #113300, #001a00); border: 2px solid #00FF66; padding: 12px; border-radius: 10px; margin: 10px 0; text-align: center;'>
            <p style='color: #00FF66; font-size: 14px; font-weight: 900; margin: 0;'>💎 2 दिन समाप्त होने पर ₹1500 का भुगतान करके नया UTR डालें</p>
            <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करें:</p>
            <div style='background: #FFFFFF; padding: 10px; display: inline-block; border-radius: 8px; margin-top: 6px; box-shadow: 0 0 15px rgba(0,255,102,0.4);'>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=1500" width="160" height="160">
            </div>
            <p style='color: #FFD700; font-size: 12px; margin-top: 6px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
        </div>
    """, unsafe_allow_html=True)
    
    renew_utr_input = st.text_input("📝 नया 12-Digit UTR Number", placeholder="Enter new 12-digit UTR", max_chars=12, key="renew_utr_input")

    if st.button("🔄 नया UTR सबमिट करें (RENEW REQUEST)", use_container_width=True, key="user_renew_btn"):
        clean_r_mob = "".join(filter(str.isdigit, renew_mob))
        clean_utr = "".join(filter(str.isdigit, renew_utr_input))

        if len(clean_r_mob) < 10:
            st.error("⚠️ कृपया सही 10 अंकों का मोबाइल नंबर दर्ज करें!")
        elif not renew_pass:
            st.error("⚠️ कृपया अपना पासवर्ड दर्ज करें!")
        elif len(clean_utr) != 12:
            st.error("⚠️ अमान्य UTR! कृपया 12 अंकों का सही UTR नंबर डालें।")
        elif clean_utr in st.session_state.used_utrs_list:
            st.error("🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका है! कृपया कोई नया UTR नंबर डालें।")
        else:
            st.session_state.utr_requests[clean_r_mob] = {
                "utr": clean_utr,
                "password": renew_pass,
                "status": "PENDING",
                "expiry": datetime.now() + timedelta(days=2),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            st.success("📩 नया UTR सफलतापूर्वक सबमिट हो गया है! 🔴 (पेंडिंग)। ओनर द्वारा वेरीफाई और अप्रूव होने के बाद आपका पैनल चालू होगा।")

    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 📊 डैशबोर्ड और ओनर कंट्रोल पैनल
# ==========================================
else:
    if st.session_state.is_owner:
        st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #FFD700; text-align: center; margin: 0;'>👑 OWNER / ADMIN APPROVAL PANEL</h3>", unsafe_allow_html=True)
        st.markdown("<p style='color: #00FFFF; text-align: center; font-size: 12px;'>यहाँ यूज़र का नया UTR चेक करें और Approve (हरा टिक) दें:</p>", unsafe_allow_html=True)
        
        if not st.session_state.utr_requests:
            st.info("अभी तक कोई UTR रिक्वेस्ट नहीं आई है।")
        else:
            for mob, req in list(st.session_state.utr_requests.items()):
                status_icon = "🟢 (रिचार्ज स्वीकृत - ग्रीन टिक)" if req["status"] == "APPROVED" else "🔴 (रिचार्ज पेंडिंग)"
                border_color = "#00FF66" if req["status"] == "APPROVED" else "#FF0000"
                
                st.markdown(f"""
                    <div style='border: 1.5px solid {border_color}; padding: 10px; border-radius: 8px; margin-bottom: 8px; background: #000000;'>
                        <p style='margin:0; font-weight:900; color:#FFFFFF;'>📱 मोबाइल: <span style='color:#00FFFF;'>{mob}</span> | {status_icon}</p>
                        <p style='margin:0; font-size:12px; color:#FFD700;'>📝 UTR No: {req['utr']} | ⏰ समय: {req['time']}</p>
                    </div>
                """, unsafe_allow_html=True)
                
                col_app, col_rej = st.columns(2)
                with col_app:
                    if st.button(f"✅ Approve (हरा टिक दें)", key=f"app_{mob}"):
                        if req['utr'] not in st.session_state.used_utrs_list:
                            st.session_state.used_utrs_list.append(req['utr'])
                        
                        st.session_state.utr_requests[mob]["status"] = "APPROVED"
                        st.session_state.utr_requests[mob]["expiry"] = datetime.now() + timedelta(days=2)
                        st.success(f"यूज़र {mob} को अप्रूव कर दिया गया है! 2 दिन का समय शुरू हो गया है।")
                        time.sleep(0.5)
                        st.rerun()
                with col_rej:
                    if st.button(f"❌ Reject (लाल चिन्ह)", key=f"rej_{mob}"):
                        st.session_state.utr_requests[mob]["status"] = "REJECTED"
                        st.error(f"यूज़र {mob} का UTR रिजेक्ट कर दिया गया।")
                        time.sleep(0.5)
                        st.rerun()
                        
        st.markdown("</div>", unsafe_allow_html=True)

    # --- गेमिंग प्रेडिक्शन डैशबोर्ड ---
    @st.fragment(run_every=1)
    def success_dashboard_core():
        current_time_epoch = int(time.time())
        random.seed(current_time_epoch // 90)
        dynamic_online_count = random.randint(340000, 370000)
        random.seed()

        selected_game = st.radio(
            "Select Game Mode",
            ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed",
            key="main_radio_mode"
        )
        
        current_game = selected_game
        now = datetime.now()
        
        st.markdown('<div class="master-single-box">', unsafe_allow_html=True)
        col_l, col_m, col_r = st.columns([1.1, 1.2, 1.1])
        
        with col_l:
            st.markdown('<div style="color: #00FFFF; font-size: 11px; font-weight: 900; white-space: nowrap; display: flex; align-items: center;"><span class="blinking-red-light"></span>⚡ BDG SNIPER PANEL</div>', unsafe_allow_html=True)
        with col_m:
            manual_period_input = st.text_input("Period Input", value="51251", max_chars=6, key="user_live_period_input_main", label_visibility="collapsed")
        with col_r:
            st.markdown(f'<div style="color: #00FF66; font-size: 11px; font-weight: 900; white-space: nowrap; display: flex; align-items: center; justify-content: flex-end;"><span class="blinking-red-light"></span>👥 {dynamic_online_count:,}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        def render_game_panel(seconds, tab_offset, mode_name):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds
            clean_input = "".join(filter(str.isdigit, manual_period_input)) or "51251"

            state_input_key = f"matrix_input_{seconds}"
            state_block_key = f"matrix_block_{seconds}"

            if state_input_key not in st.session_state or st.session_state[state_input_key] != clean_input:
                st.session_state[state_input_key] = clean_input
                st.session_state[state_block_key] = current_block_index

            block_diff = current_block_index - st.session_state.get(state_block_key, current_block_index)
            base_val = int(clean_input)
            target_period_str = str(base_val + block_diff)

            def calculate_ultra_syndicate_trend(p_num, offset_val):
                server_sum = sum([(p_num * i + offset_val) % 5 for i in range(1, 12)])
                zigzag_toggle = p_num % 2
                pattern_mod = (p_num ^ offset_val + server_sum + zigzag_toggle) % 8
                return "SMALL" if pattern_mod in [0, 1, 3] else "BIG"

            history = [calculate_ultra_syndicate_trend(int(target_period_str) - h, tab_offset) for h in range(5, 0, -1)]
            pred_size = calculate_ultra_syndicate_trend(int(target_period_str), tab_offset)

            p_rng = random.Random(int(target_period_str) + tab_offset)
            if pred_size == "BIG":
                pred_num = p_rng.choice([5, 6, 7, 8, 9])
                pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
            else:
                pred_num = p_rng.choice([0, 1, 2, 3, 4])
                pred_color = "GREEN" if pred_num in [1, 3] else "RED"

            is_bad_market = (int(target_period_str) % 17 == 0) or (int(target_period_str) % 7 == 3)

            st.markdown(f"""
                <div class="target-period-box">
                    <div style="display: flex; align-items: center;">
                        <span class="blinking-red-light"></span>
                        <span style="color: #FFD700; font-size: 13px; font-weight: 900; margin-right: 6px;">TARGET PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 15px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div class="timer-box-large">⏰ {timer_str}</div>
                </div>
            """, unsafe_allow_html=True)

            if is_bad_market:
                st.markdown('<div class="wait-warning-banner">🛑 STOP / WAITING: लाइन खराब है, 11 सर्वर्स से मैच नहीं हो रहा! ⚠️</div>', unsafe_allow_html=True)
            else:
                banner_class = "super-banner-small" if pred_size == "SMALL" else "super-banner-big"
                banner_color = "#00CCFF" if pred_size == "SMALL" else "#FF9900"
                st.markdown(f'<div class="{banner_class}">💎 100% SURE SHOT MATCH : <span style="color: {banner_color}; font-size: 18px;">{pred_size}</span> 🚀</div>', unsafe_allow_html=True)

            color_bg = "#FF4444" if pred_color == "RED" else "#00AA55"
            size_bg = "linear-gradient(135deg, #00CCFF, #0044FF)" if pred_size == "SMALL" else "linear-gradient(135deg, #FF9900, #FF5500)"

            st.markdown(f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white;">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 8px; font-weight: 900; font-size: 13px; text-align: center;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 8px; font-weight: 900; font-size: 13px; text-align: center;">{pred_color}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            boxes_html = "".join([f"<div style='background: {'#0077FF' if item == 'SMALL' else '#FF9900'}; color: white; padding: 6px 12px; border-radius: 6px; font-weight: 900; font-size: 12px; margin: 0 3px; display: inline-block;'>{item}</div>" for item in history])
            st.markdown(f"""
                <div style="margin-top: 10px; background: #000000; padding: 12px; border-radius: 12px; text-align: center; border: 1.5px solid #FFD700;">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 8px;">📊 {current_game} 11-सर्वर सिंडिकेट रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px; margin-bottom: 10px;">{boxes_html}</div>
                    <div style="display: inline-block; background: {size_bg}; color: white; padding: 8px 20px; border-radius: 20px; font-weight: 900; font-size: 13px; border: 2px solid #00FF66;">🎯 NEXT: {pred_size}</div>
                </div>
            """, unsafe_allow_html=True)
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
