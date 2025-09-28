import re

def assess_password_strength(password):
    """
    Assesses the strength of a password based on length and character complexity.

    A simple scoring system is used: points are awarded for meeting different criteria.

    :param password: The input password string.
    :return: A tuple containing (score, feedback_list)
    """
    score = 0
    feedback = []
    
    # 1. Length Check
    length = len(password)
    if length >= 12:
        score += 3
        feedback.append("✅ Great length (12+ characters)")
    elif length >= 8:
        score += 1
        feedback.append("👍 Good length (8+ characters)")
    else:
        feedback.append("❌ Short length (needs at least 8 characters)")
        
    # 2. Complexity Checks (using Regular Expressions)
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Includes lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")
        
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Includes uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")

    # Check for numbers
    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✅ Includes numbers")
    else:
        feedback.append("❌ Missing numbers")
        
    # Check for special characters (using common special characters)
    # The pattern includes characters like !@#$%^&*()_+-=[]{};:'"|/?.,<>\`~
    if re.search(r'[!@#$%^&*()\-_+=|\\:;"\'<,>.?/`~]', password):
        score += 2  # Special characters often count more
        feedback.append("✅ Includes special characters")
    else:
        feedback.append("❌ Missing special characters")
        
    return score, feedback

def get_strength_rating(score):
    """Maps the score to a strength rating."""
    if score >= 8:
        return "Excellent", "🟢"
    elif score >= 6:
        return "Strong", "✅"
    elif score >= 4:
        return "Moderate", "🟡"
    elif score >= 2:
        return "Weak", "🟠"
    else:
        return "Very Weak", "🔴"

def main():
    """Main function to handle user input and display assessment."""
    print("--- Password Strength Assessor Tool ---")
    print("Assessment based on length, case, numbers, and special characters.")
    print("-" * 50)
    
    password = input("Enter the password to assess: ")

    if not password:
        print("Password cannot be empty.")
        return

    # Perform the assessment
    score, feedback_list = assess_password_strength(password)
    rating, emoji = get_strength_rating(score)

    # Display results
    print("-" * 50)
    print(f"Password Score: {score}")
    print(f"Overall Strength: {emoji} {rating}")
    print("\nDetailed Feedback:")
    for item in feedback_list:
        print(f"  - {item}")
    print("-" * 50)

if __name__ == "__main__":
    main()
