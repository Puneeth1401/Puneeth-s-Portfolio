import random
x=int(input("Enter the number you want to roll"))
# Define a function to simulate rolling a die
def roll_die():
    return random.randint(x,6)

# Define a function to calculate the probability of rolling a certain number
def probability_of_rolling(target, num_rolls):
    # Initialize the count of times we roll the target number
    count = 0

    # Roll the die num_rolls times and count the number of times we roll the target
    for i in range(num_rolls):
        roll = roll_die()
        if roll == target:
            count += 1

    # Calculate the probability of rolling the target number
    probability = count / num_rolls

    # Return the probability
    return probability
print(probability_of_rolling(6, x))

