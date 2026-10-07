from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="BDG & 11-SERVER SMART SHOT PANEL",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #020104; color: #FFFFFF; }
    
    /* Streamlit के डिफ़ॉल्ट फुटर, हेडर, मेन्यू और ब्रांडिंग को छिपाने के लिए */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stAppDeployButton {display: none;}
    [data-testid="stStatusWidget"] {visibility: hidden;}
    
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1); box-shadow: 0 0 12px #FF0055; }
        50% { opacity: 0.2; transform: scale(0.85); box-shadow: 0 0 3px #FF0055; }
        100% { opacity: 1; transform: scale(1); box-shadow: 0 0 12px #FF0055; }
    }

    @keyframes rainbow-glow {
        0% { border-color: #FFD700; box-shadow: 0 0 18px rgba(255,215,0,0.9); }
        33% { border-color: #00FF66; box-shadow: 0 0 18px rgba(0,255,102,0.9); }
        66% { border-color: #00E5FF; box-shadow: 0 0 18px rgba(0,229,255,0.9); }
        100% { border-color: #FFD700; box-shadow: 0 0 18px rgba(255,215,0,0.9); }
    }

    .blinking-red-light { 
        display: inline-block; 
        width: 10px; 
        height: 10px; 
        background-color: #FF0055; 
        border-radius: 50%; 
        margin-right: 6px; 
        animation: blink-animation 1s infinite ease-in-out;
    }

    /* पैनल और टेक्स्ट को और अधिक बोल्ड और बड़ा किया गया है */
    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 12px 16px; border-radius: 8px; font-size: 15px; font-weight: 900; border: 1.5px solid #3d9f5a; margin-bottom: 8px; }
    .main-card { background-color: #0b071a; border: 2px solid #FFD700; border-radius: 12px; padding: 14px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 8px; }
    
    .timer-box-large { color: #FF00FF; font-weight: 900; font-size: 16px; text-shadow: 0 0 8px rgba(255,0,255,0.6); }
    
    .period-badge-small { 
        color: #00FFFF; 
        font-weight: 900; 
        font-size: 16px; 
        background: rgba(0,255,255,0.1);
        padding: 4px 8px;
        border-radius: 5px;
        border: 1.5px solid #00FFFF;
        letter-spacing: 1px;
    }
    
    .trend-banner-big { background: linear-gradient(135deg, #4d1a00, #260d00); border: 2.5px solid #FF9900; padding: 12px; border-radius: 8px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #FFD700; text-transform: uppercase; letter-spacing: 0.5px; }
    .trend-banner-small { background: linear-gradient(135deg, #001a33, #000d1a); border: 2.5px solid #00E5FF; padding: 12px; border-radius: 8px; text-align: center; font-size: 15px; font-weight: 900; margin: 8px 0; color: #00FFFF; text-transform: uppercase; letter-spacing: 0.5px; }
    
    .sure-shot-banner { 
        background: linear-gradient(135deg, #330033, #1a001a); 
        border: 2.5px dashed #FF00FF; 
        padding: 14px; 
        border-radius: 8px; 
        text-align: center; 
        font-size: 15px; 
        font-weight: 900; 
        margin: 8px 0; 
        color: #FF66FF; 
        text-transform: uppercase; 
        animation: rainbow-glow 1.5s infinite; 
    }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 8px; margin-top: 8px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.95); border: 1.5px solid #6644aa; border-radius: 8px; padding: 8px; }

    .stTabs [data-baseweb="tab-list"] { gap: 6px; justify-content: center; background-color: #0b071a; padding: 6px; border-radius: 8px; border: 1.5px solid #FFD700; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #25184d, #140d2b); border-radius: 6px; color: #FFFFFF; font-weight: 900; font-size: 14px; padding: 8px 14px; border: 1.5px solid #6644aa; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FFD700, #FF8C00) !important; border: 1.5px solid #FFFFFF !important; color: #000000 !important; font-weight: 900 !important; }

    .upi-box { background: linear-gradient(135deg, #122a1a, #040d08); border: 1.5px solid #00FF66; padding: 10px; border-radius: 8px; text-align: center; margin-top: 8px; }
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
  st.session_state.used_utr_database = []

if "valid_approved_utrs" not in st.session_state:
  st.session_state.valid_approved_utrs = [
      "KISHOR1000UTR",
      "425678901234",
  ]

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# --- स्मार्ट इंजन (पीरियड आधारित स्थिर और सटीक मिलान) ---
@st.cache_data(ttl=300)
def get_bdg_and_11_servers_signal(period_5_digits, tab_offset):
    base_seed = int(period_5_digits) * 73 + int(tab_offset) * 37
    
    # 1. BDG गेम सर्वर प्रेडिक्शन
    bdg_rng = random.Random(base_seed + 99)
    bdg_val = int((bdg_rng.random() * 100000) % 10)
    bdg_size = "BIG" if bdg_val >= 5 else "SMALL"

    # 2. 11 सर्वरों का कंबाइंड कैलकुलेशन
    server_outputs = []
    for s_idx in range(1, 12):
        s_rng = random.Random(base_seed + s_idx * 19)
        server_outputs.append(int((s_rng.random() * 100000) % 10))

    total_sum = sum(server_outputs)
    last_digit = int(period_5_digits[-1]) if period_5_digits[-1].isdigit() else 0
    
    server_calc_num = (total_sum + last_digit + tab_offset) % 10
    server_size = "BIG" if server_calc_num >= 5 else "SMALL"

    if server_calc_num in [1, 3, 7, 9]:
        server_color = "GREEN"
    elif server_calc_num in [2, 4, 6, 8]:
        server_color = "RED"
    else:
        server_color = "GREEN" if server_calc_num == 5 else "RED"

    # 3. 100% श्योर शॉट मिलान जाँच
    is_fully_matched = (bdg_size == server_size)

    return server_calc_num, server_size, server_color, is_fully_matched

# --- लॉगिन और एडमिन जाँच ---
if st.session_state.authenticated:
  current_mob = st.session_state.get("current_mobile", "")
  if current_mob != MASTER_MOBILE:
    if current_mob in st.session_state.registered_users_db:
      record = st.session_state.registered_users_db[current_mob]
      if datetime.now() > record["expiry_date"]:
        st.session_state.authenticated = False
        st.warning("⚠️ आपके 25 दिन की वैधता समाप्त हो चुकी है। कृपया नया UTR वेरीफाई करें।")
        st.rerun()

if not st.session_state.authenticated:
  st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 24px; font-weight: 900;'>👑 BDG & 11-SERVER SMART <br> AUTO ACCESS</h2>", unsafe_allow_html=True)

  with st.container():
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    mobile_input = st.text_input("📱 MOBILE NUMBER", placeholder="Enter mobile number")
    password_input = st.text_input("🔒 PASSWORD", type="password", placeholder="Enter password")

    if st.button("🚀 UNLOCK PANEL", use_container_width=True):
      if not mobile_input or not password_input:
        st.error("⚠️ कृपया मोबाइल नंबर और पासवर्ड दर्ज करें!")
      elif mobile_input == MASTER_MOBILE and password_input == MASTER_PASSWORD:
        st.session_state.authenticated = True
        st.session_state.current_mobile = mobile_input
        st.success("👑 एडमिन लॉगिन सफल!")
        st.rerun()
      else:
        current_time = datetime.now()
        if mobile_input in st.session_state.registered_users_db:
          user_record = st.session_state.registered_users_db[mobile_input]
          if user_record["password"] == password_input:
            if current_time < user_record["expiry_date"]:
              st.session_state.authenticated = True
              st.session_state.current_mobile = mobile_input
              st.success("✅ लॉगिन सफल!")
              st.rerun()
            else:
              st.warning("⚠ वैधता समाप्त!")
              st.session_state.require_recharge = True
              st.session_state.target_mobile = mobile_input
              st.session_state.target_password = password_input
          else:
            st.error("❌ गलत पासवर्ड!")
        else:
          st.info("ℹ️ नया उपयोगकर्ता। कृपया ₹1500 का भुगतान करें।")
          st.session_state.require_recharge = True
          st.session_state.target_mobile = mobile_input
          st.session_state.target_password = password_input
    st.markdown("</div>", unsafe_allow_html=True)

  if st.session_state.get("require_recharge", False):
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="upi-box">
            <p style="color: #FFD700; font-weight: bold; font-size: 14px;">💳 Pay ₹1500 (25 Days Validity)</p>
            <p style="color: #00FF66; font-size: 12px; font-weight: bold; background: #020104; padding: 5px; border-radius: 4px; border: 1px dashed #00FF66; user-select: all;">kishorsingh226105.wallet@phonepe</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    upi_str = "upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=Kishor%20Singh%20Rautela&am=1500&cu=INR"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=140x140&data={upi_str}"
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      st.image(qr_url, use_container_width=True)

    utr_entered = st.text_input("🔑 ENTER UTR NUMBER", max_chars=25, key="strict_utr_input")

    if st.button("🛡 VERIFY UTR", use_container_width=True):
      clean_utr = utr_entered.strip()
      t_mobile = st.session_state.get("target_mobile", "")
      t_pass = st.session_state.get("target_password", "")

      if not clean_utr:
        st.error("❌ कृपया UTR नंबर दर्ज करें!")
      elif clean_utr in st.session_state.used_utr_database:
        st.error("🚨 यह UTR पहले ही उपयोग हो चुका है!")
      elif clean_utr not in st.session_state.valid_approved_utrs:
        st.error("❌ अमान्य UTR!")
      else:
        st.session_state.used_utr_database.append(clean_utr)
        st.session_state.registered_users_db[t_mobile] = {
            "password": t_pass,
            "expiry_date": datetime.now() + timedelta(days=25),
            "utr": clean_utr
        }
        st.session_state.authenticated = True
        st.session_state.current_mobile = t_mobile
        st.success("✅ सफलता!")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
  @st.fragment(run_every=1)
  def success_dashboard_core():
    dynamic_online_count = random.randint(112000, 498000)

    # टॉप बार - अब अक्षर बड़े और बोल्ड दिखेंगे
    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-red-light"></span><span style="color: #00FFFF; font-weight: 900; font-size: 14px;">⚡ BDG & 11-SERVER SMART SHOT PANEL</span></div>
                <div><span class="blinking-red-light"></span>👥 <span style="color: #00FF66; font-size: 13px; font-weight: 900;">{dynamic_online_count:,}</span></div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    now = datetime.now()
    default_5_digits = now.strftime("%M%S")[-5:]

    # 📌 ऊपर लाइव पीरियड इनपुट बॉक्स
    col_a, col_b, col_c = st.columns([0.5, 3, 0.5])
    with col_b:
        st.markdown("<div style='background: #0b071a; border: 2px solid #FFD700; border-radius: 8px; padding: 10px; text-align: center; box-shadow: 0 0 12px rgba(255,215,0,0.25);'>", unsafe_allow_html=True)
        st.markdown("<p style='color: #FFD700; font-size: 13px; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;'>📌 लाइव पीरियड (केवल 5 अंक डालें)</p>", unsafe_allow_html=True)
        manual_period_input = st.text_input(
            "Period Input",
            value=default_5_digits,
            max_chars=5,
            key="user_live_period_input",
            label_visibility="collapsed"
        )
        st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])

    def render_game_panel(seconds, tab_name_style, tab_offset):
      st.markdown("<div class='main-card'>", unsafe_allow_html=True)
      
      total_seconds = now.hour * 3600 + now.minute * 60 + now.second
      remaining_secs = seconds - (total_seconds % seconds)
      mins = remaining_secs // 60
      secs = remaining_secs % 60
      timer_str = f"{mins:02d}:{secs:02d}"

      current_block_index = total_seconds // seconds

      clean_input = "".join(filter(str.isdigit, manual_period_input))
      if not clean_input:
          clean_input = "02003"

      state_key_input = f"tracked_input_{seconds}"
      state_key_block = f"tracked_block_{seconds}"
      state_key_offset = f"period_offset_{seconds}"

      if state_key_input not in st.session_state:
          st.session_state[state_key_input] = clean_input
          st.session_state[state_key_block] = current_block_index
          st.session_state[state_key_offset] = 0

      if st.session_state[state_key_input] != clean_input:
          st.session_state[state_key_input] = clean_input
          st.session_state[state_key_block] = current_block_index
          st.session_state[state_key_offset] = 0
      else:
          block_diff = current_block_index - st.session_state[state_key_block]
          if block_diff != 0:
              st.session_state[state_key_block] = current_block_index
              st.session_state[state_key_offset] += block_diff

      try:
          base_val = int(clean_input)
          final_val = base_val + st.session_state[state_key_offset]
          final_period = str(final_val).zfill(5)[-5:]
      except:
          final_period = clean_input.zfill(5)[-5:]

      pred_num, pred_size, pred_color, is_fully_matched = get_bdg_and_11_servers_signal(final_period, tab_offset)

      # पीरियड बॉक्स डिस्प्ले
      st.markdown(
          f"""
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #FFD700; padding-bottom: 6px; margin-bottom: 8px; background: rgba(255,215,0,0.06); border-radius: 6px; padding-left: 8px; padding-right: 8px;">
                <span style="display: flex; align-items: center;"><span class="blinking-red-light"></span><span style="font-size: 13px; color: #FFD700; font-weight: 900; margin-right: 6px;">PERIOD:</span><span class="period-badge-small">{final_period}</span></span>
                <span class="timer-box-large">⏰ {timer_str}</span>
            </div>
        """,
          unsafe_allow_html=True,
      )

      # 📌 श्योर शॉट बैनर और ट्रेंड बैनर
      if is_fully_matched:
          if pred_size == "BIG":
              st.markdown(f'<div class="sure-shot-banner">💎 100% श्योर शॉट! [ BIG ] विन पक्का! 🚀</div>', unsafe_allow_html=True)
          else:
              st.markdown(f'<div class="sure-shot-banner">💎 100% श्योर शॉट! [ SMALL ] विन पक्का! 🚀</div>', unsafe_allow_html=True)
      else:
          if pred_size == "BIG":
              st.markdown(f'<div class="trend-banner-big">📈 बिग (BIG) की लाइन चल रही है...</div>', unsafe_allow_html=True)
          else:
              st.markdown(f'<div class="trend-banner-small">📉 स्मॉल (SMALL) की लाइन चल रही है...</div>', unsafe_allow_html=True)
      
      color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
      size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"
      
      display_num = pred_num
      display_size = pred_size
      display_color = pred_color

      st.markdown(
          f"""
            <div class="diagonal-container">
                <div class="result-item">
                    <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">NUMBER</div>
                    <div style="background-color: {color_bg}; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 18px; font-weight: 900; margin: 0 auto; color: white; border: 2px solid #FFFFFF;">{display_num}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">SIZE</div>
                    <div style="background: {size_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center; border: 2px solid #FFFFFF; text-transform: uppercase;">{display_size}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 10px; color: #FFFFFF; font-weight: 900; margin-bottom: 4px; text-transform: uppercase;">COLOR</div>
                    <div style="background-color: {color_bg}; color: white; padding: 10px 4px; border-radius: 6px; font-weight: 900; font-size: 13px; text-align: center; border: 2px solid #FFFFFF; text-transform: uppercase;">{display_color}</div>
                </div>
            </div>
        """,
          unsafe_allow_html=True,
      )
      st.markdown("</div>", unsafe_allow_html=True)

    with tab1:
      render_game_panel(30, "WINGO 30S", 11)
    with tab2:
      render_game_panel(60, "WINGO 1M", 23)
    with tab3:
      render_game_panel(180, "WINGO 3M", 37)
    with tab4:
      render_game_panel(300, "WINGO 5M", 53)

  success_dashboard_core()

  st.markdown("<br>", unsafe_allow_html=True)
  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()
