# #Day12
#
# import random
#
# number = random.randint(1, 100)
#
# level = input("Welcome to the Number Guessing Game! \n"
#               "I'm thinking of a number between 1 and 100. \n"
#               f"Pssst, the correct answer is {number} \n"
#               "Choose a difficulty. Type 'easy' or 'hard':")
#
# if level == 'hard':
#     number_of_attempts = 5
# else:
#     number_of_attempts = 10
#
#
# def game():
#     global number_of_attempts, number
#     while number_of_attempts > 0:
#         print(f"You have {number_of_attempts} remaining to guess the number.")
#         answer = input("Make a guess: ")
#         if int(answer) < number:
#             print("Too low.")
#         elif int(answer) > number:
#             print("Too high.")
#         number_of_attempts -= 1
#         if int(answer) == number:
#             print(f"You got it! The answer was {number}.")
#             return
#     if number_of_attempts == 0:
#         print("You've run out of guesses, you lose.")
#
#
# game()

# Day 13

############DEBUGGING#####################

# Describe Problem
# def my_function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You got it")
#
#
# my_function()

# Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millenial.")
# elif year >= 1994:
#     print("You are a Gen Z.")


# # Fix the Errors
# age = input("How old are you?")
# if int(age) > 18:
#     print(f"You can drive at age {age}.")


# #Print is Your Friend
#
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# # Use a Debugger
# def mutate(a_list):
#     b_list = []
#     for item in a_list:
#         new_item = item * 2
#         b_list.append(new_item)
#     print(b_list)
#
#
# mutate([1, 2, 3, 5, 8, 13])
import random
import pyautogui

from art import logo, vs
from game_data import data

is_game_over = False
score = 0
random_A = random.randint(0, len(data) - 1)
random_B = random_A
answer = ""


def game():
    global score, is_game_over, answer, random_B, random_A
    while data[random_A]['follower_count'] == data[random_B]['follower_count']:
        random_B = random.randint(0, len(data) - 1)
    print(logo)
    print(f"Your score is: {score}")
    print(f"Compare A: {data[random_A]['name']}, a {data[random_A]['description']}, from {data[random_A]['country']}.")
    print(vs)
    print(f"Against B: {data[random_B]['name']}, a {data[random_B]['description']}, from {data[random_B]['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ")
    if (answer == 'A' and data[random_A]['follower_count'] > data[random_B]['follower_count']) or \
       (answer == 'B' and data[random_A]['follower_count'] < data[random_B]['follower_count']):
        score += 1
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        is_game_over = True
    pyautogui.hotkey('CTRL', 'l')
    random_A = random_B


while not is_game_over:
    game()
