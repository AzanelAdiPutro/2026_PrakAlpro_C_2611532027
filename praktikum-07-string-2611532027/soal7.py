# Name: <AZANEL ADI PUTRO>
# NIM: <2611532027>
# Question 7

name = "Siti Aisyah".lower()
nim = "2610511023"

space = name.find(" ")

if space == -1:
    first_name = name
else:
    first_name = name[:space]

username = first_name + nim[-3:]
intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print(f"{'Name':<10}: {name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)


