import tkinter as tk
from tkinter import messagebox
import random
import string

# Evaluate password strength
def evaluate_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])
    if length >= 12 and score == 4:
        return "🟢 STRONG", 100, "lime"
    elif length >= 8 and score >= 3:
        return "🟡 MEDIUM", 60, "orange"
    else:
        return "🔴 WEAK", 30, "red"

# Generate random password
def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_digits = digits_var.get()
        use_specials = specials_var.get()

        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_digits:
            characters += string.digits
        if use_specials:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("❌ ERROR", "Choose at least one character type!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        strength, value, color = evaluate_strength(password)

        result_var.set(password)
        strength_var.set(strength)
        strength_bar.set(value)
        strength_bar.config(fg=color, bg=color)

    except ValueError:
        messagebox.showerror("❌ ERROR", "Enter a valid number for password length.")

# Show password tips
def show_tips():
    tips = (
        "⚠️ CYBERSECURITY TIPS ⚠️\n\n"
        "✔ Use 12+ characters\n"
        "✔ Combine UPPER/lower, numbers & symbols\n"
        "✘ Avoid simple words or repeated patterns\n"
        "✔ Use different passwords for different accounts\n"
        "✔ Use a password manager like Bitwarden/KeePass"
    )
    messagebox.showinfo("DANGER MODE SECURITY", tips)

# Custom password strength check
def check_custom_strength():
    password = custom_entry.get()
    if not password:
        messagebox.showerror("❌ ERROR", "Please enter a password to check.")
        return
    strength, value, color = evaluate_strength(password)
    custom_strength_var.set(f"Strength: {strength}")
    strength_bar.set(value)
    strength_bar.config(fg=color, bg=color)

# GUI Setup
root = tk.Tk()
root.title("💀 Password Generator 💀")
root.geometry("500x580")
root.configure(bg="black")
root.resizable(False, False)

style_font = ("Courier New", 12, "bold")
label_color = "red"
entry_bg = "#1e1e1e"
entry_fg = "lime"

# ----- Header -----
tk.Label(root, text="💀 SECURE PASSWORD GENERATOR 💀", font=("Courier New", 13, "bold"), fg="red", bg="black").pack(pady=10)

# ----- Generate Section -----
tk.Label(root, text="Enter Length:", font=style_font, fg=label_color, bg="black").pack()
length_entry = tk.Entry(root, font=style_font, bg=entry_bg, fg=entry_fg, justify="center", width=8)
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
specials_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters (A-Z)", variable=letters_var, bg="black", fg="white", selectcolor="black").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=digits_var, bg="black", fg="white", selectcolor="black").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols (@#*&)", variable=specials_var, bg="black", fg="white", selectcolor="black").pack(anchor='w', padx=40)

tk.Button(root, text="⚔️ GENERATE ⚔️", font=style_font, bg="red", fg="white", command=generate_password).pack(pady=10)

result_var = tk.StringVar()
strength_var = tk.StringVar()

tk.Entry(root, textvariable=result_var, font=("Courier New", 12), bg="black", fg="lime", justify="center", width=35, bd=2, relief="sunken").pack()
tk.Label(root, textvariable=strength_var, font=("Courier New", 10, "bold"), fg="yellow", bg="black").pack(pady=5)

# ----- Strength Bar -----
strength_bar = tk.Scale(
    root, from_=0, to=100, orient="horizontal",
    length=300, showvalue=False,
    troughcolor="#222", sliderlength=20,
    bg="black", highlightthickness=0
)
strength_bar.pack()

# ----- Custom Password Check -----
tk.Label(root, text="🔍 CUSTOM PASSWORD STRENGTH CHECK 🔍", font=("Courier New", 11), fg="red", bg="black").pack(pady=15)
custom_entry = tk.Entry(root, font=style_font, bg=entry_bg, fg="white", justify="center", width=30)
custom_entry.pack(pady=5)

tk.Button(root, text="Check Strength", font=("Courier New", 10), bg="#222", fg="white", command=check_custom_strength).pack(pady=5)

custom_strength_var = tk.StringVar()
tk.Label(root, textvariable=custom_strength_var, font=("Courier New", 10, "bold"), fg="cyan", bg="black").pack()

# ----- Tips & Watermark -----
tk.Button(root, text="📚 SECURITY TIPS", font=("Courier New", 10), bg="#222", fg="red", command=show_tips).pack(pady=10)
tk.Label(root, text="⚠ Developed by Anugraha ⚠", font=("Courier New", 8), fg="gray", bg="black").place(relx=1.0, rely=1.0, anchor='se', x=-8, y=-8)

# Run
root.mainloop()
