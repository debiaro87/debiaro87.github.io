import tkinter as tk

COMMON_PASSWORDS = {
    "123456", "password", "12345678", "qwerty",
    "abc123", "111111", "password1", "123123"
}

def check_password(password: str):
    feedback = []

    length_ok = len(password) >= 8
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    not_common = password not in COMMON_PASSWORDS

    score = sum([length_ok, has_digit, has_upper, has_lower, has_symbol, not_common])

    if not length_ok:
        feedback.append("Use at least 8 characters")
    if not has_digit:
        feedback.append("Add at least one number")
    if not has_upper:
        feedback.append("Add an uppercase letter")
    if not has_lower:
        feedback.append("Add a lowercase letter")
    if not has_symbol:
        feedback.append("Add a symbol (!, @, #, etc.)")
    if not not_common:
        feedback.append("Avoid common passwords (e.g. '123456', 'password')")

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, feedback, color


def evaluate():
    password = entry.get()
    strength, feedback, color = check_password(password)

    result_label.config(text=f"Strength: {strength}", fg=color)

    feedback_box.delete("1.0", tk.END)
    if feedback:
        feedback_box.insert(tk.END, "\n".join(f"- {f}" for f in feedback))
    else:
        feedback_box.insert(tk.END, "Your password looks good!")


root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

tk.Label(root, text="Enter Password:").pack()

entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Password", command=evaluate).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

feedback_box = tk.Text(root, height=8, width=40)
feedback_box.pack()

root.mainloop()