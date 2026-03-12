numbers = [1, 2, 3, 4]
square_dict = {}

for n in numbers:
    square_dict[n] = n**2

print(square_dict)



numbers = [1,2,3,4]
square_dict = {n: n**2 for n in numbers}
print(square_dict)


numbers = [1,2,3,4,5,6]
even_square = {n: n**2 for n in numbers if n%2==0}
print(even_square)


n=[4,5,6,7]
odd_square= {b: b**2 for b in n if b%2!=0}
print(odd_square)

kunal=[1,2,3,4,5,6,7,8,9]
jyotir={n:n**2 for n in kunal if n%2==0}
print(jyotir)