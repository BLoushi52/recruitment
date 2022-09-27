
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
def get_skills():
    skills = ["Python", "C++", "Javascript", "Juggling", "Running", "Eating"]
    return skills


# This function pretty prints the skills to the user
# It takes the list of skills as an argument and prints them numbered
# This function doesn't return anything
def show_skills(skills):
    num = 0
    for skill in skills:
        num = num + 1
        print(f"{num}. {skill}")
        





# Shows the available skills and have user pick from them two skills
# HINT: Use previous built functions to show the skills
# For example, if the user enters 1, the first skill in your list of skills will be added to the list
# Return a list of the two skills that the user inputted
def get_user_skills(skills):
    user_skills = []
    skill_1 = input("Choose a skill from above by entering its number:")
    if skill_1 in skills:
        user_skills.append(skill_1)

        skill_2 = input("Choose another skill from above by entering its number: ")
    if skill_2 in skills:
        user_skills.append(skill_2)

    return  user_skills
   


# This function will get the user's cv from their inputs
# HINT: Use previous built functions to get the skills from the user
def get_user_cv(skills):
    user_cv = {}
    user_cv["name"]                 =     input("What's your name? ")                           #string
    user_cv["age"]                  = int(input("How old are you? "))                           #integer
    user_cv["years_of_experience"]  = int(input("How many years of expericence do you have? ")) #integer
    user_cv["skills"]               = get_user_skills(skills)
 
    return user_cv


# This functions checks if the cv is acceptable or not, by checking the age, experience and skills and return a boolean (True or False) based on that
def check_acceptance(cv, desired_skill):
    ...


def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    show_skills(get_skills())
    get_user_skills(get_skills())



if __name__ == "__main__":
    main()
