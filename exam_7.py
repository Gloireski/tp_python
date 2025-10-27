cn_p, cn_u = 0, 0

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for it in numbers:
    if it%2 == 0:
        cn_p+=1
    else:
        cn_u+=1
print('Nombre de nombres pairs : ',cn_p)
print('Nombre de nombres impairs : ',cn_u)