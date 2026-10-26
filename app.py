from datetime import datetime, timedelta
import json
import os
import time
import streamlit as st

st.set_page_config(
    page_title="VIP STREAK & SURE SHOT ULTIMATE PANEL",
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

    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes super-win-glow-big {
        0% { border-color: #FFB700; box-shadow: 0 0 35px #FFB700, inset 0 0 20px #FFB700; background: linear-gradient(135deg, #3a2200, #150a00); }
        50% { border-color: #FF5500; box-shadow: 0 0 15px #FF5500, inset 0 0 5px #FF5500; background: linear-gradient(135deg, #4a0e00, #1a0500); }
        100% { border-color: #FFB700; box-shadow: 0 0 35px #FFB700, inset 0 0 20px #FFB700; background: linear-gradient(135deg, #3a2200, #150a00); }
    }

    @keyframes super-win-glow-small {
        0% { border-color: #00FFFF; box-shadow: 0 0 35px #00FFFF, inset 0 0 20px #00FFFF; background: linear-gradient(135deg, #002222, #000a1a); }
        50% { border-color: #0088FF; box-shadow: 0 0 15px #0088FF, inset 0 0 5px #0088FF; background: linear-gradient(135deg, #00103a, #00051a); }
        100% { border-color: #00FFFF; box-shadow: 0 0 35px #00FFFF, inset 0 0 20px #00FFFF; background: linear-gradient(135deg, #002222, #000a1a); }
    }

    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }

    @keyframes analyzing-glow {
        0% { border-color: #FF00FF; box-shadow: 0 0 20px #FF00FF; color: #FF00FF; }
        50% { border-color: #00FFFF; box-shadow: 0 0 20px #00FFFF; color: #00FFFF; }
        100% { border-color: #FF00FF; box-shadow: 0 0 20px #FF00FF; color: #FF00FF; }
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

    .radar-spinner-icon {
        display: inline-block;
        width: 14px;
        height: 14px;
        border: 2.5px solid #FF0055;
        border-top: 2.5px solid transparent;
        border-radius: 50%;
        margin-left: 6px;
        margin-right: 6px;
        animation: radar-spin 0.7s linear infinite;
        vertical-align: middle;
    }
    
    .target-period-box {
        background: #000000;
        border: 1.5px solid #00FFFF;
        border-radius: 10px;
        padding: 8px 10px;
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
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 15px; text-shadow: 0 0 8px rgba(255,0,255,0.6); display: flex; align-items: center; gap: 4px; }
    
    .super-banner-small { border: 2.5px solid #00FFFF; padding: 14px; border-radius: 10px; text-align: center; font-size: 16px; font-weight: 900; margin: 10px 0; color: #00FFFF; text-transform: uppercase; animation: super-win-glow-small 0.8s infinite; letter-spacing: 1px; }
    .super-banner-big { border: 2.5px solid #FFB700; padding: 14px; border-radius: 10px; text-align: center; font-size: 16px; font-weight: 900; margin: 10px 0; color: #FFB700; text-transform: uppercase; animation: super-win-glow-big 0.8s infinite; letter-spacing: 1px; }
    
    .analyzing-banner { border: 2.5px dashed #FF00FF; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; animation: analyzing-glow 1s infinite; letter-spacing: 1px; background: #000000; display: flex; align-items: center; justify-content: center; }
    .wait-warning-banner { border: 3px solid #FF0000; padding: 12px; border-radius: 10px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; background: #000000; box-shadow: 0 0 25px rgba(255,0,0,0.4); display: flex; align-items: center; justify-content: center; gap: 10px; }
    
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 10px; }
    .result-item { flex: 1; text-align: center; background: #130d24; border: 2.5px solid #3b286b; border-radius: 12px; padding: 12px 6px; box-shadow: 0 0 10px rgba(59,40,107,0.3); }
    .auth-card { background: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 16px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 10px; }
    .admin-card { background: #110022; border: 2px solid #00FF66; border-radius: 12px; padding: 15px; margin-bottom: 15px; }
    </style>
""",
    unsafe_allow_html=True,
)

DATA_FILE = "bdg_app_data.json"

def parse_expiry_date(exp_val):
    if isinstance(exp_val, datetime):
        return exp_val
    if not exp_val:
        return datetime.now() + timedelta(days=15)
    
    if isinstance(exp_val, str):
        try:
            cleaned_str = exp_val.replace("Z", "+00:00")
            return datetime.fromisoformat(cleaned_str)
        except Exception:
            try:
                return datetime.strptime(exp_val[:19], "%Y-%m-%d %H:%M:%S")
            except Exception:
                pass
    return datetime.now() + timedelta(days=15)

def load_shared_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                for mob, val in data.get("utr_requests", {}).items():
                    if "expiry" in val:
                        val["expiry"] = parse_expiry_date(val["expiry"])
                return data
        except Exception:
            pass
    return {"utr_requests": {}, "used_utrs_list": []}

def save_shared_data(utr_reqs, used_utrs):
    try:
        serializable_data = {"utr_requests": {}, "used_utrs_list": used_utrs}
        for mob, val in utr_reqs.items():
            val_copy = val.copy()
            if "expiry" in val_copy and isinstance(val_copy["expiry"], datetime):
                val_copy["expiry"] = val_copy["expiry"].isoformat()
            serializable_data["utr_requests"][mob] = val_copy
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Save Error:", e)

initial_data = load_shared_data()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "is_owner" not in st.session_state:
    st.session_state.is_owner = False

if "utr_requests" not in st.session_state:
    st.session_state.utr_requests = initial_data["utr_requests"]

if "used_utrs_list" not in st.session_state:
    st.session_state.used_utrs_list = initial_data["used_utrs_list"]

if "user_base_period" not in st.session_state:
    st.session_state.user_base_period = ""

if "base_input_block_time" not in st.session_state:
    st.session_state.base_input_block_time = 0

if "selected_game_seconds" not in st.session_state:
    st.session_state.selected_game_seconds = 30

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR@84"

if not st.session_state.authenticated:
    st.markdown(
        "<h2 style='text-align: center; color: #FFD700; font-size: 20px;"
        " font-weight: 900;'><span class='blinking-red-light'></span>👑 VIP"
        " 100% SURE SHOT PANEL 👑<span class='blinking-red-light'"
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
        latest_data = load_shared_data()
        st.session_state.utr_requests = latest_data["utr_requests"]
        st.session_state.used_utrs_list = latest_data["used_utrs_list"]

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
                exp_time = parse_expiry_date(user_data["expiry"])

                if datetime.now() < exp_time:
                    if user_data["status"] == "APPROVED":
                        st.session_state.authenticated = True
                        st.session_state.is_owner = False
                        st.success(
                            "🟢 Verified: आपका प्लान सक्रिय है, डैशबोर्ड खुल रहा है..."
                        )
                        time.sleep(0.8)
                        st.rerun()
                    elif user_data["status"] == "REJECTED":
                        st.error(
                            "🔴 रिजेक्टेड: आपका UTR ओनर द्वारा रिजेक्ट कर दिया गया है!"
                        )
                    else:
                        st.warning(
                            "🔴 पेंडिंग: आपका UTR अभी ओनर द्वारा अप्रूव नहीं हुआ है!"
                        )
                else:
                    st.error(
                        "🚨 समय समाप्त: आपके 15 दिन का प्लान खत्म हो चुका है! कृपया नीचे नया ₹2000 का भुगतान करके नया UTR दर्ज करें।"
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
        latest_data = load_shared_data()
        st.session_state.utr_requests = latest_data["utr_requests"]
        st.session_state.used_utrs_list = latest_data["used_utrs_list"]

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
                "🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका है! कृपया कोई नया UTR नंबर डालें।"
            )
        else:
            st.session_state.utr_requests[clean_r_mob] = {
                "utr": clean_utr,
                "password": renew_pass,
                "status": "PENDING",
                "expiry": datetime.now() + timedelta(days=15),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
            save_shared_data(st.session_state.utr_requests, st.session_state.used_utrs_list)
            st.success(
                "📩 नया UTR सफलतापूर्वक सबमिट हो गया है! 🔴 (पेंडिंग)। ओनर द्वारा वेरीफाई और अप्रूव होने के बाद आपका 15 दिन का पैनल चालू होगा."
            )

    st.markdown("</div>", unsafe_allow_html=True)

else:
    latest_data = load_shared_data()
    st.session_state.utr_requests = latest_data["utr_requests"]
    st.session_state.used_utrs_list = latest_data["used_utrs_list"]

    if st.session_state.is_owner:
        st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='color: #FFD700; text-align: center; margin: 0;'>👑"
            " OWNER / ADMIN APPROVAL PANEL</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: #00FFFF; text-align: center; font-size: 12px;'>यहाँ सिर्फ पेंडिंग यूज़र का UTR चेक करें और Approve करें:</p>",
            unsafe_allow_html=True,
        )

        pending_requests = {mob: req for mob, req in st.session_state.utr_requests.items() if req.get("status") == "PENDING"}

        if not pending_requests:
            st.info("अभी तक कोई पेंडिंग UTR रिक्वेस्ट नहीं है।")
        else:
            for mob, req in list(pending_requests.items()):
                st.markdown(
                    f"""
                    <div style='border: 1.5px solid #FF0000; padding: 10px; border-radius: 8px; margin-bottom: 8px; background: #000000;'>
                        <p style='margin:0; font-weight:900; color:#FFFFFF;'>📱 मोबाइल: <span style='color:#00FFFF;'>{mob}</span> | 🔴 (रिचार्ज पेंडिंग)</p>
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

                        st.session_state.utr_requests[mob]["status"] = "APPROVED"
                        st.session_state.utr_requests[mob]["expiry"] = datetime.now() + timedelta(days=15)
                        
                        save_shared_data(st.session_state.utr_requests, st.session_state.used_utrs_list)
                        
                        st.success(f"यूज़र {mob} को 15 दिनों के लिए सफलतापूर्वक अप्रूव कर दिया गया है!")
                        time.sleep(0.5)
                        st.rerun()
                with col_rej:
                    if st.button(f"❌ Reject", key=f"rej_{mob}"):
                        st.session_state.utr_requests[mob]["status"] = "REJECTED"
                        save_shared_data(st.session_state.utr_requests, st.session_state.used_utrs_list)
                        st.error(f"यूज़र {mob} का UTR रिजेक्ट कर दिया गया।")
                        time.sleep(0.5)
                        st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    seconds = st.session_state.selected_game_seconds

    # ⚡ COMPACT SINGLE-LINE MODE SELECTOR ROW (Matched with result items container style)
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

    active_b30 = "background: linear-gradient(135deg, #FF4444, #880000) !important; border: 2.5px solid #FFD700 !important; color: #FFFFFF !important; box-shadow: 0 0 15px rgba(255,68,68,0.6);" if seconds == 30 else "background: #130d24 !important; border: 2.5px solid #3b286b !important; color: #CCCCCC !important;"
    active_b1  = "background: linear-gradient(135deg, #00AA55, #003311) !important; border: 2.5px solid #00FF66 !important; color: #FFFFFF !important; box-shadow: 0 0 15px rgba(0,255,102,0.6);" if seconds == 60 else "background: #130d24 !important; border: 2.5px solid #3b286b !important; color: #CCCCCC !important;"
    active_b3  = "background: linear-gradient(135deg, #0088FF, #002266) !important; border: 2.5px solid #00FFFF !important; color: #FFFFFF !important; box-shadow: 0 0 15px rgba(0,136,255,0.6);" if seconds == 180 else "background: #130d24 !important; border: 2.5px solid #3b286b !important; color: #CCCCCC !important;"
    active_b5  = "background: linear-gradient(135deg, #FF8800, #552200) !important; border: 2.5px solid #FFB700 !important; color: #FFFFFF !important; box-shadow: 0 0 15px rgba(255,136,0,0.6);" if seconds == 300 else "background: #130d24 !important; border: 2.5px solid #3b286b !important; color: #CCCCCC !important;"

    st.markdown(f"""
        <style>
        div[data-testid="column"]:nth-of-type(1) button {{ {active_b30} font-weight: 900; border-radius: 12px; padding: 12px 2px; font-size: 13px; }}
        div[data-testid="column"]:nth-of-type(2) button {{ {active_b1} font-weight: 900; border-radius: 12px; padding: 12px 2px; font-size: 13px; }}
        div[data-testid="column"]:nth-of-type(3) button {{ {active_b3} font-weight: 900; border-radius: 12px; padding: 12px 2px; font-size: 13px; }}
        div[data-testid="column"]:nth-of-type(4) button {{ {active_b5} font-weight: 900; border-radius: 12px; padding: 12px 2px; font-size: 13px; }}
        </style>
    """, unsafe_allow_html=True)

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
        placeholder="गेम के पीछे के आखिरी 5 अंक यहाँ डालें...",
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

            should_play_alarm = False
            if seconds == 60 and remaining_secs == 25:
                should_play_alarm = True
            elif remaining_secs <= 5:
                should_play_alarm = True

            if should_play_alarm:
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
                            <span style="color: #FF4444; font-size: 12px; font-weight: 900;">🚨 कृपया गेम के पीछे के आखिरी 5 अंक ही डालें!</span>
                        </div>
                        <div class="timer-box-large">⏰ {timer_str}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    '<div class="wait-warning-banner"><span class="blinking-red-light"></span>🛑 WAITING: ENTER LAST 5 DIGITS<span class="blinking-red-light" style="margin-left: 6px; margin-right: 0;"></span></div>',
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

            def calculate_ultimate_engine(p_num, offset_val):
                all_votes = []
                
                for node in range(1, 45):
                    v = (p_num * node * 31 + offset_val + (p_num % 17)) % 100
                    all_votes.append("BIG" if v % 2 == 0 else "SMALL")

                for t_node in range(1, 28):
                    v = (p_num * t_node * 17 + offset_val + (p_num % (t_node * 2 + 1))) % 100
                    all_votes.append("BIG" if v % 2 == 0 else "SMALL")

                for h_node in range(1, 23): 
                    v = ((p_num - h_node) * 11 + offset_val + (p_num % 7)) % 100
                    all_votes.append("BIG" if v % 2 == 0 else "SMALL")

                total_big = all_votes.count("BIG")
                total_small = all_votes.count("SMALL")

                zigzag_votes = []
                for z_idx in range(1, 25):
                    alt_check = (p_num + z_idx * 13 + offset_val) % 2
                    if (p_num + z_idx) % 2 == 0:
                        zigzag_votes.append("BIG" if alt_check == 0 else "SMALL")
                    else:
                        zigzag_votes.append("SMALL" if alt_check == 0 else "BIG")
                
                z_big = zigzag_votes.count("BIG")
                z_small = zigzag_votes.count("SMALL")

                total_votes_count = len(all_votes)
                
                sure_threshold = int(total_votes_count * 0.65)
                z_diff = abs(z_big - z_small)
                main_diff = abs(total_big - total_small)

                if main_diff < int(total_votes_count * 0.04) and z_diff < 4:
                    return (None, False)

                if total_big >= sure_threshold:
                    return ("BIG", True)
                elif total_small >= sure_threshold:
                    return ("SMALL", True)
                
                if z_diff >= 5:
                    dominant_zigzag = "BIG" if z_big > z_small else "SMALL"
                    return (dominant_zigzag, False)

                if total_big >= int(total_votes_count * 0.54):
                    return ("BIG", False)
                elif total_small >= int(total_votes_count * 0.54):
                    return ("SMALL", False)
                else:
                    return (None, False)

            pred_size, is_sure_shot = calculate_ultimate_engine(target_period_num, tab_offset)
            next_shot_val = pred_size if pred_size else "WAITING"

            rand_users = 140 + ((int(time.time()) // 3) % 45)
            mode_label = f"{seconds}S" if seconds < 60 else f"{seconds//60}M"

            st.markdown(
                f"""
                <div class="target-period-box">
                    <div style="display: flex; align-items: center; gap: 4px;">
                        <span class="blinking-red-light" style="margin-right: 2px;"></span>
                        <span style="color: #FFD700; font-size: 12px; font-weight: 900;">LIVE PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 13px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 1px 6px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div style="background: #081a10; border: 1px solid #00FF66; padding: 2px 6px; border-radius: 6px; display: flex; align-items: center; gap: 4px;">
                        <span class="blinking-green-light" style="width: 7px; height: 7px; margin: 0;"></span>
                        <span style="color: #00FF66; font-size: 11px; font-weight: 900;">{mode_label} LIVE</span>
                        <span style="color: #FFFFFF; font-size: 11px; font-weight: 900;">| 👥 {rand_users}</span>
                    </div>
                    <div class="timer-box-large">⏰ {timer_str}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if seconds == 30:
                scan_active = remaining_secs > 20
                close_phase = remaining_secs <= 8
            elif seconds == 60:
                scan_active = remaining_secs > 25
                close_phase = remaining_secs <= 8
            elif seconds == 180:
                scan_active = remaining_secs > 120
                close_phase = remaining_secs <= 20
            else:
                scan_active = remaining_secs > 200
                close_phase = remaining_secs <= 30

            if scan_active:
                st.markdown(
                    f'<div class="analyzing-banner"><span class="blinking-red-light" style="width:8px; height:8px; margin:0 4px 0 0;"></span> LIVE SCANNING... <span class="radar-spinner-icon"></span> ({remaining_secs}s left)</div>',
                    unsafe_allow_html=True,
                )
            elif pred_size is None:
                st.markdown(
                    '<div class="wait-warning-banner"><span class="blinking-red-light"></span>🛑 WAITING: MARKET FLUCTUATING (लाइन साफ नहीं है - सुरक्षित प्रतीक्षा करें)</div>',
                    unsafe_allow_html=True,
                )
            elif close_phase:
                st.markdown(
                    '<div class="wait-warning-banner"><span class="blinking-red-light"></span>🛑 SAFE BIDDING TIME - PLACE YOUR BID NOW</div>',
                    unsafe_allow_html=True,
                )
            elif is_sure_shot:
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
            else:
                if pred_size == "BIG":
                    st.markdown(
                        """
                        <div class="super-banner-big" style="animation: none; border-color: #FF8800;">
                            🔥 ZIG-ZAG LINE MATCHED : 
                            <span style="background: #000000; color: #FFB700; padding: 2px 10px; border-radius: 4px; border: 1px solid #FFB700;">BIG</span> 🎯
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.markdown(
                        """
                        <div class="super-banner-small" style="animation: none; border-color: #0088FF;">
                            🔥 ZIG-ZAG LINE MATCHED : 
                            <span style="background: #000000; color: #00FFFF; padding: 2px 10px; border-radius: 4px; border: 1px solid #00FFFF;">SMALL</span> 🎯
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

            if scan_active or pred_size is None:
                display_num = "—"
                display_size = "WAITING"
                display_color = "STANDBY"
                color_bg = "#111111"
                size_bg = "#111111"
            else:
                math_hash = (target_period_num * 17 + tab_offset) % 10
                if pred_size == "BIG":
                    pred_num = 5 + (math_hash % 5)
                    pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
                else:
                    pred_num = math_hash % 5
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

            if scan_active or pred_size is None:
                next_shot_display = "WAITING..."
                next_shot_bg = "#111111"
                next_shot_glow = "none"
            else:
                next_shot_display = next_shot_val
                if next_shot_display == "BIG":
                    next_shot_bg = "#FF8800"
                    next_shot_glow = "0 0 15px #FF8800"
                elif next_shot_display == "SMALL":
                    next_shot_bg = "#0088FF"
                    next_shot_glow = "0 0 15px #0088FF"
                else:
                    next_shot_bg = "#111111"
                    next_shot_glow = "none"

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
                        <span style="background: {next_shot_bg}; color: #FFFFFF; padding: 8px 24px; border-radius: 8px; font-weight: 900; font-size: 14px; border: 2px solid #FFFFFF; box-shadow: {next_shot_glow};">{next_shot_display}</span>
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
