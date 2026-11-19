# Name: <AZANEL ADI PUTRO>
# NIM: <2611532027>
# Question 3

#A
text = "Informatika"

print(text[10])
print(text.upper())
print(text[0:20])
#B
text = "Algoritma dan Pemrograman"

count = 0

for char in text:
    if char in "aiueoAIUEO":
        count += 1

print("Vowels:", count)