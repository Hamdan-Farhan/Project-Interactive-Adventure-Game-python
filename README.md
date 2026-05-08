
🧠 Decision Tree + Interactive Adventure Game

A simple project that combines Machine Learning (Decision Tree Classifier) with an interactive text-based adventure game.

🎯 Project Idea

This project uses a Decision Tree model to classify the outcomes of different player decisions, and then implements a fun interactive story where choices determine the ending.

🛠️ Technologies Used

Python
NumPy
Matplotlib
Scikit-learn (DecisionTreeClassifier)

🌳 Decision Tree Model

from sklearn.tree import DecisionTreeClassifier

Data
X: Represents player decisions
y: Represents outcomes of each decision path

📊 Decision Tree Visualization

plot_tree(model, feature_names=["Enter Forest", "Path Choice"], class_names=y, filled=True)

🎮 Interactive Adventure Game

The game is based on user input decisions:

1. Start
Enter the forest or return to the village

2. Inside the forest
Choose a path: Dark or Bright

3. Outcomes
Fight or run from a wolf 🐺
Find a treasure 💰 or get lost 🌲

▶️ Run the Project

python adventure.py

🧩 Features

-Interactive text-based game
-Practical use of Decision Trees
-Simple AI decision modeling
-Fun storytelling experience

🎯 Learning Goals

-Understand Decision Tree classifiers
-Practice basic Machine Learning concepts
-Build interactive Python applications
-Combine AI with storytelling


🏁 Result

A fun and educational project that blends machine learning + storytelling + interactivity in a simple way.
