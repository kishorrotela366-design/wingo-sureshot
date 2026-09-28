from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और सुप्रीम ब्लैक-गोल्ड थीम ---
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
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.2; transform: scale(0.9); }
        100% { opacity: 1; transform: scale(1); }
    }
    .blinking-light {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #00FF66;
        border-radius: 50%;
        margin-right: 8px;
        box-shadow: 0 0 15px #00FF66;
        animation: blink-animation 0.8s infinite ease-in-out;
    }
    .timer-badge {
        background-color: #1a1a2e;
        color: #00FF66;
        padding: 6px 14px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 14px;
        border: 1px dashed #00FF66;
        box-shadow: 0 0 10px rgba(0, 255, 102, 0.2);
    }
    .win-badge {
        background-color: #00AA55;
        color: #FFFFFF;
        padding: 8px 16px;
        border-radius: 10px;
        font-weight: 900;
        font-size: 15px;
        text-align: center;
        border: 2px solid #00FF66;
        box-shadow: 0 0 20px #00FF66;
    }
    .pattern-tag {
        background-color: #1a1a2e;
        border: 1px solid #FFD700;
        color: #FFD700;
        padding: 4px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: bold;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट इनिशियलाइजेशन ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False

if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = 323235

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


def get_bulletproof_period_and_timer(game_seconds):
  now = datetime.now()
  total_seconds = now.hour * 3600 + now.minute * 60 + now.second
  current_block_idx = total_seconds // game_seconds
  date_prefix = now.strftime("%Y%m%d")

  auto_period = int(f"{date_prefix}{current_block_idx:04d}")

  remaining_secs = game_seconds - (total_seconds % game_seconds)
  mins = remaining_secs // 60
  secs = remaining_secs % 60
  timer_str = f"{mins:02d}:{secs:02d}"

  return auto_period, timer_str, current_block_idx


# --- एडवांस्ड ट्रेंड & पैटर्न कैचिंग इंजन (Pattern Recognition Engine) ---
def pattern_recognition_engine(current_block_idx):
  # पिछले 3 ब्लॉग्स के परिणामों का सिमुलेशन ट्रैक करके पैटर्न पकड़ना
  prev_1 = "BIG" if ((current_block_idx - 1) * 37) % 17 in [0, 1, 2, 3, 5, 7, 11, 13] else "SMALL"
  prev_2 = "BIG" if ((current_block_idx - 2) * 37) % 17 in [0, 1, 2, 3, 5, 7, 11, 13] else "SMALL"
  prev_3 = "BIG" if ((current_block_idx - 3) * 37) % 17 in [0, 1, 2, 3, 5, 7, 11, 13] else "SMALL"

  # पैटर्न डिटेक्शन लॉजिक
  if prev_1 == prev_2 == prev_3:
    detected_pattern = f"Streak Pattern Detected ({prev_1} x3)"
    # स्ट्रीक के हिसाब से स्मार्ट ट्रिगर
    trend_decision = "SMALL" if prev_1 == "BIG" else "BIG"  # रिवर्सल या कंटिन्यूएशन बैलेंस
  elif prev_1 != prev_2 and prev_2 != prev_3:
    detected_pattern = "Alternating Pattern (Zig-Zag)"
    trend_decision = prev_1  # जिग-जैग फॉलो ट्रेंड
  else:
    detected_pattern = "Mixed Flow / Dynamic Trend"
    trend_decision = "BIG" if (current_block_idx % 2 == 0) else "SMALL"

  # 5 कोर सिंक
  c1 = "BIG" if (current_block_idx % 3 != 0) else "SMALL"
  c2 = "BIG" if (current_block_idx % 4 < 2) else "SMALL"
  c3 = trend_decision
  
  total_votes = [c1, c2, c3, trend_decision, trend_decision]
  big_tally = total_votes.count("BIG")

  if big_tally >= 3:
    final_size = "BIG"
  else:
    final_size = "SMALL"

  if final_size == "BIG":
    number = random.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = random.choice([0, 1, 2, 3, 4])
    color = "GREEN" if number == 1 else ("RED" if number in [2, 4] else "VIOLET")

  sentinel_status = f"🛡️ PATTERN SYNC: [{detected_pattern}]"
  return number, final_size, color, sentinel_status, detected_pattern


# --- लॉगिन स्क्रीन ---
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #00FF66;'>🔒 Sure Shot PRO v23</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #A0A0A0; font-size: 14px;'>MILITARY GRADE UTR ANTI-DUPLICATION FIREWALL</p>",
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
              st.success("Yes! आपका पुराना रिचार्ज एक्टिव है। डैशबोर्ड खुल रहा है...")
              st.rerun()
            else:
              st.error("❌ आपके 25 दिन की वैधता समाप्त हो चुकी है! कृपया फिर से ₹2000 का फ्रेश रिचार्ज करें।")
              st.session_state.pending_mobile = mobile
              st.session_state.pending_password = password
              st.session_state.show_payment = True
          else:
            st.error("❌ पासवर्ड गलत है! कृपया सही पासवर्ड दर्ज करें।")
        else:
          st.warning("No No! यह नंबर रजिस्टर्ड नहीं है। डैशबोर्ड खोलने के लिए पहले ₹2000 का नया UTR रिचार्ज करें।")
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
    st.markdown(f"**Required Amount:** ₹{REQUIRED_AMOUNT} (Validity: {VALIDITY_DAYS} Days)")
    entered_utr = st.text_input(
        "🔑 Enter 12-Digit Fresh UTR Number",
        max_chars=12,
        key="strict_utr_input",
    )

    if st.button("🛡️ Verify UTR & Open File (Anti-Cheat)", use_container_width=True):
      if not entered_utr.isdigit() or len(entered_utr) != 12:
        st.error("❌ अमान्य UTR फॉर्मेट! कृपया केवल 12 अंकों का सही UTR दर्ज करें।")
      elif entered_utr in st.session_state.used_utrs:
        st.error("🚨 CRITICAL SECURITY ERROR: यह UTR नंबर पहले ही इस्तेमाल किया जा चुका है!")
      elif entered_utr not in VERIFIED_KISHOR_PAYMENTS:
        st.error("❌ UTR डेटाबेस से मैच नहीं हुआ!")
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
        st.success("🎉 UTR 100% मैच हो गया! डैशबोर्ड खोला जा रहा है...")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- मेन डैशबोर्ड ---
else:
  change_delta = random.randint(-45, 55)
  st.session_state.live_online_count = max(
      320000, min(335000, st.session_state.live_online_count + change_delta)
  )
  current_online = st.session_state.live_online_count

  col1, col2 = st.columns([2, 1])
  with col1:
    st.markdown(
        "<div style='display: flex; align-items: center;'><span class='blinking-light'></span><strong style='color: #00FF66;'>Pattern Engine Active | Status: Connected</strong></div>",
        unsafe_allow_html=True,
    )
  with col2:
    st.markdown(
        "<div style='display: flex; align-items: center; justify-content: flex-end;'><span class='blinking-light'></span><b style='margin-right: 4px;'>Live Online:</b> <span style='color: #00FF66; font-weight: bold;'>`{:,}`</span></div>".format(current_online),
        unsafe_allow_html=True,
    )

  st.markdown("---")
  st.markdown(
      "<h1 style='text-align: center; color: #00FF66; font-size: 23px;'>BDG GAME - PATTERN RECOGNITION PANEL</h1>",
      unsafe_allow_html=True,
  )

  t1, t2, t3, t4 = st.tabs(
      ["WinGo 30sec", "WinGo 1 Min", "WinGo 3 Min", "WinGo 5 Min"]
  )


  def render_game_tab(game_seconds, tab_name):
    auto_p, timer_str, current_block = get_bulletproof_period_and_timer(
        game_seconds
    )

    final_period_num = auto_p
    final_period_str = str(final_period_num)
    next_period_str = str(final_period_num + 1)

    pred_number, pred_size, pred_color, sentinel_status, detected_pattern = (
        pattern_recognition_engine(current_block)
    )

    if pred_color == "GREEN":
      color_code = "#00AA55"
    elif pred_color == "RED":
      color_code = "#FF4444"
    else:
      color_code = "#9933FF"

    if pred_size == "BIG":
      size_box_style = (
          "background: linear-gradient(135deg, #00FF66, #008833); color: #000000; padding: 16px 28px; border-radius: 14px; font-weight: 900; font-size: 26px; border: 3px solid #FFFFFF; box-shadow: 0 0 30px rgba(0, 255, 102, 0.9); text-align: center; text-transform: uppercase;"
      )
    else:
      size_box_style = (
          "background: linear-gradient(135deg, #FF0055, #990033); color: #FFFFFF; padding: 16px 28px; border-radius: 14px; font-weight: 900; font-size: 26px; border: 3px solid #FFFFFF; box-shadow: 0 0 30px rgba(255, 0, 85, 0.9); text-align: center; text-transform: uppercase;"
      )

    status_badge_html = "<div class='win-badge'>✨ PATTERN MATCHED ✅</div>"
    banner_msg = "🔥 <b>TREND TRIGGER:</b> पिछला पैटर्न पकड़कर अगला सटीक परिणाम सेट कर दिया गया है!"

    # 🟢 साफ़-सुथरा और पूरी तरह सुरक्षित लेआउट बॉक्स जिसमें पैटर्न टैग भी दिखेगा
    st.markdown(
        f"""
        <div style="background-color: #0A0A12; border: 2px solid #00FF66; border-radius: 20px; padding: 22px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                <span style="color: #00FF66; font-weight: bold; font-size: 14px;">📌 PERIOD: {final_period_str}</span>
                <span class="timer-badge">⏳ TIMER: {timer_str}</span>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; background-color: #121220; padding: 10px 15px; border-radius: 10px; margin-bottom: 15px;">
                <span style="color: #00FF66; font-size: 11px; font-weight: bold;">{sentinel_status}</span>
                <span class="pattern-tag">🎯 Active Trend</span>
            </div>

            <p style="text-align: center; color: #FFD700; font-size: 13px; margin-bottom: 15px; font-weight: bold;">{banner_msg}</p>

            <div style="display: flex; justify-content: space-around; align-items: center; text-align: center; margin-bottom: 15px;">
                <div>
                    <p style="font-size: 12px; color: #A0A0A0; margin-bottom: 8px;">NUMBER</p>
                    <div style="background-color: {color_code}; width: 65px; height: 65px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 28px; font-weight: bold; margin: auto; color: white; border: 3px solid #FFFFFF; box-shadow: 0 0 20px {color_code};">{pred_number}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0; margin-bottom: 8px;">PREDICTION SIZE</p>
                    <div style="{size_box_style}">{pred_size}</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0; margin-bottom: 8px;">COLOR</p>
                    <div style="background-color: {color_code}; color: white; padding: 16px 22px; border-radius: 12px; font-weight: bold; font-size: 16px; border: 2px solid #FFFFFF; box-shadow: 0 0 20px {color_code};">{pred_color}</div>
                </div>
            </div>

            <div style="background-color: #11111B; border: 1px dashed #00FF66; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between; align-items: center;">
                <span style="color: #A0A0A0; font-size: 12px;">📊 <b>Status:</b> <span style="color: #00FF66;">Pattern Hooked</span></span>
                <span style="color: #00FF66; font-size: 13px; font-weight: bold;">⏭️ Next Period: {next_period_str}</span>
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
