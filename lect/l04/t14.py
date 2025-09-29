# поелементне введення списку з клавіатури

N = int(input("кількість елементів в списку? "))

lst = []
for i in range(N):
    a = float(input(f"задайте {i}-й елемент "))
    lst.append(a)

print(lst)
