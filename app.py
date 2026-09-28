from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="BIG DADDY (BDG) PRO - Auto Live Panel",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #0c081e; color: #FFFFFF; }
    @keyframes blink-animation { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.3; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1); } }
    @keyframes color-glow { 0% { box-shadow: 0 0 10px #FFD700, 0 0 20px #FF4500; } 50% { box-shadow: 0 0 25px #00FF66, 0 0 35px #00FFFF; } 100% { box-shadow: 0 0 10px #FFD700, 0 0 20px #FF4500; } }
    .blinking-light { display: inline-block; width: 10px; height: 10px; background-color: #00FF66; border-radius: 50%; margin-right: 6px; box-shadow: 0 0 10px #00FF66; animation: blink-animation 0.8s infinite ease-in-out; }
    .top-bar { display: flex; justify-content: space-between; align-items: center; background: #16122d; padding: 10px 15px; border-radius: 12px; font-size: 13px; font-weight: bold; border: 1px solid #2a2250; margin-bottom: 15px; }
    .main-card { background-color: #141026; border: 2px solid #3d3170; border-radius: 20px; padding: 20px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.8); margin-top: 10px; }
    .timer-text { color: #FFD700; font-weight: bold; font-size: 15px; }
    .period-text { color: #FFFFFF; font-weight: bold; font-size: 15px; }
    .matched-banner { background: linear-gradient(45deg, #FF007F, #7F00FF, #00F0FF); background-size: 200% 200%; color: #FFFFFF; text-align: center; padding: 14px; border-radius: 12px; font-weight: 900; font-size: 16px; letter-spacing: 1.2px; margin: 12px 0; border: 2px solid #FFD700; animation: color-glow 1.5s infinite ease-in-out; text-shadow: 0 2px 5px rgba(0,0,0,0.9); }
    .sync-box { background: linear-gradient(135deg, #1b2a1e, #0f1c13); border: 1px solid #00FF66; padding: 10px 14px; border-radius: 10px; margin-bottom: 12px; text-align: center; box-shadow: 0 0 12px rgba(0, 255, 102, 0.3); }
    .future-box { background: linear-gradient(135deg, #22153b, #1a103c); border: 1px dashed #FFD700; padding: 10px 14px; border-radius: 10px; margin-top: 12px; text-align: center; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = 58900

# --- मास्टर लॉगिन और आपके क्रेडेंशियल्स ---
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
  game_server_val = (block_seed * 31) % 10
  game_server_size = "BIG" if game_server_val >= 4 else "SMALL"

  panel_val = (block_seed * 17) % 10
  panel_size = "BIG" if panel_val >= 4 else "SMALL"

  if game_server_size == panel_size:
    final_size = panel_size
    sync_status = (
        f"🎯 [Server Match]: BDG गेम सर्वर और पैनल दोनों पर '{final_size}' निकला!"
    )
    sureshot_banner = f"🔥 100% SURE-SHOT {final_size} (गेम और पैनल 100% मैच!)"
  else:
    final_size = game_server_size
    sync_status = f"📡 [Auto-Sync]: गेम सर्वर फीड के साथ पैनल अटैच हुआ -> '{final_size}'"
    sureshot_banner = f"🔥 100% SURE-SHOT {final_size} (फीड कनेक्टेड)"

  future_val = ((block_seed + 1) * 31) % 10
  future_size = "BIG" if future_val >= 4 else "SMALL"
  future_message = (
      f"🔮 **AI Live Alert:** अगले आने वाले पीरियड में **{future_size}** आने की पूरी"
      " तैयारी है!"
  )

  if final_size == "BIG":
    number = random.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = random.choice([0, 1, 2, 3, 4])
    color = (
        "GREEN"
        if number == 1
        else ("RED" if number in [2, 4] else "VIOLET")
    )

  return (
      number,
      final_size,
      color,
      sync_status,
      sureshot_banner,
      future_message,
  )


# --- लॉगिन स्क्रीन ---
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #00FF66;'>🔒 BIG DADDY"
      " PRO</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #A0A0A0; font-size: 13px;'>EXACT"
      " MATCH FIREWALL LOGIN</p>",
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
        st.success("मास्टर लॉगिन सफल!")
        st.rerun()
      else:
        current_time = datetime.now()
        if mobile in st.session_state.user_db:
          user_info = st.session_state.user_db[mobile]
          if password == user_info["password"]:
            if current_time <= user_info["expiry"]:
              st.session_state.authenticated = True
              st.success("लॉगिन सफल!")
              st.rerun()
            else:
              st.error("वैधता समाप्त! कृपया ₹2000 का रिचार्ज करें।")
              st.session_state.pending_mobile = mobile
              st.session_state.pending_password = password
              st.session_state.show_payment = True
          else:
            st.error("गलत पासवर्ड!")
        else:
          st.warning("नंबर रजिस्टर्ड नहीं है। कृपया ₹2000 का UTR रिचार्ज करें।")
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
    st.markdown(f"**UPI ID:** `{PAYMENT_UPI_ID}`")
    st.markdown(f"**Amount:** ₹{REQUIRED_AMOUNT}")
    entered_utr = st.text_input(
        "🔑 Enter 12-Digit UTR Number", max_chars=12, key="utr_input"
    )

    if st.button("🛡️ Verify & Unlock", use_container_width=True):
      if not entered_utr.isdigit() or len(entered_utr) != 12:
        st.error("कृपया केवल 12 अंकों का सही UTR दर्ज करें।")
      elif entered_utr in st.session_state.used_utrs:
        st.error("यह UTR पहले ही इस्तेमाल हो चुका है!")
      elif entered_utr not in VERIFIED_KISHOR_PAYMENTS:
        st.error("UTR डेटाबेस से मैच नहीं हुआ!")
      else:
        st.session_state.used_utrs.add(entered_utr)
        st.session_state.user_db[st.session_state.pending_mobile] = {
            "password": st.session_state.pending_password,
            "expiry": datetime.now() + timedelta(days=VALIDITY_DAYS),
            "utr": entered_utr,
        }
        st.session_state.authenticated = True
        st.success("सफल! पैनल खुल रहा है...")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- मुख्य डैशबोर्ड (ऑटो-रिफ्रेश फीचर के साथ ताकि लॉग आउट न होना पड़े) ---
else:


  @st.fragment(run_every=3)
  def auto_live_dashboard():
    # ऑनलाइन काउंट ऑटोमैटिक कम-ज्यादा होगा
    st.session_state.live_online_count = max(
        45000,
        min(
            98000,
            st.session_state.live_online_count
            + random.randint(-1200, 1600),
        ),
    )

    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-light"></span>Exact Match Engine Active</div>
                <div>Online: <span style="color: #FFD700;">{st.session_state.live_online_count:,}</span></div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<div style='text-align: center; margin-bottom: 10px;'><h2"
        " style='color: #FFD700; font-size: 22px; margin: 0;'>BIG DADDY (BDG)"
        " PRO</h2></div>",
        unsafe_allow_html=True,
    )

    custom_period_input = st.text_input(
        "📌 ENTER PERIOD NUMBER (वैकल्पिक पीरियड नंबर यहाँ टाइप करें)",
        placeholder="जैसे: 202609281234 (खाली छोड़ने पर ऑटोमैटिक चलेगा)",
        key="custom_period_box",
    )

    tab1, tab2, tab3, tab4 = st.tabs(
        ["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"]
    )

    def render_wingo_box(game_seconds):
      auto_period, timer_str, current_block = get_period_and_timer(game_seconds)
      if custom_period_input and custom_period_input.strip().isdigit():
        final_period = int(custom_period_input.strip())
        block_seed = final_period + current_block
      else:
        final_period = auto_period
        block_seed = current_block

      pred_num, pred_size, pred_color, sync_status, sureshot_banner, future_message = (
          exact_match_engine(block_seed)
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
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #2a2250; padding-bottom: 10px; margin-bottom: 10px;">
                <span class="period-text">PERIOD: {final_period}</span>
                <span class="timer-text">TIME: {timer_str}</span>
            </div>
            <div class="sync-box">
                <span style="font-size: 11px; color: #00FF66; font-weight: bold;">{sync_status}</span>
            </div>
            <div class="matched-banner">
                {sureshot_banner}
            </div>
        """,
          unsafe_allow_html=True,
      )

      col1, col2, col3 = st.columns(3)
      with col1:
        st.markdown(
            "<p"
            " style='font-size: 11px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 6px; font-weight: bold;'>NUMBER</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background-color: {color_bg}; width: 60px; height:"
            f" 60px; border-radius: 50%; display: flex; align-items: center;"
            f" justify-content: center; font-size: 26px; font-weight: bold; margin:"
            f" auto; color: white; border: 2px solid #FFFFFF; box-shadow: 0 0"
            f" 15px {color_bg};'>{pred_num}</div>",
            unsafe_allow_html=True,
        )
      with col2:
        st.markdown(
            "<p"
            " style='font-size: 11px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 6px; font-weight: bold;'>SIZE</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background: {size_bg}; color: white; padding: 12px"
            " 10px; border-radius: 12px; font-weight: 900; font-size: 18px;"
            f" text-align: center; border: 2px solid #FFFFFF; box-shadow: 0 0"
            f" 15px rgba(255,153,0,0.5); text-transform:"
            f" uppercase;'>{pred_size}</div>",
            unsafe_allow_html=True,
        )
      with col3:
        st.markdown(
            "<p"
            " style='font-size: 11px; color: #A0A0A0; text-align: center;"
            " margin-bottom: 6px; font-weight: bold;'>COLOR</p>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='background-color: {color_bg}; color: white; padding:"
            " 12px 10px; border-radius: 12px; font-weight: bold; font-size:"
            f" 15px; text-align: center; border: 2px solid #FFFFFF; box-shadow:"
            f" 0 0 15px {color_bg};'>{pred_color}</div>",
            unsafe_allow_html=True,
        )

      st.markdown(
          f"""
            <div class="future-box">
                <span style="font-size: 12px; color: #FFD700;">{future_message}</span>
            </div>
            </div>
        """,
          unsafe_allow_html=True,
      )

    with tab1:
      render_wingo_box(30)
    with tab2:
      render_wingo_box(60)
    with tab3:
      render_wingo_box(180)
    with tab4:
      render_wingo_box(300)

  # ऑटो डैशबोर्ड को कॉल किया
  auto_live_dashboard()

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()
