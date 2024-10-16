grade = int(input("What was your grade: "))
print("You will receive a \"" +
      ("High Distinction" if grade >= 85
       else "Distinction" if grade >= 70
       else "Credit" if grade >= 60
       else "Pass" if grade >= 50
       else "Fail")
      + "\""
      )