from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क पर्पल थीम ---
st.set_page_config(
    page_title="Sure Shot PRO v3 - BDG Game Pro",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #120A2A;
        color: #FFFFFF;
    }
    .card-box {
        background-color: #1A103C;
        border: 1px solid #3B2A6B;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
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

# --- मास्टर और पेमेंट क्रेडेंशियल सेटिंग्स ---
MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"
PAYMENT_UPI_ID = "kishorsingh226105.wallet@phonepe"
REQUIRED_AMOUNT = 2000
VALIDITY_DAYS = 25

if "user_db" not in st.session_state:
  st.session_state.user_db = {}
if "used_utrs" not in st.session_state:
  st.session_state.used_utrs = set()

# 🔒 मान्य UTRs
VERIFIED_KISHOR_PAYMENTS = {"482910384756": 2000, "918273645012": 2000}


# --- अल्टीमेट सिंक और ऑटो-प्रोग्रेसिव पीरियड इंजन ---
def get_bulletproof_period_and_timer(game_type_seconds, tab_key):
  now = datetime.now()
  total_seconds = now.hour * 3600 + now.minute * 60 + now.second
  current_block_idx = total_seconds // game_type_seconds
  date_prefix = now.strftime("%Y%m%d")

  if game_type_seconds == 30:
    auto_period = int(f"{date_prefix}10005{current_block_idx:04d}")
  elif game_type_seconds == 60:
    auto_period = int(f"{date_prefix}10001{current_block_idx:04d}")
  elif game_type_seconds == 180:
    auto_period = int(f"{date_prefix}10003{current_block_idx:04d}")
  else:
    auto_period = int(f"{date_prefix}10005{current_block_idx:04d}")

  remaining_secs = game_type_seconds - (total_seconds % game_type_seconds)
  mins = remaining_secs // 60
  secs = remaining_secs % 60
  timer_str = f"{mins:02d}:{secs:02d}"

  return auto_period, timer_str, current_block_idx


# ==========================================================
# भाग 1: लॉगिन स्क्रीन
# ==========================================================
if not st.session_state.authenticated:
  st.markdown(
      "<h2 style='text-align: center; color: #FFA500;'>🎯 Sure Shot PRO"
      " v3</h2>",
      unsafe_allow_html=True,
  )
  st.markdown(
      "<p style='text-align: center; color: #A0A0A0; font-size: 14px;'>GAME HUB"
      " ACCESS</p>",
      unsafe_allow_html=True,
  )

  with st.container():
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='color: #FFFFFF;'>✨ WELCOME BACK</h3>", unsafe_allow_html=True
    )

    mobile = st.text_input("📱 PHONE NUMBER", placeholder="Enter mobile number")
    password = st.text_input(
        "🔒 PASSWORD", type="password", placeholder="Enter password"
    )

    if st.button("🚀 LOGIN NOW", use_container_width=True):
      if not mobile or not password:
        st.error("कृपया मोबाइल नंबर और पासवर्ड दर्ज करें!")
      elif mobile == MASTER_MOBILE and password == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.session_state.user_mobile = mobile
        st.success("Yes! मास्टर क्रेडेंशियल सही है। डैशबोर्ड खुल रहा है...")
        st.rerun()
      else:
        current_time = datetime.now()
        is_valid = False
        if mobile in st.session_state.user_db:
          if current_time <= st.session_state.user_db[mobile]["expiry"]:
            is_valid = True

        if is_valid:
          st.session_state.authenticated = True
          st.session_state.user_mobile = mobile
          st.success("Yes! सब्स्क्रिप्शन सक्रिय है। डैशबोर्ड खुल रहा है...")
          st.rerun()
        else:
          st.warning(
              "No No No! आपके पास सक्रिय पास नहीं है। कृपया ₹2000 का भुगतान करें।"
          )
          st.session_state.pending_mobile = mobile
          st.session_state.pending_password = password
          st.session_state.show_payment = True
    st.markdown("</div>", unsafe_allow_html=True)

  if st.session_state.get("show_payment", False):
    st.markdown(
        "<div class='card-box' style='border-color: #FFA500;'>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='color: #FFA500;'>🔒 UTR Verification System</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(f"**UPI ID (Kishor):** `{PAYMENT_UPI_ID}`")
    st.markdown(f"**Required Amount:** ₹{REQUIRED_AMOUNT}")
    st.markdown(
        "⚠️ UTR मैच नहीं होने पर **No No No** आएगा और फाइल ओपन नहीं होगी!"
    )

    entered_utr = st.text_input(
        "🔑 Enter 12-Digit UTR Number", max_chars=12, key="utr_input"
    )

    if st.button("✅ Verify & Match UTR", use_container_width=True):
      if not entered_utr.isdigit() or len(entered_utr) != 12:
        st.error("❌ No No No! अमान्य UTR (12 अंकों का सही नंबर डालें)।")
      elif entered_utr in st.session_state.used_utrs:
        st.error("❌ No No No! यह UTR पहले ही इस्तेमाल किया जा चुका है।")
      elif entered_utr not in VERIFIED_KISHOR_PAYMENTS:
        st.error(
            "❌ No No No! UTR मैच नहीं हुआ! किशोर जी के खाते में ₹2000 प्राप्त नहीं"
            " हुए हैं।"
        )
      else:
        st.session_state.used_utrs.add(entered_utr)
        expiry = datetime.now() + timedelta(days=VALIDITY_DAYS)
        mob = st.session_state.get("pending_mobile", mobile)
        pwd = st.session_state.get("pending_password", password)

        st.session_state.user_db[mob] = {
            "password": pwd,
            "expiry": expiry,
            "utr": entered_utr,
        }
        st.session_state.authenticated = True
        st.session_state.user_mobile = mob
        st.success("Yes! UTR सफलतापूर्वक मैच हो गया है। फाइल ओपन हो रही है...")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================================
# भाग 2: मेन डैशबोर्ड
# ==========================================================
else:
  current_online = random.randint(10000, 50000)

  col1, col2 = st.columns([2, 1])
  with col1:
    st.markdown("🟢 **Server Active**")
  with col2:
    st.markdown(f"👤 **Online:** `{current_online:,}`")

  st.markdown("---")
  st.markdown(
      "<h1 style='text-align: center; color: #FFA500; font-size: 24px;'>BDG"
      " GAME PRO</h1>",
      unsafe_allow_html=True,
  )

  t1, t2, t3, t4 = st.tabs(
      ["WinGo 30sec", "WinGo 1 Min", "WinGo 3 Min", "WinGo 5 Min"]
  )


  def render_game_tab(game_seconds, tab_name):
    auto_p, timer, current_block = get_bulletproof_period_and_timer(
        game_seconds, tab_name
    )

    st.markdown(
        f"<p style='color: #FFA500; font-size: 13px; margin-bottom: 2px;'>⚙️"
        f" लाइव गेम से मैच करने के लिए यहाँ पीरियड दर्ज करें ({tab_name}):</p>",
        unsafe_allow_html=True,
    )
    manual_input = st.text_input(
        "Live Period Override",
        placeholder=f"जैसे: {auto_p}",
        key=f"override_{tab_name}",
        label_visibility="collapsed",
    )

    final_period = str(auto_p)

    base_block_key = f"base_block_{tab_name}"
    base_val_key = f"base_val_{tab_name}"
    input_cache_key = f"input_cache_{tab_name}"

    if manual_input and manual_input.strip().isdigit():
      entered_val = int(manual_input.strip())
      if (
          input_cache_key not in st.session_state
          or st.session_state[input_cache_key] != manual_input
      ):
        st.session_state[base_block_key] = current_block
        st.session_state[base_val_key] = entered_val
        st.session_state[input_cache_key] = manual_input

      if base_block_key in st.session_state:
        block_diff = current_block - st.session_state[base_block_key]
        final_period = str(st.session_state[base_val_key] + block_diff)

    st.markdown(
        f"""
        <div style="background-color: #1A103C; border: 1px solid #3B2A6B; border-radius: 15px; padding: 20px; margin-top: 10px;">
            <div style="display: flex; justify-content: space-between; color: #A0A0A0; font-size: 13px;">
                <span>PERIOD: {final_period}</span>
                <span>TIME REMAINING: {timer}</span>
            </div>
            <h3 style="text-align: center; color: #FFA500; margin-top: 10px;">👇 NEXT RESULT PREDICTION 👇</h3>
            <div style="display: flex; justify-content: space-around; align-items: center; margin-top: 15px; text-align: center;">
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">NUMBER</p>
                    <div style="background-color: #00AA55; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: auto;">7</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">SIZE</p>
                    <div style="background-color: #FFA500; color: black; padding: 12px 20px; border-radius: 10px; font-weight: bold; font-size: 18px;">BIG</div>
                </div>
                <div>
                    <p style="font-size: 12px; color: #A0A0A0;">COLOR</p>
                    <div style="background-color: #00CC66; color: white; padding: 12px 20px; border-radius: 10px; font-weight: bold; font-size: 18px;">GREEN</div>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )


  with t1:
    st.write("⏱️ **WinGo 30sec Active**")
    render_game_tab(30, "30s")

  with t2:
    st.write("⏱️ **WinGo 1 Min Active**")
    render_game_tab(60, "1m")

  with t3:
    st.write("⏱️ **WinGo 3 Min Active**")
    render_game_tab(180, "3m")

  with t4:
    st.write("⏱️ **WinGo 5 Min Active**")
    render_game_tab(300, "5m")

  st.markdown("<br>", unsafe_allow_html=True)
  bc1, bc2 = st.columns(2)
  with bc1:
    st.button("⚡ HACK", use_container_width=True)
  with bc2:
    st.button("🎮 GAME HISTORY", use_container_width=True)

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()
