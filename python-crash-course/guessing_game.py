secret_word = "lion"

guessed_word = ""
try_count = 0
count_limit = 3
out_of_count = False


while guessed_word != secret_word and not out_of_count:
    if try_count < count_limit:
        guessed_word = input("Guess the secret word: ")
        try_count += 1
    else:
        out_of_count = True

if out_of_count:
    print("Out of count")
else:
    print("you won!")    

# while guessed_word != secret_word:
#     if try_count >= 3:
#         print("Too many attempts! Game over.")
#         break
#     guessed_word = input("Guess the secret word: ")
#     try_count += 1
    
# if try_count > 3:
#     print("Out of guesses")
# else: 
#     print("You won!")        