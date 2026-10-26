
from time import sleep


print("""
========================================
       PASSWORD COMPLEXITY CHECKER
========================================

Requirements:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one special character
""")

password = input("Enter your password: ").strip()

print("\nLoading password checker...")
print("-" * 40)


def checking_length(password):
    """Check whether the password has at least 8 characters."""
    print("Checking password length...")
    sleep(3)

    length = len(password)

    if length >= 8:
        return True, length

    return False, length


def checking_uppercase(password):
    """Check whether the password contains an uppercase letter."""
    print("Checking uppercase letters...")
    sleep(2)

    has_uppercase = any(char.isupper() for char in password)

    return has_uppercase


def checking_lowercase(password):
    """Check whether the password contains a lowercase letter."""
    print("Checking lowercase letters...")
    sleep(2)

    has_lowercase = any(char.islower() for char in password)

    return has_lowercase


def checking_special_char(password):
    """Check whether the password contains a special character."""
    print("Checking special characters...")
    sleep(3)

    special_characters = "!@#$%&*"
    has_special_char = any(
        char in special_characters for char in password
    )

    return has_special_char


# Initialize password strength
strength = 0

print("\n" + "=" * 40)
print("             CHECKING RESULTS")
print("=" * 40)

# 1. Check password length
is_valid_length, length = checking_length(password)

if is_valid_length:
    print(f"[PASS] Password length is valid: {length} characters")
    strength += 1
elif not is_valid_length:
    print(f"[FAIL] Password length is invalid: {length} characters")

# 2. Check uppercase letters
has_uppercase = checking_uppercase(password)

if has_uppercase:
    print("[PASS] At least one uppercase letter was found")
    strength += 1
elif not has_uppercase:
    print("[FAIL] No uppercase letters were found")

# 3. Check lowercase letters
has_lowercase = checking_lowercase(password)

if has_lowercase:
    print("[PASS] At least one lowercase letter was found")
    strength += 1
elif not has_lowercase:
    print("[FAIL] No lowercase letters were found")

# 4. Check special characters
has_special_char = checking_special_char(password)

if has_special_char:
    print("[PASS] At least one special character was found")
    strength += 1
else:
    print("[FAIL] No special characters were found")

# Display final password strength
print("\n" + "=" * 40)
print(f"Password strength score: {strength}/4")
print("-" * 40)

if strength <= 1:
    print("Result: WEAK")
elif strength <= 3:
    print("Result: MODERATE")
else:
    print("Result: STRONG")

print("=" * 40)
