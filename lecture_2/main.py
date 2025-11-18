# Determines user's life stage based on age
def generate_profile(current_age):
    if 0 <= int(current_age) <= 12:
        return "Child"
    elif 13 <= int(current_age) <= 19:
        return "Teenager"
    elif 20 <= int(current_age):
        return "Adult"
    return None


def main():
    # Gets user's full name
    print("Enter your full name")
    user_name = input()

    # Gets user's birth year
    print("Enter your birth year")
    birth_year_str = input()
    birth_year = int(birth_year_str)
    this_year = 2025
    current_age = this_year - birth_year

    # Gathers user's favorite hobbies
    hobbies = []
    while True:
        print ("Enter a favorite hobby or type 'stop' to finish")
        hobby_str = input()
        if hobby_str != "stop":
            hobbies.append(hobby_str)
        else:
            break

    life_stage = generate_profile(current_age)

    #Creates a dictionary 'user_profile' to store all the collected information
    user_profile = {
        "name": user_name,
        "age" : current_age,
        "stage" : life_stage,
        "hobbies" : hobbies
    }

    #Prints a summary of the user's profile
    print("---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if not user_profile["hobbies"]:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies: ({len(user_profile['hobbies'])})")
        for hobbie in user_profile["hobbies"]:
            print(f"- {hobbie}")
    print("---")
if __name__ == "__main__":
    main()