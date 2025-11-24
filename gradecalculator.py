print(" FINAL GRADE CALCULATOR")
print("--------------------------------\n")

# Inputs
mid = float(input("Enter Midterm marks (out of 50): "))
term = float(input("Enter Term-End marks (out of 100): "))
internal = float(input("Enter Internal marks: "))

# Weighted marks
mid_weighted = (mid / 50) * 30
term_weighted = (term / 100) * 30

# Final Score
final_score = mid_weighted + term_weighted + internal

# Grade based on final score
if final_score >= 90:
    grade = "A+"
elif final_score >= 80:
    grade = "A"
elif final_score >= 70:
    grade = "B"
elif final_score >= 60:
    grade = "C"
elif final_score >= 50:
    grade = "D"
else:
    grade = "F"

# Pass/Fail (updated)
status = "PASS" if final_score >= 60 else "FAIL"

# Output
print("\nRESULT")
print("--------------------------------")
print("Weighted Midterm Marks :", round(mid_weighted, 2))
print("Weighted Term-End Marks:", round(term_weighted, 2))
print("Internal Marks         :", internal)
print("Final Score            :", round(final_score, 2))
print("Grade                  :", grade)
print("Status                 :", status)
