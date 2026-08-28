import re
import streamlit as st

st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)


def check_password_strength(password):
    """
    Returns a tuple: (level, message, checklist)
    level is one of: "empty", "weak", "medium", "strong"
    checklist is a dict of rule -> bool
    """
    checklist = {
        "At least 8 characters": len(password) >= 8,
        "Contains a digit": any(char.isdigit() for char in password),
        "Contains an uppercase letter": any(char.isupper() for char in password),
        "Contains a lowercase letter": any(char.islower() for char in password),
        "Contains a special character": bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
    }

    if not password:
        return "empty", "Start typing to check your password strength.", checklist

    if not checklist["At least 8 characters"]:
        return "weak", "Password length must be at least 8 characters.", checklist
    if not checklist["Contains a digit"]:
        return "weak", "Password must contain a digit.", checklist
    if not checklist["Contains an uppercase letter"]:
        return "weak", "Password must contain an uppercase character.", checklist
    if not checklist["Contains a lowercase letter"]:
        return "weak", "Password must contain a lowercase character.", checklist
    if not checklist["Contains a special character"]:
        return "medium", "Add special characters to make your password stronger.", checklist

    return "strong", "Your password is secured!", checklist


# ---- Styling ----
st.markdown("""
<style>
.big-title {
    font-size: 2.2rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.2rem;
}
.subtitle {
    text-align: center;
    color: #888;
    margin-bottom: 2rem;
}
.result-box {
    padding: 1rem 1.2rem;
    border-radius: 10px;
    font-weight: 600;
    font-size: 1.05rem;
    margin-top: 1rem;
}
.weak-box {
    background-color: rgba(255, 76, 76, 0.15);
    border: 1px solid #ff4c4c;
    color: #ff4c4c;
}
.medium-box {
    background-color: rgba(255, 176, 32, 0.15);
    border: 1px solid #ffb020;
    color: #ffb020;
}
.strong-box {
    background-color: rgba(46, 204, 113, 0.15);
    border: 1px solid #2ecc71;
    color: #2ecc71;
}
.checklist-item {
    font-size: 0.95rem;
    margin: 0.15rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🔐 Password Strength Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type a password below to see how strong it is, in real time.</div>', unsafe_allow_html=True)

show_password = st.toggle("Show password", value=False)

password = st.text_input(
    "Enter your password",
    type="default" if show_password else "password",
    placeholder="Type your password here..."
)

level, message, checklist = check_password_strength(password)

# Progress bar mapping
progress_map = {"empty": 0, "weak": 33, "medium": 66, "strong": 100}
color_map = {"empty": "#888", "weak": "#ff4c4c", "medium": "#ffb020", "strong": "#2ecc71"}

st.progress(progress_map[level] / 100)

if level != "empty":
    box_class = f"{level}-box"
    label = {"weak": "Weak", "medium": "Medium", "strong": "Strong"}[level]
    st.markdown(
        f'<div class="result-box {box_class}">{label}: {message}</div>',
        unsafe_allow_html=True
    )

st.markdown("### Checklist")
for rule, passed in checklist.items():
    icon = "✅" if passed else "❌"
    st.markdown(f'<div class="checklist-item">{icon} {rule}</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("Tip: Combine length, mixed case, numbers, and symbols for the strongest passwords.")
