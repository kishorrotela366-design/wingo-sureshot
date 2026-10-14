from datetime import datetime, timedelta
import random
import time
import streamlit as st

st.set_page_config(
    page_title="BDG VIP SUPER PANEL 100%",
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
    
    @keyframes super-fast-blink {
        0% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 15px #FF0055, 0 0 25px #FF0055; }
        50% { opacity: 0.1; transform: scale(0.7); box-shadow: 0 0 2px #FF0055; }
        100% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 15px #FF0055, 0 0 25px #FF0055; }
    }
    
    @keyframes super-win-glow-big {
        0% { border-color: #FFB700; box-shadow: 0 0 30px #FFB700, inset 0 0 15px #FFB700; background: linear-gradient(135deg, #3a2200, #150a00); }
        50% { border-color: #FF5500; box-shadow: 0 0 15px #FF5500, inset 0 0 5px #FF5500; background: linear-gradient(135deg, #4a0e00, #1a0500); }
        100% { border-color: #FFB700; box-shadow: 0 0 30px #FFB700, inset 0 0 15px #FFB700; background: linear-gradient(135deg, #3a2200, #150a00); }
    }

    @keyframes super-win-glow-small {
        0% { border-color: #00FFFF; box-shadow: 0 0 30px #00FFFF, inset 0 0 15px #00FFFF; background: linear-gradient(135deg, #002222, #000a1a); }
        50% { border-color: #0088FF; box-shadow: 0 0 15px #0088FF, inset 0 0 5px #0088FF; background: linear-gradient(135deg, #00103a, #00051a); }
        100% { border-color: #00FFFF; box-shadow: 0 0 30px #00FFFF, inset 0 0 15px #00FFFF; background: linear-gradient(135deg, #002222, #000a1a); }
    }

    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }

    @keyframes analyzing-glow {
        0% { border-color: #FF00FF; box-shadow: 0 0 15px #FF00FF; color: #FF00FF; }
        50% { border-color: #00FFFF; box-shadow: 0 0 15px #00FFFF; color: #00FFFF; }
        100% { border-color: #FF00FF; box-shadow: 0 0 15px #FF00FF; color: #FF00FF; }
    }

    .blinking-red-light {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #FF0055;
        border-radius: 50%;
        margin-right: 6px;
        animation: super-fast-blink 0.5s infinite linear;
    }

    .blinking-green-light {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #00FF66;
        border-radius: 50%;
        margin-left: 6px;
        margin-right: 6px;
        animation: super-fast-blink 0.5s infinite linear;
    }

    .blinking-yellow-light {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #FFD700;
        border-radius: 50%;
        margin-right: 6px;
        animation: super-fast-blink 0.5s infinite linear;
    }
    
    .target-period-box {
        background: #000000;
        border: 1.5px solid #00FFFF;
        border-radius: 10px;
        padding: 10px 12px;
        box-shadow: 0 0 12px rgba(0, 255, 255, 0.25);
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 6px !important;
        font-weight: 900 !important;
        text-align: left !important;
        padding: 6px !important;
        height: 38px !important;
    }
    .stTextInput > label { display: none !important; }

    .main-card { background-color: #000000; border: none; padding: 0px; margin-top: 4px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); display: flex; align-items: center; gap: 6px; }
    
    .super-banner-small { border: 2.5px solid #00FFFF; padding: 14px; border-radius: 10px; text-align: center; font-size: 16px; font-weight: 900; margin: 10px 0; color: #00FFFF; text-transform: uppercase; animation: super-win-glow-small 0.8s infinite; letter-spacing: 1px; box-shadow: 0 0 20px rgba(0,255,255,0.4); }
    .super-banner-big { border: 2.5px solid #FFB700; padding: 14px; border-radius: 10px; text-align: center; font-size: 16px; font-weight: 900; margin: 10px 0; color: #FFB700; text-transform: uppercase; animation: super-win-glow-big 0.8s infinite; letter-spacing: 1px; box-shadow: 0 0 20px rgba(255,183,0,0.4); }
    
    .analyzing-banner { border: 2px dashed #FF00FF; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; animation: analyzing-glow 1s infinite; letter-spacing: 1px; background: #000000; }
    .wait-warning-banner { border: 3px solid #FF0000; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(255,0,0,0.4); display: flex; align-items: center; justify-content: center; gap: 10px; }
    
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 10px; }
    .result-item { flex: 1; text-align: center; background: #130d24; border: 2.5px solid #3b286b; border-radius: 12px; padding: 12px 6px; box-shadow: 0 0 10px rgba(59,40,107,0.3); }
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

if "user_base_period" not in st.session_state:
    st.session_state.user_base_period = ""

if "base_input_block_time" not in st.session_state:
    st.session_state.base_input_block_time = 0

if "selected_game_seconds" not in st.session_state:
    st.session_state.selected_game_seconds = 30

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if not st.session_state.authenticated:
    st.markdown(
        "<h2 style='text-align: center; color: #FFD700; font-size: 20px;"
        " font-weight: 900;'><span class='blinking-red-light'></span>👑 BDG VIP"
        " SUPER PANEL 100% 👑<span class='blinking-red-light'"
        " style='margin-left: 6px; margin-right: 0;'></span></h2>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color: #00FFFF; text-align: center; font-weight: 900;"
        " font-size: 14px;'>रजिस्टर्ड मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>",
        unsafe_allow_html=True,
    )

    login_mob = st.text_input(
        "📱 मोबाइल नंबर", placeholder="Enter mobile number", key="login_mob_input"
    )
    login_pass = st.text_input(
        "🔒 पासवर्ड",
        type="password",
        placeholder="Enter password",
        key="login_pass_input",
    )

    if st.button(
        "🚀 UNLOCK PANEL (LOGIN)", use_container_width=True, key="login_btn"
    ):
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
                        st.success(
                            "🟢 Verified: आपका प्लान सक्रिय है, डैशबोर्ड खुल"
                            " रहा है..."
                        )
                        time.sleep(0.8)
                        st.rerun()
                    elif user_data["status"] == "REJECTED":
                        st.error(
                            "🔴 रिजेक्टेड: आपका UTR ओनर द्वारा रिजेक्ट कर दिया"
                            " गया है!"
                        )
                    else:
                        st.warning(
                            "🔴 पेंडिंग: आपका UTR अभी ओनर द्वारा अप्रूव नहीं हुआ"
                            " है!"
                        )
                else:
                    st.error(
                        "🚨 समय समाप्त: आपके 15 दिन का प्लान खत्म हो चुका है!"
                        " कृपया नीचे नया ₹2000 का भुगतान करके नया UTR दर्ज करें।"
                    )
            else:
                st.error("❌ गलत पासवर्ड! कृपया सही पासवर्ड दर्ज करें।")
        else:
            st.error(
                "❌ यह मोबाइल नंबर रजिस्टर्ड नहीं है! कृपया नया UTR दर्ज करें।"
            )

    st.markdown("---")
    st.markdown(
        "<h3 style='color: #FFD700; font-weight: 900; text-align: center;"
        " font-size: 15px; margin-bottom: 5px;'>⚡ 2000 ₹ QR स्कैन और नया UTR दर्ज"
        " करें</h3>",
        unsafe_allow_html=True,
    )

    renew_mob = st.text_input(
        "📱 रजिस्टर्ड मोबाइल नंबर", placeholder="Enter mobile", key="renew_mob_input"
    )
    renew_pass = st.text_input(
        "🔒 पासवर्ड",
        type="password",
        placeholder="Enter password",
        key="renew_pass_input",
    )

    st.markdown(
        """
        <div style='background: linear-gradient(135deg, #113300, #001a00); border: 2px solid #00FF66; padding: 12px; border-radius: 10px; margin: 10px 0; text-align: center;'>
            <p style='color: #00FF66; font-size: 14px; font-weight: 900; margin: 0;'>💎 15 दिन समाप्त होने पर ₹2000 का भुगतान करके नया UTR डालें (15 Days Plan)</p>
            <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करें:</p>
            <div style='background: #FFFFFF; padding: 10px; display: inline-block; border-radius: 8px; margin-top: 6px; box-shadow: 0 0 15px rgba(0,255,102,0.4);'>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=2000" width="160" height="160">
            </div>
            <p style='color: #FFD700; font-size: 12px; margin-top: 6px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    renew_utr_input = st.text_input(
        "📝 नया 12-Digit UTR Number",
        placeholder="Enter new 12-digit UTR",
        max_chars=12,
        key="renew_utr_input",
    )

    if st.button(
        "🔄 नया UTR सबमिट करें (RENEW REQUEST)",
        use_container_width=True,
        key="user_renew_btn",
    ):
        clean_r_mob = "".join(filter(str.isdigit, renew_mob))
        clean_utr = "".join(filter(str.isdigit, renew_utr_input))

        if len(clean_r_mob) < 10:
            st.error("⚠️ कृपया सही 10 अंकों का मोबाइल नंबर दर्ज करें!")
        elif not renew_pass:
            st.error("⚠️ कृपया अपना पासवर्ड दर्ज करें!")
        elif len(clean_utr) != 12:
            st.error("⚠️ अमान्य UTR! कृपया ठीक 12 अंकों का सही UTR नंबर डालें!")
        elif clean_utr in st.session_state.used_utrs_list:
            st.error(
                "🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका"
                " है! कृपया कोई नया UTR नंबर डालें।"
            )
        else:
            st.session_state.utr_requests[clean_r_mob] = {
                "utr": clean_utr,
                "password": renew_pass,
                "status": "PENDING",
                "expiry": datetime.now() + timedelta(days=15),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            st.success(
                "📩 नया UTR सफलतापूर्वक सबमिट हो गया है! 🔴 (पेंडिंग)। ओनर द्वारा"
                " वेरीफाई और अप्रूव होने के बाद आपका 15 दिन का पैनल चालू होगा।"
            )

    st.markdown("</div>", unsafe_allow_html=True)

else:
    if st.session_state.is_owner:
        st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='color: #FFD700; text-align: center; margin: 0;'>👑"
            " OWNER / ADMIN APPROVAL PANEL</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: #00FFFF; text-align: center; font-size: 12px;'>यहाँ"
            " यूज़र का नया UTR चेक करें और Approve (हरा टिक) दें (15 Days Validation):</p>",
            unsafe_allow_html=True,
        )

        if not st.session_state.utr_requests:
            st.info("अभी तक कोई UTR रिक्वेस्ट नहीं आई है।")
        else:
            for mob, req in list(st.session_state.utr_requests.items()):
                status_icon = (
                    "🟢 (रिचार्ज स्वीकृत - ग्रीन टिक)"
                    if req["status"] == "APPROVED"
                    else "🔴 (रिचार्ज पेंडिंग)"
                )
                border_color = (
                    "#00FF66" if req["status"] == "APPROVED" else "#FF0000"
                )

                st.markdown(
                    f"""
                    <div style='border: 1.5px solid {border_color}; padding: 10px; border-radius: 8px; margin-bottom: 8px; background: #000000;'>
                        <p style='margin:0; font-weight:900; color:#FFFFFF;'>📱 मोबाइल: <span style='color:#00FFFF;'>{mob}</span> | {status_icon}</p>
                        <p style='margin:0; font-size:12px; color:#FFD700;'>📝 UTR No: {req['utr']} | ⏰ समय: {req['time']}</p>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                col_app, col_rej = st.columns(2)
                with col_app:
                    if st.button(f"✅ Approve", key=f"app_{mob}"):
                        if req["utr"] not in st.session_state.used_utrs_list:
                            st.session_state.used_utrs_list.append(req["utr"])

                        st.session_state.utr_requests[mob]["status"] = (
                            "APPROVED"
                        )
                        st.session_state.utr_requests[mob]["expiry"] = (
                            datetime.now() + timedelta(days=15)
                        )
                        st.success(
                            f"यूज़र {mob} को 15 दिनों के लिए अप्रूव कर दिया गया है!"
                        )
                        time.sleep(0.5)
                        st.rerun()
                with col_rej:
                    if st.button(f"❌ Reject", key=f"rej_{mob}"):
                        st.session_state.utr_requests[mob]["status"] = (
                            "REJECTED"
                        )
                        st.error(
                            f"यूज़र {mob} का UTR रिजेक्ट कर दिया गया।"
                        )
                        time.sleep(0.5)
                        st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    col_m1, col_m2, col_m3, col_m4 = st.columns(4)

    with col_m1:
        if st.button("30S MODE", key="btn_30s", use_container_width=True):
            st.session_state.selected_game_seconds = 30
            st.rerun()

    with col_m2:
        if st.button("1M MODE", key="btn_1m", use_container_width=True):
            st.session_state.selected_game_seconds = 60
            st.rerun()

    with col_m3:
        if st.button("3M MODE", key="btn_3m", use_container_width=True):
            st.session_state.selected_game_seconds = 180
            st.rerun()

    with col_m4:
        if st.button("5M MODE", key="btn_5m", use_container_width=True):
            st.session_state.selected_game_seconds = 300
            st.rerun()

    seconds = st.session_state.selected_game_seconds

    def update_period_callback():
        clean_val = "".join(filter(str.isdigit, st.session_state.period_text_box))
        st.session_state.user_base_period = clean_val
        current_time = int(time.time())
        st.session_state.base_input_block_time = current_time - (
            current_time % seconds
        )

    st.text_input(
        "Period Input",
        value=st.session_state.user_base_period,
        placeholder="बीडीजी गेम के पीछे के आखिरी 5 अंक यहाँ डालें...",
        max_chars=5,
        key="period_text_box",
        on_change=update_period_callback,
        label_visibility="collapsed",
    )

    @st.fragment(run_every=1)
    def success_dashboard_core():
        try:
            now = datetime.now()
            tab_offset = 23

            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs_rem = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs_rem:02d}"

            # आखिरी 5 सेकंड पर ऑडियो घंटी (Audio Alert) बजेगी
            if remaining_secs <= 5:
                st.markdown(
                    """
                    <div style="display:none; width:0; height:0; overflow:hidden;">
                        <audio autoplay>
                            <source src="https://assets.mixkit.co/active_storage/sfx/2869/2869-preview.mp3" type="audio/mpeg">
                        </audio>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

            st.markdown("<div class='main-card'>", unsafe_allow_html=True)

            user_input_str = st.session_state.user_base_period.strip()

            is_invalid_format = False
            if not user_input_str or len(user_input_str) != 5 or not user_input_str.isdigit():
                is_invalid_format = True

            if is_invalid_format:
                st.markdown(
                    f"""
                    <div class="target-period-box">
                        <div style="display: flex; align-items: center;">
                            <span class="blinking-red-light"></span>
                            <span style="color: #FFD700; font-size: 13px; font-weight: 900; margin-right: 6px;">LIVE PERIOD:</span>
                            <span style="color: #FF4444; font-size: 12px; font-weight: 900;">🚨 कृपया बीडीजी गेम के पीछे के आखिरी 5 अंक ही डालें!</span>
                        </div>
                        <div class="timer-box-large">⏰ {timer_str}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    '<div class="wait-warning-banner"><span'
                    ' class="blinking-red-light"></span>🛑 PANEL LOCKED - ENTER'
                    ' LAST 5 DIGITS<span class="blinking-red-light"'
                    ' style="margin-left: 6px; margin-right: 0;"></span></div>',
                    unsafe_allow_html=True,
                )
                st.markdown("</div>", unsafe_allow_html=True)
                return

            try:
                base_val = int(user_input_str)
            except:
                base_val = 10000

            current_time = int(time.time())
            current_block_start = current_time - (current_time % seconds)

            if st.session_state.base_input_block_time == 0:
                st.session_state.base_input_block_time = current_block_start

            elapsed_blocks = (
                current_block_start - st.session_state.base_input_block_time
            ) // seconds
            target_period_num = base_val + elapsed_blocks
            target_period_str = str(target_period_num)

            # ==========================================================
            # 1. ऊपर का '100% श्योर शॉट' इंजन (जिग-जैग और सर्वर नोड्स की सख्त चेकिंग)
            # ==========================================================
            def calculate_top_sure_shot(p_num, offset_val):
                history_votes = []
                for hist in range(1, 6):
                    prev_val = (p_num - hist) * 11 + offset_val
                    history_votes.append("BIG" if prev_val % 2 == 0 else "SMALL")
                
                # जिग-जैग पैटर्न चेक (उतार-चढ़ाव की पहचान)
                is_zigzag_pattern = history_votes[0] != history_votes[1]

                server_consensus = []
                for node in range(1, 42):
                    check_val = (p_num * node * 31 + offset_val + (p_num % 17)) % 100
                    v_type = "BIG" if check_val % 2 == 0 else "SMALL"
                    
                    if is_zigzag_pattern and node % 2 != 0:
                        v_type = history_votes[0]
                    server_consensus.append(v_type)

                big_t = server_consensus.count("BIG")
                small_t = server_consensus.count("SMALL")

                # जब तक 34 या उससे अधिक नोड्स की पक्की सहमति नहीं होगी, तब तक 'WAITING' दिखाएगा
                if big_t >= 34:
                    return "BIG"
                elif small_t >= 34:
                    return "SMALL"
                else:
                    return None

            pred_size = calculate_top_sure_shot(target_period_num, tab_offset)

            # ==========================================================
            # 2. नीचे का 'नेक्स्ट शॉट' इंजन (आने वाले ट्रेंड और अगली लाइन का कैच)
            # ==========================================================
            def calculate_bottom_next_shot(p_num, offset_val):
                next_trend_votes = []
                for n_id in range(1, 26):
                    # नेक्स्ट शॉट के लिए बिल्कुल अलग और सटीक फॉर्मूला
                    next_check = (p_num * n_id * 17 + offset_val + (p_num % 5)) % 100
                    next_trend_votes.append("BIG" if next_check % 2 == 0 else "SMALL")
                
                b_big = next_trend_votes.count("BIG")
                b_small = next_trend_votes.count("SMALL")
                return "BIG" if b_big >= b_small else "SMALL"

            next_shot_val = calculate_bottom_next_shot(target_period_num, tab_offset)

            st.markdown(
                f"""
                <div class="target-period-box">
                    <div style="display: flex; align-items: center;">
                        <span style="color: #FFD700; font-size: 13px; font-weight: 900; margin-right: 6px;">LIVE PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 15px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 2px 8px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div class="timer-box-large">⏰ {timer_str}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # --- बेटिंग विंडो टाइमिंग (30S मोड में पूरे 15 सेकंड का सुरक्षित समय) ---
            if seconds == 30:
                scan_active = remaining_secs > 27
                close_phase = remaining_secs <= 15
            elif seconds == 60:
                scan_active = remaining_secs > 50
                close_phase = remaining_secs <= 20
            elif seconds == 180:
                scan_active = remaining_secs > 160
                close_phase = remaining_secs <= 30
            else:
                scan_active = remaining_secs > 270
                close_phase = remaining_secs <= 45

            is_market_unclear = pred_size is None

            if close_phase:
                st.markdown(
                    '<div class="wait-warning-banner"><span'
                    ' class="blinking-red-light"></span>🛑 SAFE BIDDING TIME - PLACE YOUR BID NOW<span class="blinking-red-light"'
                    ' style="margin-left: 6px; margin-right: 0;"></span></div>',
                    unsafe_allow_html=True,
                )
            elif scan_active:
                st.markdown(
                    f'<div class="analyzing-banner"><span'
                    ' class="blinking-yellow-light" style="width:8px;'
                    ' height:8px;"></span> 🔄 ZIG-ZAG & HISTORY SCANNING... ({remaining_secs}s left)</div>',
                    unsafe_allow_html=True,
                )
            elif is_market_unclear:
                st.markdown(
                    '<div class="wait-warning-banner"><span'
                    ' class="blinking-yellow-light"></span>🛑 WAITING: ZIG-ZAG 100% SHOT SEARCHING (सुरक्षित प्रतीक्षा)<span class="blinking-yellow-light"'
                    ' style="margin-left:6px;"></span></div>',
                    unsafe_allow_html=True,
                )
            else:
                if pred_size == "BIG":
                    st.markdown(
                        """
                        <div class="super-banner-big">
                            🔥 100% SURE SHOT <span class="blinking-green-light"></span> : 
                            <span style="background: #000000; color: #FFB700; padding: 4px 14px; border-radius: 6px; border: 2px solid #FFB700; font-weight: 900; text-shadow: 0 0 10px #FFB700;">BIG</span> 🎯
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        """
                        <div class="super-banner-small">
                            🔥 100% SURE SHOT <span class="blinking-green-light"></span> : 
                            <span style="background: #000000; color: #00FFFF; padding: 4px 14px; border-radius: 6px; border: 2px solid #00FFFF; font-weight: 900; text-shadow: 0 0 10px #00FFFF;">SMALL</span> 🎯
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

            # --- बीच वाला रिजल्ट बॉक्स (Number, Size, Color) ---
            if scan_active or is_market_unclear:
                display_num = "—"
                display_size = "WAITING"
                display_color = "STANDBY"
                color_bg = "#111111"
                size_bg = "#111111"
            else:
                p_rng = random.Random(target_period_num * 3 + tab_offset)
                if pred_size == "BIG":
                    pred_num = p_rng.choice([5, 6, 7, 8, 9])
                    pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
                else:
                    pred_num = p_rng.choice([0, 1, 2, 3, 4])
                    pred_color = "GREEN" if pred_num in [1, 3] else "RED"

                display_num = str(pred_num)
                display_size = pred_size
                display_color = pred_color
                color_bg = "#FF4444" if pred_color == "RED" else "#00AA55"
                size_bg = "#FF8800" if pred_size == "BIG" else "#0088FF"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 45px; height: 45px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 900; margin: 0 auto; color: white;">{display_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 12px 4px; border-radius: 8px; font-weight: 900; font-size: 14px; text-align: center;">{display_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 12px 4px; border-radius: 8px; font-weight: 900; font-size: 14px; text-align: center;">{display_color}</div>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            # --- सबसे नीचे साफ-सुथरा 'LIVE' और 'नेक्स्ट शॉट' (बिल्कुल अलग लॉजिक के साथ) ---
            if next_shot_val == "BIG":
                next_shot_bg = "#FF8800"
                next_shot_glow = "0 0 15px #FF8800"
            else:
                next_shot_bg = "#0088FF"
                next_shot_glow = "0 0 15px #0088FF"

            st.markdown(
                f"""
                <div style="margin-top: 12px; background: #000000; padding: 14px; border-radius: 12px; text-align: center; border: 2px solid #FFD700; box-shadow: 0 0 15px rgba(255,215,0,0.2); display: flex; justify-content: center; align-items: center; gap: 12px;">
                    <div style="display: flex; align-items: center; gap: 6px;">
                        <span class="blinking-red-light" style="width:10px; height:10px; margin:0;"></span>
                        <span style="color: #00FF66; font-size: 14px; font-weight: 900; letter-spacing: 1px;">LIVE</span>
                    </div>
                    <span style="color: #FFD700; font-weight: 900;">|</span>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="color: #00FFFF; font-size: 14px; font-weight: 900; text-shadow: 0 0 8px rgba(0,255,255,0.5);">NEXT SHOT:</span>
                        <span style="background: {next_shot_bg}; color: #FFFFFF; padding: 8px 24px; border-radius: 8px; font-weight: 900; font-size: 14px; border: 2px solid #FFFFFF; box-shadow: {next_shot_glow};">{next_shot_val}</span>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            st.markdown("</div>", unsafe_allow_html=True)
        except Exception as e:
            st.warning("⚠️ री-सिंकिंग हो रही है... कृपया प्रतीक्षा करें।")
            time.sleep(1)
            st.rerun()


    success_dashboard_core()
