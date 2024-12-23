import re
import pyfiglet
from termcolor import colored

# Create and print the banner
banner_text = "Password Strength Checker"
banner = pyfiglet.figlet_format(banner_text)
print(colored(banner, "blue"))
print(colored("- By Premkumar Soni", "blue"))

# First we take input from the user
print("### Password Strength Checker ###")
wpassword = input("Enter The Password : ")
print("Entered Password:", wpassword)

# Now we defining criteria of password and condition
def password_criteria(wpassword):
    # Here is a criteria below.
    length_criteria = len(wpassword) >= 8
    digi_num_criteria = re.search(r"\d", wpassword) is not None
    uppercase_criteria = re.search(r"[A-Z]", wpassword) is not None
    lowercase_criteria = re.search(r"[a-z]", wpassword) is not None
    special_char_criteria = re.search(r"[!@#$%^&*():;,./]", wpassword) is not None

    score = sum([length_criteria, digi_num_criteria, uppercase_criteria, lowercase_criteria, special_char_criteria])
    
    if score == 5:
        strength = "Password is: Extreme Strong"
    elif score == 4:
        strength = "Password is: Strong"
    elif score == 3:
        strength = "Password is: Moderate"
    elif score == 2:
        strength = "Password is: Weak"
    else:
        strength = "Password is: Extremely Weak"
    
    feedback = []

    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not digi_num_criteria:
        feedback.append("Password should include at least one digit.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")
    
    return strength, feedback, score

strength_message, feedback_messages, score = password_criteria(wpassword)

# Print strength message with color
if "Extreme Strong" in strength_message:
    print(colored(strength_message, "yellow"))
elif "Strong" in strength_message:
    print(colored(strength_message, "green"))
elif "Moderate" in strength_message:
    print(colored(strength_message, "blue"))
else:
    print(colored(strength_message, "red"))

print(f"Score: {score}/5")

# Print feedback messages with color
if feedback_messages:
    print("Feedback:")
    for message in feedback_messages:
        print(colored(f" - {message}", "red"))
