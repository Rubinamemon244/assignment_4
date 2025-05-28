import streamlit as st # type: ignore
import random

st.title("🌟 Madlib Story Generator")
st.write("Fill in the blanks and create a fun story! ✨")

# User inputs
noun = st.text_input("📝 Enter a noun:")
verb = st.text_input("🏃 Enter a verb:")
adjective = st.text_input("🎨 Enter an adjective:")
place = st.text_input("🌍 Enter a place:")

# Optional twist list
twists = [
    "suddenly vanished into thin air 🌬️",
    "discovered a hidden treasure 💎",
    "started dancing like no one's watching 💃",
    "met a talking cat 🐱",
    "built a spaceship and flew away 🚀",
    "became a superhero overnight 🦸",
]

# Generate story
if st.button("🧙 Generate Story"):
    if noun and verb and adjective and place:
        twist = random.choice(twists)
        create_story = (
            f"📖 Once upon a time in **{place}**, there was a **{adjective} {noun}** "
            f"who loved to **{verb}**. One day, {twist}!"
        )
        st.subheader("🎉 Your Generated Story")
        st.markdown(create_story)
    else:
        st.warning("⚠️ Please fill in all fields to generate a story.")
