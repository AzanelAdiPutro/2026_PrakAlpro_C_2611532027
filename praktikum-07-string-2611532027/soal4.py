# Name: <AZANEL ADI PUTRO>
# NIM: <2611532027>
# Question 4
phone = "082611532027"

masked = phone[:4] + "*" * (len(phone) - 7) + phone[-3:]

print(masked)