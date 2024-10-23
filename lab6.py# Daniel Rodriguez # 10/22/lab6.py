# Atharv Gupta
# 10/23/2024
# Encode string of 8 numbers by shifting each digit up by 3
def encode(inputPassword):
    encodedPassword = ''
    for value in decodedPassword:
        encodedPassword = encodedPassword + str(int(value) + 3)
    return encodedPassword


def main():
  encodedPassword = None
    while True:
        print('Menu')
        print('------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        option = int(input('Please enter an option: '))

        if option == 1:
            inputPassword = input('Please enter your password to encode: ')
            encodedPassword = encode(inputPassword)
            print('Your password has been encoded and stored!')
        elif option == 2:
            # decodedPassword = decode(encodedPassword) - Add decode() function please
            # print(f'The encoded password is {encodedPassword}, and the original password is {decodedPassword}.')
        elif option == 3:
            break        
        print()
      
if __name__ == '__main__':
  main()
