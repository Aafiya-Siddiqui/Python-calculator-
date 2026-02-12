def add(x,y):return x+y
def substract(x,y):return x-y
def multiply(x,y):return x*y
def divide(x,y):
    if y==0:
        return "DIVIDE BY ZERO"
    return x/y

def main():
    print("*****PYTHON CLI CALCULATOR*****")
    while True:
        print("1.ADDITION(+):")
        print("2.SUBSTRACTION(-):")
        print("3.MULTIPLICATION(*):")
        print("4.DIVISION(/):")
        print("5.EXIT:")
        choice=input("Enter your choice(1-5):")
        if choice == '5':
            print("Exiting.Have a great day!")
            break
        if choice in ('1','2','3','4'):
            try:
                num1=float(input("Enter 1st number:"))
                num2=float(input("Enter 2nd number:"))
            except ValueError:
                print("Invalid input,please enter only numeric value.")
                continue
            if choice =='1':
                print(f"Result:{num1}+{num2}={add(num1,num2)}")
            elif choice=='2':
                print(f"Result:{num1}-{num2}={substract(num1,num2)}")
            elif choice =='3':
                print(f"Result:{num1}*{num2}={multiply(num1,num2)}")
            elif choice =='4':
                print(f"Result:{num1}/{num2}={divide(num1,num2)}")
            else:
                print("Invalid selection,please try again")
if __name__ == "__main__":
    main()
                
                       
        
