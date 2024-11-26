def check(case_number):
    
    a, b = map(int, input("Enter two numbers separated by space: ").split())
    s = a + b  
    print(f"Case {case_number}: {s}")  

x = int(input("Enter the number of cases: "))

for i in range(1, x + 1):
    check(i)  


