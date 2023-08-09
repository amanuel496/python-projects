############### Blackjack Project #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear # NOTE: import clear for the respective platform
import art

def blackJack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player = []
    computer = []
    playerSum = 0
    computerSum = 0
    count = 0

    while True:
        count += 1
        if count > 1:
            randChoice  = random.choice(cards)
            player.append(randChoice)
            randChoice  = random.choice(cards)
            computer.append(randChoice)
            playerSum = sum(player)
            computerSum = sum(computer)

            print(f"    Your cards: {player}, current score: {playerSum}")
            print(f"    Computer's first card: {computer[0]}")
            if 11 in player:
                if sum(player) > 21:
                    aceIndex = player.index(11)
                    player[aceIndex] = 1
                if sum(computer) > 21:
                    aceIndex = computer.index(11)
                    computer[aceIndex] = 1
            
            if playerSum > 21:
                print(f"    Your final hand: {player}, final score: {playerSum}")
                print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                print("You went over. You lose 😭")
                if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
                    clear()
                    blackJack()
                else:
                    break
            elif computerSum > 21:
                print(f"    Your final hand: {player}, final score: {playerSum}")
                print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                print("Opponent went over. You win 😀")
                if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                    clear()
                    blackJack()
                else:
                    break

            elif playerSum == 21 and computerSum == 21:
                print(f"    Your final hand: {player}, final score: {playerSum}")
                print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                print("It's a Draw")
                if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                    clear()
                    blackJack()
                else:
                    break
            elif playerSum == 21:
                print(f"    Your final hand: {player}, final score: {playerSum}")
                print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                print("You hit the Blackjack! You win 😀")
                if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                        clear()
                        blackJack()
                else:
                    break
            elif computerSum == 21:
                print(f"    Your final hand: {player}, final score: {playerSum}")
                print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                print("Computer hit the Blackjack! You lose 😭")
                if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                        clear()
                        blackJack()
                else:
                    break

            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    pass
                else:
                    if playerSum > computerSum:
                            print(f"    Your final hand: {player}, final score: {playerSum}")
                            print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                            print("You win 😀")
                            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                                clear()
                                blackJack()
                            else:
                                 break
                    elif playerSum < computerSum: 
                        print(f"    Your final hand: {player}, final score: {playerSum}")
                        print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                        print("You lose 😭")
                        if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                        else:
                                break
                    else:
                        print(f"    Your final hand: {player}, final score: {playerSum}")
                        print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                        print("It's a Draw")
                        if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                        else:
                            break
                break
        else:
            randChoice  = random.sample(cards, k=2)
            player.extend(randChoice)
            randChoice  = random.choices(cards, k=2)
            computer.extend(randChoice)
            playerSum = sum(player)
            computerSum = sum(computer)
            print(f"    Your cards: {player}, current score: {playerSum}")
            print(f"    Computer's first card: {computer[0]}")
            if 11 in player or 11 in computer:
                if playerSum == 21 and computerSum == 21:
                        print(f"    Your final hand: {player}, final score: {playerSum}")
                        print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                        print("It's a Draw")
                        if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                        else:
                            break
                elif playerSum == 21:
                    print(f"    Your final hand: {player}, final score: {playerSum}")
                    print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                    print("You hit the Blackjack! You win 😀")
                    if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                    else:
                        break
                elif computerSum == 21:
                    print(f"    Your final hand: {player}, final score: {playerSum}")
                    print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                    print("Computer hit the Blackjack! You lose 😭")
                    if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                    else:
                        break
                else:
                    if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                        pass
                    else:
                        if playerSum > computerSum:
                            print(f"    Your final hand: {player}, final score: {playerSum}")
                            print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                            print("You win 😀")
                            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                                clear()
                                blackJack()
                            else:
                                 break
                        elif playerSum < computerSum: 
                            print(f"    Your final hand: {player}, final score: {playerSum}")
                            print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                            print("You lose 😭")
                            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                                clear()
                                blackJack()
                            else:
                                 break
                        else:
                            print(f"    Your final hand: {player}, final score: {playerSum}")
                            print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                            print("It's a Draw")
                            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                                clear()
                                blackJack()
                            else:
                                break
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    pass
                else:
                    if playerSum > computerSum:
                            print(f"    Your final hand: {player}, final score: {playerSum}")
                            print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                            print("You win 😀")
                            if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                                clear()
                                blackJack()
                            else:
                                 break
                    elif playerSum < computerSum: 
                        print(f"    Your final hand: {player}, final score: {playerSum}")
                        print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                        print("You lose 😭")
                        if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                        else:
                                break
                    else:
                        print(f"    Your final hand: {player}, final score: {playerSum}")
                        print(f"    Computer's final hand: {computer}, final score: {computerSum}")
                        print("It's a Draw")
                        if input("Would you like to play again? Type 'y' or 'n': ") == 'y':
                            clear()
                            blackJack()
                        else:
                            break
                            
def main():
    response = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if response == 'y':
        clear()
        print(art.logo)
        blackJack()

main()
