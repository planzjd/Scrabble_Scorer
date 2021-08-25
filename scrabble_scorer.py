# inspired by https://exercism.io/tracks/javascript/exercises/etl/solutions/91f99a3cca9548cebe5975d7ebca6a85
#%%

old_point_structure = {
  1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
  2: ['D', 'G'],
  3: ['B', 'C', 'M', 'P'],
  4: ['F', 'H', 'V', 'W', 'Y'], 
  5: ['K'],             
  8: ['J', 'X'],
  10: ['Q', 'Z']
}

def old_scrabble_scorer(provided_word):
    word = provided_word.upper()
    letterPoints = ""

    for char in word:
        for point_value in old_point_structure:

            if char in old_point_structure[point_value]:
                letterPoints += 'Points for {char}: {point_value}\n'.format(
                    char=char, point_value=point_value)

    return letterPoints

old_scrabble_scorer("Hello")
# your job is to finish writing these functions and variables that we've named
# don't change the names or your program won't work as expected.

# Modify the provided initial_prompt() function to prompt the user to enter a word to score. 
# The function should return the text inputted by the user.

def initial_prompt():
    print("Let's play some Scrabble!\n")
    print("Enter a word to score: ")
    user_input = input()

    return user_input

# simple_scorer: Define a function that takes a word as a parameter and returns a numerical score. 
# Each letter within the word is worth 1 point.

def simple_scorer(word):
    score = 0
    for letter in word.lower():
        score += 1

    return score

simple_score = simple_scorer('wizard')
print(simple_score)

# vowel_bonus_scorer: Define a function that takes a word as a parameter and returns a score. 
# Each vowel within the word is worth 3 points, and each consonant is worth 1 point.
def vowel_bonus_scorer(word):
    word = word.upper()
    score = 0

    for char in word:
        if char in ['A', 'E', 'I', 'O', 'U']:
            score += 3
        else: score +=1 

    return score

# vowel_score = vowel_bonus_scorer('wizard')
# print(vowel_score)

def scrabble_scorer(word):
    score = 0
    
    for letter in word.lower():
        if letter in new_point_structure:
            score += new_point_structure[letter]

    return score 

# Finish writing the scoring_algorithms tuple. 
# It should be populated with three dictionary objects, one for each of the three scoring options. 
# Each dictionary should contain three keys: name, description, and scoring_function.
old_scrabble_scorer_dict = {
    'name': 'Scrabble',
    'description': 'The traditional scoring algorithm.',
    'score_function': scrabble_scorer
}
simple_scorer_dict = {
    'name': 'Simple Score',
    'description': 'Each letter is worth 1 point. A function with a parameter for user input that returns a score.',
    'score_function': simple_scorer
}
vowel_bonus_scorer_dict = {
    'name': 'Bonus Vowels',
    'description': 'Vowels are 3 pts, consonants are 1 pt.',
    'score_function': vowel_bonus_scorer
}

# Once you’ve written these scoring functions, organize all three of the scoring options 
# into a tuple called scoring_algorithms. 
# scoring_algorithms = (
#     old_scrabble_scorer,
#     simple_scorer,
#     vowel_bonus_scorer)

scoring_algorithms = (
    old_scrabble_scorer_dict,
    simple_scorer_dict,
    vowel_bonus_scorer_dict
)

# 0 = simple scorer 
# 1 = vowel
# 2= scrabble

def scorer_prompt():
    print('Which scoring algorithm would you like to use?')

    for index, algorithm in enumerate(scoring_algorithms):
        print(f'{index} - {algorithm["name"]}: {algorithm["description"]}')

    user_selection = int(input('Enter 0, 1, or 2:'))

    selected_score_algorithm_dict = scoring_algorithms[user_selection]

    return selected_score_algorithm_dict


# Write the rest of the transform() function. It will need to take a dictionary object as a parameter - 
# specifically the OLD_POINT_STRUCTURE object. Calling transform(OLD_POINT_STRUCTURE) 
# will return a dictionary with lowercase letters as keys. 
# The value for each key will be the points assigned to that letter.
def transform(provided_dict):
    new_dict = {}

    for (key, value) in provided_dict.items():
        for letter in value:
            new_dict[letter.lower()] = key

    return new_dict

new_point_structure = transform(old_point_structure)

# Use the old_scrabble_scorer() function provided to score the word provided by the user. 
# To do this, invoke old_scrabble_scorer() inside of the final function in the file, run_program(). 
# old_scrabble_scorer() will take the return value of initial_prompt(). Print the result.
def run_program():
    word = initial_prompt()

    selected_score_algorithm_dict = scorer_prompt()

    score = selected_score_algorithm_dict['score_function'](word)

    print(
        f'''

Your word is worth {score} points!!'''
    )


run_program()




