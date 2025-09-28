# 🔑 Task 03: Password Strength Assessor

This project is a **Password Strength Assessor Tool** built in Python.\
It evaluates the strength of a password based on **length** and
**character complexity** using regular expressions.

------------------------------------------------------------------------

## 📌 Features

-   Checks password **length** (short, good, great).\
-   Validates inclusion of:
    -   ✅ Lowercase letters\
    -   ✅ Uppercase letters\
    -   ✅ Numbers\
    -   ✅ Special characters (!@#\$%\^&\* etc.)\
-   Assigns a **score** and provides **feedback**.\
-   Gives an **overall strength rating** with emojis.

------------------------------------------------------------------------

## 🛠️ Requirements

-   Python 3.x

No external libraries required (only `re`, part of Python standard
library).

------------------------------------------------------------------------

## 🚀 How to Run

1.  Clone or download this repository.\
2.  Run the script from the terminal:

``` bash
python password_assessor.py
```

------------------------------------------------------------------------

## 🖥️ Example Run

    --- Password Strength Assessor Tool ---
    Assessment based on length, case, numbers, and special characters.
    --------------------------------------------------
    Enter the password to assess: P@ssw0rd123!

    --------------------------------------------------
    Password Score: 9
    Overall Strength: 🟢 Excellent

    Detailed Feedback:
      - ✅ Great length (12+ characters)
      - ✅ Includes lowercase letters
      - ✅ Includes uppercase letters
      - ✅ Includes numbers
      - ✅ Includes special characters
    --------------------------------------------------

------------------------------------------------------------------------

## 📊 Strength Ratings

  Score Range   Rating      Emoji
  ------------- ----------- -------
  8+            Excellent   🟢
  6--7          Strong      ✅
  4--5          Moderate    🟡
  2--3          Weak        🟠
  0--1          Very Weak   🔴

------------------------------------------------------------------------

## 📌 Author

Developed as part of **Cybersecurity Fundamentals Practice** 🚀
