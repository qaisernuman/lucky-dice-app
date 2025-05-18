
import streamlit as st
import random
import time

st.set_page_config(page_title="🎲 Lucky Dice Game", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎲 Lucky Dice Roller</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Roll 8 dice and win amazing prizes!</p>", unsafe_allow_html=True)

dice_faces = {
    1: "🎲1️⃣",
    2: "🎲2️⃣",
    3: "🎲3️⃣",
    4: "🎲4️⃣",
    5: "🎲5️⃣",
    6: "🎲6️⃣"
}

rewards = {
    8: "🎉 Congratulations! You have won an iPhone 16 Pro Max!",
    9: "🎉 Congrats! You have won the Samsung S24 Ultra!",
    10: "🎉 Congrats! You have won the iPad Air!",
    11: "🎉 You have won an iPhone 13!",
    12: "🎉 You have won AirPods Pro!",
    13: "🎉 You have won AirPods Pro!",
    14: "🎉 You have won AirPods Pro!",
    41: "🎉 You have won Noon 100 Credit Points!",
    42: "🎉 You have won AirPods Pro!",
    43: "🎉 You have won AirPods Pro!",
    44: "🎉 You have won AirPods Pro!",
    45: "🎉 You have won an iPhone 13!",
    46: "🎉 Congrats! You have won the iPad Air!",
    47: "🎉 Congrats! You have won the Samsung S24 Ultra!",
    48: "🎉 Congratulations! You have won an iPhone 16 Pro Max!",
}

def roll_dice():
    return [random.randint(1, 6) for _ in range(8)]

if st.button("🎲 Roll Dice!"):
    with st.spinner("Rolling..."):
        time.sleep(1)
    dice = roll_dice()
    total = sum(dice)

    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>Your Dice Rolls:</h3>", unsafe_allow_html=True)
    st.markdown(
        f"<div style='font-size: 2rem; text-align: center;'>{' '.join([dice_faces[d] for d in dice])}</div>",
        unsafe_allow_html=True
    )

    st.markdown(f"<h2 style='text-align: center;'>Total: {total}</h2>", unsafe_allow_html=True)

    result = rewards.get(total, "😞 Sorry, try again!")
    st.markdown(f"<h3 style='text-align: center; color: #FF5722;'>{result}</h3>", unsafe_allow_html=True)
