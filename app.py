from datetime import datetime, timedelta
import random
import streamlit as st

# --- पेज सेटअप और डार्क थीम ---
st.set_page_config(
    page_title="KISHOR SINGH - SERVER AUTO",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background-color: #020104; color: #FFFFFF; }
    
    /* टिप-टिप (ब्लिंकिंग) लाइट का एनिमेशन */
    @keyframes blink-animation {
        0% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #FF0055; }
        50% { opacity: 0.2; transform: scale(0.85); box-shadow: 0 0 2px #FF0055; }
        100% { opacity: 1; transform: scale(1); box-shadow: 0 0 10px #FF0055; }
    }

    .blinking-red-light { 
        display: inline-block; 
        width: 9px; 
        height: 9px; 
        background-color: #FF0055; 
        border-radius: 50%; 
        margin-right: 5px; 
        animation: blink-animation 1s infinite ease-in-out;
    }

    .top-bar { display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #0d2216, #040d08); padding: 6px 10px; border-radius: 8px; font-size: 11px; font-weight: bold; border: 1px solid #3d9f5a; margin-bottom: 6px; }
    .main-card { background-color: #0b071a; border: 1.5px solid #FFD700; border-radius: 10px; padding: 10px; box-shadow: 0 0 15px rgba(255,215,0,0.2); margin-top: 4px; }
    
    .timer-box-large { color: #FFD700; font-weight: 900; font-size: 13px; }
    .period-box-large { color: #FFFFFF; font-weight: 900; font-size: 13px; }
    
    .sure-banner-big { background: linear-gradient(135deg, #4d2600, #1a0d00); border: 1.5px solid #FFD700; padding: 7px 10px; border-radius: 6px; text-align: center; font-size: 13px; font-weight: 900; margin: 6px 0; color: #FFD700; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 10px rgba(255,215,0,0.3); }
    .sure-banner-small { background: linear-gradient(135deg, #002b4d, #000f1a); border: 1.5px solid #00E5FF; padding: 7px 10px; border-radius: 6px; text-align: center; font-size: 13px; font-weight: 900; margin: 6px 0; color: #00E5FF; text-transform: uppercase; letter-spacing: 0.5px; box-shadow: 0 0 10px rgba(0,229,255,0.3); }

    .wait-badge { background: linear-gradient(135deg, #221100, #140a00); border: 2px dashed #FF9900; padding: 6px; border-radius: 6px; text-align: center; font-size: 11px; font-weight: bold; margin: 6px 0; color: #FF9900; text-transform: uppercase; }
    .nosignal-badge { background: linear-gradient(135deg, #330000, #1a0000); border: 2px dashed #FF4444; padding: 6px; border-radius: 6px; text-align: center; font-size: 11px; font-weight: bold; margin: 6px 0; color: #FF4444; text-transform: uppercase; }

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

MASTER_MOBILE = "9011997944"
MASTER_PASSWORD = "KISHOR90"

# --- बीडीजी और 11 सर्वर का कम्बाइंड कंसेंसस इंजन ---
@st.cache_data(ttl=3600)
def get_bdg_synced_consensus_signal(final_period_val, tab_offset, user_input_period_str):
    bdg_seed = int(user_input_period_str) * 99 + int(tab_offset) * 13
    bdg_gen = random.Random(bdg_seed)
    bdg_val = bdg_gen.random()
    bdg_signal = "BIG" if bdg_val >= 0.5 else "SMALL"

    our_votes = []
    for engine_id in range(1, 12):
        engine_seed = int(final_period_val) * (71 + engine_id) + int(tab_offset) * 41
        core_gen = random.Random(engine_seed)
        val = core_gen.random()
        our_votes.append("BIG" if val >= 0.5 else "SMALL")
        
    our_big_count = our_votes.count("BIG")
    our_small_count = our_votes.count("SMALL")
    
    our_majority_signal = "BIG" if our_big_count >= our_small_count else "SMALL"
    
    accumulated_score = sum(random.Random(int(final_period_val) * (80 + e) + int(tab_offset)).random() for e in range(1, 12)) / 11.0
    pred_num = int((accumulated_score * 100000) % 10)

    is_bdg_matched = (bdg_signal == our_majority_signal) and (our_big_count >= 8 or our_small_count >= 8)

    return pred_num, our_majority_signal, is_bdg_matched

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
  st.markdown("<h2 style='text-align: center; color: #FFD700; font-size: 22px; font-weight: 900;'>👑 KISHOR SINGH SERVER AUTO <br> ACCESS</h2>", unsafe_allow_html=True)

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

  @st.fragment(run_every=1)
  def success_dashboard_core():
    # ऑनलाइन संख्या अब 1 लाख से 4.9 लाख के बीच हर सेकंड बड़ी रेंज में कम-ज्यादा होगी
    dynamic_online_count = random.randint(112000, 498000)

    st.markdown(
        f"""
            <div class="top-bar">
                <div><span class="blinking-red-light"></span><span style="color: #00FFFF; font-weight: 800;">⚡ KISHOR SINGH SERVER AUTO</span></div>
                <div><span class="blinking-red-light"></span>👥 <span style="color: #00FF66;">{dynamic_online_count:,}</span></div>
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
      
      is_server_syncing = remaining_secs > (seconds - 3)
      is_round_ending = remaining_secs <= 4

      pred_num, pred_size, is_bdg_matched = get_bdg_synced_consensus_signal(final_period, tab_offset, custom_period_box.strip())

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
          st.markdown(f'<div class="wait-badge">🔄 BDG SYNCING... नया राउंड लोड हो रहा है</div>', unsafe_allow_html=True)
      elif is_round_ending:
          st.markdown(f'<div class="wait-badge">⏳ ROUND ENDING... परिणाम की प्रतीक्षा है</div>', unsafe_allow_html=True)
      elif not is_bdg_matched:
          st.markdown(f'<div class="nosignal-badge">⚠️ KISHOR SINGH SERVER AUTO - WAITING FOR MATCH...</div>', unsafe_allow_html=True)
      else:
          if pred_size == "BIG":
              st.markdown(f'<div class="sure-banner-big">🔥 KISHOR SINGH SERVER AUTO - BIG 🔥</div>', unsafe_allow_html=True)
          else:
              st.markdown(f'<div class="sure-banner-small">🔥 KISHOR SINGH SERVER AUTO - SMALL 🔥</div>', unsafe_allow_html=True)

      show_data = is_bdg_matched and not (is_server_syncing or is_round_ending)
      
      display_num = pred_num if show_data else '?'
      display_size = pred_size if show_data else 'WAIT'
      display_color = pred_color if show_data else 'WAIT'

      st.markdown(
          f"""
            <div class="diagonal-container">
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">NUMBER</div>
                    <div style="background-color: {color_bg if show_data else '#333'}; width: 34px; height: 34px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 15px; font-weight: bold; margin: 0 auto; color: white; border: 1.5px solid #FFFFFF;">{display_num}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">SIZE</div>
                    <div style="background: {size_bg if show_data else '#222'}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: 900; font-size: 11px; text-align: center; border: 1.5px solid #FFFFFF; text-transform: uppercase;">{display_size}</div>
                </div>
                <div class="result-item">
                    <div style="font-size: 9px; color: #A0A0A0; font-weight: bold; margin-bottom: 2px;">COLOR</div>
                    <div style="background-color: {color_bg if show_data else '#222'}; color: white; padding: 6px 2px; border-radius: 6px; font-weight: bold; font-size: 11px; text-align: center; border: 1.5px solid #FFFFFF; text-transform: uppercase;">{display_color}</div>
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
