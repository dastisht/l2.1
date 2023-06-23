a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a+b<c or a+c<b or c+b<a:
    print("Треугольника с такими сторонами не существует")
elif a== b and b==c:
    print("Треугольник равносторонний")
elif a == b or c==b or a==c:
    print('треугольник равнобедренный')
    
else:
    print("треугольник разносторонний")

 