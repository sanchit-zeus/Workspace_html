#get guess
def get_guess():
    return list(input("WHta is your guess?"))


#generate computer code 123
def generate_code():
    digits=[str(num)for num in range (10)]

    #shuffle the digits
    #then grab the first three
    random.shuffle(digits)
    #then grab first three
    return digits[:3]
    


#generate the clue
def generate_clues(code,user_guess):
    if user_guess==code:
        return "Code cracked!"
    clues=[]
    for ind,num in enumerate(user_guess):
        if num==code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("close")
    if clues==[]:
        return ["nope"]
    else:
        return clues


#run game logic
print("Welcome Code Breaker!")
secret_code=generate_code()
clue_report=[]
while clue_report !="Code Cracked!":
    guess=get_guess()

clue_report=generate_clues(guess,secre_code)
print("here is the result of the guess: ")
for clue in clue_report:
    print(clue)
