s = input()
d = {
    "cat" : "meo",
    "dog" : "cho",
    "horse" : "ngua",
    "turtle" : "rua",
    "cow" : "bo"
}

if s in d:
    print(d[s])
else:
    print("KHONG TIM THAY")