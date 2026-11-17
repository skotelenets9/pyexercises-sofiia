# Name : Sofiia Kotelenets
# Group : A, CL05

# 1. In : 
# A CSV file with 30 marketing scenarios.
# The file uses commas and contains 14 columns. 
# Budget and reputation changes are signed integers. 

# 2. Process: 
# The program loads and shuffles scenarios. 
# Each day the plaer chooses A, B or C. 
# The budget and reputation change based on the choise. 
# The game stops after 10 days or if a gauge reaches zero. 

# 3. Out: 
# The plauer sees the final budget, repitation, result, title, and best and worst decisions. 
# results are saved in results.csv.

# 4. What could go wrong: 
# Invalid answer: ask the player again. 
# Budget or reputation reaches zero: end the game.
# Missing CSV file: display an error message. 

# My chosen feature: Difficulty.
# Easy mode starts with 15000 euros.
# Hard mode starts with 6000 euros.
# I chose this feature because it makes the game more challenging.


import csv
import random
from datetime import date

# Read the scenarios from the CSV file
def load_scenarios(filename):
    scenarios = []

    with open(filename, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)

        for row in reader:
            options = {}

            for letter in "ABC":
                options[letter] = (
                    row["Option" + letter],
                    int(row["Budget" + letter]),
                    int(row["Reputation" + letter]),
                    row["Feedback" + letter]
                )

            scenarios.append({
                "situation": row["Scenario"],
                "options": options
            })

    return scenarios


# Ask the player to choose a valid answer
def ask_choice(question, valid_answers):
    while True:
        answer = input(question).strip().upper()

        if answer in valid_answers:
            return answer

        print("Please enter a valid choice.")


# Update the budget and reputation
def apply_choice(budget, reputation, option):
    text, budget_change, reputation_change, feedback = option

    budget = budget + budget_change
    reputation = min(100, reputation + reputation_change)

    return budget, reputation


# Calculate the final title
def calculate_title(budget, reputation):
    score = reputation + budget // 200

    if score < 95:
        return score, "Eternal Intern"
    elif score < 120:
        return score, "Growth Hacker"
    elif score < 140:
        return score, "CMO Material"
    else:
        return score, "Viral Legend"


# Save the result of each game
def save_result(name, budget, reputation, title):
    import os

    new_file = not os.path.exists("results.csv")

    with open("results.csv", "a", newline="") as file:
        writer = csv.writer(file)

        if new_file:
            writer.writerow([
                "name", "budget", "reputation", "title", "date"
            ])

        writer.writerow([
            name, budget, reputation, title, date.today()
        ])


# Start the game
def play_game():
    print("Welcome to Survive the Quarter!")

    name = input("Enter your name: ").strip()

    # Choose difficulty
    difficulty = ask_choice(
        "Choose difficulty (E = Easy, H = Hard): ",
        ["E", "H"]
    )

    if difficulty == "E":
        budget = 15000
    else:
        budget = 6000

    reputation = 50

    # Load the scenarios
    try:
        scenarios = load_scenarios("scenarios_A.csv")
    except (FileNotFoundError, ValueError, csv.Error) as error:
        print("Could not load scenarios:", error)
        return

    if len(scenarios) < 10:
        print("Not enough scenarios to play.")
        return

    # Randomly select ten scenarios
    random.shuffle(scenarios)
    selected_scenarios = scenarios[:10]

    history = []

    # Play each day
    for day, scenario in enumerate(selected_scenarios, start=1):

        print("\n--- Day", day, "---")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/100")
        print(scenario["situation"])

        for letter, option in scenario["options"].items():
            print(letter + ":", option[0])

        choice = ask_choice(
            "Your choice (A, B or C): ",
            ["A", "B", "C"]
        )

        option = scenario["options"][choice]

        old_budget = budget
        old_reputation = reputation

        budget, reputation = apply_choice(
            budget, reputation, option
        )

        actual_change = reputation - old_reputation

        print(option[3])
        print("Budget change:", budget - old_budget)
        print("Reputation change:", actual_change)

        history.append((actual_change, day, option[0]))

        # Stop if a gauge reaches zero
        if budget <= 0 or reputation <= 0:
            print("\nGAME OVER!")
            break

    # Calculate the final result
    if budget <= 0 or reputation <= 0:
        title = "Fired"

        if budget <= 0:
            print("You were fired: no budget left!")
        if reputation <= 0:
            print("You were fired: reputation reached zero!")

    else:
        score, title = calculate_title(budget, reputation)

        print("\nQuarter survived!")
        print("Final score:", score)
        print(name, "your title is:", title)

    print("Final budget:", budget)
    print("Final reputation:", reputation)

    # Find the best and worst decisions
    best_move = max(history, key=lambda move: move[0])
    worst_move = min(history, key=lambda move: move[0])

    print("Best move: Day", best_move[1],
          best_move[2], "Reputation:", best_move[0])

    print("Worst move: Day", worst_move[1],
          worst_move[2], "Reputation:", worst_move[0])

    # Save the game result
    save_result(name, budget, reputation, title)

    print("Results saved in results.csv")


# Run the game
if __name__ == "__main__":
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print("\nGame interrupted.")
