from sklearn.tree import DecisionTreeClassifier, plot_tree
import numpy as np
import matplotlib.pyplot as plt

# Prepare the data: Features are the decisions, and the targets are the adventure outcomes
X = [
    [0, 0],  # Option 1: Enter the forest, Option 2: Dark path
    [0, 1],  # Option 1: Enter the forest, Option 2: Bright path
    [1, 0],  # Option 1: Return to the village
    [1, 1],  # Option 1: Return to the village
]

# The results based on choices (what happens after the decision)
y = [
    "You encountered a wild wolf! Fight or Run?",  # Enter forest and choose dark path
    "You find a bright river! Cross or Follow?",  # Enter forest and choose bright path
    "You returned safely to the village. Maybe next time!",  # Return to the village
    "You returned safely to the village. Maybe next time!",  # Return to the village
]

# Create a Decision Tree model
model = DecisionTreeClassifier(criterion="gini", max_depth=3, random_state=42)
model.fit(X, y)

# Plot the Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=["Enter Forest", "Path Choice"], class_names=y, filled=True)
plt.title("Decision Tree Adventure Story")
plt.show()

# Interactive adventure game
def start_adventure():
    print("Welcome to the Interactive Adventure Story!")
    print("You stand at the edge of a mysterious forest. Legends say there's a treasure hidden inside.")
    
    # The first choice: enter the forest or return to the village
    choice1 = input("Do you want to ENTER the forest or RETURN to the village? (Enter/Return): ").strip().lower()

    if choice1 == "enter":
        path_choice()  # Proceed to the next decision if the player enters the forest
    elif choice1 == "return":
        print("You decide to return to the village. Maybe another day, you'll seek adventure!")
        end_adventure()  # End the adventure if the player returns to the village
    else:
        print("Invalid choice. Please try again.")
        start_adventure()

def path_choice():
    print("\nYou step into the forest. The air is thick, and the trees whisper secrets.")
    
    # The second choice: choose between dark or bright path
    choice2 = input("There are two paths: a DARK one and a BRIGHT one. Which path do you choose? (Dark/Bright): ").strip().lower()

    if choice2 == "dark":
        dark_path()  # Proceed to dark path decision
    elif choice2 == "bright":
        bright_path()  # Proceed to bright path decision
    else:
        print("Invalid choice. Please try again.")
        path_choice()

def dark_path():
    print("\nYou walk along the dark path, hearing strange noises around you.")
    
    # The third choice: fight the wolf or run away
    choice3 = input("Suddenly, a wild wolf appears! Do you FIGHT it or RUN away? (Fight/Run): ").strip().lower()

    if choice3 == "fight":
        print("\nYou bravely fight the wolf and manage to scare it away. You find a hidden treasure!")
        end_adventure()  # End the adventure after finding treasure
    elif choice3 == "run":
        print("\nYou run back to the forest entrance, safe but empty-handed. Maybe next time you'll find the treasure!")
        end_adventure()  # End the adventure after running away from the wolf
    else:
        print("Invalid choice. Please try again.")
        dark_path()

def bright_path():
    print("\nYou walk along the bright path, feeling the sun's warmth on your face.")
    
    # The fourth choice: cross or follow the river
    choice4 = input("You find a sparkling river. Do you CROSS it or FOLLOW it? (Cross/Follow): ").strip().lower()

    if choice4 == "cross":
        print("\nYou cross the river and discover a hidden cave. Inside, you find the treasure chest! You win!")
        end_adventure()  # End the adventure after finding treasure
    elif choice4 == "follow":
        print("\nYou follow the river but get lost in the forest. Eventually, you find your way out, but the treasure remains hidden.")
        end_adventure()  # End the adventure after getting lost
    else:
        print("Invalid choice. Please try again.")
        bright_path()

def end_adventure():
    print("\nThank you for playing the Interactive Adventure Story! The end.")
    replay = input("Do you want to play again? (Yes/No): ").strip().lower()
    
    # Ask the player if they want to replay
    if replay == "yes":
        start_adventure()  # Restart the adventure if the player wants to play again
    else:
        print("Goodbye, adventurer!")  # End the game if the player doesn't want to play again

# Start the game
start_adventure()
