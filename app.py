from datetime import datetime, timedelta
import random
import time
import streamlit as st

# --- पेज सेटअप और प्रीमियम UI ---
st.set_page_config(
    page_title="Big Daddy (BDG) PRO - Baap Engine",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0B0716;
        color: #FFFFFF;
    }
    .top-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #150F24;
        padding: 8px 15px;
        border-radius: 20px;
        border: 1px solid #332244;
        margin-bottom: 15px;
        font-size: 12px;
    }
    .main-title {
        font-size: 22px;
        font-weight: 900;
        text-align: center;
        color: #FFB800;
        margin-top: 5px;
        margin-bottom: 15px;
        letter-spacing: 1px;
    }
    .card-box {
        background-color: #120D22;
        border: 2px solid #FFB800;
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        box-shadow: 0 0 25px rgba(255, 184, 0, 0.2);
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


# 🛡️ 7-8 एडवांस्ड इंजन और सेंटिनल ओवरवाच मास्टर कोर
def sentinel_overwatch_master_engine(current_block_idx):
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
  sentinel_factor = (current_block_idx * 37) % 17
  final_decision = "BIG" if sentinel_factor in [0, 1, 2, 3, 5, 7, 11, 13] else "SMALL"

  total_votes = active_cores + [final_decision, final_decision, final_decision]
  final_size = "BIG" if total_votes.count("BIG") >= 4 else "SMALL"

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
      "<h2 style='text-align: center; color: #FFB800;'>🔒 Big Daddy (BDG)"
      " PRO</h2>",
      unsafe_allow_html=True,
  )
  with st.container():
    st.markdown("<div class='card-box'>", unsafe_allow_html=True)
    mobile = st.text_input("📱 PHONE NUMBER", placeholder="Enter mobile number")
    password = st.text_input(
        "🔒 PASSWORD", type="password", placeholder="Enter password"
    )

    if st.button("🚀 LOGIN", use_container_width=True):
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
  st.markdown(
      """
    <div class="top-bar">
        <span>🟢 Server Active</span>
        <span>🔥 Online: 13,222</span>
    </div>
    <div class="main-title">BIG DADDY (BDG) PRO</div>
    """,
      unsafe_allow_html=True,
  )

  t1, t2, t3, t4 = st.tabs(["WINGO 30S", "WINGO 1M", "WINGO 3M", "WINGO 5M"])


  def render_game_tab(game_seconds, tab_name):
    auto_p, timer_str, current_block = get_bulletproof_period(game_seconds)

    base_block_key = f"base_block_{tab_name}"
    base_val_key = f"base_val_{tab_name}"

    if base_block_key not in st.session_state:
      st.session_state[base_block_key] = current_block
      st.session_state[base_val_key] = auto_p

    block_diff = current_block - st.session_state[base_block_key]
    default_period = st.session_state[base_val_key] + block_diff

    # लाइव पीरियड नंबर डालने का खाचा (Box)
    manual_input_str = st.text_input(
        "Live Period Number",
        value=str(default_period),
        key=f"override_str_{tab_name}",
    )

    try:
      manual_input_val = int(manual_input_str.strip())
    except ValueError:
      manual_input_val = int(default_period)

    if manual_input_val != default_period:
      st.session_state[base_block_key] = current_block
      st.session_state[base_val_key] = manual_input_val

    final_period_num = st.session_state[base_val_key] + (
        current_block - st.session_state[base_block_key]
    )

    pred_number, pred_size, pred_color = sentinel_overwatch_master_engine(current_block)

    color_code = (
        "#00AA55"
        if pred_color == "GREEN"
        else ("#FF4444" if pred_color == "RED" else "#9933FF")
    )
    size_bg = "#FFB800" if pred_size == "BIG" else "#FF3366"
    size_text_color = "#000000" if pred_size == "BIG" else "#FFFFFF"

    st.markdown(
        f"""
        <div class="card-box">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; font-size: 13px; font-weight: bold; color: #BBBBCC;">
                <span>PERIOD: {final_period_num}</span>
                <span>TIME: {timer_str}</span>
            </div>

            <div style="text-align: center; color: #FFB800; font-weight: 900; font-size: 15px; margin-bottom: 12px; letter-spacing: 1px;">
                👇 NEXT RESULT 👇
            </div>

            <div style="display: flex; justify-content: space-around; align-items: center; text-align: center;">
                <div>
                    <p style="font-size: 11px; color: #9999AA; margin-bottom: 4px; font-weight: bold;">NUMBER</p>
                    <div style="background-color: {color_code}; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; margin: auto; color: white; box-shadow: 0 0 12px {color_code};">{pred_number}</div>
                </div>
                <div>
                    <p style="font-size: 11px; color: #9999AA; margin-bottom: 4px; font-weight: bold;">SIZE</p>
                    <div style="background-color: {size_bg}; color: {size_text_color}; padding: 12px 22px; border-radius: 12px; font-weight: 900; font-size: 18px; box-shadow: 0 0 15px {size_bg};">{pred_size}</div>
                </div>
                <div>
                    <p style="font-size: 11px; color: #9999AA; margin-bottom: 4px; font-weight: bold;">COLOR</p>
                    <div style="background-color: {color_code}; color: white; padding: 12px 20px; border-radius: 12px; font-weight: bold; font-size: 16px; box-shadow: 0 0 12px {color_code};">{pred_color}</div>
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

  if st.button("🚪 Logout", use_container_width=True):
    st.session_state.authenticated = False
    st.rerun()

  time.sleep(1)
  st.rerun()
