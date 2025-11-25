import random
def category_waste_quiz():
    # --- Game Data ---
# Dictionary containing waste items and their correct disposal categories.
# Categories: 1=Recycling (blue), 2=Compost (green), 3=Landfill (black/grey)
   
    wastes_type = {"Aluminum Can (Rinsed)": 1,
    "Plastic Milk Jug": 1,
    "Clean Cardboard Box (Flattened)": 1,
    "Newspaper": 1,
    "Glass Jar (Rinsed)": 1,
    "Coffee Grounds": 2,
    "Banana Peel": 2,
    "Apple Core": 2,
    "Yard Waste (Leaves, Grass)": 2,
    "Pizza Box (Greasy)": 3,
    "Plastic Bag/Wrap": 3,
    "Broken Ceramic Plate": 3,
    "Styrofoam Container": 3,
    "Used Napkin/Paper Towel": 3,
    "Disposable Diaper": 3,  }
    # 2. Get the list of items using d.keys [L]
    # 'L' is a list of all item names (keys) from the dictionary.
    L = list(wastes_type.keys())
    # 3. Maintain a score variable initialized with zero.
    score = 0
    print('welcome to the waste category quiz')
    print("Your goal is to correctly guess the category of the item displayed.")
    print("Categories are: 1=Recycling (blue), 2=Compost (green), 3=Landfill (black/grey)")
    print("The game ends when you make an incorrect guess.")
    print("---")
    

    #start the game loop 
    while True:
        #choose randomm item from the above list
        random_item = random.choice(L)
        
        # Get the correct category for comparison later.
        correct_category = wastes_type[random_item]
        
        #display to the user
        print(f"\nWhat is the category of: {random_item}?")

        #user input
        player_guess = int(input('enter category'))

        # 8. Match the user input with category of the item
        if player_guess == correct_category:
            # if it matches properly, increase the score
            score += 1
            print(f"Correct! Category: {correct_category}. Your current score is **{score}**.")
            
            # Remove the item so it doesn't get asked again
            L.remove(random_item)
            
            # Check if all items have been guessed
        
        else:
            # else break the loop and display the total score.
            print(f"\nIncorrect! The correct category for **{random_item}** was **{correct_category}**.")
            break # Exit the game loop
            
    # Display the final score outside the loop
    print(f"\nGame Over! Your final score is **{score}**.")

# Execute the function to start the game
if __name__ == "__main__":
    category_waste_quiz()
        
