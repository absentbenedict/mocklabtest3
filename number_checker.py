def check_even_odd(num):#odd
    if (num%2 == 1):
        value = 1
    elif (num%2 ==0):#even
        value =  0
    return value
    
def get_user_input():
    num = int(input(f"Please input your number:"))
    return num

def main():
    num = get_user_input()
    value = check_even_odd(num)
    if value == 0 :
        print("The number is even") 
    elif value == 1:
        print("The number is odd")

if __name__ == '__main__':
    main()   