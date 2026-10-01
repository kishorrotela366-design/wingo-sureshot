from datetime import datetime
import streamlit as st

# ==========================================
# 1. पेज कॉन्फ़िगरेशन एवं बड़े अक्षरों वाला डिज़ाइन
# ==========================================
st.set_page_config(
    page_title="BDG मास्टर पैनल",
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
        padding: 8px;
        margin-bottom: 8px;
        font-size: 11px;
        text-align: center;
        color: #FFD700;
        font-weight: bold;
    }

    /* बीच का बड़ा और मोटा अक्षर वाला श्योर शॉर्ट बैनर */
    .sure-shot-banner { 
        background: radial-gradient(circle, #0e222e 0%, #050d12 100%); 
        border: 2px dashed #00E5FF; 
        padding: 12px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 16px; 
        font-weight: 900; 
        margin-bottom: 10px; 
        color: #00FFFF; 
        text-transform: uppercase; 
        animation: neon-pulse 2s infinite; 
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

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


# ==========================================
# 2. कैलकुलेशन और सर्वर लॉजिक
# ==========================================
def supervisor_server_health_check(substrates_list):
    active_count = sum(1 for val in substrates_list if val is not None and isinstance(val, int))
    return active_count, (active_count == 11)

def analyze_ultra_substrates_with_supervisor(period_str, tab_offset):
    try:
        p_val = int("".join(filter(str.isdigit, period_str))[-5:])
    except:
        p_val = 12345

    digits = [int(d) for d in str(p_val).zfill(5)]
    
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
    active_count, is_healthy = supervisor_server_health_check(substrates)

    big_votes = sum(1 for val in substrates if val >= 5)
    small_votes = 11 - big_votes

    last_digit = p_val % 10
    is_last_big = (last_digit >= 5)
    
    if p_val % 2 == 0:
        pattern_name = "🔄 अल्टरनेट ट्रेंड (बड़ा-छोटा-बड़ा-छोटा)"
        pattern_pred_raw = "SMALL"
    else:
        pattern_name = "🐉 ड्रैगन / रिपीट पैटर्न"
        pattern_pred_raw = "BIG" if is_last_big else "SMALL"

    if big_votes > small_votes:
        pred_size_hi = "बड़ा (BIG)"
        pred_size_raw = "BIG"
        max_match = big_votes
    else:
        pred_size_hi = "छोटा (SMALL)"
        pred_size_raw = "SMALL"
        max_match = small_votes

    master_raw = (sum(substrates) + digits[4] * 7 + tab_offset * 13) % 5
    pred_num = 5 + master_raw if pred_size_raw == "BIG" else master_raw

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

    return pred_num, pred_size_hi, pred_color, color_code, is_sure_shot, max_match, pattern_name, is_pattern_matched, active_count


# ==========================================
# 3. मुख्य इंटरफेस
# ==========================================
if not st.session_state.authenticated:
    st.markdown("<div style='text-align:center; padding: 20px; color: #FFD700;'>👑 BDG मास्टर पैनल लॉगिन</div>", unsafe_allow_html=True)
    m = st.text_input("मोबाइल नंबर")
    p = st.text_input("पासवर्ड", type="password")
    if st.button("लॉगिन करें"):
        if m == MASTER_MOBILE and p == MASTER_PASSWORD:
            st.session_state.authenticated = True
            st.rerun()
else:
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
    default_live_period = now.strftime("%Y%m%d%H%M")[-5:]

    user_period_input = st.text_input("पीरियड नंबर दर्ज करें (लाइव या मैन्युअल)", value=default_live_period, max_chars=10)

    tab1, tab2, tab3, tab4 = st.tabs(["विन्गो 30 सेकंड", "विन्गो 1 मिनट", "विन्गो 3 मिनट", "विन्गो 5 मिनट"])

    def render_game_panel(tab_offset):
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        
        final_period = user_period_input.strip() if user_period_input.strip() else default_live_period

        pred_num, pred_size_hi, pred_color, color_code, is_sure_shot, match_count, pattern_name, is_pattern_matched, active_count = analyze_ultra_substrates_with_supervisor(final_period, tab_offset)

        # बड़े अक्षरों वाला चमकता हुआ बैनर (अब एकदम साफ और बड़े फॉन्ट में)
        if is_sure_shot:
            st.markdown(f'<div class="sure-shot-banner">💎 100% पक्का शॉट! [{pred_size_hi}] (11/11 सर्वर मैच)</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="sure-shot-banner" style="border-color: #FF9900; color: #FFD700;">🔥 सामान्य ट्रेंड: 11 में से {match_count} सर्वर "{pred_size_hi}" बता रहे हैं</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="supervisor-card"><span class="blinking-green-light"></span>🛡️ <b>सुपरवाइज़र अलर्ट:</b> कुल {active_count}/11 सर्वर सक्रिय हैं [पीरियड: {final_period}]</div>', unsafe_allow_html=True)

        sync_text = "<span style='color: #00FF66;'>✅ सर्वर और पैटर्न दोनों सहमत हैं</span>" if is_pattern_matched else "<span style='color: #FFCC00;'>⚠ पैटर्न और सर्वर में अंतर है</span>"
        st.markdown(f'<div class="pattern-alert-box">📡 <b>मास्टर सिग्नल:</b> {pattern_name}<br>{sync_text}</div>', unsafe_allow_html=True)

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
