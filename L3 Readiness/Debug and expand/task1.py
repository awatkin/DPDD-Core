''' Debug and expand task
In this code is some logic and syntax errors, you need to test and debug these out of the code before moving on to the extension tasks.


Extension tasks:

Attempt these in any order, but you must:
    DESIGN (flowchart) your solution to adding these
    CODE your solution
    TEST your solution

Add items: Allow the player to pick up and drop items.

Introduce characters: Create non-player characters that the player can interact with.

Enhance the user interface: Provide more descriptive messages and feedback.

Save and load games: Allow the player to save and resume their game.

Create multiple endings: Offer different outcomes based on the player's choices.

'''

def describe_location(location):
  print(f"You are in the {location['name']}.")
  print("Exits:", end=" ")
  for exit in location['exits']:
    print(exit, end=" ")
  print()

def move(direction):
  global current_location
  if direction in current_location['exits']:
    current_location = locations[current_location['exits'][direction]]
    describe_location(current_location)
  else:
    print("You can't go that way.")

def main():
locations = { # this is a dictionary that is being used.
  "start": {"name": "Start", "exits": {"north": "forest"}},
  "forest": {"name": "Forest", "exits": {"south": "start", "west": "cave"}},
  "cave": {"name": "Cave", "exits": {"east": "forest"}}
}

inventory = [] # this is a list

# Start the game
current_location = locations['start']
describe_location(current_location)

while True:
  direction = input("Which direction do you want to go? ")
  move(direction)

  if __name__ == "__main__":
      main()