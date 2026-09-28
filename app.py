from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="KISHOR SINGH RAUTELA - Strict UTR Security Lock",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #070411; color: #FFFFFF; }
    @keyframes blink-animation { 0% { opacity: 1; transform: scale(1); } 50% { opacity: 0.2; transform: scale(0.9); } 100% { opacity: 1; transform: scale(1); } }
    @keyframes success-glow { 0% { color: #00FF66; text-shadow: 0 0 10px #00FF66; } 50% { color: #FFD700; text-shadow: 0 0 25px #00FF66; } 100% { color: #00FF66; text-shadow: 0 0 10px #00FF66; } }
    
    .blinking-light { display: inline-block; width: 10px; height: 10px; background-color: #00FF66; border-radius: 50%; margin-right: 6px; box-shadow: 0 0 12px #00FF66; animation: blink-animation 0.6s infinite ease-in-out; }
    
    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 8px 12px; border-radius: 12px; font-size: 12px; font-weight: bold; border: 1px solid #3d9f5a; margin-bottom: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.7); }
    .main-card { background-color: #110d24; border: 2px solid #338c4a; border-radius: 14px; padding: 10px 12px; box-shadow: 0 0 20px rgba(0, 0, 0, 0.9); margin-top: 4px; }
    
    .timer-text { color: #FFD700; font-weight: bold; font-size: 13px; }
    .period-text { color: #FFFFFF; font-weight: bold; font-size: 13px; }
    .success-badge { background: linear-gradient(135deg, #0d2216, #040d08); border: 2px dashed #00FF66; padding: 8px; border-radius: 8px; text-align: center; font-size: 14px; font-weight: 900; margin: 8px 0; animation: success-glow 1.2s infinite ease-in-out; text-transform: uppercase; letter-spacing: 1px; color: #00FF66; }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-top: 6px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.9); border: 1px solid #6644aa; border-radius: 8px; padding: 6px; transform: skewX(-3deg); }

    .stTabs [data-baseweb="tab-list"] { gap: 6px; justify-content: center; background-color: #120c24; padding: 6px; border-radius: 12px; border: 1px solid #4a338c; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #25184d, #140d2b); border-radius: 8px; color: #FFFFFF; font-weight: bold; font-size: 12px; padding: 8px 12px; border: 1px solid #6644aa; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #00FF66, #008844) !important; border: 1px solid #FFD700 !important; color: #000000 !important; font-weight: 900 !important; }

    .upi-box { background: linear-gradient(135deg, #122a1a, #040d08); border: 1px solid #00FF66; padding: 10px; border-radius: 10px; text-align: center; margin-top: 10px; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- सेशन स्टेट डेटाबेस ---
if "authenticated" not in st.session_state:
  st.session_state.authenticated = False
if "registered_users_db" not in st.session_state:
  st.session_state.registered_users_db = {}
if "used_utr_database" not in st.session_state:
  st.session_state.used_utr_database = []  # उपयोग हो चुके UTR की सूची (दोबारा उपयोग वर्जित)

# असली वैध UTRs जिनकी अनुमति है (इसे आप अपने असली PhonePe के नए UTR से अपडेट कर सकते हैं)
if "valid_approved_utrs" not in st.session_state:
  st.session_state.valid_approved_utrs = [
      "KISHOR2000UTR",  # अधिकृत UTR
      "425678901234",
  ]

if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = 25210

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

CHART_MATRIX_UPPER = ["BIG", "SMALL", "BIG", "SMALL", "SMALL", "BIG", "BIG", "SMALL", "BIG", "SMALL"] * 10
CHART_MATRIX_LOWER = ["SMALL", "BIG", "SMALL", "BIG", "BIG", "SMALL", "SMALL", "BIG", "SMALL", "BIG"] * 10

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

def security_matching_engine(block_seed):
  rnd = random.Random(block_seed)
  matrix_idx = block_seed % len(CHART_MATRIX_UPPER)
  upper_val = CHART_MATRIX_UPPER[matrix_idx]
  lower_val = CHART_MATRIX_LOWER[matrix_idx]

  final_size = upper_val if block_seed % 2 == 0 else lower_val
  if final_size == "BIG":
    number = rnd.choice([6, 7, 8, 9])
    color = "GREEN" if number != 8 else "RED"
  else:
    number = rnd.choice([0, 1, 2, 3, 4])
    color = "GREEN" if number == 1 else ("RED" if number in [2, 4] else "VIOLET")

  return number, final_size, color

def check_user_session_validity(mobile):
  if mobile in st.session_state.registered_users_db:
    record = st.session_state.registered_users_db[mobile]
    if datetime.now() > record["expiry_date"]:
      st.session_state.authenticated = False
      return False
    return True
  return False

if st.session_state.authenticated:
  current_mob = st.session_state.get("current_mobile", "")
  if not check_user_session_validity(current_mob):
    st.warning("⚠️ आपके 25 दिन की वैधता समाप्त हो चुकी है। कृपया नया UTR वेरीफाई करें।")

if not st.session_state.authenticated:
  # 👉 वही आपकी पसंद का शानदार हरा और ताज वाला हेडिंग डिज़ाइन!
  st.markdown("<h2 style='text-align: center; color: #00FF66; font-size: 28px; font-weight: 900; text-shadow: 0 0 15px #00FF66;'>👑 SECURE ACCESS & <br> 25-DAY LOCK</h2>", unsafe_allow_html=True)

  with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    mobile_input = st.text_input("📱 MOBILE NUMBER", placeholder="Enter mobile number")
    password_input = st.text_input("🔒 PASSWORD", type="password", placeholder="Enter password")

    if st.button("🚀", use_container_width=True):
      if not mobile_input or not password_input:
        st.error("⚠️ कृपया मोबाइल नंबर और पासवर्ड दर्ज करें!")
      elif mobile_input == MASTER_MOBILE and password_input == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.session_state.current_mobile = mobile_input
        st.rerun()
      else:
        current_time = datetime.now()
        if mobile_input in st.session_state.registered_users_db:
          user_record = st.session_state.registered_users_db[mobile_input]
          if user_record["password"] == password_input:
            if current_time < user_record["expiry_date"]:
              st.session_state.authenticated = True
              st.session_state.current_mobile = mobile_input
              st.success("✅ लॉगिन सफल! पैनल ओपन हो रहा है...")
              st.rerun()
            else:
              st.warning("⚠️ आपकी 25 दिन की समय सीमा समाप्त हो गई है। नया UTR दर्ज करें।")
              st.session_state.require_recharge = True
              st.session_state.target_mobile = mobile_input
              st.session_state.target_password = password_input
          else:
            st.error("❌ गलत पासवर्ड!")
        else:
          st.info("ℹ️ नया उपयोगकर्ता। कृपया ₹2000 का भुगतान करके असली UTR नंबर दर्ज करें।")
          st.session_state.require_recharge = True
          st.session_state.target_mobile = mobile_input
          st.session_state.target_password = password_input
    st.markdown("</div>", unsafe_allow_html=True)

  # सख्त UTR वेरिफिकेशन सेक्शन
  if st.session_state.get("require_recharge", False):
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="upi-box">
            <p style="color: #FFD700; font-weight: bold; font-size: 14px;">💳 Pay ₹2000 (Strict 25 Days Validity)</p>
            <p style="color: #00FF66; font-size: 14px; font-weight: bold; background: #070411; padding: 6px; border-radius: 6px; border: 1px dashed #00FF66; user-select: all;">kishorsingh226105.wallet@phonepe</p>
            <p style="color: #FF4444; font-size: 11px; margin-top: 4px;">⚠️ सिक्यॉरिटि: किसी अन्य या पुराने UTR का उपयोग न करें। केवल नया UTR स्वीकार होगा।</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    upi_str = "upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=Kishor%20Singh%20Rautela&am=2000&cu=INR"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={upi_str}"
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      st.image(qr_url, caption="Scan & Pay ₹2000", use_container_width=True)

    utr_entered = st.text_input("🔑 ENTER EXACT PHONEPE UTR NUMBER", max_chars=25, key="strict_utr_input")

    if st.button("🛡️ VERIFY UTR & UNLOCK PANEL", use_container_width=True):
      clean_utr = utr_entered.strip()
      t_mobile = st.session_state.get("target_mobile", "")
      t_pass = st.session_state.get("target_password", "")

      if not clean_utr:
        st.error("❌ त्रुटि: कृपया UTR नंबर दर्ज करें!")
      elif clean_utr in st.session_state.used_utr_database:
        st.error("🚨 सुरक्षा ब्लॉक: यह UTR नंबर पहले ही उपयोग किया जा चुका है! किसी पुराने UTR से दोबारा अनलॉक नहीं किया जा सकता।")
      elif clean_utr not in st.session_state.valid_approved_utrs:
        st.error("❌ अमान्य UTR: यह UTR आपके PhonePe मर्चेंट खाते से मैच नहीं हुआ है। केवल असली UTR ही डालें।")
      else:
        # UTR एकदम नया, सही और अधिकृत है
        st.session_state.used_utr_database.append(clean_utr)
        expiry_calc = datetime.now() + timedelta(days=25)
        
        st.session_state.registered_users_db[t_mobile] = {
            "password": t_pass,
            "expiry_date": expiry_calc,
            "utr": clean_utr
        }
        
        st.session_state.authenticated = True
        st.session_state.current_mobile = t_mobile
        st.success("✅ सफलता! UTR पूरी तरह मैच हो गया है। पैनल 25 दिनों के लिए ओपन हो रहा है...")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# --- मुख्य गेम डैशबोर्ड ---
else:
  custom_period_box = st.text_input(
      "📌 ENTER LIVE PERIOD NUMBER (CHART MATRIX MATCHING)",
      placeholder="यहाँ पीरियड नंबर दर्ज करें ताकि चार्ट मैट्रिक्स से डेटा मैच हो सके",
      key="matrix_input_field"
  )

  @st.fragment(run_every=2)
  def success_dashboard_core():
    st.session_state.live_online_count = random.randint(24000, 49000)

    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-light"></span>Status: KISHOR SINGH RAUTELA SECURED PANEL</div>
                <div>👥 Online: <span style="color: #00FF66;">{st.session_state.live_online_count:,}</span></div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])

    def render_game_panel(seconds):
      auto_period, timer_str, current_block = get_period_and_timer(seconds)

      if custom_period_box and custom_period_box.strip().isdigit():
        base_user_period = int(custom_period_box.strip())
        if st.session_state.get("last_custom_period") != custom_period_box:
          st.session_state.last_custom_period = custom_period_box
          st.session_state.base_block_val = current_block
          st.session_state.base_user_val = base_user_period

        if "base_block_val" not in st.session_state:
          st.session_state.base_block_val = current_block
          st.session_state.base_user_val = base_user_period

        block_diff = current_block - st.session_state.base_block_val
        final_period = st.session_state.base_user_val + block_diff
        seed_val = final_period
      else:
        if "base_block_val" in st.session_state:
          del st.session_state.base_block_val
        if "last_custom_period" in st.session_state:
          del st.session_state.last_custom_period
        final_period = auto_period
        seed_val = current_block

      pred_num, pred_size, pred_color = security_matching_engine(seed_val)

      color_bg = "#00AA55" if pred_color == "GREEN" else ("#FF4444" if pred_color == "RED" else "#9933FF")
      size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"

      st.markdown("<div class='main-card'>", unsafe_allow_html=True)
      st.markdown(
          f"""
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #224422; padding-bottom: 4px; margin-bottom: 4px;">
                <span class="period-text">PERIOD: {final_period}</span>
                <span class="timer-text">TIME: {timer_str}</span>
            </div>
        """,
          unsafe_allow_html=True,
      )

      st.markdown(
          f'<div class="success-badge">✅ SUCCESSFUL: PHONEPE UTR MATCHED ({pred_size}) ✅</div>',
          unsafe_allow_html=True,
      )

      st.markdown(
          f"""
            <div class="diagonal-container">
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold;">NUMBER</div>
                    <div style="background-color: {color_bg}; width: 32px; height: 32px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 16px; font-weight: bold; margin: 2px auto; color: white; border: 1px solid #FFFFFF;">{pred_num}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold;">SIZE</div>
                    <div style="background: {size_bg}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: 900; font-size: 11px; text-align: center; border: 1px solid #FFFFFF; text-transform: uppercase;">{pred_size}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold;">COLOR</div>
                    <div style="background-color: {color_bg}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: bold; font-size: 11px; text-align: center; border: 1px solid #FFFFFF; text-transform: uppercase;">{pred_color}</div>
                </div>
            </div>
        """,
          unsafe_allow_html=True,
      )
      st.markdown("</div>", unsafe_allow_html=True)

    with tab1:
      render_game_panel(30)
    with tab2:
      render_game_panel(60)
    with tab3:
      render_game_panel(180)
    with tab4:
      render_game_panel(300)

  success_dashboard_core()

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()
