import time
import streamlit as st

st.title("⏱️ เกมเติมศัพท์จับเวลา")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""


# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าช่องข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าช่องข้อ 2
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()

    # ตรวจข้อ 1
    if u_ans1 == "happy":
        st.success("✅ Question 1: Correct!")
        score += 1
    else:
        st.error(f"❌ Question 1: Wrong! (You answered '{u_ans1}')")

    # ตรวจข้อ 2
    if u_ans2 == "lonely":
        st.success("✅ Question 2: Correct!")
        score += 1
    else:
        st.error(f"❌ Question 2: Wrong! (You answered '{u_ans2}')")

    # ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มตรวจข้อ 3, 4 ตรงนี้
    if u_ans3 == "excited":
        st.success("✅ Question 3: Correct!")
        score += 1
    else:
        st.error(f"❌ Question 3: Wrong! (You answered '{u_ans3}')")

    if u_ans4 == "peaceful":
        st.success("✅ Question 4: Correct!")
        score += 1
    else:
        st.error(f"❌ Question 4: Wrong! (You answered '{u_ans4}')")

    st.info(f"🏆 You got: {score}! ")

    if score == 4:
        st.success("Your heart is full of feeling today!")
    
    if score == 3:
        st.success("It’s okay, time to makes progress.")

    if score == 2:
        st.success("Probably could do better?")
        
    if score <= 1:
        st.error("No worries, atleast you tried!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 Play", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ Time Left: {time_left} Seconds")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ (ใช้ value ผูกกับตัวแปรตรงๆ เพื่อสั่งเคลียร์ได้)
ans1 = st.text_input(
    "Question 1: Smiling wide, full of joy and laughter - ‘ h _ p _ y ’",
    value=st.session_state.ans1_val,
)
ans2 = st.text_input(
    "Question 2: Sitting in a room, missing the company - ‘ l _ n _ e _ y ’",
    value=st.session_state.ans2_val,
)

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# ✏️ [พื้นที่สำหรับนักเรียน]: เพิ่มข้อ 3, 4 ตรงนี้
ans3 = st.text_input(
    "Question 3: Heart racing before a big adventure! - ‘ e x _ c _ _ _ d ’",
    value=st.session_state.ans3_val,
)
ans4 = st.text_input(
    "Question 4: Listening with gentle without worries - ‘ p _ a _ e f _ l ’",
    value=st.session_state.ans4_val,
)

st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4

# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4)

st.divider()
