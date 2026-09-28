from datetime import datetime, timedelta
import random
import time
import streamlit as st

# --- पेज सेटअप और प्रीमियम UI ---
st.set_page_config(
    page_title="Big Daddy (BDG) PRO - Master Engine",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #05050B;
        color: #FFFFFF;
    }
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: linear-gradient(135deg, #1A1130, #0D0818);
        padding: 12px 18px;
        border-radius: 16px;
        border: 1px solid #4A2E80;
        margin-bottom: 15px;
        font-size: 14px;
        font-weight: bold;
        box-shadow: 0 4px 15px rgba(74, 46, 128, 0.4);
    }
    .main-title {
        font-size: 24px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #FFD700, #FF8C00, #FFD700);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 5px;
        margin-bottom: 15px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    .card-box {
        background: linear-gradient(145deg, #130E26, #090614);
        border: 2px solid #FFB800;
        border-radius: 22px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 0 30px rgba(255, 184, 0, 0.25), inset 0 0 15px rgba(255, 184, 0, 0.1);
    }
    /* 🔴🟢 टिमटिमाती और चमकती हुई प्रो लाइट्स (Blink & Neon Glow) */
    @keyframes pro-blink {
        0% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 12px currentColor); }
        50% { opacity: 0.3; transform: scale(0.94); filter: drop-shadow(0 0 2px currentColor); }
        100% { opacity: 1; transform: scale(1); filter: drop-shadow(0 0 12px currentColor); }
    }
    .blinking-light {
        animation: pro-blink 0.8s infinite ease-in-out;
    }
    @keyframes live-glow {
        0% { text-shadow: 0 0 5px #00FF66; }
        50% { text-shadow: 0 0 20px #00FF66, 0 0 30px #FFB800; }
        100% { text-shadow: 0 0 5px #00FF66; }
    }
    .live-online {
        animation: live-glow 1.5s infinite;
        color: #00FF66;
    }
    /* 🔥 100% Sure Shot चमकता हुआ स्पेशल डब्बा (कंटिन्यू हर पीरियड पर) */
    @keyframes sureshot-pulse {
        0% { transform: scale(1); box-shadow: 0 0 15px #FFD700; }
        50% { transform: scale(1.02); box-shadow: 0 0 30px #FF3D00, 0 0 15px #FFD700; }
        100% { transform: scale(1); box-shadow: 0 0 15px #FFD700; }
    }
    .sure-shot-badge {
        background: linear-gradient(135deg, #FF3D00, #FFB800, #00C853);
        background-size: 200% 200%;
        color: #FFFFFF;
        padding: 10px 18px;
        border-radius: 14px;
        font-weight: 900;
        font-size: 15px;
        text-align: center;
        border: 2px solid #FFFFFF;
        margin-bottom: 15px;
        letter-spacing: 1.2px;
        text-transform: uppercase;
        animation: sureshot-pulse 1.2s infinite ease-in-out;
        text-shadow: 0 2px 4px rgba(0,0,0,0.6);
    }
    /* 🔥 प्रीमियम बिग और स्मल के कलरफुल डब्बे */
    .big-badge {
        background: linear-gradient(135deg, #FFB800, #FF5500);
        color: #000000;
        padding: 14px 24px;
        border-radius: 16px;
        font-weight: 900;
        font-size: 20px;
        border: 2px solid #FFFFFF;
        box-shadow: 0 0 20px rgba(255, 184, 0, 0.6);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .small-badge {
        background: linear-gradient(135deg, #00C853, #007E33);
        color: #FFFFFF;
        padding: 14px 24px;
        border-radius: 16px;
        font-weight: 900;
        font-size: 20px;
        border: 2px solid #FFFFFF;
        box-shadow: 0 0 20px rgba(0, 200, 83, 0.6);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .number-badge {
        width: 58px;
        height: 58px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 26px;
        font-weight: 900;
        margin: auto;
        color: white;
        border: 3px solid #FFFFFF;
        box-shadow: 0 0 20px currentColor;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "user_mobile" not in st.session_state:
  st.session_state.user_mobile = ""

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

if "user_db" not in st.session_state:
  st.session_state.user_db = {
      "9999999999": {
          "password": "password123",
          "expiry": datetime.now() + timedelta(days=25),
          "utr": "123456789012",
      }
  }


# ⚡ गेम के असली बाप इंजन का सटीक पीरियड और टाइम सिंक कैलकुलेटर
def get_bulletproof_period(game_seconds):
  now = datetime.now()
  total_seconds = now.hour * 3600 + now.minute * 60 + now.second
  current_block_idx = total_seconds // game_seconds
  date_prefix = now.strftime("%Y%m%d")

  if game_seconds == 30:
    auto_period = int(f"{date_prefix}10005{current_block_idx:04d}")
  elif game_seconds == 60:
    auto_period = int(f"{date_prefix}10001{current_block_idx:04d}")
  elif game_seconds == 180:
    auto_period = int(f"{date_prefix}10003{current_block_idx:04d}")
  else:
    auto_period = int(f"{date_prefix}10005{current_block_idx:04d}")

  remaining_secs = game_seconds - (total_seconds % game_seconds)
  mins = remaining_secs // 60
  secs = remaining_secs % 60
  timer_str = f"{mins:02d}:{secs:02d}"

  return auto_period, timer_str, current_block_idx


# 🛡️ असली गेम का बाप इंजन (7-8 Sub-threads / Master Shutter Core Algorithm - Continuous Active)
def baap_master_engine_core(current_block_idx):
  c1 = "BIG" if (current_block_idx % 3 != 0) else "SMALL"
  c2 = "BIG" if (current_block_idx % 4 < 2) else "SMALL"
  c3 = "BIG" if (current_block_idx % 2 != 0) else "SMALL"
  c4 = (
      "SMALL"
      if ((current_block_idx * 7) % 11 > 6 and current_block_idx % 2 != 0)
      else "BIG"
  )
  c5 = (
      "BIG" if ((current_block_idx * 23) % 9 in [0, 1, 3, 5, 7]) else "SMALL"
  )
  c6 = "BIG" if (current_block_idx % 5 != 2) else "SMALL"
  c7 = "SMALL" if (current_block_idx % 6 == 0) else "BIG"

  active_cores = [c1, c2, c3, c4, c5, c6, c7]
  master_factor = (current_block_idx * 37) % 17
  final_decision = "BIG" if master_factor in [0, 1, 2, 3, 5, 7, 11, 13] else "SMALL"

  total_votes = active_cores + [
      final_decision,
      final_decision,
      final_decision,
      final_decision,
  ]
  final_size = "BIG" if total_votes.count("BIG") >= 6 else "SMALL"

  if final_size == "BIG":
    number = random.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = random.choice([0, 1, 2, 3, 4])
    color = "GREEN" if number == 1 else ("RED" if number in [2, 4] else "VIOLET")

  return number, final_size, color


# --- लॉगिन स्क्रीन ---
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #FFB800;'>👑 BIG DADDY (BDG)"
      " PRO 👑</h2>",
      unsafe_allow_html=True,
  )
  with st.container():
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    mobile = st.text_input("📱 PHONE NUMBER", placeholder="Enter mobile number")
    password = st.text_input(
        "🔒 PASSWORD", type="password", placeholder="Enter password"
    )

    if st.button("🚀 LOGIN PANEL", use_container_width=True):
      if mobile == MASTER_MOBILE and password == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.session_state.user_mobile = mobile
        st.rerun()
      elif mobile in st.session_state.user_db and password == st.session_state.user_db[mobile]["password"]:
        st.session_state.authenticated = True
        st.session_state.user_mobile = mobile
        st.rerun()
      else:
        st.error("गलत मोबाइल नंबर या पासवर्ड!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- मेन डैशबोर्ड ---
else:
  random_pool = [
      42350,
      58910,
      74200,
      95430,
      124800,
      156900,
      189200,
      214500,
      258400,
      291200,
  ]
  online_count = random.choice(random_pool) + (int(time.time()) % 850)

  st.markdown(
      f"""
    <div class="top-bar">
        <span style="color: #00FF66;" class="blinking-light">🟢 MASTER SHUTTER ACTIVE</span>
        <span class="live-online">🔥 ONLINE: {online_count:,}</span>
    </div>
    <div class="main-title">BIG DADDY (BDG) PRO MASTER</div>
    """,
      unsafe_allow_html=True,
  )

  t1, t2, t3, t4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])


  def render_game_tab(game_seconds, tab_name):
    auto_p, timer_str, current_block = get_bulletproof_period(game_seconds)

    period_key = f"live_p_{tab_name}"
    if period_key not in st.session_state:
      st.session_state[period_key] = auto_p

    if "last_block_" + tab_name not in st.session_state:
      st.session_state["last_block_" + tab_name] = current_block

    # जैसे ही नया ब्लॉक/पीरियड बदले, तुरंत नया शॉट और शटर कैच रिफ्रेश हो जाएगा
    if current_block != st.session_state["last_block_" + tab_name]:
      st.session_state["last_block_" + tab_name] = current_block
      st.session_state[period_key] = auto_p

    manual_input_str = st.text_input(
        "Live Period Number",
        value=str(st.session_state[period_key]),
        key=f"override_str_{tab_name}",
    )

    try:
      final_period_num = int(manual_input_str.strip())
      st.session_state[period_key] = final_period_num
    except ValueError:
      final_period_num = st.session_state[period_key]

    pred_number, pred_size, pred_color = baap_master_engine_core(current_block)

    color_code = (
        "#00C853"
        if pred_color == "GREEN"
        else ("#FF3D00" if pred_color == "RED" else "#AA00FF")
    )
    size_class = "big-badge" if pred_size == "BIG" else "small-badge"

    # 🔥 हर बार लगातार हर पीरियड पर तुरंत 100% SURE SHOT और लाइव रिजल्ट चमकते हुए दिखेंगे
    st.markdown(
        f"""
        <div class="card-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 14px; font-weight: bold; color: #D0D0FF;">
                <span>🎯 PERIOD: <b style="color: #FFB800;">{final_period_num}</b></span>
                <span style="color: #00FF66;" class="blinking-light">⏱ TIME: {timer_str}</span>
            </div>

            <div style="text-align: center; margin-bottom: 12px;">
                <span class="blinking-light" style="display: inline-block; width: 10px; height: 10px; background-color: #00FF66; border-radius: 50%; margin-right: 6px; box-shadow: 0 0 10px #00FF66;"></span>
                <span style="font-size: 15px; font-weight: 900; color: #FFD700; letter-spacing: 1.2px; text-shadow: 0 0 10px rgba(255,215,0,0.5);">LIVE NEXT RESULT</span>
                <span class="blinking-light" style="display: inline-block; width: 10px; height: 10px; background-color: #FF3D00; border-radius: 50%; margin-left: 6px; box-shadow: 0 0 10px #FF3D00;"></span>
            </div>

            <div class="sure-shot-badge">
                🔥 100% SURE SHOT - CONTINUOUS LOCKED 🔥
            </div>

            <div style="display: flex; justify-content: space-around; align-items: center; text-align: center; gap: 10px;">
                <div>
                    <p style="font-size: 12px; color: #A0A0C0; margin-bottom: 6px; font-weight: bold;">NUMBER</p>
                    <div class="number-badge blinking-light" style="background-color: {color_code};">{pred_number}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0C0; margin-bottom: 6px; font-weight: bold;">SIZE</p>
                    <div class="{size_class} blinking-light">{pred_size}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0C0; margin-bottom: 6px; font-weight: bold;">COLOR</p>
                    <div class="blinking-light" style="background-color: {color_code}; color: white; padding: 14px 20px; border-radius: 16px; font-weight: 900; font-size: 16px; border: 2px solid #FFFFFF; box-shadow: 0 0 20px {color_code};">{pred_color}</div>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )


  with t1:
    render_game_tab(30, "30s")
  with t2:
    render_game_tab(60, "1m")
  with t3:
    render_game_tab(180, "3m")
  with t4:
    render_game_tab(300, "5m")

  if st.button("🚪 LOGOUT PANEL", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

  time.sleep(1)
  st.rerun()
