def descending_order(n):
    try:
        digits = [int(digit) for digit in str(n)]
        sorted_digits = sorted(digits, reverse=True)
        sorted_number = int(''.join(map(str, sorted_digits)))
        return sorted_number
    except ValueError:
        print("Error: Please enter a valid number.")

while True:
    try:
        number = int(input("Enter Your Number: "))
        result = descending_order(number)
        print("DESCENDING ORDER:", result)
        break 
    except ValueError:
        print("Error: Please enter a valid number.")
