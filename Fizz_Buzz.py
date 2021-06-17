# Write a program that prints the numbers from 1 to 100. 
# For multiples of three (3), print "Fizz"
# and for multiples of five (5) print "Buzz".

def main():
    i = 1
    while i <= 100:
        if i % 15 == 0:
            print(str(i).zfill(3) + ": ", end = '')
            print("Fizz Buzz")
        elif i % 3 == 0:
            print(str(i).zfill(3) + ": ", end = '')
            print("Fizz")
        elif i % 5 == 0:
            print(str(i).zfill(3) + ": ", end = '')
            print("Buzz")
        else:
            print(str(i).zfill(3) + ":")
        i += 1

main()