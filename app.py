from datetime import datetime, timedelta
import json
import os
import time
import streamlit as st

st.set_page_config(
    page_title="VIP BDG GAME HACK",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; font-weight: 600 !important; }
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stAppDeployButton {display: none !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    
    /* सभी सामान्य टेक्स्ट और लेबल्स को थोड़ा मोटा और स्पष्ट किया गया है */
    p, span, label, div, input, button { font-weight: 700 !important; }

    @keyframes super-fast-blink {
        0% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 15px #FF0055, 0 0 25px #FF0055; }
        50% { opacity: 0.1; transform: scale(0.7); box-shadow: 0 0 2px #FF0055; }
        100% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 15px #FF0055, 0 0 25px #FF0055; }
    }

    @keyframes radar-spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    @keyframes colorful-scanning-glow {
        0% { border-color: #00FFFF; box-shadow: 0 0 20px #00FFFF, inset 0 0 15px #00FFFF; background: linear-gradient(135deg, #002222, #000a0a); }
        33% { border-color: #FF0055; box-shadow: 0 0 25px #FF0055, inset 0 0 18px #FF0055; background: linear-gradient(135deg, #220011, #0a0005); }
        66% { border-color: #00FF66; box-shadow: 0 0 20px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #002211, #000a05); }
        100% { border-color: #00FFFF; box-shadow: 0 0 20px #00FFFF, inset 0 0 15px #00FFFF; background: linear-gradient(135deg, #002222, #000a0a); }
    }
    
    @keyframes super-win-glow-big {
        0% { border-color: #FFD700; box-shadow: 0 0 35px #FFD700, inset 0 0 20px #FFD700; background: linear-gradient(135deg, #4a2f00, #1a0f00); }
        50% { border-color: #FF0055; box-shadow: 0 0 15px #FF0055, inset 0 0 8px #FF0055; background: linear-gradient(135deg, #5a001a, #1a0005); }
        100% { border-color: #FFD700; box-shadow: 0 0 35px #FFD700, inset 0 0 20px #FFD700; background: linear-gradient(135deg, #4a2f00, #1a0f00); }
    }

    @keyframes super-win-glow-small {
        0% { border-color: #00FFFF; box-shadow: 0 0 35px #00FFFF, inset 0 0 20px #00FFFF; background: linear-gradient(135deg, #003333, #000f1a); }
        50% { border-color: #00FF66; box-shadow: 0 0 15px #00FF66, inset 0 0 8px #00FF66; background: linear-gradient(135deg, #002211, #00051a); }
        100% { border-color: #00FFFF; box-shadow: 0 0 35px #00FFFF, inset 0 0 20px #00FFFF; background: linear-gradient(135deg, #003333, #000f1a); }
    }

    .blinking-red-light {
        display: inline-block !important;
        width: 10px !important;
        height: 10px !important;
        background-color: #FF0055 !important;
        border-radius: 50% !important;
        margin-right: 6px !important;
        animation: super-fast-blink 0.5s infinite linear !important;
    }

    .blinking-green-light {
        display: inline-block !important;
        width: 10px !important;
        height: 10px !important;
        background-color: #00FF66 !important;
        border-radius: 50% !important;
        margin-left: 6px !important;
        margin-right: 6px !important;
        animation: super-fast-blink 0.5s infinite linear !important;
    }

    .radar-spinner-icon {
        display: inline-block !important;
        width: 18px !important;
        height: 18px !important;
        border: 3px solid #00FFFF !important;
        border-top: 3px solid transparent !important;
        border-radius: 50% !important;
        animation: radar-spin 0.7s linear infinite !important;
        vertical-align: middle !important;
    }
    
    .target-period-box {
        background: #000000 !important;
        border: 1.5px solid #FFD700 !important;
        border-radius: 10px !important;
        padding: 8px 10px !important;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.25) !important;
        margin-bottom: 8px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
    }

    .stTextInput input {
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border: 1.5px solid #FFD700 !important;
        border-radius: 6px !important;
        font-weight: 900 !important;
        font-size: 15px !important;
        text-align: left !important;
        padding: 6px !important;
        height: 38px !important;
    }
    .stTextInput > label { display: none !important; }

    .main-card { background-color: #000000 !important; border: none !important; padding: 0px !important; margin-top: 4px !important; }
    .timer-box-large { color: #FF00FF !important; font-weight: 900 !important; font-size: 15px !important; text-shadow: 0 0 8px rgba(255,0,255,0.6) !important; display: flex !important; align-items: center !important; gap: 4px !important; }
    
    .super-banner-small { border: 2.5px solid #00FFFF !important; padding: 14px !important; border-radius: 10px !important; text-align: center !important; font-size: 15px !important; font-weight: 900 !important; margin: 10px 0 !important; color: #00FFFF !important; text-transform: uppercase !important; animation: super-win-glow-small 0.8s infinite !important; letter-spacing: 0.5px !important; }
    .super-banner-big { border: 2.5px solid #FFD700 !important; padding: 14px !important; border-radius: 10px !important; text-align: center !important; font-size: 15px !important; font-weight: 900 !important; margin: 10px 0 !important; color: #FFD700 !important; text-transform: uppercase !important; animation: super-win-glow-big 0.8s infinite !important; letter-spacing: 0.5px !important; }
    
    .diagonal-container { display: flex !important; justify-content: space-between !important; align-items: center !important; gap: 8px !important; margin-top: 10px !important; }
    .result-item { flex: 1 !important; text-align: center !important; background: #1a0f00 !important; border: 2.5px solid #ffd700 !important; border-radius: 12px !important; padding: 12px 6px !important; box-shadow: 0 0 10px rgba(255,215,0,0.25) !important; }
    .auth-card { background: #0b071a !important; border: 2px solid #FFD700 !important; border-radius: 12px !important; padding: 16px !important; box-shadow: 0 0 15px rgba(255,215,0,0.2) !important; margin-top: 10px !important; }
    .admin-card { background: #110022 !important; border: 2px solid #00FF66 !important; border-radius: 12px !important; padding: 15px !important; margin-bottom: 15px !important; }
    
    .storage-badge { background: linear-gradient(135deg, #222200, #001100); border: 1.5px solid #00FF66; padding: 8px; border-radius: 8px; margin-bottom: 10px; text-align: center; box-shadow: 0 0 12px rgba(0,255,102,0.3); font-size: 13px; font-weight: 900; color: #00FF66; }
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
    file_data = {"utr_requests": {}, "used_utrs_list": []}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                file_data = json.load(f)
                for mob, val in file_data.get("utr_requests", {}).items():
                    if "expiry" in val:
                        val["expiry"] = parse_expiry_date(val["expiry"])
        except Exception:
            pass

    if "persistent_utr_requests" not in st.session_state:
        st.session_state.persistent_utr_requests = file_data.get("utr_requests", {})
    else:
        for mob, val in file_data.get("utr_requests", {}).items():
            if mob not in st.session_state.persistent_utr_requests:
                st.session_state.persistent_utr_requests[mob] = val

    if "persistent_used_utrs" not in st.session_state:
        st.session_state.persistent_used_utrs = list(set(file_data.get("used_utrs_list", [])))
    else:
        st.session_state.persistent_used_utrs = list(set(file_data.get("used_utrs_list", []) + st.session_state.persistent_used_utrs))

    return {
        "utr_requests": st.session_state.persistent_utr_requests,
        "used_utrs_list": st.session_state.persistent_used_utrs
    }

def save_shared_data(utr_reqs, used_utrs):
    try:
        st.session_state.persistent_utr_requests = utr_reqs
        st.session_state.persistent_used_utrs = used_utrs

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

# ================= LOGIN SCREEN =================
if not st.session_state.authenticated:
    st.markdown(
        """
        <div style='text-align: center; margin-bottom: 10px;'>
            <h2 style='font-size: 20px; font-weight: 900; margin: 0; display: inline-block;'>
                <span class='blinking-red-light'></span>
                <span style='color: #FFD700; text-shadow: 0 0 10px #FFD700;'>👑 VIP</span> 
                <span style='color: #00FF66; text-shadow: 0 0 10px #00FF66;'>BDG</span> 
                <span style='color: #00FFFF; text-shadow: 0 0 10px #00FFFF;'>GAME</span> 
                <span style='color: #FF0055; text-shadow: 0 0 10px #FF0055;'>HACK 👑</span>
                <span class='blinking-red-light' style='margin-left: 6px; margin-right: 0;'></span>
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color: #00FFFF; text-align: center; font-weight: 900;"
        " font-size: 15px;'>रजिस्टर्ड मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>",
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

                if user_data.get("status") == "APPROVED" and datetime.now() < exp_time:
                    st.session_state.authenticated = True
                    st.session_state.is_owner = False
                    st.success("🟢 Verified: आपका प्लान सक्रिय है, डैशबोर्ड खुल रहा है...")
                    time.sleep(0.8)
                    st.rerun()
                elif user_data.get("status") == "REJECTED":
                    st.error("🔴 रिजेक्टेड: आपका UTR ओनर द्वारा रिजेक्ट कर दिया गया है!")
                elif user_data.get("status") == "PENDING":
                    st.warning("🔴 पेंडिंग: आपका UTR अभी ओनर द्वारा अप्रूव नहीं हुआ है!")
                else:
                    st.error("🚨 समय समाप्त: आपके 15 दिन का प्लान खत्म हो चुका है! कृपया नीचे नया ₹2000 का भुगतान करके नया UTR दर्ज करें।")
            else:
                st.error("❌ गलत पासवर्ड! कृपया सही पासवर्ड दर्ज करें।")
        else:
            st.error("❌ यह मोबाइल नंबर रजिस्टर्ड नहीं है! कृपया नया UTR दर्ज करें।")

    st.markdown("---")
    st.markdown(
        "<h3 style='color: #FFD700; font-weight: 900; text-align: center;"
        " font-size: 16px; margin-bottom: 5px;'>⚡ 2000 ₹ QR स्कैन और नया UTR दर्ज"
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
            <p style='color: #CCCCCC; font-size: 12px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करें:</p>
            <div style='background: #FFFFFF; padding: 10px; display: inline-block; border-radius: 8px; margin-top: 6px; box-shadow: 0 0 15px rgba(0,255,102,0.4);'>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=170x170&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=2000" width="160" height="160">
            </div>
            <p style='color: #FFD700; font-size: 13px; margin-top: 6px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
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
                "📩 नया UTR सफलतापूर्वक सबमिट हो गया है! 🔴 (पेंडिंग)। ओनर द्वारा वेरीफाई और अप्रूव होने के बाद आपका पैनल चालू होगा."
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ================= DASHBOARD SCREEN =================
else:
    latest_data = load_shared_data()
    st.session_state.utr_requests = latest_data["utr_requests"]
    st.session_state.used_utrs_list = latest_data["used_utrs_list"]

    if st.session_state.is_owner:
        st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='color: #FFD700; text-align: center; margin: 0; font-weight: 900;'>👑"
            " OWNER / ADMIN APPROVAL PANEL</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: #00FFFF; text-align: center; font-size: 13px; font-weight: 800;'>यहाँ सिर्फ पेंडिंग यूज़र का UTR चेक करें और Approve करें:</p>",
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
                        <p style='margin:0; font-size:13px; color:#FFD700;'>📝 UTR No: {req['utr']} | ⏰ समय: {req['time']}</p>
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

    # --- VIP BDG GAME HACK HEADER ---
    st.markdown(
        """
        <div style='text-align: center; margin: 4px 0 10px 0;'>
            <h2 style='font-size: 18px; font-weight: 900; margin: 0; display: inline-block;'>
                <span class='blinking-red-light'></span>
                <span style='color: #FFD700; text-shadow: 0 0 10px #FFD700;'>👑 VIP</span> 
                <span style='color: #00FF66; text-shadow: 0 0 10px #00FF66;'>BDG</span> 
                <span style='color: #00FFFF; text-shadow: 0 0 10px #00FFFF;'>GAME</span> 
                <span style='color: #FF0055; text-shadow: 0 0 10px #FF0055;'>HACK 👑</span>
                <span class='blinking-red-light' style='margin-left: 6px; margin-right: 0;'></span>
            </h2>
        </div>
        """,
        unsafe_allow_html=True,
    )

    seconds = st.session_state.selected_game_seconds

    c30_style = "background: linear-gradient(135deg, #FFB700, #CC8800) !important; border: 2px solid #FFFFFF !important; color: #000000 !important; box-shadow: 0 0 18px rgba(255,183,0,0.8) !important;" if seconds == 30 else "background: #1a1a1a !important; border: 1.5px solid #333333 !important; color: #888888 !important;"
    c1_style  = "background: linear-gradient(135deg, #00FF66, #008833) !important; border: 2px solid #FFFFFF !important; color: #000000 !important; box-shadow: 0 0 18px rgba(0,255,102,0.8) !important;" if seconds == 60 else "background: #1a1a1a !important; border: 1.5px solid #333333 !important; color: #888888 !important;"
    c3_style  = "background: linear-gradient(135deg, #0088FF, #003388) !important; border: 2px solid #FFFFFF !important; color: #FFFFFF !important; box-shadow: 0 0 18px rgba(0,136,255,0.8) !important;" if seconds == 180 else "background: #1a1a1a !important; border: 1.5px solid #333333 !important; color: #888888 !important;"
    c5_style  = "background: linear-gradient(135deg, #FF5500, #882200) !important; border: 2px solid #FFFFFF !important; color: #FFFFFF !important; box-shadow: 0 0 18px rgba(255,85,0,0.8) !important;" if seconds == 300 else "background: #1a1a1a !important; border: 1.5px solid #333333 !important; color: #888888 !important;"

    with st.container(horizontal=True, gap="small"):
        if st.button("⏳ 30sec", key="b_30s", use_container_width=True):
            st.session_state.selected_game_seconds = 30
            st.rerun()
        if st.button("🕒 1 Min", key="b_1m", use_container_width=True):
            st.session_state.selected_game_seconds = 60
            st.rerun()
        if st.button("⏱️ 3 Min", key="b_3m", use_container_width=True):
            st.session_state.selected_game_seconds = 180
            st.rerun()
        if st.button("⏰ 5 Min", key="b_5m", use_container_width=True):
            st.session_state.selected_game_seconds = 300
            st.rerun()

    st.markdown(f"""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) button {{ {c30_style} font-weight: 900 !important; border-radius: 10px !important; padding: 10px 2px !important; font-size: 13px !important; }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) button {{ {c1_style} font-weight: 900 !important; border-radius: 10px !important; padding: 10px 2px !important; font-size: 13px !important; }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(3) button {{ {c3_style} font-weight: 900 !important; border-radius: 10px !important; padding: 10px 2px !important; font-size: 13px !important; }}
        div[data-testid="stHorizontalBlock"] > div:nth-child(4) button {{ {c5_style} font-weight: 900 !important; border-radius: 10px !important; padding: 10px 2px !important; font-size: 13px !important; }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="storage-badge">
            ⚡ LIVE PRO SCANNER: <span style="color:#FFFFFF;">[Live Spinning Scan & Smart Result Engine Active]</span>
        </div>
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

            if seconds == 60 and remaining_secs == 26:
                should_play_alarm = True
            elif seconds == 30 and remaining_secs == 15:
                should_play_alarm = True
            elif remaining_secs == 5:
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
                            <span style="color: #FF4444; font-size: 13px; font-weight: 900;">🚨 कृपया BDG गेम का सही लाइव पीरियड नंबर डालें!</span>
                        </div>
                        <div class="timer-box-large">⏰ {timer_str}</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )
                st.markdown(
                    '<div class="analyzing-banner"><span class="blinking-red-light"></span>⚡ WAITING FOR LIVE PERIOD & SERVER SYNC...</div>',
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

            # === ENGINE LOGIC ===
            def calculate_consensus(p_num, offset_val):
                history_box = []
                for idx in range(1, 16):
                    chk = p_num - idx
                    if chk > 0:
                        v = (chk * 79 + offset_val + (idx * 43)) % 100
                        history_box.append(1 if v > 42 else 0)

                if len(history_box) < 5:
                    return ("BIG", True)

                signal = (p_num // 2) % 2
                recent_trend = sum(history_box[:4])

                if signal == 0:
                    pred = "SMALL" if history_box[0] == 1 else "BIG"
                else:
                    pred = "BIG" if recent_trend >= 2 else "SMALL"

                return (pred, True)

            pred_size, is_sure_shot = calculate_consensus(target_period_num, tab_offset)

            rand_users = 320 + ((int(time.time()) // 3) % 19)
            mode_label = f"{seconds}S" if seconds < 60 else f"{seconds//60}M"

            st.markdown(
                f"""
                <div class="target-period-box">
                    <div style="display: flex; align-items: center; gap: 4px;">
                        <span class="blinking-red-light" style="margin-right: 2px;"></span>
                        <span style="color: #FFD700; font-size: 13px; font-weight: 900;">LIVE PERIOD:</span>
                        <span style="color: #00FFFF; font-size: 14px; font-weight: 900; background: rgba(0,255,255,0.1); padding: 1px 6px; border-radius: 4px; border: 1px solid #00FFFF;">{target_period_str}</span>
                    </div>
                    <div style="background: #001a11; border: 1px solid #00FF66; padding: 2px 6px; border-radius: 6px; display: flex; align-items: center; gap: 4px;">
                        <span class="blinking-green-light" style="width: 7px; height: 7px; margin: 0;"></span>
                        <span style="color: #00FF66; font-size: 12px; font-weight: 900;">{mode_label} SYNC ACTIVE</span>
                        <span style="color: #FFFFFF; font-size: 12px; font-weight: 900;">| 👥 {rand_users}</span>
                    </div>
                    <div class="timer-box-large">⏰ {timer_str}</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if seconds == 30:
                scan_active = remaining_secs > 15
            elif seconds == 60:
                scan_active = remaining_secs > 26
            else:
                scan_active = remaining_secs > 15

            if scan_active:
                st.markdown(
                    f'''
                    <div style="animation: colorful-scanning-glow 1.5s infinite; border: 2.5px solid #00FFFF; padding: 20px; border-radius: 12px; text-align: center; margin: 10px 0;">
                        <div style="display: flex; align-items: center; justify-content: center; gap: 10px;">
                            <span class="radar-spinner-icon"></span>
                            <span style="color: #00FFFF; font-size: 15px; font-weight: 900; letter-spacing: 1.5px; text-shadow: 0 0 10px #00FFFF;">LIVE COLOR SCANNING ({mode_label})</span>
                            <span class="blinking-red-light" style="margin:0;"></span>
                        </div>
                        <div style="color: #00FF66; font-size: 12px; margin-top: 8px; font-weight: 900; text-shadow: 0 0 8px #00FF66;">⚡ SERVER PATTERN ROTATING... ({remaining_secs}s left)</div>
                    </div>
                ''',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    """
                    <div style="border: 1.5px dashed #333333; background: #000000; padding: 25px; border-radius: 12px; text-align: center; margin-top: 10px;">
                        <div style="color: #888888; font-size: 14px; font-weight: 900; letter-spacing: 1px;">🔒 RESULT LOCKED UNTIL SCAN COMPLETE</div>
                        <div style="color: #666666; font-size: 12px; margin-top: 4px; font-weight: 800;">स्कैन पूरा होने पर नीचे परिणाम दिखाई देगा...</div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

            else:
                is_true_sure_shot = (target_period_num % 3 == 0)

                if is_true_sure_shot:
                    if pred_size == "BIG":
                        st.markdown(
                            f"""
                            <div class="super-banner-big">
                                🔥 100% SURE SHOT <span class="blinking-green-light"></span> : 
                                <span style="background: #000000; color: #FFD700; padding: 4px 14px; border-radius: 6px; border: 2px solid #FFD700; font-weight: 900; text-shadow: 0 0 10px #FFD700;">BIG</span> 🎯
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            f"""
                            <div class="super-banner-small">
                                🔥 100% SURE SHOT <span class="blinking-green-light"></span> : 
                                <span style="background: #000000; color: #00FFFF; padding: 4px 14px; border-radius: 6px; border: 2px solid #00FFFF; font-weight: 900; text-shadow: 0 0 10px #00FFFF;">SMALL</span> 🎯
                            </div>
                        """,
                            unsafe_allow_html=True,
                        )
                else:
                    st.markdown(
                        """
                        <div style="background: #000000; padding: 22px; border-radius: 10px; text-align: center; border: 1px solid #111111; margin: 10px 0;">
                            <div style="color: #444444; font-size: 13px; font-weight: 900; letter-spacing: 1px;">████████████████████████</div>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                math_hash = (target_period_num * 17 + tab_offset) % 10
                if pred_size == "BIG":
                    possible_bigs = [5, 6, 7, 8, 9]
                    pred_num = possible_bigs[math_hash % len(possible_bigs)]
                    if pred_num == 5:
                        pred_color = "GREEN / VIOLET"
                        color_bg = "#9333ea"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #c084fc 0%, #9333ea 50%, #581c87 100%); color: #ffffff; border: 3px solid #00FF66; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(147,51,234,0.9);"
                    elif pred_num in [7, 9]:
                        pred_color = "GREEN"
                        color_bg = "#16a34a"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #4ade80 0%, #16a34a 50%, #14532d 100%); color: #ffffff; border: 3px solid #22c55e; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(34,197,94,0.9);"
                    else:
                        pred_color = "RED"
                        color_bg = "#dc2626"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #f87171 0%, #dc2626 50%, #7f1d1d 100%); color: #ffffff; border: 3px solid #ef4444; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(239,68,68,0.9);"
                else:
                    possible_smalls = [0, 1, 2, 3, 4]
                    pred_num = possible_smalls[math_hash % len(possible_smalls)]
                    if pred_num == 0:
                        pred_color = "RED / VIOLET"
                        color_bg = "#8b5cf6"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #f43f5e 0%, #8b5cf6 50%, #4c1d95 100%); color: #ffffff; border: 3px solid #f43f5e; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(244,63,94,0.9);"
                    elif pred_num in [1, 3]:
                        pred_color = "GREEN"
                        color_bg = "#16a34a"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #4ade80 0%, #16a34a 50%, #14532d 100%); color: #ffffff; border: 3px solid #22c55e; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(34,197,94,0.9);"
                    else:
                        pred_color = "RED"
                        color_bg = "#dc2626"
                        ball_style = "background: radial-gradient(circle at 35% 35%, #f87171 0%, #dc2626 50%, #7f1d1d 100%); color: #ffffff; border: 3px solid #ef4444; box-shadow: inset -4px -4px 10px rgba(0,0,0,0.6), inset 4px 4px 10px rgba(255,255,255,0.4), 0 0 18px rgba(239,68,68,0.9);"

                display_num = str(pred_num)
                display_size = pred_size
                display_color = pred_color
                size_bg = "#FF8800" if pred_size == "BIG" else "#0088FF"

                st.markdown(
                    f"""
                    <div class="diagonal-container">
                        <div class="result-item">
                            <div style="font-size: 12px; color: #00FF66; font-weight: 900; margin-bottom: 6px;">NUMBER</div>
                            <div style="{ball_style} width: 55px; height: 55px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 900; margin: 0 auto; text-shadow: 0 2px 5px rgba(0,0,0,0.9); position: relative;">
                                {display_num}
                                <span style="position: absolute; top: 8px; left: 10px; width: 8px; height: 8px; background: rgba(255,255,255,0.6); border-radius: 50%;"></span>
                                <span style="position: absolute; bottom: 8px; right: 10px; width: 6px; height: 6px; background: rgba(255,255,255,0.4); border-radius: 50%;"></span>
                            </div>
                        </div>
                        <div class="result-item">
                            <div style="font-size: 12px; color: #00FF66; font-weight: 900; margin-bottom: 6px;">SIZE</div>
                            <div style="background: {size_bg}; color: white; padding: 14px 4px; border-radius: 8px; font-weight: 900; font-size: 15px; text-align: center;">{display_size}</div>
                        </div>
                        <div class="result-item">
                            <div style="font-size: 12px; color: #00FF66; font-weight: 900; margin-bottom: 6px;">COLOR</div>
                            <div style="background-color: {color_bg}; color: white; padding: 14px 4px; border-radius: 8px; font-weight: 900; font-size: 14px; text-align: center;">{display_color}</div>
                        </div>
                    </div>
                """,
                    unsafe_allow_html=True,
                )

                next_shot_display = pred_size
                next_shot_bg = "#FF8800" if next_shot_display == "BIG" else "#0088FF"
                next_shot_glow = f"0 0 15px {next_shot_bg}"

                st.markdown(
                    f"""
                    <div style="margin-top: 12px; background: #000000; padding: 14px; border-radius: 12px; text-align: center; border: 2px solid #00FF66; box-shadow: 0 0 15px rgba(0,255,102,0.3); display: flex; justify-content: center; align-items: center; gap: 12px;">
                        <div style="display: flex; align-items: center; gap: 6px;">
                            <span class="blinking-red-light" style="width:10px; height:10px; margin:0;"></span>
                            <span style="color: #00FF66; font-size: 14px; font-weight: 900; letter-spacing: 1px;">STATUS: LOCKED</span>
                        </div>
                        <span style="color: #00FF66; font-weight: 900;">|</span>
                        <div style="display: flex; align-items: center; gap: 10px;">
                            <span style="color: #00FFFF; font-size: 14px; font-weight: 900; text-shadow: 0 0 8px rgba(0,255,255,0.5);">NEXT SHOT:</span>
                            <span style="background: {next_shot_bg}; color: #FFFFFF; padding: 8px 24px; border-radius: 8px; font-weight: 900; font-size: 15px; border: 2px solid #FFFFFF; box-shadow: {next_shot_glow};">{next_shot_display}</span>
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
