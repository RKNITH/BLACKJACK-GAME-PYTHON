
import random 
print("welcome to the Blackjack game")

def random_choice_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card =random.choice(cards)
    return card

def calculate_score(card):
    if len(card)==2 and sum(card) >21:
        return 0
    
    if 11 in card and sum(card) >21:
        card.remove(11)
        card.append(1)
    return sum(card)

  
def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
 
    
is_game_over =False
user_card =[]
computer_card =[]

for _ in range(2):
    user_card.append(random_choice_card())
    computer_card.append(random_choice_card())


while not is_game_over:
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"user card :{user_card} and current score is: {user_score} ")
    print(f" computer first card is: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_want_to_add_card = input("do you want to add any other card. yes or no\n").lower()
        if user_want_to_add_card =="yes":
            user_card.append(random_choice_card())
        elif user_want_to_add_card =="no":
            is_game_over = True

        while computer_score != 0 and computer_score < 17:
            computer_card.append(random_choice_card())
            computer_score = calculate_score(computer_card)



print(f"   Your final hand: {user_card}, final score: {user_score}")
print(f"   Computer's final hand: {computer_card}, final score: {computer_score}")
print(compare_score(user_score, computer_score))

    
