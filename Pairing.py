def formatting(a, b):
    temp1 = a * b
    temp2 = a + b
    if temp1 % 2 == 0 and temp2 % 2 > 0:
        print(a, ",", b)


while True:
    print("Enter the elements:")
    try:
        my_list = []
        while True:
            my_list.append(int(input()))
    except:
        for i in range(0, len( my_list)):
            if i != len(my_list):
                for j in range(i + 1, len( my_list)):
                    formatting(my_list[i], my_list[j])
    print("\nDo you want to exit? [y/n]")
    if input() == "y":
        break
    print("\n")