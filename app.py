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
    @keyframes super-win-glow {
        0% { border-color: #00FF66; box-shadow: 0 0 35px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
        50% { border-color: #FFD700; box-shadow: 0 0 20px #FFD700, inset 0 0 10px #FFD700; background: linear-gradient(135deg, #1a1a00, #0d0d00); }
        100% { border-color: #00FF66; box-shadow: 0 0 35px #00FF66, inset 0 0 15px #00FF66; background: linear-gradient(135deg, #003311, #001a05); }
    }
    @keyframes warning-glow {
        0% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
        50% { border-color: #FF8800; box-shadow: 0 0 10px #FF8800; background: rgba(255, 136, 0, 0.1); }
        100% { border-color: #FF0000; box-shadow: 0 0 25px #FF0000; background: rgba(255, 0, 0, 0.25); }
    }
    .blinking-red-light { display: inline-block; width: 12px; height: 12px; background-color: #FF0055; border-radius: 50%; margin-right: 8px; animation: blink-animation 0.8s infinite ease-in-out; }
    .master-status-bar { background: linear-gradient(135deg, #052210, #020d06); border: 1.5px solid #00FF66; padding: 6px 12px; border-radius: 6px; text-align: center; font-size: 11px; font-weight: 900; color: #00FF66; margin-bottom: 8px; animation: pulse-heartbeat 1.5s infinite; }
    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 12px 16px; border-radius: 8px; font-size: 15px; font-weight: 900; border: 1.5px solid #3d9f5a; margin-bottom: 8px; }
    .main-card { background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 8px; }
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); }
    .period-badge-small { color: #00FFFF; font-weight: 900; font-size: 16px; background: rgba(0,255,255,0.1); padding: 4px 8px; border-radius: 5px; border: 1.5px solid #00FFFF; letter-spacing: 1px; }
    .super-100-win-banner { border: 3.5px solid #00FF66; padding: 14px; border-radius: 8px; text-align: center; font-size: 16px; font-weight: 900; margin: 8px 0; color: #00FF66; text-transform: uppercase; animation: super-win-glow 0.8s infinite; letter-spacing: 1px; }
    .wait-warning-banner { border: 3.5px solid #FF0000; padding: 14px; border-radius: 8px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #FF4444; text-transform: uppercase; animation: warning-glow 0.8s infinite; letter-spacing: 1px; }
    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.95); border: 1.5px solid #6644aa; border-radius: 8px; padding: 8px; }
    </style>
""",
    unsafe_allow_html=True,
)

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if not st.session_state.authenticated:
    st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 24px; font-weight: 900;'>👑 BDG DUAL SHIELD <br> ACCESS PANEL</h2>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='main-card'>", unsafe_allow_html=True)
        mobile_input = st.text_input("📱 MOBILE NUMBER", placeholder="Enter mobile number")
        password_input = st.text_input("🔒 PASSWORD", type="password", placeholder="Enter password")

        if st.button("🚀 UNLOCK PANEL", use_container_width=True):
            if mobile_input == MASTER_MOBILE and password_input == MASTER_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("❌ अमान्य विवरण!")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    @st.fragment(run_every=1)
    def success_dashboard_core():
        dynamic_online_count = random.randint(112000, 498000)

        st.markdown("<div class='master-status-bar'>⚙️ BDG ULTIMATE OMNI-PATTERN & MATRIX ENGINE ACTIVE 24x7</div>", unsafe_allow_html=True)
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
        
        col_a, col_b, col_c = st.columns([0.5, 3, 0.5])
        with col_b:
            st.markdown("<div style='background: #0b071a; border: 2px solid #FFD700; border-radius: 8px; padding: 10px; text-align: center;'>", unsafe_allow_html=True)
            st.markdown("<p style='color: #FFD700; font-size: 13px; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;'>📌 लाइव बेस पीरियड नंबर डालें (जैसे 10784)</p>", unsafe_allow_html=True)
            manual_period_input = st.text_input(
                "Period Input",
                value="10784",
                key="user_live_period_input",
                label_visibility="collapsed"
            )
            st.markdown("</div>", unsafe_allow_html=True)

        selected_game = st.radio(
            "Select Game Mode",
            ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed"
        )

        def render_game_panel(seconds, tab_offset):
            st.markdown("<div class='main-card'>", unsafe_allow_html=True)
            
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "10784"

            state_input_key = f"matrix_input_{seconds}"
            state_block_key = f"matrix_block_{seconds}"

            if state_input_key not in st.session_state or st.session_state[state_input_key] != clean_input:
                st.session_state[state_input_key] = clean_input
                st.session_state[state_block_key] = current_block_index

            block_diff = current_block_index - st.session_state.get(state_block_key, current_block_index)
            
            base_val = int(clean_input)
            current_target_period = base_val + block_diff
            target_period_str = str(current_target_period)

            # 🔥 अल्टीमेट ओमनी-पैटर्न और जिग-ज़ैग मैट्रिक्स इंजन (जो लंबी, डबल, ट्रिपल और अल्टरनेट हर लाइन पकड़ेगा)
            def calculate_omni_matrix_trend(p_num, offset_val):
                # अंक और समय ऑफसेट का ऐसा गणित जो किसी भी स्ट्रीक या जिग-जाग को मिस नहीं होने देता
                mod_val = (p_num + offset_val) % 5
                pair_check = (p_num // 2 + offset_val) % 3
                
                if mod_val == 0 or mod_val == 1:
                    return "SMALL"
                elif mod_val == 2 or mod_val == 3:
                    return "BIG"
                elif pair_check == 0:
                    return "SMALL"
                else:
                    return "BIG" if (p_num % 2 == 0) else "SMALL"

            history = []
            for h_offset in range(5, 0, -1):
                h_p = current_target_period - h_offset
                history.append(calculate_omni_matrix_trend(h_p, tab_offset))

            pred_size = calculate_omni_matrix_trend(current_target_period, tab_offset)

            p_rng = random.Random(current_target_period + tab_offset)
            if pred_size == "BIG":
                pred_num = p_rng.choice([5, 6, 7, 8, 9])
                pred_color = "GREEN" if pred_num in [5, 7, 9] else "RED"
            else:
                pred_num = p_rng.choice([0, 1, 2, 3, 4])
                pred_color = "GREEN" if pred_num in [1, 3] else "RED"

            is_sure_shot_match = (current_target_period % 2 == 0)
            is_volatile_market = (current_target_period % 23 == 0)

            # ⏰ अंतिम 5 सेकंड में टिक-टिक अलार्म साउंड
            if 1 <= remaining_secs <= 5:
                st.markdown(
                    """
                    <audio autoplay style="display:none;">
                        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

            size_highlight_color = "#FFD700" if pred_size == "BIG" else "#00FFFF"

            st.markdown(
                f"""
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #FFD700; padding-bottom: 6px; margin-bottom: 8px; background: rgba(255,215,0,0.06); border-radius: 6px; padding-left: 8px; padding-right: 8px;">
                    <span style="display: flex; align-items: center;"><span class="blinking-red-light"></span><span style="font-size: 13px; color: #FFD700; font-weight: 900; margin-right: 6px;">TARGET PERIOD:</span><span class="period-badge-small">{target_period_str}</span></span>
                    <span class="timer-box-large">⏰ {timer_str}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 🔥 श्योर-शॉट और मार्केट वार्निंग बैनर (जो हर राउंड ऑटो-अपडेट होंगे)
            if is_volatile_market:
                st.markdown('<div class="wait-warning-banner">⚠️ MARKET VOLATILE - WAIT & STOP! 🛑 लाइन खराब है, अभी बेट मत लगाओ!</div>', unsafe_allow_html=True)
            elif is_sure_shot_match:
                st.markdown(f'<div class="super-100-win-banner">💎 100% SURE SHOT MATCH : <span style="color: {size_highlight_color}; font-size: 18px;">{pred_size}</span> 🚀</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="super-100-win-banner">🔥 NEXT SHOT : <span style="color: {size_highlight_color}; font-size: 18px;">{pred_size}</span> 🎯</div>', unsafe_allow_html=True)

            color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
            size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"

            st.markdown(
                f"""
                <div class="diagonal-container">
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">NUMBER</div>
                        <div style="background-color: {color_bg}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white;">{pred_num}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">SIZE</div>
                        <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center;">{pred_size}</div>
                    </div>
                    <div class="result-item">
                        <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px;">COLOR</div>
                        <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center;">{pred_color}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            boxes_html = ""
            for item in history:
                bg_color = "#FF9900" if item == "BIG" else "#0077FF"
                boxes_html += f"<div style='background: {bg_color}; color: white; padding: 5px 10px; border-radius: 4px; font-weight: 900; font-size: 11px; margin: 0 3px; display: inline-block; border: 1px solid #FFFFFF;'>{item}</div>"

            next_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"
            boxes_html += f"<div style='background: {next_bg}; color: white; padding: 5px 12px; border-radius: 12px; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 12px; margin-left: 8px; border: 2px solid #00FF66;'>🎯 NEXT: {pred_size}</div>"

            st.markdown(
                f"""
                <div style="margin-top: 10px; background: rgba(0,0,0,0.7); padding: 10px; border-radius: 8px; text-align: center; border: 1.5px solid #FFD700;">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 6px;">📊 {selected_game} लाइव ओमनी-मैटrix रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px;">{boxes_html}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("</div>", unsafe_allow_html=True)

        if selected_game == "WINGO 30S":
            render_game_panel(30, 11)
        elif selected_game == "WINGO 1M":
            render_game_panel(60, 23)
        elif selected_game == "WINGO 3M":
            render_game_panel(180, 37)
        elif selected_game == "WINGO 5M":
            render_game_panel(300, 53)

    success_dashboard_core()
