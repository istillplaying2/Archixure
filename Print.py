import random

# Generate a random number between 1 and 100
randomNumber = random.randint(1, 100)

# Check if the number is even or odd
if randomNumber % 2 == 0:
  print("The number is even.")
else:
  print("The number is odd.")

# Print a random color
color = random.choice(["red", "green", "blue", "yellow"])
print("The random color is:", color)

# Print a random fact
facts = ["The Earth is the third planet from the Sun.",
          "The population of the Earth is about 8 billion people.",
          "The tallest mountain on Earth is Mount Everest, which is 8,848 meters tall.",
          "The deepest ocean is the Mariana Trench, which is 11,034 meters deep."]
fact = random.choice(facts)
print(fact)
