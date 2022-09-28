
'''
print(f"\n Welcome to the special recruitment program, please answer the following questions:")


name                =     input("What's your name? ")                           #string
age                 = int(input("How old are you? "))                           #integer
years_of_experience = int(input("How many years of expericence do you have? ")) #integer
'''

# print(f"\n Skils: \n 1. Python \n 2. C++ \n 3. Javascript \n 4. Juggling \n 5. Running \n 6. Eating \n")




# This function returns a list of skills.
# This is the list that the user will choose from
# Add at least 3 random skills for the user to select from
from ast import Return


def get_skills():
    skills = ["Python", "C++", "Javascript", "Juggling", "Running", "Eating"]
    return skills


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    print()
    for index, skill in enumerate(skills, 1):
        print(f"{index}. {skill}")
        





# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    show_skills(skills)
    user_skills = []
    skill_1 = input(f"\nChoose a skill from above by entering its number:")
    if skill_1 in skills:
        user_skills.append(skill_1)

        skill_2 = input("Choose another skill from above by entering its number: ")
    if skill_2 in skills:
        user_skills.append(skill_2)

    return  user_skills
   


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    
    cv = {}
    cv["name"]                 =     input("What's your name? ")                           #string
    cv["age"]                  = int(input("How old are you? "))                           #integer
    cv["years_of_experience"]  = int(input("How many years of expericence do you have? ")) #integer
    cv["skills"]               = get_user_skills(skills)
 
    return cv


# This function checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    if 25 <= cv["age"] <= 40:
        if cv["years_of_experience"] > 3:
            if  desired_skill in cv["skills"]:
                return True
    else:
        return False


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    print(f"\n Welcome to the special recruitment program, please answer the following questions:\n")
    skills = get_skills()
   
    cv = get_user_cv(skills)

    if check_acceptance(cv, skills[2]):
        print(f"You are accepted, {cv['name']}!")
    else:
        print("You are rejected! , good luck.")
 




if __name__ == "__main__":
    main()
