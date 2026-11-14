from datetime import datetime, timedelta
import json
import os
import time
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="VIP PRO SCANNER PANEL",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #000000 !important; color: #FFFFFF !important; }
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stAppDeployButton {display: none !important;}
    [data-testid="stStatusWidget"] {visibility: hidden !important;}
    
    @keyframes super-fast-blink {
        0% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 12px #FF0055, 0 0 20px #FF0055; }
        50% { opacity: 0.1; transform: scale(0.7); box-shadow: 0 0 2px #FF0055; }
        100% { opacity: 1; transform: scale(1.3); box-shadow: 0 0 12px #FF0055, 0 0 20px #FF0055; }
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

    @keyframes vip-zipzap {
        0% { color: #FFD700; text-shadow: 0 0 8px #FFD700, 0 0 15px #FF0055; }
        50% { color: #00FFFF; text-shadow: 0 0 12px #00FFFF, 0 0 20px #00FF66; }
        100% { color: #FFD700; text-shadow: 0 0 8px #FFD700, 0 0 15px #FF0055; }
    }

    @keyframes pro-zipzap {
        0% { color: #FF0055; text-shadow: 0 0 8px #FF0055, 0 0 15px #FFD700; }
        50% { color: #00FF66; text-shadow: 0 0 12px #00FF66, 0 0 20px #00FFFF; }
        100% { color: #FF0055; text-shadow: 0 0 8px #FF0055, 0 0 15px #FFD700; }
    }

    @keyframes panel-zipzap {
        0% { color: #00FFFF; text-shadow: 0 0 8px #00FFFF, 0 0 15px #00FF66; }
        50% { color: #FFD700; text-shadow: 0 0 12px #FFD700, 0 0 20px #FF0055; }
        100% { color: #00FFFF; text-shadow: 0 0 8px #00FFFF, 0 0 15px #00FF66; }
    }

    .vip-word { animation: vip-zipzap 1.2s infinite ease-in-out; font-weight: 900; margin: 0 2px; }
    .pro-word { animation: pro-zipzap 1.2s infinite ease-in-out; font-weight: 900; margin: 0 2px; }
    .panel-word { animation: panel-zipzap 1.2s infinite ease-in-out; font-weight: 900; margin: 0 2px; }

    /* यहाँ हेडिंग की साइज को कॉम्पैक्ट और स्लिम कर दिया है ताकि मोबाइल में फिट बैठे */
    .vip-pro-heading {
        text-align: center;
        font-size: 16px;
        font-weight: 900;
        letter-spacing: 0.3px;
        margin-bottom: 8px;
        padding: 4px 0;
        white-space: nowrap;
    }

    .blinking-red-light {
        display: inline-block !important;
        width: 8px !important;
        height: 8px !important;
        background-color: #FF0055 !important;
        border-radius: 50% !important;
        margin-right: 4px !important;
        animation: super-fast-blink 0.5s infinite linear !important;
    }

    .blinking-green-light {
        display: inline-block !important;
        width: 8px !important;
        height: 8px !important;
        background-color: #00FF66 !important;
        border-radius: 50% !important;
        margin-left: 4px !important;
        margin-right: 4px !important;
        animation: super-fast-blink 0.5s infinite linear !important;
    }

    .radar-spinner-icon {
        display: inline-block !important;
        width: 18px !important;
        height: 18px !important;
        border: 3px solid #00FFFF !important;
        border-top: 3px solid transparent !important;
        border-radius: 50% !important;
        animation: radar-spin 0.6s linear infinite !important;
        vertical-align: middle !important;
        box-shadow: 0 0 8px #00FFFF;
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
    </style>
""",
    unsafe_allow_html=True,
)

DATA_FILE = "bdg_app_titanium_vault.json"

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

    if "titanium_vault_requests" not in st.session_state:
        st.session_state.titanium_vault_requests = file_data.get("utr_requests", {})
    else:
        for mob, val in file_data.get("utr_requests", {}).items():
            if mob not in st.session_state.titanium_vault_requests:
                st.session_state.titanium_vault_requests[mob] = val

    if "titanium_vault_used_utrs" not in st.session_state:
        st.session_state.titanium_vault_used_utrs = list(set(file_data.get("used_utrs_list", [])))
    else:
        st.session_state.titanium_vault_used_utrs = list(set(file_data.get("used_utrs_list", []) + st.session_state.titanium_vault_used_utrs))

    return {
        "utr_requests": st.session_state.titanium_vault_requests,
        "used_utrs_list": st.session_state.titanium_vault_used_utrs
    }

def save_shared_data(utr_reqs, used_utrs):
    try:
        st.session_state.titanium_vault_requests = utr_reqs
        st.session_state.titanium_vault_used_utrs = used_utrs

        serializable_data = {"utr_requests": {}, "used_utrs_list": used_utrs}
        for mob, val in utr_reqs.items():
            val_copy = val.copy()
            if "expiry" in val_copy and isinstance(val_copy["expiry"], datetime):
                val_copy["expiry"] = val_copy["expiry"].isoformat()
            serializable_data["utr_requests"][mob] = val_copy
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(serializable_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Vault Save Error:", e)

initial_data = load_shared_data()

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "is_owner" not in st.session_state:
    st.session_state.is_owner = False

components.html(
    """
    <script>
    try {
        const savedAuth = localStorage.getItem('vip_titanium_auth');
        const savedExpiry = localStorage.getItem('vip_titanium_expiry');
        if (savedAuth && savedExpiry) {
            const expDate = new Date(savedExpiry);
            if (new Date() < expDate) {
                // Active session valid
            }
        }
    } catch(e) {}
    </script>
    """,
    height=0,
)

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
        """
        <h2 class='vip-pro-heading'>
            <span class='blinking-red-light'></span>
            👑 <span class='vip-word'>VIP</span> <span class='pro-word'>PRO</span> <span class='panel-word'>PANEL</span> 👑
            <span class='blinking-red-light' style='margin-left: 4px; margin-right: 0;'></span>
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='auth-card'>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='color: #00FFFF; text-align: center; font-weight: 900;"
        " font-size: 13px;'>रजिस्टर्ड मोबाइल नंबर और पासवर्ड से लॉगिन करें</h4>",
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
                curr_time = datetime.now()

                if user_data.get("status") == "APPROVED" and curr_time < exp_time:
                    st.session_state.authenticated = True
                    st.session_state.is_owner = False
                    
                    exp_iso = exp_time.isoformat()
                    components.html(f"""
                        <script>
                            try {{
                                localStorage.setItem('vip_titanium_auth', '{clean_l_mob}');
                                localStorage.setItem('vip_titanium_expiry', '{exp_iso}');
                            }} catch(e) {{}}
                        </script>
                    """, height=0)

                    st.success("🟢 Verified: आपका 15 दिन का प्लान सुरक्षित रूप से सक्रिय है...")
                    time.sleep(0.8)
                    st.rerun()
                elif user_data.get("status") == "REJECTED":
                    st.error("🔴 रिजेक्टेड: आपका UTR ओनर द्वारा रिजेक्ट कर दिया गया है!")
                elif user_data.get("status") == "PENDING":
                    st.warning("🔴 पेंडिंग: आपका UTR अभी ओनर द्वारा अप्रूव नहीं हुआ है!")
                else:
                    st.error("🚨 समय समाप्त: आपके 15 दिन पूरे हो चुके हैं! कृपया नया ₹2000 का भुगतान करके नया UTR दर्ज करें।")
            else:
                st.error("❌ गलत पासवर्ड! कृपया सही पासवर्ड दर्ज करें।")
        else:
            st.error("❌ यह मोबाइल नंबर रजिस्टर्ड नहीं है! कृपया नया UTR दर्ज करें।")

    st.markdown("---")
    st.markdown(
        "<h3 style='color: #FFD700; font-weight: 900; text-align: center;"
        " font-size: 14px; margin-bottom: 5px;'>⚡ 2000 ₹ QR स्कैन और नया UTR दर्ज"
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
            <p style='color: #00FF66; font-size: 13px; font-weight: 900; margin: 0;'>💎 15 दिन समाप्त होने पर ₹2000 का भुगतान करके नया UTR डालें (15 Days Plan)</p>
            <p style='color: #CCCCCC; font-size: 11px; margin-top: 4px;'>नीचे दिए गए PhonePe QR को स्कैन करें:</p>
            <div style='background: #FFFFFF; padding: 10px; display: inline-block; border-radius: 8px; margin-top: 6px; box-shadow: 0 0 15px rgba(0,255,102,0.4);'>
                <img src="https://api.qrserver.com/v1/create-qr-code/?size=160x160&data=upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=KishorSinghRautela&am=2000" width="150" height="150">
            </div>
            <p style='color: #FFD700; font-size: 11px; margin-top: 6px; font-weight: 900;'>UPI ID: kishorsingh226105.wallet@phonepe</p>
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

else:
    latest_data = load_shared_data()
    st.session_state.utr_requests = latest_data["utr_requests"]
    st.session_state.used_utrs_list = latest_data["used_utrs_list"]

    if st.session_state.is_owner:
        st.markdown("<div class='admin-card'>", unsafe_allow_html=True)
        st.markdown(
            "<h3 style='color: #FFD700; text-align: center; margin: 0; font-size: 15px;'>👑"
            " OWNER / ADMIN APPROVAL PANEL</h3>",
            unsafe_allow_html=True,
        )
        st.markdown(
            "<p style='color: #00FFFF; text-align: center; font-size: 11px;'>यहाँ सिर्फ पेंडिंग यूज़र का UTR चेक करें और Approve करें:</p>",
            unsafe_allow_html=True,
        )

        pending_requests = {mob: req for mob, req in st.session_state.utr_requests.items() if req.get("status") == "PENDING"}

        if not pending_requests:
            st.info("अभी तक कोई पेंडिंग UTR रिक्वेस्ट नहीं है।")
        else:
            for mob, req in list(pending_requests.items()):
                st.markdown(
                    f"""
                    <div style='border: 1.5px solid #FF0000; padding: 8px; border-radius: 8px; margin-bottom: 8px; background: #000000;'>
                        <p style='margin:0; font-weight:900; color:#FFFFFF; font-size: 12px;'>📱 मोबाइल: <span style='color:#00FFFF;'>{mob}</span> | 🔴 (रिचार्ज पेंडिंग)</p>
                        <p style='margin:0; font-size:11px; color:#FFD700;'>📝 UTR No: {req['utr']} | ⏰ समय: {req['time']}</p>
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
                        
                        st.success(f"यूज़र {mob} को 15 दिनों के लिए Titanium Security के साथ अप्रूव कर दिया गया है!")
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

    c30_style = "background: linear-gradient(135deg, #FFB700, #CC8800) !important; border: 2px solid #FFFFFF !important; color: #000000 !important; box-shadow: 0 0 18px rgba(255,183,0,0.8) !important;" if seconds == 30 else "background: #1a1a1a !important; border: 1.5px solid #333333 !important; color: #888888 !important;"
    c1_style  = "background: linear-gradient(135deg, #00FF66, #008833) !important; border: 2px solid #FFFFFF !important; color: #000000 !important; box-shadow: 0 0 18px rgba(0,255,102,0.8) !important;" if seconds == 60 else "background: #1a1a1a !important; border: 1.5
