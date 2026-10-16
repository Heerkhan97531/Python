# Step 1: Create an empty list to store the foods
favorite_foods = []

# Step 2: Use a loop to ask for 5 foods
for i in range(1, 6):
    food = input(f"Enter favorite food #{i}: ")
    favorite_foods.append(food)

# Step 3: Print the foods one by one
print("\nYour favorite foods are:")
for food in favorite_foods:
    print(food)



# Initialize the starting number and the sum accumulator
number = 1
sum = 0

# Loop runs for the first 10 natural numbers
while number <= 10:
    sum += number  # Add the current number to the total sum
    number += 1          # Move to the next number

# Print the final result
print("The sum of the first 10 natural numbers is:", sum)
