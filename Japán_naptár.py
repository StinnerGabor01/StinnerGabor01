év = int(input(""))

if év>= 1984 and év<=2043:
    if év %10== 4 or év %10 ==5:
        print("zöld")
    elif év %10== 6 or év %10 ==7:
        print("piros")
    elif év %10== 8 or év %10 ==9:
        print("sárga")
    elif év %10== 0 or év %10 ==1:
        print("fehér")
    elif év %10== 2 or év %10 ==3:
        print("fekete")
else:
    print("Az év nem megfelelő")