d = {
    "An" : [8,9,7],
    "Binh": [6,7,5],
    "Chau" : [9,8,10]
}
for x,y in d.items():
    print(x, end = " ")
    sum = 0
    for i in y:
        sum += int(i)
    print(sum)
