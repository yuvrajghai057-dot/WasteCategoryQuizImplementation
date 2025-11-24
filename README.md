# ♻️ Waste Category Quiz

A simple, command-line Python game designed to test your knowledge of waste sorting and disposal. Sharpen your recycling skills by correctly assigning common household items to the right bin!

## 🎯 How to Play

The game is a **streak challenge**. You are presented with a random waste item and must input the correct category number.

* **1:** **Recycling** (Blue Bin)
* **2:** **Compost** (Green Bin)
* **3:** **Landfill** (Black/Grey Bin)

The game continues until you make one incorrect guess, or successfully categorize all items.

## 🚀 Getting Started

### Prerequisites

You only need **Python 3** installed on your system.

### Running the Game

1.  **Clone the Repository** (assuming you've uploaded the code):
    ```bash
    git clone [YOUR_GITHUB_REPO_URL]
    cd waste-category-quiz
    ```

2.  **Execute the Script:**
    ```bash
    python waste_quiz.py
    ```

## 📊 Game Data & Categories

The quiz uses the following default mapping for its 15 items: 

| Category | Number | Examples |
| :--- | :----: | :--- |
| **Recycling** | 1 | Aluminum Can, Plastic Milk Jug, Glass Jar |
| **Compost** | 2 | Coffee Grounds, Banana Peel, Apple Core |
| **Landfill** | 3 | Greasy Pizza Box, Plastic Bag/Wrap, Disposable Diaper |

## ⚙️ Scoring

* **Correct Guess:** Score increases by 1. The item is removed and won't be asked again.
* **Incorrect Guess:** The game ends immediately, and your final streak score is displayed.

---
