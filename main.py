import random


def list_to_string(word):
    temporary = ""
    for element in word:
        temporary += element
    return temporary


def checking_occurrences():
    if random_word.count(guess) > 1:
        for element in random_word:
            if element is guess:
                occurrences = [i for i, element in enumerate(random_word) if element == guess]
                for j in occurrences:
                    covered_letters[j] = element
    else:
        covered_letters[random_word.index(guess)] = random_word[random_word.index(guess)]


words = ['spoon', 'table', 'borowkarz', 'tissue', 'bottle', 'laptop', 'pszczola']


random_word = words[random.randint(0, len(words)-1)]

random_word = list(random_word)

chances = 5
number_of_guesses = 0
uncovered_letters = [random_word[0], random_word[len(random_word)-1]]
covered_letters = []

for letter in random_word:
    covered_letters.append("_")

covered_letters[0] = uncovered_letters[0]
covered_letters[len(covered_letters)-1] = uncovered_letters[1]

while number_of_guesses < chances:
    for letter in range(0, len(random_word)):
        print(f'{covered_letters[letter]}', end=" ")

    guess = input("Type a letter: ")
    if guess in random_word:
        print(f'Excellent! Letter "{guess}" is in the word!')
        checking_occurrences()

    elif guess not in random_word:
        number_of_guesses += 1
        print(f'Too bad :( Letter "{guess}" is not in this word. You have {chances-number_of_guesses} tries left.')

    if "_" not in covered_letters:
        print(f"Congrtulations! You won! The correct word was '{list_to_string(random_word)}'")
        break

    elif number_of_guesses == chances:
        print(f"'You lose! Correct word was '{list_to_string(random_word)}'")

