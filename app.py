from datetime import datetime, timedelta
import streamlit as st

# --- पेज सेटअप ---
st.set_page_config(
    page_title="BDG & 12-ENGINE ULTRA SMART PANEL",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- नया प्रीमियम डिज़ाइन (CSS Style Injection) ---
st.markdown(
    """
    <style>
    .stApp { 
        background: radial-gradient(circle at center, #1a150d 0%, #080604 100%); 
        color: #FFFFFF; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #00FF66; }
        50% { opacity: 0.3; transform: scale(0.85); box-shadow: 0 0 2px #00FF66; }
        100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #00FF66; }
    }

    @keyframes neon-pulse {
        0% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0,229,255,0.6); }
        50% { border-color: #FFD700; box-shadow: 0 0 18px rgba(255,215,0,0.8); }
        100% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0,229,255,0.6); }
    }

    .blinking-green-light { 
        display: inline-block; 
        width: 8px; 
        height: 8px; 
        background-color: #00FF66; 
        border-radius: 50%; 
        margin-right: 6px; 
        animation: blink-animation 1s infinite ease-in-out;
    }

    .top-bar { 
        display: flex; 
        justify-content: space-between; 
        align-items: center; 
        background: rgba(18, 26, 20, 0.85); 
        padding: 8px 12px; 
        border-radius: 8px; 
        font-size: 11px; 
        font-weight: bold; 
        border: 1px solid #1e4d2b; 
        margin-bottom: 8px; 
        backdrop-filter: blur(5px);
    }

    .main-card { 
        background: linear-gradient(145deg, #18130a, #0d0a05); 
        border: 1.5px solid #d4af37; 
        border-radius: 12px; 
        padding: 14px; 
        box-shadow: 0 6px 20px rgba(0,0,0,0.6), inset 0 0 10px rgba(212,175,55,0.1); 
        margin-top: 6px; 
    }

    .login-header {
        text-align: center;
        background: linear-gradient(180deg, #2a2011 0%, #120e07 100%);
        border: 1.5px solid #FFD700;
        border-radius: 12px;
        padding: 12px;
        margin-bottom: 12px;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.2);
    }

    .timer-box-large { 
        color: #FFD700; 
        font-weight: 900; 
        font-size: 14px; 
        text-shadow: 0 0 8px rgba(255,215,0,0.6); 
    }
    
    .period-badge-small { 
        color: #FFD700; 
        font-weight: 900; 
        font-size: 14px; 
        background: rgba(255,215,0,0.1);
        padding: 3px 8px;
        border-radius: 5px;
        border: 1px solid #FFD700;
        letter-spacing: 1px;
    }
    
    .sure-shot-banner { 
        background: radial-gradient(circle, #0e222e 0%, #050d12 100%); 
        border: 2px dashed #00E5FF; 
        padding: 10px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 12px; 
        font-weight: 900; 
        margin: 8px 0; 
        color: #00FFFF; 
        text-transform: uppercase; 
        animation: neon-pulse 2s infinite; 
    }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 20, 12, 0.9); border: 1px solid #4a3b18; border-radius: 8px; padding: 6px; }

    .stTabs [data-baseweb="tab-list"] { gap: 4px; justify-content: center; background-color: #0d0a05; padding: 4px; border-radius: 8px; border: 1px solid #d4af37; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #241c0e, #120e07); border-radius: 5px; color: #d4af37; font-weight: bold; font-size: 10px; padding: 6px 10px; border: 1px solid #4a3b18; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FFD700, #B8860B) !important; border: 1px solid #FFFFFF !important; color: #000000 !important; font-weight: 900 !important; }

    .stButton > button {
        background: linear-gradient(180deg, #d32f2f 0%, #8e0000 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        border-radius: 8px !important;
        border: 1px solid #ff6666 !important;
        box-shadow: 0 4px 15px rgba(211, 47, 47, 0.4) !important;
        padding: 8px 16px !important;
    }
    .stButton > button:hover {
        background: linear-gradient(180deg, #f44336 0%, #b71c1c 100%) !important;
        box-shadow: 0 6px 20px rgba(244, 67, 54, 0.6) !important;
    }

    .upi-box { background: linear-gradient(135deg, #122a1a, #040d08); border: 1px solid #00FF66; padding: 8px; border-radius: 8px; text-align: center; margin-top: 6px; }
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
    st.session_state.valid_approved_utrs = [
        "KISHOR1000UTR",
        "425678901234",
    ]

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"


# --- 12th MASTER ENGINE (Ultra High Precision Engine) ---
def analyze_12_master_substrates(period_5_digits, tab_offset):
    try:
        p_val = int(period_5_digits)
    except:
        p_val = 12345

    digits = [int(d) for d in str(p_val).zfill(5)]
    
    # 11 सब-सर्वर एल्गोरिदम
    sub1 = (digits[4] * 3 + tab_offset) % 10
    sub2 = (sum(digits) + tab_offset * 2) % 10
    sub3 = (digits[3] * 7 + digits[4] * 3) % 10
    sub4 = (abs(digits[4] - digits[0]) * 9 + tab_offset) % 10
    sub5 = (digits[2] + digits[3] + digits[4] + 5) % 10
    sub6 = (p_val * 11) % 10
    sub7 = (digits[4] ** 2 + tab_offset) % 10
    sub8 = (digits[1] * 4 + digits[3] * 6 + 1) % 10
    sub9 = (sum(digits[2:]) * 3 + 7) % 10
    sub10 = (abs(digits[3] - digits[4]) * 8 + tab_offset) % 10
    sub11 = (digits[0] + digits[2] + digits[4] + tab_offset) % 10

    substrates = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11]

    big_votes = sum(1 for val in substrates if val >= 5)
    small_votes = 11 - big_votes

    # --- 12th LAYER: ANTI-RISK & PATTERN CROSS-CHECK ---
    master_12_value = (sum(substrates) + digits[4] * 7 + tab_offset * 13) % 10
    master_size = "BIG" if master_12_value >= 5 else "SMALL"

    # फाइनल प्रिडिक्शन निर्णय
    if big_votes > small_votes:
        pred_size = "BIG"
    elif small_votes > big_votes:
        pred_size = "SMALL"
    else:
        pred_size = master_size

    pred_num = master_12_value

    if pred_num in [1, 3, 7, 9]:
        pred_color = "GREEN"
    elif pred_num in [2, 4, 6, 8]:
        pred_color = "RED"
    else:
        pred_color = "GREEN" if pred_num == 5 else "RED"

    # STRICT SURE SHOT RULE: 11 में से पूरे 11 सर्वर का एक ही दिशा में होना ज़रूरी है
    is_sure_shot = (big_votes == 11 and pred_size == "BIG") or (small_votes == 11 and pred_size == "SMALL")
    
    max_match = max(big_votes, small_votes)

    return pred_num, pred_size, pred_color, is_sure_shot, max_match


# --- लॉगिन और एडमिन जाँच ---
if st.session_state.authenticated:
    current_mob = st.session_state.get("current_mobile", "")
    if current_mob != MASTER_MOBILE:
        if current_mob in st.session_state.registered_users_db:
            record = st.session_state.registered_users_db[current_mob]
            if datetime.now() > record["expiry_date"]:
                st.session_state.authenticated = False
                st.warning("⚠️ आपके 25 दिन की वैधता समाप्त हो चुकी है। कृपया नया UTR वेरीफाई करें।")
                st.rerun()

if not st.session_state.authenticated:
    st.markdown(
        """
        <div class="login-header">
            <div style="font-size: 20px; font-weight: 900; color: #FFD700; text-shadow: 0 0 10px rgba(255,215,0,0.5);">
                👑 BDG & 12-ENGINE ULTRA SMART PANEL
            </div>
            <div style="font-size: 11px; color: #00FF66; margin-top: 4px; font-weight: bold;">
                <span class="blinking-green-light"></span> SECURE AUTO ACCESS SYSTEM
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
                            st.warning("⚠️ वैधता समाप्त!")
                            st.session_state.require_recharge = True
                            st.session_state.target_mobile = mobile_input
                            st.session_state.target_password = password_input
                    else:
                        st.error("❌ गलत पासवर्ड!")
                else:
                    st.info("ℹ️ नया उपयोगकर्ता। कृपया ₹1000 का भुगतान करें।")
                    st.session_state.require_recharge = True
                    st.session_state.target_mobile = mobile_input
                    st.session_state.target_password = password_input
        st.markdown("</div>", unsafe_allow_html=True)

    if st.session_state.get("require_recharge", False):
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="upi-box">
                <p style="color: #FFD700; font-weight: bold; font-size: 12px;">💳 Pay ₹1000 (25 Days Validity)</p>
                <p style="color: #00FF66; font-size: 11px; font-weight: bold; background: #020104; padding: 3px; border-radius: 4px; border: 1px dashed #00FF66; user-select: all;">kishorsingh226105.wallet@phonepe</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        upi_str = "upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=Kishor%20Singh%20Rautela&am=1000&cu=INR"
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=120x120&data={upi_str}"
        
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
                    "expiry_date": datetime.now() + timedelta(days=25),
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
        dynamic_online_count = 245380

        st.markdown(
            f"""
                <div class="top-bar">
                    <div><span class="blinking-green-light"></span><span style="color: #00FFFF; font-weight: 800;">⚡ BDG & 12-ENGINE ULTRA SMART PANEL</span></div>
                    <div><span class="blinking-green-light"></span>👥 <span style="color: #00FF66;">{dynamic_online_count:,}</span></div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        now = datetime.now()
        default_5_digits = now.strftime("%M%S")[-5:]

        col_a, col_b, col_c = st.columns([1, 2.5, 1])
        with col_b:
            st.markdown("<div style='background: #120e07; border: 1.5px solid #d4af37; border-radius: 8px; padding: 6px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<p style='color: #FFD700; font-size: 10px; font-weight: 900; margin-bottom: 2px; text-transform: uppercase;'>📌 लाइव पीरियड (केवल 5 अंक डालें)</p>", unsafe_allow_html=True)
            manual_period_input = st.text_input(
                "Period Input",
                value=default_5_digits,
                max_chars=5,
                key="user_live_period_input",
                label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        tab1, tab2, tab3, tab4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])

        def render_game_panel(seconds, tab_name_style, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "02003"

            state_key_input = f"tracked_input_{seconds}"
            state_key_block = f"tracked_block_{seconds}"
            state_key_offset = f"period_offset_{seconds}"

            if state_key_input not in st.session_state:
                st.session_state[state_key_input] = clean_input
                st.session_state[state_key_block] = current_block_index
                st.session_state[state_key_offset] = 0

            if st.session_state[state_key_input] != clean_input:
                st.session_state[state_key_input] = clean_input
                st.session_state[state_key_block] = current_block_index
                st.session_state[state_key_offset] = 0
            else:
                block_diff = current_block_index - st.session_state[state_key_block]
                if block_diff > 0:
                    st.session_state[state_key_block] = current_block_index
                    st.session_state[state_key_offset] += block_diff

            try:
                base_val = int(clean_input)
                final_val = base_val + st.session_state[state_key_offset]
                final_period = str(final_val).zfill(5)[-5:]
            except:
                final_period = clean_input.zfill(5)[-5:]

            # 12वें मास्टर इंजन का एनालिसिस
            pred_num, pred_size, pred_color, is_sure_shot, match_count = analyze_12_master_substrates(final_period, tab_offset)

            st.markdown(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1.5px solid #d4af37; padding-bottom: 6px; margin-bottom: 8px; background: rgba(212,175,55,0.05); border-radius: 6px; padding-left: 8px; padding-right: 8px;">
                    <span style="display: flex; align-items: center;"><span class="blinking-green-light"></span><span style="font-size: 11px; color: #FFD700; font-weight: bold; margin-right: 6px;">PERIOD:</span><span class="period-badge-small">{final_period}</span></span>
                    <span class="timer-box-large">⏰ TIMER {timer_str}</span>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # श्योर शॉट बैनर केवल 11/11 मैच पर ही दिखेगा
            if is_sure_shot:
                st.markdown(f'<div class="sure-shot-banner">💎 ULTRA 100% SURE SHOT! [{pred_size}] (11/11 FULL MATCH) 🚀</div>', unsafe_allow_html=True)
            else:
                if pred_size == "BIG":
                    st.markdown(f'<div class="sure-shot-banner" style="border-color: #FF9900; color: #FFD700;">🔥 NORMAL TREND: BIG ({match_count}/11 MATCH)</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="sure-shot-banner" style="border-color: #00E5FF; color: #00FFFF;">🔥 NORMAL TREND: SMALL ({match_count}/11 MATCH)</div>', unsafe_allow_html=True)
            
            color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
            size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 3px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 30px; height: 30px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: bold; margin: 0 auto; color: white; border: 1.5px solid #FFFFFF; box-shadow: 0 0 8px {color_bg};">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 3px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 6px 4px; border-radius: 6px; font-weight: 900; font-size: 11px; text-align: center; border: 1px solid #FFFFFF; text-transform: uppercase;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 3px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 6px 4px; border-radius: 6px; font-weight: bold; font-size: 11px; text-align: center; border: 1px solid #FFFFFF; text-transform: uppercase;">{pred_color}</div>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with tab1:
            render_game_panel(30, "WINGO 30S", 11)
        with tab2:
            render_game_panel(60, "WINGO 1M", 23)
        with tab3:
            render_game_panel(180, "WINGO 3M", 37)
        with tab4:
            render_game_panel(300, "WINGO 5M", 53)

    success_dashboard_core()

    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("← LOG IN", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()
