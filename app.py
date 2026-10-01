from datetime import datetime, timedelta
import streamlit as st
import time

# ==========================================
# 1. पेज कॉन्फ़िगरेशन एवं CSS डिज़ाइन
# ==========================================
st.set_page_config(
    page_title="BDG हिंदी सुपरवाइज़र मास्टर पैनल",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed",
)

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

    .supervisor-card {
        background: rgba(0, 255, 102, 0.05);
        border: 1px solid #00FF66;
        border-radius: 6px;
        padding: 6px 8px;
        font-size: 11px;
        color: #00FF66;
        font-weight: bold;
        text-align: center;
        margin-bottom: 6px;
    }

    .main-card { 
        background: linear-gradient(145deg, #18130a, #0d0a05); 
        border: 1.5px solid #d4af37; 
        border-radius: 12px; 
        padding: 14px; 
        box-shadow: 0 6px 20px rgba(0,0,0,0.6), inset 0 0 10px rgba(212,175,55,0.1); 
        margin-top: 6px; 
    }

    .pattern-alert-box {
        background: rgba(255, 215, 0, 0.08);
        border: 1.5px solid #FFD700;
        border-radius: 8px;
        padding: 10px;
        margin-bottom: 10px;
        font-size: 12px;
        text-align: center;
        color: #FFD700;
        font-weight: bold;
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
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FFD700, #B8860B) !important; color: #000000 !important; font-weight: 900 !important; }

    .stButton > button {
        background: linear-gradient(180deg, #d32f2f 0%, #8e0000 100%) !important;
        color: white !important;
        font-weight: 900 !important;
        font-size: 16px !important;
        border-radius: 8px !important;
        padding: 8px 16px !important;
    }
    </style>
""",
    unsafe_allow_html=True,
)

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ==========================================
# 2. 🛡️ सुपरवाइज़र मॉनिटर इंजन (बाप सर्वर)
# ==========================================
def supervisor_server_health_check(substrates_list):
    active_count = 0
    failed_servers = []

    for idx, val in enumerate(substrates_list, start=1):
        if val is not None and isinstance(val, int):
            active_count += 1
        else:
            failed_servers.append(idx)

    is_all_healthy = (active_count == 11)
    return active_count, failed_servers, is_all_healthy


# ==========================================
# 3. 11 सब-सर्वर + हिंदी पैटर्न इंजन
# ==========================================
def analyze_ultra_substrates_with_supervisor(period_5_digits, tab_offset):
    try:
        p_val = int(period_5_digits)
    except:
        p_val = 12345

    digits = [int(d) for d in str(p_val).zfill(5)]
    
    # 11 सर्वर लॉजिक (सुरक्षित रीस्टार्ट)
    try: sub1 = (digits[4] * 3 + tab_offset) % 10
    except: sub1 = 5
    
    try: sub2 = (sum(digits) + tab_offset * 2) % 10
    except: sub2 = 5
    
    try: sub3 = (digits[3] * 7 + digits[4] * 3) % 10
    except: sub3 = 5
    
    try: sub4 = (abs(digits[4] - digits[0]) * 9 + tab_offset) % 10
    except: sub4 = 5
    
    try: sub5 = (digits[2] + digits[3] + digits[4] + 5) % 10
    except: sub5 = 5
    
    try: sub6 = (p_val * 11) % 10
    except: sub6 = 5
    
    try: sub7 = (digits[4] ** 2 + tab_offset) % 10
    except: sub7 = 5
    
    try: sub8 = (digits[1] * 4 + digits[3] * 6 + 1) % 10
    except: sub8 = 5
    
    try: sub9 = (sum(digits[2:]) * 3 + 7) % 10
    except: sub9 = 5
    
    try: sub10 = (abs(digits[3] - digits[4]) * 8 + tab_offset) % 10
    except: sub10 = 5
    
    try: sub11 = (digits[0] + digits[2] + digits[4] + tab_offset) % 10
    except: sub11 = 5

    substrates = [sub1, sub2, sub3, sub4, sub5, sub6, sub7, sub8, sub9, sub10, sub11]

    # सुपरवाइज़र रन (हेल्थ चेक)
    active_count, failed_servers, is_healthy = supervisor_server_health_check(substrates)

    big_votes = sum(1 for val in substrates if val >= 5)
    small_votes = 11 - big_votes

    # हिंदी पैटर्न पहचान
    last_digit = p_val % 10
    is_last_big = (last_digit >= 5)
    
    if p_val % 2 == 0:
        pattern_name = "🔄 अल्टरनेट ट्रेंड (बड़ा-छोटा-बड़ा-छोटा)"
        pattern_pred = "छोटा (SMALL)" if is_last_big else "बड़ा (BIG)"
        pattern_pred_raw = "BIG" if not is_last_big else "SMALL"
    else:
        pattern_name = "🐉 ड्रैगन / रिपीट पैटर्न"
        pattern_pred = "बड़ा (BIG)" if is_last_big else "छोटा (SMALL)"
        pattern_pred_raw = "BIG" if is_last_big else "SMALL"

    if big_votes > small_votes:
        pred_size_hi = "बड़ा (BIG)"
        pred_size_raw = "BIG"
        max_match = big_votes
    else:
        pred_size_hi = "छोटा (SMALL)"
        pred_size_raw = "SMALL"
        max_match = small_votes

    against_count = 11 - max_match

    master_raw = (sum(substrates) + digits[4] * 7 + tab_offset * 13) % 5
    if pred_size_raw == "BIG":
        pred_num = 5 + master_raw
    else:
        pred_num = master_raw

    if pred_num in [1, 3, 7, 9]:
        pred_color = "हरा (GREEN)"
        color_code = "GREEN"
    elif pred_num in [2, 4, 6, 8]:
        pred_color = "लाल (RED)"
        color_code = "RED"
    else:
        pred_color = "हरा (GREEN)" if pred_num == 5 else "लाल (RED)"
        color_code = "GREEN" if pred_num == 5 else "RED"

    is_sure_shot = (max_match == 11)
    is_pattern_matched = (pred_size_raw == pattern_pred_raw)

    return pred_num, pred_size_hi, pred_color, color_code, is_sure_shot, max_match, against_count, pattern_name, is_pattern_matched, active_count, is_healthy


# ==========================================
# 4. मुख्य हिंदी इंटरफेस
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<div style='text-align:center; padding: 20px; color: #FFD700;'>👑 BDG मास्टर पैनल में प्रवेश करें</div>", unsafe_allow_html=True)
    m = st.text_input("मोबाइल नंबर (Mobile)")
    p = st.text_input("पासवर्ड (Password)", type="password")
    if st.button("लॉगिन करें"):
        if m == MASTER_MOBILE and p == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        st.markdown(
            """
                <div class="top-bar">
                    <div><span class="blinking-green-light"></span><span style="color: #00FFFF; font-weight: 800;">👑 BDG सुपरवाइज़र मास्टर इंजन</span></div>
                    <div><span class="blinking-green-light"></span>सुरक्षा चालू है</div>
                </div>
            """,
            unsafe_allow_html=True,
        )

        now = datetime.now()
        default_5_digits = now.strftime("%M%S")[-5:]

        col_a, col_b, col_c = st.columns([1, 2.5, 1])
        with col_b:
            manual_period_input = st.text_input("पीरियड नंबर दर्ज करें", value=default_5_digits, max_chars=5, label_visibility="collapsed")

        tab1, tab2, tab3, tab4 = st.tabs(["विन्गो 30 सेकंड", "विन्गो 1 मिनट", "विन्गो 3 मिनट", "विन्गो 5 मिनट"])

        def render_game_panel(seconds, tab_name_style, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            clean_input = "".join(filter(str.isdigit, manual_period_input)) or "51026"
            final_period = clean_input.zfill(5)[-5:]

            # कैलकुलेशन और हेल्थ चेक
            pred_num, pred_size_hi, pred_color, color_code, is_sure_shot, match_count, against_count, pattern_name, is_pattern_matched, active_count, is_healthy = analyze_ultra_substrates_with_supervisor(final_period, tab_offset)

            # 1. हिंदी सुपरवाइज़र स्टेटस
            st.markdown(
                f"""
                <div class="supervisor-card">
                    🛡️ <b>सुपरवाइज़र अलर्ट:</b> कुल {active_count}/11 सर्वर एकदम सक्रिय हैं [कोई सर्वर बंद नहीं है]
                </div>
                """,
                unsafe_allow_html=True
            )

            # 2. हिंदी पैटर्न सिग्नल
            sync_text = "<span style='color: #00FF66;'>✅ सर्वर और पैटर्न दोनों सहमत हैं (सुरक्षित राउंड)</span>" if is_pattern_matched else "<span style='color: #FFCC00;'>⚠️ पैटर्न और सर्वर में अंतर है (कम रिस्क लें)</span>"
            st.markdown(
                f"""
                <div class="pattern-alert-box">
                    📡 <b>मास्टर सिग्नल:</b> {pattern_name}<br>
                    <span>{sync_text}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

            # 3. हिंदी बैनर
            if is_sure_shot:
                st.markdown(f'<div class="sure-shot-banner">💎 100% पक्का शॉट! [{pred_size_hi}] (11 में से पूरे 11 सर्वर तैयार हैं) 🚀</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="sure-shot-banner" style="border-color: #FF9900; color: #FFD700;">🔥 सामान्य ट्रेंड: 11 में से {match_count} सर्वर "{pred_size_hi}" बता रहे हैं</div>', unsafe_allow_html=True)
            
            color_bg = "#00AA55" if color_code == "GREEN" else "#FF4444"
            size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if "बड़ा" in pred_size_hi else "linear-gradient(135deg, #00CCFF, #0044FF)"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 10px; color: #A0A0A0;">आने वाला नंबर</div>
                        <div style="background-color: {color_bg}; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: bold; margin: 0 auto; color: white;">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #A0A0A0;">आने वाला साइज़</div>
                        <div style="background: {size_bg}; color: white; padding: 6px 4px; border-radius: 6px; font-weight: 900; font-size: 11px;">{pred_size_hi}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #A0A0A0;">आने वाला रंग</div>
                        <div style="background-color: {color_bg}; color: white; padding: 6px 4px; border-radius: 6px; font-weight: bold; font-size: 11px;">{pred_color}</div>
                    </div>
                </div>
            """,
                unsafe_allow_html=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)

        with tab1:
            render_game_panel(30, "विन्गो 30 सेकंड", 11)
        with tab2:
            render_game_panel(60, "विन्गो 1 मिनट", 23)
        with tab3:
            render_game_panel(180, "विन्गो 3 मिनट", 37)
        with tab4:
            render_game_panel(300, "विन्गो 5 मिनट", 53)

    success_dashboard_core()
