#Jackie_Merritt-Chp7_8_Lab1-7/1/2025

def main():
    
    file_name = input('What is the name of the file you wish to work with? ')
    print()
    valid_data = False
    while valid_data == False:
        
        l = input('Are you going to (r)ead the file or (w)rite the file? ')
        print()

        if l.lower() == 'r' or l.lower() == 'w':
            
            valid_data = True
            
        else:
            print("Invalid response, please input r or w")


    if l == 'w':
        write(file_name)
    if l == 'r':
        first = read(file_name)
        print("The content of the file is:\n")
        print(first)

#Input if write
def write(file_name):
    
    infile = open(file_name, 'w')
    
    first_name = input('Enter your first name: ')
    infile.write(first_name)
    infile.write(' ')

    last_name = input('Enter your last name: ')
    infile.write(last_name)
    infile.write('\n')

    street = input('Enter the street address: ')
    infile.write(street)
    infile.write('\n')

    city = input('Enter the city: ')
    infile.write(city)
    infile.write(', ')

    state = input('Enter the state: ')
    infile.write(state)
    infile.write(' ')

    zip_code = input('Enter the zip code: ')
    infile.write(zip_code)

    infile.close()

def read(file_name):
    try:
        infile = open(file_name, 'r')
    
        first = infile.read()
        return first

    except FileNotFoundError:
        print('Invalid, please enter an existing file name')

if __name__ == '__main__':
    main()
    
