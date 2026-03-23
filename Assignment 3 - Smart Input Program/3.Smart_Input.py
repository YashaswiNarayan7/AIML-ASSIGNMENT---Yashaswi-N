# Assignment: Smart Input Program
# Date: 12/02/2026
# Name: Yashaswi N

def main():
    print("=== Welcome to the Smart Input Program! ===\n")

    try:
        name = input("Enter your name: ").strip()
        age_input = input("Enter your age: ").strip()

        while not age_input.isdigit():
            print("Please enter a valid number for age.")
            age_input = input("Enter your age: ").strip()
        age = int(age_input)

        hobby = input("Enter your hobby: ").strip()

        if age < 13:
            category = "Child"
        elif age < 20:
            category = "Teenager"
        elif age < 60:
            category = "Adult"
        else:
            category = "Senior"

        print("\n=== Personalized Message ===")
        print(f"Hello {name}! You are a {category} and it's great that you enjoy {hobby}.\n")

    except Exception as e:
        print("An error occurred:", e)

    input("Press Enter to exit...") 
if __name__ == "__main__":
    main()