# Atharv Gupta
# 10/23/2024
# Encodes user's password by shifting each number by 3
def encode(inputPassword):
    encodedPassword = ""
    for i in range(0, len(inputPassword), 0)
        encodedPassword = encodedPassword + str(int(inputPassword[i]) + 3)
    return encodedPassword

#TBD - def decode():

def main():
  encodedPassword = None
    
    while True:
        print('Menu')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter the option choice to perform: '))
        
        if option == 1:
            inputPassword = input('Please enter the password desired to be encoded: ')
            encodedPassword = encode(inputPassword)
            print('Your password has been encoded and stored!')
        elif option == 2:
            # decodedPassword = decode(encodedPassword) - Add decode() function please
            # print(f'The encoded password is {encodedPassword}, and the original password is {decodedPassword}.')
        elif option == 3:
            break        
        print()
        
    print("Thank you for using our program and have a great day!)

      
if __name__ == '__main__':
  main()
