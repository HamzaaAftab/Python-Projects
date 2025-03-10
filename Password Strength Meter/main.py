import streamlit as st
import re
import random
import string

# Blacklist of weak passwords
BLACKLIST = ["password", "123456", "qwerty", "abc123", "password123", "letmein"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Blacklist check
    if password.lower() in BLACKLIST:
        return 0, "❌ This password is too common! Choose a unique one."
    
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return 5, "✅ Strong Password!"
    elif score == 3:
        return 4, "⚠️ Moderate Password - Consider adding more security features."
    else:
        return score, "\n".join(feedback)

# Function to generate a strong password
def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter a password to check its strength and get security tips!")

password = st.text_input("Enter Password:", type="password")

if password:
    score, feedback = check_password_strength(password)
    st.markdown(f"**Strength Score:** {score}/5")
    
    if score == 5:
        st.success(feedback)
    else:
        st.warning(feedback)

# Password Generator Button
if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("Suggested Strong Password:", value=strong_password, type="default")
