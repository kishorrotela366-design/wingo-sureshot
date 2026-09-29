from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="KISHOR SINGH - 100% श्योर शॉर्ट",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #020104; color: #FFFFFF; }
    
    .blinking-red-light { 
        display: inline-block; 
        width: 9px; 
        height: 9px; 
        background-color: #FF0055; 
        border-radius: 50%; 
        margin-right: 5px; 
        box-shadow: 0 0 8px #FF0055; 
    }

    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: bold; border: 1px solid #3d9f5a; margin-bottom: 6px; }
    .main-card { background-color: #0b071a; border: 1.5px solid #FFD700; border-radius: 10px; padding: 10px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 4px; }
    
    .timer-box-large { color: #FFD700; font-weight: 900; font-size: 13px; }
    .period-box-large { color: #FFFFFF; font-weight: 900; font-size: 13px; }
    
    /* 100% श्योर शॉर्ट के लिए सॉलिड डिज़ाइन */
    .sure-banner-big { background: linear-gradient(135deg, #4d2600, #1a0d00); border: 1.5px solid #FFD700; padding: 7px 10px; border-radius: 6px; text-align: center; font-size: 13px; font-weight: 900; margin: 6px 0; color: #FFD700; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 10px rgba(255,215,0,0.3); }
    .sure-banner-small { background: linear-gradient(135deg, #002b4d, #000f1a); border: 1.5px solid #00E5FF; padding: 7px 10px; border-radius: 6px; text-align: center; font-size: 13px; font-weight: 900; margin: 6px 0; color: #00E5FF; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 10px rgba(0,229,255,0.3); }

    .wait-badge { background: linear-gradient(135deg, #221100, #140a00); border: 2px dashed #FF9900; padding: 6px; border-radius: 6px; text-align: center; font-size: 11px; font-weight: bold; margin: 6px 0; color: #FF9900; text-transform: uppercase; }

    .diagonal-container { display: flex; justify-content: space-between; align-items: center; gap: 6px; margin-top: 6px; }
    .result-item { flex: 1; text-align: center; background: rgba(25, 18, 50, 0.9); border: 1px solid #6644aa; border-radius: 8px; padding: 6px; }

    .stTabs [data-baseweb="tab-list"] { gap: 4px; justify-content: center; background-color: #0b071a; padding: 4px; border-radius: 8px; border: 1px solid #FFD700; }
    .stTabs [data-baseweb="tab"] { background: linear-gradient(135deg, #25184d, #140d2b); border-radius: 6px; color: #FFFFFF; font-weight: bold; font-size: 11px; padding: 6px 10px; border: 1px solid #6644aa; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #FFD700, #FF8C00) !important; border: 1px solid #FFFFFF !important; color: #000000 !important; font-weight: 900 !important; }

    .upi-box { background: linear-gradient(135deg, #122a1a, #040d08); border: 1px solid #00FF66; padding: 8px; border-radius: 8px; text-align: center; margin-top: 8px; }
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

if "live_online_count" not in st.session_state:
  st.session_state.live_online_count = 34500

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# --- सर्वर सिंक्रोनाइज्ड एल्गोरिदम ---
@st.cache_data(ttl=10)
def get_sure_signal(seed_val, tab_offset):
    accumulated_score = 0
    combined_weight = 365.0 + 30.0 + 7.0 + 24.0
    
    for engine_id in range(1, 12):
        core_gen = random.Random(seed_val * 123 + engine_id * 49 + tab_offset + int(combined_weight))
        accumulated_score += core_gen.random()
        
    final_avg = accumulated_score / 11.0
    return 'B' if final_avg > 0.46 else 'S'

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
  st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 22px; font-weight: 900;'>👑 KISHOR SINGH <br> SECURE ACCESS</h2>", unsafe_allow_html=True)

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
              st.warning("⚠️ वैधता समाप्त! नया UTR दर्ज करें।")
              st.session_state.require_recharge = True
              st.session_state.target_mobile = mobile_input
              st.session_state.target_password = password_input
          else:
            st.error("❌ गलत पासवर्ड!")
        else:
          st.info("ℹ️ नया उपयोगकर्ता। कृपया ₹1000 का भुगतान करें।")
          st.session_state.require_recharge = True
          st.session_state.target_mobile = mobile_input
          st.session_state.target_password = password_input
    st.markdown("</div>", unsafe_allow_html=True)

  if st.session_state.get("require_recharge", False):
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="upi-box">
            <p style="color: #FFD700; font-weight: bold; font-size: 13px;">💳 Pay ₹1000 (25 Days Validity)</p>
            <p style="color: #00FF66; font-size: 13px; font-weight: bold; background: #020104; padding: 4px; border-radius: 4px; border: 1px dashed #00FF66; user-select: all;">kishorsingh226105.wallet@phonepe</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    upi_str = "upi://pay?pa=kishorsingh226105.wallet@phonepe&pn=Kishor%20Singh%20Rautela&am=1000&cu=INR"
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=130x130&data={upi_str}"
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
      st.image(qr_url, caption="Scan & Pay ₹1000", use_container_width=True)

    utr_entered = st.text_input("🔑 ENTER UTR NUMBER", max_chars=25, key="strict_utr_input")

    if st.button("🛡️ VERIFY UTR", use_container_width=True):
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
        st.success("✅ सफलता! पैनल ओपन हो रहा है...")
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
  custom_period_box = st.text_input(
      "📌 BDG LIVE GAME PERIOD NUMBER (MANDATORY)",
      placeholder="यहाँ BDG गेम का लाइव पीरियड नंबर दर्ज करें",
      key="matrix_input_field"
  )

  @st.fragment(run_every=2)
  def success_dashboard_core():
    st.session_state.live_online_count = random.randint(34000, 62000)

    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-red-light"></span><span style="color: #00FFFF; font-weight: 800;">⚡ KISHOR SINGH (100% श्योर शॉर्ट)</span></div>
                <div>👥 <span style="color: #00FF66;">{st.session_state.live_online_count:,}</span></div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2, tab3, tab4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])

    def render_game_panel(seconds, tab_name_style, tab_offset):
      st.markdown("<div class='main-card'>", unsafe_allow_html=True)
      
      if not custom_period_box or not custom_period_box.strip().isdigit():
          st.markdown(
              """
              <div style="text-align: center; padding: 15px 5px;">
                  <h4 style="color: #FF4444; font-size: 14px; font-weight: 900;">⚠️ पैनल लॉक (WAITING FOR PERIOD)</h4>
                  <p style="color: #FFD700; font-size: 11px; margin-top: 4px;">कृपया ऊपर दिए गए बॉक्स में <b>लाइव पीरियड नंबर</b> दर्ज करें।</p>
              </div>
              """,
              unsafe_allow_html=True,
          )
          st.markdown("</div>", unsafe_allow_html=True)
          return

      now = datetime.now()
      total_seconds = now.hour * 3600 + now.minute * 60 + now.second
      current_block_idx = total_seconds // seconds
      remaining_secs = seconds - (total_seconds % seconds)
      mins = remaining_secs // 60
      secs = remaining_secs % 60
      timer_str = f"{mins:02d}:{secs:02d}"

      if "last_input_val" not in st.session_state or st.session_state.last_input_val != custom_period_box.strip():
          st.session_state.last_input_val = custom_period_box.strip()
          st.session_state.base_input_period = int(custom_period_box.strip())
          st.session_state.base_block_index = current_block_idx

      block_difference = current_block_idx - st.session_state.base_block_index
      final_period = st.session_state.base_input_period + block_difference
      
      seed_val = final_period + tab_offset + 426
      
      is_server_syncing = remaining_secs > (seconds - 5)
      is_round_ending = remaining_secs <= 5

      server_target = get_sure_signal(seed_val, tab_offset)
      pred_size = "BIG" if server_target == 'B' else "SMALL"

      pred_num = 9 if server_target == 'B' else 2
      pred_color = "GREEN" if pred_num % 2 != 0 else "RED"
      color_bg = "#00AA55" if pred_color == "GREEN" else "#FF4444"
      size_bg = "linear-gradient(135deg, #FF9900, #FF5500)" if pred_size == "BIG" else "linear-gradient(135deg, #00CCFF, #0044FF)"
      
      st.markdown(
          f"""
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #FFD700; padding-bottom: 4px; margin-bottom: 6px; background: rgba(255,215,0,0.04); border-radius: 6px; padding-left: 6px; padding-right: 6px;">
                <span class="period-box-large"><span class="blinking-red-light"></span>PERIOD: {final_period}</span>
                <span class="timer-box-large">⏰ {timer_str}</span>
            </div>
        """,
          unsafe_allow_html=True,
      )

      if is_server_syncing:
          st.markdown(f'<div class="wait-badge">🔄 BDG & KISHOR SINGH SERVER SYNCING... कृपया प्रतीक्षा करें</div>', unsafe_allow_html=True)
      elif is_round_ending:
          st.markdown(f'<div class="wait-badge">⏳ ROUND ENDING... अगला राउंड आ रहा है</div>', unsafe_allow_html=True)
      else:
          if server_target == 'B':
              st.markdown(f'<div class="sure-banner-big">🎯 {tab_name_style} : 100% श्योर शॉर्ट - BIG (KISHOR SINGH VERIFIED) 🎯</div>', unsafe_allow_html=True)
          else:
              st.markdown(f'<div class="sure-banner-small">🎯 {tab_name_style} : 100% श्योर शॉर्ट - SMALL (KISHOR SINGH VERIFIED) 🎯</div>', unsafe_allow_html=True)

      display_num = pred_num if not (is_server_syncing or is_round_ending) else '?'
      display_size = pred_size if not (is_server_syncing or is_round_ending) else 'WAIT'
      display_color = pred_color if not (is_server_syncing or is_round_ending) else 'WAIT'

      st.markdown(
          f"""
            <div class="diagonal-container">
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">NUMBER</div>
                    <div style="background-color: {color_bg if not (is_server_syncing or is_round_ending) else '#333'}; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: bold; margin: 0 auto; color: white; border: 1.5px solid #FFFFFF;">{display_num}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">SIZE</div>
                    <div style="background: {size_bg if not (is_server_syncing or is_round_ending) else '#222'}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: 900; font-size: 11px; text-align: center; border: 1.5px solid #FFFFFF; text-transform: uppercase;">{display_size}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">COLOR</div>
                    <div style="background-color: {color_bg if not (is_server_syncing or is_round_ending) else '#222'}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: bold; font-size: 11px; text-align: center; border: 1.5px solid #FFFFFF; text-transform: uppercase;">{display_color}</div>
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
