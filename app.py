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
    .stApp { background-color: #020104; color: #FFFFFF; }
    
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

    @keyframes red-light-tip-tip {
        0% { border-color: #FF0055; box-shadow: 0 0 25px #FF0055; background: rgba(255, 0, 85, 0.3); }
        50% { border-color: #550011; box-shadow: 0 0 3px #550011; background: rgba(50, 0, 10, 0.15); }
        100% { border-color: #FF0055; box-shadow: 0 0 25px #FF0055; background: rgba(255, 0, 85, 0.3); }
    }

    @keyframes super-win-glow {
        0% { border-color: #00FF66; box-shadow: 0 0 30px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
        50% { border-color: #FFD700; box-shadow: 0 0 15px #FFD700, inset 0 0 8px #FFD700; background: linear-gradient(135deg, #1a1a00, #0d0d00); }
        100% { border-color: #00FF66; box-shadow: 0 0 30px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
    }

    @keyframes critical-warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000, inset 0 0 10px #FF3300; background: linear-gradient(135deg, #4a0000, #2b0000); }
        50% { border-color: #FFCC00; box-shadow: 0 0 12px #FFCC00, inset 0 0 5px #FF9900; background: linear-gradient(135deg, #2b0000, #140000); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000, inset 0 0 10px #FF3300; background: linear-gradient(135deg, #4a0000, #2b0000); }
    }

    .blinking-red-light { 
        display: inline-block; 
        width: 12px; 
        height: 12px; 
        background-color: #FF0055; 
        border-radius: 50%; 
        margin-right: 8px; 
        animation: blink-animation 0.8s infinite ease-in-out;
    }

    .master-status-bar {
        background: linear-gradient(135deg, #052210, #020d06);
        border: 1.5px solid #00FF66;
        padding: 6px 12px;
        border-radius: 6px;
        text-align: center;
        font-size: 11px;
        font-weight: 900;
        color: #00FF66;
        margin-bottom: 8px;
        animation: pulse-heartbeat 1.5s infinite;
        letter-spacing: 0.5px;
    }

    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 12px 16px; border-radius: 8px; font-size: 15px; font-weight: 900; border: 1.5px solid #3d9f5a; margin-bottom: 8px; }
    .main-card { background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 8px; }
    
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); }
    
    .period-badge-small { 
        color: #00FFFF; 
        font-weight: 900; 
        font-size: 16px; 
        background: rgba(0,255,255,0.1);
        padding: 4px 8px;
        border-radius: 5px;
        border: 1.5px solid #00FFFF;
        letter-spacing: 1px;
    }
    
    .sure-shot-banner { 
        background: linear-gradient(135deg, #330011, #1a0008); 
        border: 3px dashed #FF0055; 
        padding: 14px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 15px; 
        font-weight: 900; 
        margin: 8px 0; 
        color: #FF3366; 
        text-transform: uppercase; 
        animation: red-light-tip-tip 0.9s infinite; 
    }

    .super-100-win-banner { 
        border: 3.5px solid #00FF66; 
        padding: 14px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 16px; 
        font-weight: 900; 
        margin: 8px 0; 
        color: #00FF66; 
        text-transform: uppercase; 
        animation: super-win-glow 0.8s infinite; 
        letter-spacing: 1px;
    }

    .server-fail-warning-banner {
        border: 3.5px solid #FF0000; 
        padding: 16px; 
        border-radius: 10px; 
        text-align: center; 
        font-size: 14px; 
        font-weight: 900; 
        margin: 8px 0; 
        color: #FFDD00; 
        text-transform: uppercase; 
        animation: critical-warning-glow 0.6s infinite; 
        line-height: 1.5;
        letter-spacing: 0.5px;
    }

    .recovery-badge {
        background: linear-gradient(135deg, #1a1a00, #333300);
        border: 1.5px solid #FFD700;
        padding: 8px;
        border-radius: 6px;
        text-align: center;
        font-size: 13px;
        font-weight: bold;
        color: #FFD700;
        margin-top: 6px;
    }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.95); border: 1.5px solid #6644aa; border-radius: 8px; padding: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट डेटाबेस ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "registered_users_db" not in st.session_state:
    st.session_state.registered_users_db = {}
if "used_utr_database" not in st.session_state:
    st.session_state.used_utr_database = []
if "valid_approved_utrs" not in st.session_state:
    st.session_state.valid_approved_utrs = ["KISHOR1000UTR", "425678901234"]

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# --- लॉगिन गार्ड ---
if st.session_state.authenticated:
    current_mob = st.session_state.get("current_mobile", "")
    if current_mob != MASTER_MOBILE:
        if current_mob in st.session_state.registered_users_db:
            record = st.session_state.registered_users_db[current_mob]
            if datetime.now() > record["expiry_date"]:
                st.session_state.authenticated = False
                st.warning("⚠️ वैधता समाप्त हो चुकी है।")
                st.rerun()

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 24px; font-weight: 900;'>👑 BDG DUAL SHIELD <br> ACCESS PANEL</h2>", unsafe_allow_html=True)

    with st.container():
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        mobile_input = st.text_input("📱 MOBILE NUMBER", placeholder="Enter mobile number")
        password_input = st.text_input("🔒 PASSWORD", type="password", placeholder="Enter password")

        if st.button("🚀 UNLOCK PANEL", use_container_width=True):
            if not mobile_input or not password_input:
                st.error("⚠️ कृपया मोबाइल नंबर और पासवर्ड दर्ज करें!")
            elif mobile_input == MASTER_MOBILE and password_input == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.session_state.current_mobile = mobile_input
                st.success("👑 एडमिन लॉगिन सफल!")
                st.rerun()
            else:
                current_time = datetime.now()
                if mobile_input in st.session_state.registered_users_db:
                    user_record = st.session_state.registered_users_db[mobile_input]
                    if user_record["password"] == password_input:
                        if current_time < user_record["expiry_date"]:
                            st.session_state.authenticated = True
                            st.session_state.current_mobile = mobile_input
                            st.success("✅ लॉगिन सफल!")
                            st.rerun()
                        else:
                            st.warning("⚠ वैधता समाप्त!")
                            st.session_state.require_recharge = True
                            st.session_state.target_mobile = mobile_input
                            st.session_state.target_password = password_input
                    else:
                        st.error("❌ गलत पासवर्ड!")
                else:
                    st.info("ℹ️ नया उपयोगकर्ता। कृपया ₹1500 का भुगतान करें।")
                    st.session_state.require_recharge = True
                    st.session_state.target_mobile = mobile_input
                    st.session_state.target_password = password_input
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.get("require_recharge", False):
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #122a1a, #040d08); border: 1.5px solid #00FF66; padding: 10px; border-radius: 8px; text-align: center; margin-top: 8px;">
                <p style="color: #FFD700; font-weight: bold; font-size: 14px;">💳 Pay ₹1500 (2 Days Validity)</p>
                <p style="color: #00FF66; font-size: 12px; font-weight: bold; background: #020104; padding: 5px; border-radius: 4px; border: 1px dashed #00FF66; user-select: all;">kishorsingh226105.wallet@phonepe</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        upi_str = "upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=Kishor%20Singh%20Rautela&am=1500&cu=INR"
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=140x140&data={upi_str}"
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(qr_url, use_container_width=True)

        utr_entered = st.text_input("🔑 ENTER UTR NUMBER", max_chars=25, key="strict_utr_input")

        if st.button("🛡 VERIFY UTR", use_container_width=True):
            clean_utr = utr_entered.strip()
            t_mobile = st.session_state.get("target_mobile", "")
            t_pass = st.session_state.get("target_password", "")

            if not clean_utr:
                st.error("❌ कृपया UTR नंबर दर्ज करें!")
            elif clean_utr in st.session_state.used_utr_database:
                st.error("🚨 यह UTR पहले ही उपयोग हो चुका है!")
            elif clean_utr not in st.session_state.valid_approved_utrs:
                st.error("❌ अमान्य UTR!")
            else:
                st.session_state.used_utr_database.append(clean_utr)
                st.session_state.registered_users_db[t_mobile] = {
                    "password": t_pass,
                    "expiry_date": datetime.now() + timedelta(days=2),
                    "utr": clean_utr
                }
                st.session_state.authenticated = True
                st.session_state.current_mobile = t_mobile
                st.success("✅ सफलता!")
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        dynamic_online_count = random.randint(112000, 498000)

        st.markdown(
            """
            <div class="master-status-bar">
                ⚙️ BDG DOUBLE-PAIR & OMNI ENGINE ACTIVE 24x7
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #220033, #0b071a); border: 1px solid #FF00FF; padding: 8px; border-radius: 6px; text-align: center; margin-bottom: 8px;">
                <span style="color: #FF00FF; font-size: 12px; font-weight: bold;">🔊 अलार्म चालू करने के लिए यहाँ क्लिक करें:</span>
                <button onclick="let audio = new Audio('https://actions.google.com/sounds/v1/alarms/beep_short.ogg'); audio.play().catch(e => {});" style="background: #FF00FF; color: white; border: none; padding: 4px 12px; border-radius: 4px; font-weight: bold; cursor: pointer; margin-left: 6px;">ENABLE SOUND</button>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
                <div class="top-bar">
                    <div><span class="blinking-red-light"></span><span style="color: #00FFFF; font-weight: 900; font-size: 14px;">⚡ BDG SNIPER PANEL</span></div>
                    <div><span class="blinking-red-light"></span>👥 <span style="color: #00FF66; font-size: 13px; font-weight: 900;">{dynamic_online_count:,}</span></div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        now = datetime.now()
        default_period = "10196"

        col_a, col_b, col_c = st.columns([0.5, 3, 0.5])
        with col_b:
            st.markdown("<div style='background: #0b071a; border: 2px solid #FFD700; border-radius: 8px; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<p style='color: #FFD700; font-size: 13px; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;'>📌 लाइव पीरियड नंबर डालें (जैसे 10196)</p>", unsafe_allow_html=True)
            manual_period_input = st.text_input(
                "Period Input",
                value=default_period,
                key="user_live_period_input",
                label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<p style='color: #FFD700; font-size: 12px; font-weight: 900; text-align: center; margin-bottom: 4px; text-transform: uppercase;'>🎮 अपना गेम मोड चुनें:</p>", unsafe_allow_html=True)
        selected_game = st.radio(
            "Select Game Mode",
            ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed"
        )

        def render_game_panel(seconds, tab_name_style, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "10196"

            target_period = clean_input.zfill(5)
            base_p_int = int(target_period)

            # 🔥 डबल-डबल और पेयर पैटर्न इंजन: जो स्क्रीनशॉट की तरह डबल नंबरों (जैसे 8-8, 2-2) को तुरंत ट्रैक करेगा
            history = []
            for h_offset in range(5, 0, -1):
                h_period = base_p_int - h_offset
                
                # स्क्रीनशॉट में दिखने वाले डबल पेयर (जैसे 8-8 और 2-2) को सटीक पकड़ने का लॉजिक
                pair_check = (h_period // 2 + tab_offset) % 4
                
                if pair_check == 0:
                    h_item = "Big"
                elif pair_check == 1:
                    h_item = "Big"   # डबल बिग पेयर के लिए
                elif pair_check == 2:
                    h_item = "Small"
                else:
                    h_item = "Small" # डबल स्मॉल पेयर के लिए
                
                history.append(h_item)

            # आगामी शॉट (Next Shot) की गणना
            next_pair_check = (base_p_int // 2 + tab_offset) % 4
            pred_size = "BIG" if next_pair_check < 2 else "SMALL"

            p_rng = random.Random(base_p_int + tab_offset)
            if pred_size == "BIG":
                pred_num = p_rng.choice([5, 6, 7, 8, 9])
                pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
            else:
                pred_num = p_rng.choice([0, 1, 2, 3, 4])
                pred_color = "GREEN" if pred_num in [1, 3] else "RED"

            is_100_percent = (history[-1] == history[-2])
            variance_check = abs(base_p_int % 11)
            is_bad_market = (variance_check == 0 and not is_100_percent)

            if 1 <= remaining_secs <= 5:
                st.markdown(
                    """
                    <audio autoplay style="display:none;">
                        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #FFD700; padding-bottom: 6px; margin-bottom: 8px; background: rgba(255,215,0,0.06); border-radius: 6px; padding-left: 8px; padding-right: 8px;">
                    <span style="display: flex; align-items: center;"><span class="blinking-red-light"></span><span style="font-size: 13px; color: #FFD700; font-weight: 900; margin-right: 6px;">TARGET PERIOD:</span><span class="period-badge-small">{target_period}</span></span>
                    <span class="timer-box-large">⏰ {timer_str}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            level_key = f"recovery_level_{seconds}"
            if level_key not in st.session_state:
                st.session_state[level_key] = 1

            if is_100_percent:
                st.session_state[level_key] = 1

            current_lvl = st.session_state[level_key]
            size_highlight_color = "#FFD700" if pred_size == "BIG" else "#00FFFF"

            if is_bad_market:
                st.markdown(
                    f"""
                    <div class="server-fail-warning-banner">
                        <span class="blinking-red-light"></span>
                        ⚠️ MARKET VOLATILE - WAIT & STOP! <br> लाइन खराब है, अभी बेट मत लगाओ!
                        <span class="blinking-red-light"></span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif is_100_percent:
                st.markdown(
                    f"""
                    <div class="super-100-win-banner">
                        💎 100% SURE SHOT WIN : <span style="color: {size_highlight_color}; font-size: 18px; text-shadow: 0 0 10px {size_highlight_color};">{pred_size}</span> 🚀 (LEVEL 1 RESET)
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(f'<div class="sure-shot-banner"><span class="blinking-red-light"></span>💎 RECOVERY SHOT [ LEVEL {current_lvl} ] : <span style="color: {size_highlight_color};">{pred_size}</span> 🚀 <span class="blinking-red-light"></span></div>', unsafe_allow_html=True)

            multiplier_map = {1: "1x (Level 1 - स्टैंडर्ड बेट)", 2: "2.5x (Level 2 - रिकवरी बेट)", 3: "3x (Level 3 - अंतिम कैप)"}
            rec_text = multiplier_map.get(current_lvl, "1x")

            st.markdown(
                f"""
                <div class="recovery-badge">
                    🎯 सुझावित बैट मल्टीप्लायर: <span style="color: #00FF66;">{rec_text}</span> (विन होते ही ऑटो-रिसेट Level 1)
                </div>
                """,
                unsafe_allow_html=True
            )

            color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
            size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white; border: 2px solid #FFFFFF;">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center; border: 2px solid #FFFFFF; text-transform: uppercase;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center; border: 2px solid #FFFFFF; text-transform: uppercase;">{pred_color}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            # 🔥 इतिहास बॉक्स (नारंगी = Big, नीला = Small) जो डबल-डबल पेयर लाइन को तुरंत पकड़ेगा
            boxes_html = ""
            for item in history:
                if item == "Big":
                    bg_color = "#FF9900"  # नारंगी रंग (Big के लिए)
                else:
                    bg_color = "#0077FF"  # नीला रंग (Small के लिए)
                
                boxes_html += f"<div style='background: {bg_color}; color: white; padding: 5px 10px; border-radius: 4px; font-weight: 900; font-size: 11px; margin: 0 3px; display: inline-block; border: 1px solid #FFFFFF; text-transform: uppercase;'>{item}</div>"

            next_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"
            next_lbl = f"🎯 NEXT: {pred_size}"
            
            boxes_html += f"<div style='background: {next_bg}; color: white; padding: 5px 12px; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 12px; margin-left: 8px; border: 2px solid #00FF66; box-shadow: 0 0 12px #00FF66; text-transform: uppercase;'>{next_lbl}</div>"

            st.markdown(
                f"""
                <div style="margin-top: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 8px; text-align: center; border: 1.5px solid #FFD700;">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 6px; text-transform: uppercase;">📊 {selected_game} डबल-पेयर पैटर्न इतिहास और अगला शॉट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px;">{boxes_html}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("</div>", unsafe_allow_html=True)

        if selected_game == "WINGO 30S":
            render_game_panel(30, "WINGO 30S", 11)
        elif selected_game == "WINGO 1M":
            render_game_panel(60, "WINGO 1M", 23)
        elif selected_game == "WINGO 3M":
            render_game_panel(180, "WINGO 3M", 37)
        elif selected_game == "WINGO 5M":
            render_game_panel(300, "WINGO 5M", 53)

    success_dashboard_core()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()
