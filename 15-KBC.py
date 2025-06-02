name=input("Enter your name:")
print(f"Hello, {name}. Welcome to to the game where correct answers rewared you with a dollar.")

wel=input("Are you ready")


questions = [
    [" What is the largest lake in the world?",
     ["a.Caspian Sea", "b.Baikal", "c.Lake Superior", "d.Ontario"],
    "b"
    ],


    ["Which planet in the solar system is known as the “Red Planet”?",
     ["a.Venus", "b.Earth", "c.Mars", "d.jupiter"],
    "c"],


    ["4. Who wrote the novel “War and Peace”?",
     ["a.Anton Chekhov", "b.Fyodor Dostoevsky", "c.Leo Tolstoy", "d.Ivan Turgenev"],
    "c"],


    ["5. What is the capital of Japan?",
     ["a.Beijing", "b.Tokyo", "c.Seoul", "d.Bangkok"],
    "b"],


    ["6. Which river is the longest in the world?",
     ["a.Amazon", "b.Mississippi", "c.Nile", "d.Yangtze"],
    "c"],



]


Money=100

for q in questions:
    print ("\n" + q[0])


    for option in q[1]:
        print(option)
    userinput=input("Enter the correction option. A/B/C/D")

    if userinput==q[2]:
        Money*=2
        print(f"correct answer. you money is now :{Money}")
    else:
        print("wrong answer. Correct answer was",q[2],"\n")
        print("You lost all your money ")
        Money = 0
        break

print(f"\nGame Over, {name}! You won: ${Money}")


play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again != "yes":
        print("Thanks for playing! See you next time ")
