# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main
main()


import keyword

print(keyword.kwlist)


s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)


message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)


help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

print(help_message)

name = 'John'
message = f'Hi {name}'
print(message)


greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

value = input('Enter a value:')
print(value)

price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = int(price) * int(tax) / 100
print(f'The net price is ${net_price}')



