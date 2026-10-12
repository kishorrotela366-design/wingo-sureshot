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
    .stApp { background-color: #05050a; color: #FFFFFF; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    
    /* Animations */
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 10px #FF0055; }
        50% { opacity: 0.2; transform: scale(0.85); }
        100% { opacity: 1; transform: scale(1.1); box-shadow: 0 0 10px #FF0055; }
    }
    @keyframes green-glow-pulse {
        0% { box-shadow: 0 0 8px #00FF66, inset 0 0 5px #00FF66; }
        50% { box-shadow: 0 0 20px #00FF66, inset 0 0 10px #00FF66; }
        100% { box-shadow: 0 0 8px #00FF66, inset 0 0 5px #00FF66; }
    }
    
    /* CSS Styling Matching Screenshot */
    .blinking-red-light { display: inline-block; width: 10px; height: 10px; background-color: #FF0055; border-radius: 50%; margin-right: 8px; animation: blink-animation 0.8s infinite ease-in-out; }
    
    .panel-header-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #090e14;
        padding: 10px 14px;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 900;
        border: 2px solid #00FF66;
        box-shadow: 0 0 15px rgba(0, 255, 102, 0.3);
        margin-bottom: 10px;
    }
    
    .target-time-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #090a10;
        border: 2px solid #FFD700;
        border-radius: 8px;
        padding: 10px 14px;
        box-shadow: 0 0 12px rgba(255, 215, 0, 0.3);
        margin-bottom: 10px;
    }
    
    .target-badge {
        color: #00FFFF;
        font-weight: 900;
        font-size: 16px;
        background: rgba(0, 255, 255, 0.1);
        padding: 4px 10px;
        border-radius: 6px;
        border: 2px solid #00FFFF;
        margin-left: 6px;
    }
    
    .next-shot-banner {
        border: 2.5px solid #00FF66;
        background: rgba(0, 255, 102, 0.05);
        padding: 14px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: 900;
        margin: 10px 0;
        color: #00FF66;
        letter-spacing: 1px;
        animation: green-glow-pulse 1.2s infinite;
    }
    
    .result-grid {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-top: 10px;
    }
    
    .result-card-box {
        flex: 1;
        text-align: center;
        background: #0f0b1e;
        border: 2px solid #3d2b63;
        border-radius: 10px;
        padding: 12px 6px;
    }
    
    .history-card {
        margin-top: 12px;
        background: #090a10;
        padding: 12px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.2);
    }
    
    /* Custom Styling for Radio Buttons to match screenshot top placement */
    .stRadio > label {
        display: none !important;
    }
    div[row-widget="stRadio"] {
        background: #090a10;
        border: 2px solid #3d2b63;
        padding: 6px 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    div[row-widget="stRadio"] label p {
        font-weight: 900 !important;
        font-size: 13px !important;
    }
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
        st.markdown("<div style='background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2);'>", unsafe_allow_html=True)
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
    if "online_count" not in st.session_state:
        st.session_state.online_count = random.randint(350000, 380000)
        st.session_state.last_count_update = time.time()

    current_time_epoch = time.time()
    if current_time_epoch - st.session_state.last_count_update > 90:
        change_amount = random.randint(-1200, 1500)
        st.session_state.online_count = max(320000, min(410000, st.session_state.online_count + change_amount))
        st.session_state.last_count_update = current_time_epoch

    @st.fragment(run_every=1)
    def success_dashboard_core():
        now = datetime.now()

        # 1️⃣ सबसे ऊपर गेम मोड सेलेक्टर (WINGO 30S, 1M, 3M, 5M) जैसे स्क्रीनशॉट में है[span_4](start_span)[span_4](end_span)
        selected_game = st.radio(
            "Select Game Mode",
            ["⚪ WINGO 30S", "🔴 WINGO 1M", "⚪ WINGO 3M", "⚪ WINGO 5M"],
            horizontal=True,
            label_visibility="collapsed"
        )

        # 2️⃣ बीच में हेडर जिसमें BDG SNIPER PANEL, बीच में बेस पीरियड इनपुट (XXXXX) और दाईं ओर यूजरकाउंट है[span_5](start_span)[span_5](end_span)
        col_h1, col_h2, col_h3 = st.columns([1.2, 0.9, 1.1])
        
        with col_h1:
            st.markdown(
                f"""
                <div style="background: #090e14; border: 2px solid #00FF66; padding: 10px; border-radius: 8px; text-align: center; font-size: 13px; font-weight: 900; color: #00FFFF; box-shadow: 0 0 10px rgba(0,255,102,0.3);">
                    <span class="blinking-red-light"></span>⚡ BDG SNIPER PANEL
                </div>
                """,
                unsafe_allow_html=True
            )
            
        with col_h2:
            # यहाँ स्क्रीनशॉट जैसा छोटा XXXXX बेस पीरियड इनपुट बॉक्स है[span_6](start_span)[span_6](end_span)
            manual_period_input = st.text_input(
                "Base Period",
                value="10313",
                key="user_live_period_input",
                label_visibility="collapsed"
            )
            
        with col_h3:
            st.markdown(
                f"""
                <div style="background: #090e14; border: 2px solid #00FF66; padding: 10px; border-radius: 8px; text-align: center; font-size: 13px; font-weight: 900; color: #FFFFFF; box-shadow: 0 0 10px rgba(0,255,102,0.3);">
                    <span class="blinking-red-light"></span>👥 {st.session_state.online_count:,}
                </div>
                """,
                unsafe_allow_html=True
            )

        def render_game_panel(seconds, tab_offset):
            total_seconds = now.hour * 3600 + now.minute * 60 + now.second
            remaining_secs = seconds - (total_seconds % seconds)
            mins = remaining_secs // 60
            secs = remaining_secs % 60
            timer_str = f"{mins:02d}:{secs:02d}"

            current_block_index = total_seconds // seconds

            clean_input = "".join(filter(str.isdigit, manual_period_input))
            if not clean_input:
                clean_input = "10313"

            state_input_key = f"matrix_input_{seconds}"
            state_block_key = f"matrix_block_{seconds}"

            if state_input_key not in st.session_state or st.session_state[state_input_key] != clean_input:
                st.session_state[state_input_key] = clean_input
                st.session_state[state_block_key] = current_block_index

            block_diff = current_block_index - st.session_state.get(state_block_key, current_block_index)
            
            base_val = int(clean_input)
            current_target_period = base_val + block_diff
            target_period_str = str(current_target_period)

            def calculate_omni_matrix_trend(p_num, offset_val):
                mod_val = (p_num + offset_val) % 5
                pair_check = (p_num // 2 + offset_val) % 3
                if mod_val in [0, 1]:
                    return "SMALL"
                elif mod_val in [2, 3]:
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

            if 1 <= remaining_secs <= 5:
                st.markdown(
                    """
                    <audio autoplay style="display:none;">
                        <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
                    </audio>
                    """,
                    unsafe_allow_html=True
                )

            # 3️⃣ टारगेट पीरियड और टाइमर बॉक्स[span_7](start_span)[span_7](end_span)
            st.markdown(
                f"""
                <div class="target-time-card">
                    <div style="display: flex; align-items: center;">
                        <span class="blinking-red-light"></span>
                        <span style="font-size: 13px; color: #FFD700; font-weight: 900;">TARGET PERIOD:</span>
                        <span class="target-badge">{target_period_str}</span>
                    </div>
                    <div style="color: #FF00FF; font-weight: 900; font-size: 16px;">⏰ {timer_str}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # 4️⃣ नेक्स्ट शॉट बैनर[span_8](start_span)[span_8](end_span)
            st.markdown(
                f'<div class="next-shot-banner">🔥 NEXT SHOT : <span style="color: #00FFFF; font-size: 20px;">{pred_size}</span> 🎯</div>',
                unsafe_allow_html=True
            )

            # 5️⃣ नंबर, साइज़ और कलर बॉक्स[span_9](start_span)[span_9](end_span)
            st.markdown(
                f"""
                <div class="result-grid">
                    <div class="result-card-box">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">NUMBER</div>
                        <div style="background-color: #FF3344; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 20px; font-weight: 900; margin: 0 auto; color: white;">{pred_num}</div>
                    </div>
                    <div class="result-card-box">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">SIZE</div>
                        <div style="background: #0088FF; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 14px; text-align: center;">{pred_size}</div>
                    </div>
                    <div class="result-card-box">
                        <div style="font-size: 11px; color: #FFFFFF; font-weight: 900; margin-bottom: 6px;">COLOR</div>
                        <div style="background-color: #FF3344; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 14px; text-align: center;">{pred_color}</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            
            # 6️⃣ रनिंग हिस्ट्री चार्ट[span_10](start_span)[span_10](end_span)
            boxes_html = ""
            for item in history:
                bg_color = "#FF9900" if item == "BIG" else "#0077FF"
                boxes_html += f"<div style='background: {bg_color}; color: white; padding: 5px 10px; border-radius: 4px; font-weight: 900; font-size: 11px; margin: 0 2px;'>{item}</div>"

            next_bg = "#0077FF" if pred_size == "SMALL" else "#FF9900"
            boxes_html += f"<div style='background: {next_bg}; color: white; padding: 5px 10px; border-radius: 10px; display: inline-flex; align-items: center; justify-content: center; font-weight: 900; font-size: 11px; border: 2px solid #00FF66; margin-left: 4px;'>🎯 NEXT: {pred_size}</div>"

            clean_game_name = selected_game.replace("⚪", "").replace("🔴", "").strip()
            st.markdown(
                f"""
                <div class="history-card">
                    <div style="font-size: 11px; color: #FFD700; font-weight: 900; margin-bottom: 8px;">📊 {clean_game_name} लाइव ओमनी-मैटrix रनिंग हिस्ट्री चार्ट:</div>
                    <div style="display: flex; justify-content: center; align-items: center; flex-wrap: wrap; gap: 4px;">{boxes_html}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        if "30S" in selected_game:
            render_game_panel(30, 11)
        elif "1M" in selected_game:
            render_game_panel(60, 23)
        elif "3M" in selected_game:
            render_game_panel(180, 37)
        elif "5M" in selected_game:
            render_game_panel(300, 53)

    success_dashboard_core()
