import pandas as pd

# Load data from an Excel file
df = pd.read_excel("Personajes.xlsx")

def guess_character():
    # Start with all characters being possible
    active_df = df.copy()

    for col in df.columns[1:]:
        # Get the unique options still available based on the remaining characters.
        options = active_df[col].dropna().unique().tolist()
        print(f"\n{col}:")
        for i, opt in enumerate(options, start=1):
            print(f"{i}. {opt}")

        user_input = input("Please choose an option: ")
        while not user_input.isdigit() or int(user_input) - 1 not in range(len(options)):
            user_input = input("Invalid input. Please choose a valid option: ")

        chosen_option = options[int(user_input)-1]
        active_df = active_df[active_df[col] == chosen_option]

        # If there's only one row left in active_df, we've guessed the character!
        if len(active_df) == 1:
            print(f"El personaje es {active_df['Personajes'].iloc[0]}")
            break
    else:
        print("Could not guess the character based on the given answers.")
        
guess_character()




