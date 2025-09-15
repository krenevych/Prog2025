# визначити якій координатній чверті
# належить задана точка (x, y)

x, y = [float(el) for el in input("x, y = ").split()]

if x > 0 and y > 0:
    print("1")
else:
    if x < 0 and y > 0:
        print("2")
    else:
        if x < 0 and y < 0:
            print("3")
        else:
            if x > 0 and y < 0:
                print("4")
            else:
                print("десь на координатних осях")
