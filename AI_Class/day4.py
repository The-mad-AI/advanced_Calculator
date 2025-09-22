x = 10
if x % 2 ==0 :
    print ("add zoj ast")
else:
    print("add fard ast")
    
for num in range(1, 101):
    if num % 3 ==0 and num % 5 == 0:
        print(num)
        
        
    
    
numbres = [1,2,3,4,5,6]
even_numbres = [num for num in numbres if num % 2 ==0]
odd_numbres = [num for num in numbres if num % 2 != 0]
sum_numbrs = sum(numbres)
avg_numbrs = sum(numbres) / len(numbres)
print(even_numbres)
print(odd_numbres)
print(sum_numbrs)
print(avg_numbrs)


a , b = 0 , 1
while b < 1000:
        a , b = b , a+b
print("",a)


numbers = int(input())
if numbres > 1 :
    for i in range(2 , int(numbres ** 0.5) + 1):
        if numbers % i ==0:
            print("add aval nist")
            break
    else:
        print("add aval ast")
else:
    print("add aval nist")