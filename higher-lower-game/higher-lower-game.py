#TODO-1: Import random, clear art and game_data modules
import random
from replit import clear
import art
import game_data

#TODO-8: Define compareNumOfFollowers(user1, user2)
def compareNumOfFollowers(user1, user2):
    if user1["follower_count"] > user2["follower_count"]:
        return 'A'
    else:
        return 'B'

#TODO-2: Define higherLowerGame() 
def higherLowerGame():
    print(art.logo)
    #TODO-4: Load the game data into a list
    gameData = game_data.data
   # print(gameData[0])
    #TODO-5: Get the size of the list
    gameDataSize = len(gameData)
    #print(gameDataSize)
    #TODO-6: Randomly select two numbers from range(gameDataSize) and assign them to user1 and user2
    randChoice = random.sample(range(gameDataSize),2)
    user1 = gameData[randChoice[0]]
    user2 = gameData[randChoice[1]]
    print(user1)
    print(user2)
    #TODO-7: Create isGameOver var and assign False
    isGameOver = False
    #TODO-13: Create a count var
    score = 0
    #TODO-9: Create a while loop that checks if the game is over
    while not isGameOver:
        #TODO-10: Call  compareNumOfFollowers() to compare the 2 users and assign the returning value to correctAnswer var
        correctAnswer = compareNumOfFollowers(user1, user2)
        print(correctAnswer)
        #TODO-11: Prompt the player who has the more followrs between the IG users
        #         giving A and B options    
        print(f"Compare A: {user1['name']}, a {user1['description']}, from {user1['country']}.")
        print(art.vs)
        print(f"Against B: {user2['name']}, a {user2['description']}, from {user2['country']}.")
        #isGameOver = True
        playerChoice = input("Who has more followers? Type 'A' or 'B': ")
        #TODO-12: Compare if the player got the right answer
        if playerChoice == correctAnswer:
            score += 1
            print(f"You're right! Current score: {score}.")
            if correctAnswer == "B":
                user1 = user2
            user2 = gameData[random.randint(0,gameDataSize)]
        else:
            isGameOver = True
            print(f"Sorry, that's wrong. Final score: {score}")
#TODO-3: Call higherLowerGame() and clear()
higherLowerGame() 
#clear()
