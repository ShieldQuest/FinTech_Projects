import streamlit as st

st.set_page_config(page_title="Rate My Credit Habits", page_icon="💳")

st.title("Rate My Credit Habit 👀")
st.write("Answer the questions below to see how healthy your credit habits are.")

# User input: name
name = st.text_input("What's your name? ")

# Sliders & checkboxes
on_time = st.slider("How often do you pay your bills on time?", 0, 10, 5)
credit_usage = st.slider("How much credit do you use? (%)", 0, 100, 50)
open_accounts = st.checkbox("Do you open lots of new accounts often?")
disputes = st.checkbox("Have you ever disputed credit report errors?")

# Button to get results
if st.button("Check My Credit Habits"):
    display_name = name if name else "User"
    st.subheader(f"💳 Credit Report for {display_name}:")
    
    # Credit score points system (just to illustrate)
    score = 0 
    score += on_time
    score += (100 - credit_usage) // 10
    if not open_accounts:
        score += 2
    if disputes:
        score += 2

    # Results
    if score >= 18:
        st.success("✅ Excellent credit habits! Keep it up!")
    elif score >= 12:
        st.info("🟡 Decent credit habits, with room for improvement.")
    else:
        st.warning("🔴 Time for a credit makeover. Let's built better habits!")

    st.write("Note: This is just for illustration and practice. Not a real credit score 😅")