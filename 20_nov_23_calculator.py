#Calculator in py

print("Welcome to Calculator")
print("1 = addition")
print("2 = substraction")
print("3 = multiplication")
print("4 = division")
a = int(input("Enter a number : "))
if a == 1:
    print("Enter 1st number : ")
    num_sum1 = int(input())
    print("Enter 2nd number : ")
    num_sum2 = int(input())
    print("Sum of these numbers is : ", num_sum1+num_sum2)

elif a == 2:
    print("Enter 1st number : ")
    num_sub1 = int(input())
    print("Enter 2nd number : ")
    num_sub2 = int(input())
    print("Difference of these numbers is : ", num_sub1-num_sub2)

elif a == 3:
    print("Enter 1st number : ")
    num_mul1 = int(input())
    print("Enter 2nd number : ")
    num_mul2 = int(input())
    print("Multiplication of these numbers is : ", num_mul1*num_mul2)

elif a == 4:
    print("Enter 1st number : ")
    num_div1 = int(input())
    print("Enter 2nd number : ")
    num_div2 = int(input())
    print("Division of these numbers is : ", num_div1/num_div2)

else:
    print("Invalid choice, please choose a number between 1, 2, 3 and 4")