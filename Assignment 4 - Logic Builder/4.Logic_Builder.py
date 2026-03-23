# Assignment: Logic Builder
# Date: 17/02/2026
# Name: Yashaswi N

def fizz_buzz(n):
    """
    Returns 'Fizz', 'Buzz', 'FizzBuzz', or the number as a string
    based on divisibility by 3 and/or 5.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    print("=== Logic Builder: 1–50 Fizz/Buzz ===\n")

    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = fizz_buzz(i)
        print(result, end="  ", flush=True)  

        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1


    print("\n\n=== Occurrences ===")
    print(f"Fizz count: {fizz_count}")
    print(f"Buzz count: {buzz_count}")
    print(f"FizzBuzz count: {fizzbuzz_count}")

    input("\nPress Enter to exit...") 
if __name__ == "__main__":
    main()