import numpy as np

prumery = np.array([15.85, 15.85, 44.37, 57.05, 82.40])

print("Poloměry:")
polomery = prumery / 2
print(polomery)

print("Obvody:")
print(prumery * np.pi)

print("Obsahy:")
print(polomery * polomery * np.pi)

print("Rozdíl mezi největším a nejmenším, rozdělený na 25 kroků")
nejvetsi = np.max(prumery)
nejmensi = np.min(prumery)
print("Max a min: ", nejvetsi, nejmensi)

# for i in range(26, 10, -1):
#     kroky = np.linspace(nejmensi, nejvetsi, i)
#     # print(kroky)
#     for j in prumery:
#         if j == nejvetsi:
#             print(i)
#         else:
#             print(np.argmax(kroky>j), f"{kroky[np.argmax(kroky>j) - 1]:.2f}", end=" ")
#     print()

kroky = np.linspace(0, nejvetsi, 26, retstep=True, endpoint=False)
print(kroky)
#     # print(kroky)
# for j in prumery:
#     if j == nejvetsi:
#         print(22)
#     else:
#         print(np.argmax(kroky>j), f"{kroky[np.argmax(kroky>j)]:.2f}", end=" ")