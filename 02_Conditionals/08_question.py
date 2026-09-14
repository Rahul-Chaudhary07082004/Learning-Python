# password strength checker
# check if a password is "weak", "medium", or "strong". Criteria: <6 chars (weak), 6-10 chars (medium), >10 chars (strong).

password = input("Please enter your password: \n");
password_in_str = str(password);

if len(password_in_str) < 6:
    strength = "weak";
elif len(password_in_str) <=10:
    strength = "medium";
else:
    strength = "strong";

print(strength);