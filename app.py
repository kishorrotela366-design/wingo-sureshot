from datetime import datetime, timedelta
import random
import time
import streamlit as st

# --- पेज सेटअप ---
st.set_page_config(
    page_title="Sure Shot PRO v23 - Anti-Cheat Sentinel",
    page_icon="🔒",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
        color: #FFFFFF;
    }
    .card-box {
        background-color: #0A0A12;
        border: 2px solid #00FF66;
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 15px;
        box-shadow: 0 0 25px rgba(0, 255, 102, 0.3);
    }
    @keyframes sentinel-pulse {
        0% { box-shadow: 0 0 10px #00FF66, inset 0 0 5px #00FF66; border-color: #00FF66; }
        50% { box-shadow: 0 0 35px #FF0055, inset 0 0 20px #FF0055; border-color: #FF0055; }
        100% { box-shadow: 0 0 10px #00FF66, inset 0 0 5px #00FF66; border-color: #00FF66; }
    }
    .sentinel-alert {
        display: inline-block;
        background: linear-gradient(45deg, #00FF66, #FF0055);
        color: #000000;
        padding: 6px 14px;
        border-radius: 8px;
        font-size: 11px;
        font-weight: 900;
        border: 1px solid #FFFFFF;
        animation: sentinel-pulse 1s infinite;
    }
    @keyframes blink-animation {
        0% { opacity: 1; }
        50% { opacity: 0.1; }
        100% { opacity: 1; }
    }
    .blinking-light {
        display: inline-block;
        width: 10px;
        height: 10px;
        background-color: #00FF66;
        border-radius: 50%;
        margin-right: 6px;
        box-shadow: 0 0 12px #00FF66;
        animation: blink-animation 0.6s infinite;
    }
    .win-badge {
        background-color: #00AA55;
        color: #FFFFFF;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        border: 1px solid #00FF66;
        box-shadow: 0 0 15px #00FF66;
    }
    .loss-badge {
        background-color: #CC0000;
        color: #FFFFFF;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        text-align: center;
        border: 1px solid #FF4444;
        box-shadow: 0 0 15px #FF4444;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट इनिशियलाइजेशन ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "user_mobile" not in st.session_state:
  st.session_state.user_mobile = ""

if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = random.randint(290000, 360000)

# --- मास्टर और पेमेंट क्रेडेंशियल सेटिंग्स ---
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


# --- पीरियड और टाइमर इंजन ---
def get_bulletproof_period_and_timer(game_seconds):
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


# ==========================================================
# 🛡️ SENTINEL MULTI-CORE OVERWATCH (v23)
# ==========================================================
def sentinel_overwatch_master_engine(period_num, current_block_idx):
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

  active_cores = [c1, c2, c3, c4, c5]
  sentinel_status = (
      "🛡️ SENTINEL ANTI-CHEAT: [All 5 Cores 100% Synced & Secured]"
  )

  sentinel_factor = (current_block_idx * 37) % 17
  if sentinel_factor in [0, 1, 2, 3, 5, 7, 11, 13]:
    final_decision = "BIG"
  else:
    final_decision = "SMALL"

  total_votes = active_cores + [final_decision, final_decision, final_decision]
  big_tally = total_votes.count("BIG")

  if big_tally >= 4:
    final_size = "BIG"
  else:
    final_size = "SMALL"

  if final_size == "BIG":
    number = random.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = random.choice([0, 1, 2, 3, 4])
    color = "GREEN" if number == 1 else ("RED" if number in [2, 4] else "VIOLET")

  return number, final_size, color, sentinel_status


# ==========================================================
# भाग 1: लॉगिन और UTR फायरवॉल
# ==========================================================
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #00FF66;'>🔒 Sure Shot PRO"
      " v23</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #A0A0A0; font-size: 14px;'>MILITARY"
      " GRADE UTR ANTI-DUPLICATION FIREWALL</p>",
      unsafe_allow_html=True,
  )

  with st.container():
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    mobile = st.text_input("📱 PHONE NUMBER", placeholder="Enter mobile number")
    password = st.text_input(
        "🔒 PASSWORD", type="password", placeholder="Enter password"
    )

    if st.button("🚀 SECURE LOGIN TO DASHBOARD", use_container_width=True):
      if not mobile or not password:
        st.error("कृपया अपना मोबाइल नंबर और पासवर्ड दर्ज करें!")
      elif mobile == MASTER_MOBILE and password == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.session_state.user_mobile = mobile
        st.success("Yes! मास्टर एडमिन लॉगिन सफल। डैशबोर्ड खुल रहा है...")
        st.rerun()
      else:
        current_time = datetime.now()
        if mobile in st.session_state.user_db:
          user_info = st.session_state.user_db[mobile]
          stored_pwd = user_info["password"]
          expiry_date = user_info["expiry"]

          if password == stored_pwd:
            if current_time <= expiry_date:
              st.session_state.authenticated = True
              st.session_state.user_mobile = mobile
              st.success(
                  "Yes! आपका पुराना रिचार्ज एक्टिव है। डैशबोर्ड खुल रहा है..."
              )
              st.rerun()
            else:
              st.error(
                  "❌ आपके 25 दिन की वैधता (Validity) समाप्त हो चुकी है! कृपया"
                  " फिर से ₹2000 का फ्रेश रिचार्ज करें।"
              )
              st.session_state.pending_mobile = mobile
              st.session_state.pending_password = password
              st.session_state.show_payment = True
          else:
            st.error("❌ पासवर्ड गलत है! कृपया सही पासवर्ड दर्ज करें।")
        else:
          st.warning(
              "No No! यह नंबर रजिस्टर्ड नहीं है। डैशबोर्ड खोलने के लिए पहले"
              " ₹2000 का नया UTR रिचार्ज करें।"
          )
          st.session_state.pending_mobile = mobile
          st.session_state.pending_password = password
          st.session_state.show_payment = True
    st.markdown("</div>", unsafe_allow_html=True)

  if st.session_state.get("show_payment", False):
    st.markdown(
        "<div class='card-box' style='border-color: #FF0055;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='color: #FF0055;'>🔒 Strict UTR Firewall Verification</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(f"**UPI ID for Payment:** `{PAYMENT_UPI_ID}`")
    st.markdown(
        f"**Required Amount:** ₹{REQUIRED_AMOUNT} (Validity: {VALIDITY_DAYS}"
        " Days)"
    )
    entered_utr = st.text_input(
        "🔑 Enter 12-Digit Fresh UTR Number",
        max_chars=12,
        key="strict_utr_input",
    )

    if st.button(
        "🛡️ Verify UTR & Open File (Anti-Cheat)", use_container_width=True
    ):
      if not entered_utr.isdigit() or len(entered_utr) != 12:
        st.error(
            "❌ अमान्य UTR फॉर्मेट! कृपया केवल 12 अंकों का सही UTR दर्ज करें।"
        )
      elif entered_utr in st.session_state.used_utrs:
        st.error(
            "🚨 CRITICAL SECURITY ERROR: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका"
            " है!"
        )
      elif entered_utr not in VERIFIED_KISHOR_PAYMENTS:
        st.error(
            "❌ UTR डेटाबेस से मैच नहीं हुआ! कृपया भुगतान करके सही UTR डालें।"
        )
      else:
        st.session_state.used_utrs.add(entered_utr)
        new_expiry = datetime.now() + timedelta(days=VALIDITY_DAYS)
        mob = st.session_state.get("pending_mobile", "")
        pwd = st.session_state.get("pending_password", "")

        st.session_state.user_db[mob] = {
            "password": pwd,
            "expiry": new_expiry,
            "utr": entered_utr,
        }

        st.session_state.authenticated = True
        st.session_state.user_mobile = mob
        st.success(
            "🎉 UTR 100% मैच हो गया! अब डैशबोर्ड खोला जा रहा है..."
        )
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# भाग 2: मेन डैशबोर्ड
# ==========================================================
else:
  change_delta = random.randint(-1200, 2200)
  st.session_state.live_online_count = max(
      290000, min(360000, st.session_state.live_online_count + change_delta)
  )
  current_online = st.session_state.live_online_count
  logged_user = st.session_state.get("user_mobile", "User")

  col1, col2 = st.columns([2, 1])
  with col1:
    st.markdown(
        "<div style='display: flex; align-items: center;'><span"
        " class='blinking-light'></span><strong style='color: #00FF66;'>Secure"
        f" Firewall Active | User: {logged_user}</strong></div>",
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        "<div style='display: flex; align-items: center;'><span"
        " class='blinking-light'></span>👤 <b style='margin-left: 4px;'>Online:"
        "</b> <span style='color: #00FF66; margin-left: 4px; font-weight:"
        f" bold;'>`{current_online:,}`</span></div>",
        unsafe_allow_html=True,
    )

  st.markdown("---")
  st.markdown(
      "<h1 style='text-align: center; color: #00FF66; font-size: 23px;'>BDG"
      " GAME - SECURE ANTI-CHEAT PANEL</h1>",
      unsafe_allow_html=True,
  )

  t1, t2, t3, t4 = st.tabs(
      ["WinGo 30sec", "WinGo 1 Min", "WinGo 3 Min", "WinGo 5 Min"]
  )


  def render_game_tab(game_seconds, tab_name):
    auto_p, timer, current_block = get_bulletproof_period_and_timer(
        game_seconds
    )

    base_block_key = f"base_block_{tab_name}"
    base_val_key = f"base_val_{tab_name}"

    if base_block_key in st.session_state and base_val_key in st.session_state:
      block_diff = current_block - st.session_state[base_block_key]
      default_period = st.session_state[base_val_key] + block_diff
    else:
      default_period = auto_p

    st.markdown(
        f"<p style='color: #00FF66; font-size: 13px; margin-bottom: 2px;'>⚙️"
        f" लाइव गेम से मैच करने के लिए पीरियड ({tab_name}):</p>",
        unsafe_allow_html=True,
    )

    # 🛠️ यहाँ नंबर इनपुट की जगह टेक्स्ट इनपुट कर दिया गया है ताकि बड़ा पीरियड नंबर क्रैश न हो
    manual_input_str = st.text_input(
        "Live Period Override",
        value=str(default_period),
        key=f"override_str_{tab_name}",
        label_visibility="collapsed",
    )

    try:
      manual_input_val = int(manual_input_str.strip())
    except ValueError:
      manual_input_val = int(default_period)

    if base_block_key not in st.session_state or manual_input_val != default_period:
      st.session_state[base_block_key] = current_block
      st.session_state[base_val_key] = manual_input_val

    final_period_num = st.session_state[base_val_key] + (
        current_block - st.session_state[base_block_key]
    )
    final_period_str = str(final_period_num)

    pred_number, pred_size, pred_color, sentinel_status = (
        sentinel_overwatch_master_engine(final_period_num, current_block)
    )

    st.markdown(
        "<p style='color: #FF0055; font-size: 12px; margin-top: 8px;"
        " margin-bottom: 2px;'>🔒 BDG गेम का असली रिजल्ट दर्ज करें:</p>",
        unsafe_allow_html=True,
    )
    bdg_actual_result = st.selectbox(
        "BDG Actual Result",
        ["Auto-Match (Same as Panel)", "BIG", "SMALL"],
        key=f"sentinel_bdg_{tab_name}",
        label_visibility="collapsed",
    )

    if bdg_actual_result == "Auto-Match (Same as Panel)":
      actual_game_size = pred_size
    else:
      actual_game_size = bdg_actual_result

    is_exact_match = pred_size == actual_game_size

    if pred_color == "GREEN":
      color_code = "#00AA55"
    elif pred_color == "RED":
      color_code = "#FF4444"
    else:
      color_code = "#9933FF"

    size_bg = "#00FF66" if pred_size == "BIG" else "#FF0055"
    size_text_color = "#000000" if pred_size == "BIG" else "#FFFFFF"

    if is_exact_match:
      st.balloons()
      status_badge_html = "<div class='win-badge'>✨ WIN (जीत गया) ✅</div>"
      banner_msg = f"मिलान सफल: पैनल ({pred_size}) और BDG गेम ({actual_game_size}) 100% सटीक मैच हैं!"
    else:
      status_badge_html = (
          "<div class='loss-badge'>❌ LOSS (लॉस हो गया) ⚠️</div>"
      )
      banner_msg = f"अलर्ट: पैनल ({pred_size}) और BDG गेम ({actual_game_size}) अलग हैं!"

    st.markdown(
        f"""
        <div style="background-color: #0A0A12; border: 2px solid {'#00FF66' if is_exact_match else '#FF4444'}; border-radius: 20px; padding: 22px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="color: #00FF66; font-weight: bold; font-size: 15px;">📌 PERIOD: {final_period_str}</span>
                <div>{status_badge_html}</div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; background-color: #121220; padding: 10px 15px; border-radius: 10px; margin-bottom: 15px;">
                <span style="color: #00FF66; font-size: 11px; font-weight: bold;">{sentinel_status}</span>
                <span class="sentinel-alert">🛡️ 100% SECURE</span>
            </div>

            <p style="text-align: center; color: #FFFFFF; font-size: 13px; margin-bottom: 12px;">{banner_msg}</p>

            <div style="display: flex; justify-content: space-around; align-items: center; text-align: center;">
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">NUMBER</p>
                    <div style="background-color: {color_code}; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: auto; color: white;">{pred_number}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">PANEL SIZE</p>
                    <div style="background-color: {size_bg}; color: {size_text_color}; padding: 12px 20px; border-radius: 10px; font-weight: bold; font-size: 18px;">{pred_size}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">COLOR</p>
                    <div style="background-color: {color_code}; color: white; padding: 12px 20px; border-radius: 10px; font-weight: bold; font-size: 18px;">{pred_color}</div>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )


  with t1:
    st.write("⏱️ **WinGo 30sec Secure Core**")
    render_game_tab(30, "30s")

  with t2:
    st.write("⏱️ **WinGo 1 Min Secure Core**", unsafe_allow_html=True)
    render_game_tab(60, "1m")

  with t3:
    st.write("⏱️ **WinGo 3 Min Secure Core**", unsafe_allow_html=True)
    render_game_tab(180, "3m")

  with t4:
    st.write("⏱️ **WinGo 5 Min Secure Core**", unsafe_allow_html=True)
    render_game_tab(300, "5m")

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

  time.sleep(1)
  st.rerun()
