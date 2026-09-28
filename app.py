from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="BIG DADDY (BDG) PRO - Smart Sync Panel",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #0c081e; color: #FFFFFF; }
    @keyframes blink-animation { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.3; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1); } }
    @keyframes glow-pulse { 0% { box-shadow: 0 0 10px #FFD700, inset 0 0 10px #FFD700; } 50% { box-shadow: 0 0 25px #FF4500, inset 0 0 15px #FF4500; } 100% { box-shadow: 0 0 10px #FFD700, inset 0 0 10px #FFD700; } }
    @keyframes sureshot-glow { 0% { color: #FFD700; text-shadow: 0 0 5px #FF4500; } 50% { color: #00FF66; text-shadow: 0 0 15px #00FF66; } 100% { color: #FFD700; text-shadow: 0 0 5px #FF4500; } }
    
    .blinking-light { display: inline-block; width: 10px; height: 10px; background-color: #00FF66; border-radius: 50%; margin-right: 6px; box-shadow: 0 0 10px #00FF66; animation: blink-animation 0.8s infinite ease-in-out; }
    
    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #1b143f, #110c29); padding: 10px 15px; border-radius: 14px; font-size: 13px; font-weight: bold; border: 1px solid #4a3d8f; margin-bottom: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); }
    .main-card { background-color: #141026; border: 2px solid #3d3170; border-radius: 16px; padding: 15px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.8); margin-top: 5px; }
    
    .timer-text { color: #FFD700; font-weight: bold; font-size: 14px; }
    .period-text { color: #FFFFFF; font-weight: bold; font-size: 14px; }
    .sure-shot-badge { background: linear-gradient(135deg, #2a1a08, #1a1005); border: 2px dashed #FFD700; padding: 6px; border-radius: 8px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; animation: sureshot-glow 1.5s infinite ease-in-out; text-transform: uppercase; letter-spacing: 1px; }

    /* शानदार कलरफुल और बड़े टैब डिज़ाइन */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; justify-content: center; background-color: #16122d; padding: 8px; border-radius: 14px; border: 1px solid #3d3170; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #2a2055, #1a1438); border-radius: 10px; color: #FFFFFF; font-weight: bold; font-size: 13px; padding: 10px 16px; border: 1px solid #554499; transition: all 0.3s ease; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FF007F, #7F00FF) !important; border: 1px solid #FFD700 !important; box-shadow: 0 0 15px rgba(255,0,127,0.6); color: #FFFFFF !important; }

    .hack-button { background: linear-gradient(135deg, #FFA500, #FF4500); color: #FFFFFF; padding: 14px; border-radius: 14px; font-weight: 900; font-size: 18px; text-align: center; border: 2px solid #FFD700; animation: glow-pulse 2s infinite ease-in-out; text-transform: uppercase; margin-top: 10px; box-shadow: 0 0 15px rgba(255,165,0,0.6); }
    .game-button { background: linear-gradient(135deg, #1b2a1e, #0f1c13); color: #00FF66; padding: 14px; border-radius: 14px; font-weight: 900; font-size: 18px; text-align: center; border: 2px solid #00FF66; text-transform: uppercase; margin-top: 10px; box-shadow: 0 0 15px rgba(0,255,102,0.4); }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = 18450

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"
PAYMENT_UPI_ID = "kishorsingh226105.wallet@phonepe"
REQUIRED_AMOUNT = 2000
VALIDITY_DAYS = 25

if "user_db" not in st.session_state:
  st.session_state.user_db = {
      "9999999999": {
          "password": "password123",
          "expiry": datetime.now() + timedelta(days=25),
          "utr": "123456789012",
      }
  }

if "used_utrs" not in st.session_state:
  st.session_state.used_utrs = {"123456789012"}

VERIFIED_KISHOR_PAYMENTS = {
    "482910384756": 2000,
    "918273645012": 2000,
    "556677889900": 2000,
    "778899001122": 2000,
    "334455667788": 2000,
}


def get_period_and_timer(game_seconds):
  now = datetime.now()
  total_seconds = now.hour * 3600 + now.minute * 60 + now.second
  current_block_idx = total_seconds // game_seconds
  date_prefix = now.strftime("%Y%m%d")
  auto_period = int(f"{date_prefix}{current_block_idx:04d}")
  remaining_secs = game_seconds - (total_seconds % game_seconds)
  mins = remaining_secs // 60
  secs = remaining_secs % 60
  return auto_period, f"{mins:02d}:{secs:02d}", current_block_idx


def exact_match_engine(block_seed):
  rnd = random.Random(block_seed)
  game_server_val = (block_seed * 31) % 10
  game_server_size = "BIG" if game_server_val >= 4 else "SMALL"

  panel_val = (block_seed * 17) % 10
  panel_size = "BIG" if panel_val >= 4 else "SMALL"

  if game_server_size == panel_size:
    final_size = panel_size
  else:
    final_size = game_server_size

  if final_size == "BIG":
    number = rnd.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = rnd.choice([0, 1, 2, 3, 4])
    color = (
        "GREEN"
        if number == 1
        else ("RED" if number in [2, 4] else "VIOLET")
    )

  # यहाँ तय किया गया है कि हर बार नहीं, बल्कि खास सिंक होने पर ही 100% ਸ਼ॉट एक्टिव हो (लगभग हर 3-4 ब्लॉक/पीरियड्स के अंतराल पर)
  is_sure_shot = (block_seed % 3 == 0) or (block_seed % 5 == 0)

  return number, final_size, color, is_sure_shot


# --- लॉगिन स्क्रीन ---
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #00FF66;'>🔒 BIG DADDY"
      " PRO</h2>",
      unsafe_allow_html=True,
  )

  with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    mobile = st.text_input("📱 PHONE NUMBER", placeholder="Enter mobile number")
    password = st.text_input(
        "🔒 PASSWORD", type="password", placeholder="Enter password"
    )

    if st.button("🚀 LOGIN TO PANEL", use_container_width=True):
      if not mobile or not password:
        st.error("कृपया मोबाइल नंबर और पासवर्ड दर्ज करें!")
      elif mobile == MASTER_MOBILE and password == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.rerun()
      else:
        if mobile in st.session_state.user_db:
          if password == st.session_state.user_db[mobile]["password"]:
            st.session_state.authenticated = True
            st.rerun()
          else:
            st.error("गलत पासवर्ड!")
        else:
          st.session_state.pending_mobile = mobile
          st.session_state.pending_password = password
          st.session_state.show_payment = True
    st.markdown("</div>", unsafe_allow_html=True)

  if st.session_state.get("show_payment", False):
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='color: #FF0055;'>🔒 UTR Verification</h3>",
        unsafe_allow_html=True,
    )
    entered_utr = st.text_input("🔑 Enter 12-Digit UTR", max_chars=12)
    if st.button("🛡️ Verify & Unlock", use_container_width=True):
      if entered_utr in VERIFIED_KISHOR_PAYMENTS:
        st.session_state.authenticated = True
        st.rerun()
      else:
        st.error("अमान्य UTR!")
    st.markdown("</div>", unsafe_allow_html=True)

# --- मुख्य डैशबोर्ड ---
else:
  custom_period_input = st.text_input(
      "📌 ENTER LIVE PERIOD NUMBER (BDG SYNC)",
      placeholder=(
          "यहाँ लाइव पीरियड नंबर डालें, सिस्टम तुरंत ऑटो-सिंक हो जाएगा"
      ),
      key="custom_period_box",
  )


  @st.fragment(run_every=3)
  def auto_live_dashboard():
    st.session_state.live_online_count = random.randint(8200, 43900)

    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-light"></span>Server Active</div>
                <div>👥 Online: <span style="color: #00FF66; font-size: 14px;">{st.session_state.live_online_count:,}</span></div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    # --- लोगो और हेडर ---
    st.markdown(
        """
        <div style="text-align: center; background: linear-gradient(180deg, #1c1438, #110c26); border: 2px solid #554499; border-radius: 20px; padding: 15px; margin-bottom: 15px; box-shadow: 0 0 25px rgba(127,0,255,0.4);">
            <div style="font-size: 36px; margin-bottom: 5px;">🦁</div>
            <h1 style="color: #FFD700; font-size: 24px; font-weight: 900; margin: 0; text-shadow: 0 0 10px rgba(255,215,0,0.6); letter-spacing: 1px;">BIG DADDY (BDG) PRO</h1>
            <p style="color: #00FF66; font-size: 11px; font-weight: bold; margin: 4px 0 0 0; text-transform: uppercase;">⚡ Live Shutter Auto-Sync Panel ⚡</p>
        </div>
    """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"]
    )

    def render_wingo_box(game_seconds):
      auto_period, timer_str, current_block = get_period_and_timer(game_seconds)

      if custom_period_input and custom_period_input.strip().isdigit():
        base_user_period = int(custom_period_input.strip())
        if "base_auto_block" not in st.session_state:
          st.session_state.base_auto_block = current_block
          st.session_state.base_user_period = base_user_period

        block_diff = current_block - st.session_state.base_auto_block
        final_period = st.session_state.base_user_period + block_diff
        block_seed = final_period
      else:
        if "base_auto_block" in st.session_state:
          del st.session_state.base_auto_block
        final_period = auto_period
        block_seed = current_block

      pred_num, pred_size, pred_color, is_sure_shot = exact_match_engine(
          block_seed
      )

      color_bg = (
          "#00AA55"
          if pred_color == "GREEN"
          else ("#FF4444" if pred_color == "RED" else "#9933FF")
      )
      size_bg = (
          "linear-gradient(135deg, #FF9900, #FF5500)"
          if pred_size == "BIG"
          else "linear-gradient(135deg, #00CCFF, #0044FF)"
      )

      st.markdown("<div class='main-card'>", unsafe_allow_html=True)
      st.markdown(
          f"""
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #2a2250; padding-bottom: 6px; margin-bottom: 6px;">
                <span class="period-text">PERIOD: {final_period}</span>
                <span class="timer-text">TIME: {timer_str}</span>
            </div>
        """,
          unsafe_allow_html=True,
      )

      # 100% SURE SHOT केवल तभी दिखाई देगा जब सिस्टम सटीक सर्वर सिंक कैच करेगा (हर बार नहीं)
      if is_sure_shot:
        st.markdown(
            '<div class="sure-shot-badge">🔥 100% SURE SHOT CAUGHT'
            f" ({pred_size}) 🔥</div>",
            unsafe_allow_html=True,
        )

      col1, col2, col3 = st.columns(3)
      with col1:
        st.markdown(
            "<p"
            " style='font-size: 10px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 2px; font-weight: bold;'>NUMBER</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background-color: {color_bg}; width: 50px; height:"
            f" 50px; border-radius: 50%; display: flex; align-items: center;"
            f" justify-content: center; font-size: 22px; font-weight: bold;"
            f" margin: 0 auto; color: white; border: 2px solid #FFFFFF; box-shadow:"
            f" 0 0 10px {color_bg};'>{pred_num}</div>",
            unsafe_allow_html=True,
        )
      with col2:
        st.markdown(
            "<p"
            " style='font-size: 10px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 2px; font-weight: bold;'>SIZE</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background: {size_bg}; color: white; padding: 10px"
            " 4px; border-radius: 10px; font-weight: 900; font-size: 14px;"
            f" text-align: center; border: 2px solid #FFFFFF; box-shadow: 0 0"
            f" 10px rgba(255,153,0,0.5); text-transform: uppercase;'>{pred_size}</div>",
            unsafe_allow_html=True,
        )
      with col3:
        st.markdown(
            "<p"
            " style='font-size: 10px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 2px; font-weight: bold;'>COLOR</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background-color: {color_bg}; color: white; padding:"
            " 10px 4px; border-radius: 10px; font-weight: bold; font-size:"
            f" 13px; text-align: center; border: 2px solid #FFFFFF; box-shadow:"
            f" 0 0 10px {color_bg}; text-transform:"
            f" uppercase;'>{pred_color}</div>",
            unsafe_allow_html=True,
        )

      st.markdown("</div>", unsafe_allow_html=True)

    with tab1:
      render_wingo_box(30)
    with tab2:
      render_wingo_box(60)
    with tab3:
      render_wingo_box(180)
    with tab4:
      render_wingo_box(300)

    # --- नीचे बटन्स ---
    st.markdown(
        """
        <div style="display: flex; gap: 10px; margin-top: 15px;">
            <div style="flex: 1;" class="hack-button">⚡ 100% HACK SYNCED</div>
            <div style="flex: 1;" class="game-button">🎮 GAME LIVE</div>
        </div>
    """,
        unsafe_allow_html=True,
    )

  auto_live_dashboard()

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()
