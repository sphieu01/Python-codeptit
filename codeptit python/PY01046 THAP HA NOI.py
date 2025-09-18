def TowerOfHanoi(n, A, B, C): # a den c va lay b lam moc
    if (n > 0):
        TowerOfHanoi(n-1, A , C ,B)
        print(A ,"->", C)
        TowerOfHanoi(n-1, B, A, C)#b den c va lay a lam moc

n = int(input())
TowerOfHanoi(n, "A", "B", "C")