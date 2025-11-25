# 5.2 statement.md

##  Problem Statement

Many individuals struggle with correctly **sorting household waste** into the appropriate categories: **Recycling**, **Compost**, and **Landfill**. This confusion leads to high rates of contamination in recycling and composting streams, reducing their effectiveness and increasing the amount of waste sent to landfills. The problem is a lack of readily available, engaging, and simple educational tools to reinforce correct waste disposal knowledge.

---

##  Scope of the Project

The project is a **single-player interactive quiz application** called "Waste Category Quiz."

* **In Scope:**
    * A command-line interface (CLI) game developed in **Python**.
    * A predefined, fixed set of household waste items and their disposal categories.
    * The core game loop: present a random item, accept user input for the category (1, 2, or 3), check the answer, update the score, and remove the item from the pool.
    * **Sudden-death gameplay**: the game ends immediately upon the first incorrect guess.
    * Displaying the final score upon game termination.


---

##  Target Users

The primary target users are individuals seeking to improve their **waste sorting knowledge** in a fun, quick, and engaging format.

* **General Public/Householders:** People looking for a simple tool to test and reinforce their understanding of local recycling, composting, and trash rules.
* **Students/Educators:** Elementary or middle school students and teachers looking for a game to teach basic environmental awareness and waste management principles.
* **New Residents:** Individuals who have recently moved to an area with different waste disposal guidelines and need to quickly learn the local sorting rules (as approximated by the quiz).

---

##  High-Level Features

* **Interactive Quiz Interface:** A simple command-line interface that clearly prompts the user with a waste item.
* **Category Definitions:** Clear presentation of the three disposal categories at the start of the game: **1=Recycling (blue)**, **2=Compost (green)**, **3=Landfill (black/grey)**.
* **Random Item Selection:** Items are chosen randomly from a predefined list to ensure variety in each game session.
* **Real-time Scoring:** The player's score is immediately updated and displayed after each correct answer.
* **Sudden-Death Logic:** The game instantly terminates when the user inputs an incorrect category, reinforcing the importance of accuracy.
* **Preventing Repetition:** Items that have been correctly categorized are removed from the pool, ensuring the user is not asked the same question twice in one session.
