a1 = input("input nilai boolean-1 (True/False): ").strip().lower() =="true"
a2 = input("input nilai boolean-2 (True/False): ").strip().lower() =="true"

print("\nA1 =", a1)
print("A2 =", a2)

hasil = a1 and a2
print("\nKonjungsi (AND)")
print("A1 AND A2 = ", hasil)

hasil = a1 or a2
print("\nDisjungsi (OR)")
print("A1 OR A2 = ", hasil)

hasil = not a1
print("\nNegasi A1 (NOT)")
print("NOT A1 = ", hasil)

hasil = not a2
print("\nNegasi A2 (NOT)")
print("NOT A2 = ", hasil)

hasil = a1 != a2
print("\nDisjungsi Exclusif(OR)")
print("A1 XOR A2 = ", hasil)