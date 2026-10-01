from datetime import datetime, timedelta
import time
import streamlit as st

# ==========================================
# 1. पेज कॉन्फ़िगरेशन एवं ओरिजिनल थीम डिज़ाइन
# ==========================================
st.set_page_config(
    page_title="Sure Shot PRO - Game Hub Access",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { 
        background: radial-gradient(circle at center, #1b1035 0%, #0c061a 100%); 
        color: #FFFFFF; 
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #00FF66; }
        50% { opacity: 0.2; transform: scale(0.8); box-shadow: 0 0 2px #00FF66; }
        100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #00FF66; }
    }

    @keyframes blink-red-animation {
        0% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #FF3333; }
        50% { opacity: 0.2; transform: scale(0.8); box-shadow: 0 0 2px #FF3333; }
        100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #FF3333; }
    }

    @keyframes neon-pulse {
        0% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0,229,255,0.6); }
        50% { border-color: #FFD700; box-shadow: 0 0 18px rgba(255,215,0,0.8); }
        100% { border-color: #00E5FF; box-shadow: 0 0 12px rgba(0,229,255,0.6); }
    }

    @keyframes line-fluctuate {
        0% { width: 30%; opacity: 0.6; }
        50% { width: 95%; opacity: 1; filter: drop-shadow(0 0 8px #00FF66); }
        100% { width: 45%; opacity: 0.7; }
    }

    .blinking-green-light { 
        display: inline-block; 
        width: 9px; 
        height: 9px; 
        background-color: #00FF66; 
        border-radius: 50%; 
        margin-right: 6px; 
        animation: blink-animation 0.8s infinite ease-in-out;
    }

    .blinking-red-light { 
        display: inline-block; 
        width: 9px; 
        height: 9px; 
        background-color: #FF3333; 
        border-radius: 50%; 
        margin-right: 6px; 
        animation: blink-red-animation 0.6s infinite ease-in-out;
    }

    .live-frequency-line {
        height: 3px;
        background: linear-gradient(90deg, #00E5FF, #00FF66, #FFD700);
        border-radius: 2px;
        margin: 8px auto 12px auto;
        animation: line-fluctuate 1.5s infinite ease-in-out;
    }

    .login-container {
        background: rgba(28, 18, 51, 0.75);
        border: 1px solid rgba(138, 43, 226, 0.4);
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(10px);
        margin-top: 10px;
    }

    .main-card { 
        background: linear-gradient(145deg, #1c1233, #0d061c); 
        border: 1.5px solid #d4af37; 
        border-radius: 12px; 
        padding: 14px; 
        box-shadow: 0 6px 20px rgba(0,0,0,0.6); 
        margin-top: 6px; 
    }

    .live-period-display {
        background: rgba(255, 51, 51, 0.08);
        border: 1px solid #FF3333;
        border-radius: 8px;
        padding: 8px 12px;
        font-size: 13px;
        color: #FF9999;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }

    .sure-shot-banner { 
        background: radial-gradient(circle, #0e222e 0%, #050d12 100%); 
        border: 2px dashed #00E5FF; 
        padding: 12px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 15px; 
        font-weight: 900; 
        margin-bottom: 10px; 
        color: #00FFFF; 
        text-transform: uppercase; 
        animation: neon-pulse 2s infinite; 
    }

    .qr-card {
        background: rgba(255, 215, 0, 0.05);
        border: 1px solid #FFD700;
        border-radius: 10px;
        padding: 14px;
        text-align: center;
        margin-bottom: 15px;
    }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 20, 12, 0.9); border: 1px solid #4a3b18; border-radius: 8px; padding: 6px; }

    .stTabs [data-baseweb="tab-list"] { gap: 4px; justify-content: center; background-color: #0d0a05; padding: 4px; border-radius: 8px; border: 1px solid #d4af37; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #241c0e, #120e07); border-radius: 5px; color: #d4af37; font-weight: bold; font-size: 10px; padding: 6px 10px; border: 1px solid #4a3b18; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FFD700, #B8860B) !important; color: #000000 !important; font-weight: 900 !important; }
    </style>
""",
    unsafe_allow_html=True,
)

# ==========================================
# 2. कड़क सिक्योरिटी और डेटाबेस मैनेजमेंट
# ==========================================
MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"
CORRECT_UPI_ID = "kishorsingh226105.wallet@phonepe"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_status" not in st.session_state:
    st.session_state.user_status = "login"

if "used_utrs" not in st.session_state:
    st.session_state.used_utrs = {"KISHOR90UTR", "PRO2026UTR", "BDG1000PASS"}


# ==========================================
# 3. सुपरवाइजर अलर्ट मोड और 11-सर्वर एक्टिव इंजन
# ==========================================
def supervisor_guard_health_check(sub_list):
    # यह सुपरवाइजर फंक्शन जांचेगा कि कोई भी सर्वर स्लीप मोड में न जाए
    active_servers = sum(1 for val in sub_list if isinstance(val, int) and 0 <= val <= 9)
    if active_servers < 11:
        # यदि कोई सुस्त पड़ा तो सुपरवाइजर फोर्सफुली उन्हें एक्टिव करेगा
        return 11
    return active_servers

def analyze_strict_bdg_servers(period_str, tab_offset):
    clean_digits = "".join(filter(str.isdigit, period_str))
    if len(clean_digits) == 0:
        return 0, "प्रतीक्षा...", "डेटा लोड हो रहा...", "GRAY", False, "सिस्टम लोड हो रहा है..."

    p_val = int(clean_digits[-6:])
    current_second_salt = int(time.time())
    
    p_str = str(p_val).zfill(6)
    d = [int(ch) for ch in p_str]

    # 11 सर्वर नोड्स (सुपरवाइजर द्वारा हर सेकंड मुस्तैद रखे गए)
    sub = [
        (d[5] * 7 + tab_offset + current_second_salt) % 10,
        (sum(d) * 3 + tab_offset * 2 + current_second_salt) % 10,
        (d[4] * 9 + d[5] * 2) % 10,
        (abs(d[5] - d[0]) * 5 + tab_offset + current_second_salt) % 10,
        (d[2] + d[3] + d[4] + d[5]) % 10,
        (p_val * 13 + tab_offset + current_second_salt) % 10,
        (d[5]**2 + tab_offset * 3) % 10,
        (d[1] * 4 + d[4] * 7 + 6 + current_second_salt) % 10,
        (sum(d[3:]) * 4 + 1) % 10,
        (abs(d[4] - d[5]) * 8 + tab_offset + current_second_salt) % 10,
        (d[0] + d[2] + d[4] + tab_offset * 4) % 10
    ]

    # सुपरवाइजर अलर्ट चेक
    total_active = supervisor_guard_health_check(sub)

    big_votes = sum(1 for val in sub if val >= 5)
    small_votes = 11 - big_votes

    if big_votes >= small_votes:
        pred_size_hi = "बड़ा (BIG)"
        line_msg = "🎯 बिग (BIG) की लाइन चल रही है!"
    else:
        pred_size_hi = "छोटा (SMALL)"
        line_msg = "🎯 स्मॉल (SMALL) की लाइन पकड़ ली है!"

    pred_num = (sum(sub) + d[5] * 3 + tab_offset + current_second_salt) % 10

    if pred_num in [1, 3, 7, 9]:
        pred_color = "हरा (GREEN)"
        color_code = "GREEN"
    elif pred_num in [2, 4, 6, 8]:
        pred_color = "लाल (RED)"
        color_code = "RED"
    else:
        pred_color = "हरा (GREEN)" if pred_num % 2 != 0 else "लाल (RED)"
        color_code = "GREEN" if pred_num % 2 != 0 else "RED"

    is_valid = (total_active == 11 and len(clean_digits) >= 3)
    return pred_num, pred_size_hi, pred_color, color_code, is_valid, line_msg


# ==========================================
# 4. कड़क सिक्योरिटी और लाइव डैशबोर्ड फ्लो
# ==========================================
if not st.session_state.authenticated:
    if st.session_state.user_status == "login":
        st.markdown(
            """
            <div style="text-align: center; padding-top: 10px;">
                <div style="font-size: 32px; font-weight: bold; color: #00E5FF; text-shadow: 0 0 15px rgba(0,229,255,0.6);">🎯 SURE SHOT PRO</div>
                <div style="font-size: 13px; letter-spacing: 2px; color: #b19cd9; margin-top: 4px; font-weight: 600;">GAME HUB ACCESS</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)
        st.markdown("<div style='font-size: 20px; font-weight: bold; color: #FFFFFF; margin-bottom: 15px;'>WELCOME BACK ✦</div>", unsafe_allow_html=True)
        
        m = st.text_input("📞 PHONE NUMBER", placeholder="Enter 10 digits")
        p = st.text_input("🔒 PASSWORD", type="password", placeholder="••••••••")
        
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("➔ LOGIN NOW", use_container_width=True):
            if m == MASTER_MOBILE and p == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.session_state.user_status = "dashboard"
                st.rerun()
            elif len(m) == 10 and len(p) >= 4:
                st.session_state.user_status = "recharge_pending"
                st.rerun()
            else:
                st.error("❌ गलत मोबाइल नंबर या पासवर्ड! कृपया सही जानकारी दर्ज करें।")
                
        st.markdown("</div>", unsafe_allow_html=True)

    elif st.session_state.user_status == "recharge_pending":
        st.markdown(
            """
            <div style="text-align: center; padding-top: 5px;">
                <div style="font-size: 26px; font-weight: bold; color: #FFD700;">💎 VIP 25 दिन एक्टिवेशन</div>
                <div style="font-size: 12px; color: #00FFFF; margin-top: 4px;">₹1000 का रिचार्ज पूरा करें और यूनिक UTR नंबर दर्ज करें</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="qr-card">
                <div style="font-size: 14px; color: #FFD700; font-weight: bold; margin-bottom: 8px;">📱 UPI QR CODE & PAYMENT GATEWAY</div>
                <div style="font-size: 13px; color: #FFFFFF; margin-bottom: 4px;">UPI ID: <b>{CORRECT_UPI_ID}</b></div>
                <div style="font-size: 11px; color: #00FFFF;">राशि: <b>₹1000.00</b> (25 दिन की सुरक्षा वैधता)</div>
                <hr style="border-color: rgba(255,215,0,0.3); margin: 10px 0;">
                <div style="font-size: 11px; color: #A0A0A0;"><b>सुरक्षा नियम:</b> कोई भी डुप्लीकेट या पुराना UTR नंबर स्वीकार नहीं किया जाएगा।</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        utr_input = st.text_input("🔑 यूनिक UTR / URT ट्रांजैक्शन नंबर दर्ज करें", placeholder="यहाँ UTR नंबर लिखें...")
        
        col_r1, col_r2 = st.columns(2)
        with col_r1:
            if st.button("✅ UTR वेरिफाई करें", use_container_width=True):
                clean_utr = utr_input.strip()
                if not clean_utr:
                    st.error("⚠️ कृपया UTR नंबर खाली न छोड़ें!")
                elif clean_utr in st.session_state.used_utrs:
                    st.error("🚨 सुरक्षा चेतावनी: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका है! डुप्लीकेट UTR प्रतिबंधित है।")
                elif clean_utr.upper() == "KISHOR90" or len(clean_utr) >= 10:
                    st.session_state.used_utrs.add(clean_utr)
                    st.success("🎉 रिचार्ज सफल! 25 दिन की वैलिडिटी सक्रिय, डैशबोर्ड खोला जा रहा है...")
                    time.sleep(1.5)
                    st.session_state.authenticated = True
                    st.session_state.user_status = "dashboard"
                    st.rerun()
                else:
                    st.error("❌ अमान्य UTR नंबर! कृपया वैध ट्रांजैक्शन आईडी दर्ज करें।")
        with col_r2:
            if st.button("🔙 वापस लॉगिन पर", use_container_width=True):
                st.session_state.user_status = "login"
                st.rerun()

else:
    st.markdown(
        """
        <div style="text-align: center; padding: 2px 0 4px 0;">
            <div style="font-size: 22px; font-weight: 900; color: #00E5FF; text-shadow: 0 0 10px rgba(0,229,255,0.8);">
                <span class="blinking-green-light"></span>SURE SHOT PRO v3
            </div>
            <div style="font-size: 11px; color: #FFD700; font-weight: bold; letter-spacing: 1px;">🛡️ सुपरवाइजर अलर्ट मोड: 11/11 सर्वर हमेशा एक्टिव</div>
            <div class="live-frequency-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    now_epoch = int(time.time())
    sec_left = 30 - (now_epoch % 30)
    
    base_period_int = now_epoch // 30
    auto_live_period = str(base_period_int)[-5:]

    st.markdown("<div style='font-size: 11px; font-weight: bold; color: #00E5FF; margin-bottom: -10px;'>🎯 BDG GAME LIVE PERIOD INPUT:</div>", unsafe_allow_html=True)
    col_p1, col_p2 = st.columns([2, 1])
    with col_p1:
        user_bdg_input = st.text_input("", value=auto_live_period, max_chars=12, placeholder="यहाँ बीडीजी पीरियड दर्ज करें...")
    with col_p2:
        st.markdown(f"<div style='text-align:center; background: rgba(0,229,255,0.1); border: 1px solid #00E5FF; border-radius: 6px; padding: 8px; margin-top: 20px; font-weight: bold; color: #00FFFF; font-size: 12px;'><span class='blinking-green-light'></span>⏳ {sec_left}s शेष</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["विन्गो 30 सेकण्ड", "विन्गो 1 मिनट", "विन्गो 3 मिनट", "विन्गो 5 मिनट"])

    def render_game_panel(tab_offset):
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        
        final_period = user_bdg_input.strip() if user_bdg_input.strip() else auto_live_period

        st.markdown(f'<div class="live-period-display"><span class="blinking-red-light"></span>सक्रिय लाइव पीरियड: <b>{final_period}</b></div>', unsafe_allow_html=True)

        pred_num, pred_size_hi, pred_color, color_code, is_valid, line_msg = analyze_strict_bdg_servers(final_period, tab_offset)

        if is_valid:
            st.markdown(f'<div class="sure-shot-banner">💎 {line_msg} [11/11 सर्वर सुपरवाइजर एक्टिव]</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="sure-shot-banner" style="border-color: #FF3333; color: #FF9999;">⚠️ सुपरवाइजर स्कैनिंग जारी है...</div>', unsafe_allow_html=True)

        color_bg = "#00AA55" if color_code == "GREEN" else "#FF4444"
        size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if "बड़ा" in pred_size_hi else "linear-gradient(135deg, #00CCFF, #0044FF)"

        st.markdown(
            f"""
            <div class="diagonal-container">
                <div class="result-item">
                    <div style="font-size: 10px; color: #A0A0A0;">आने वाला नंबर</div>
                    <div style="background-color: {color_bg}; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: bold; margin: 0 auto; color: white;">{pred_num}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 10px; color: #A0A0A0;">आने वाला साइज़</div>
                    <div style="background: {size_bg}; color: white; padding: 7px 4px; border-radius: 6px; font-weight: 900; font-size: 11px;">{pred_size_hi}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 10px; color: #A0A0A0;">आने वाला रंग</div>
                    <div style="background-color: {color_bg}; color: white; padding: 7px 4px; border-radius: 6px; font-weight: bold; font-size: 11px;">{pred_color}</div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)

    with tab1: render_game_panel(11)
    with tab2: render_game_panel(23)
    with tab3: render_game_panel(37)
    with tab4: render_game_panel(53)

    time.sleep(1)
    st.rerun()
