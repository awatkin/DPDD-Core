#a simple to do list app

#this one is tricky to detect what is going on, you will need to REALLY thing and test this to the extreme

def main():
    tasks = []

    while True:
      choice = input("Choose an action (add, view, remove, complete, quit): ")

      if choice == "add":
        task = input("Enter a task: ")
        tasks.append(task)
      elif choice == "view":
        print("Your tasks:")
        for task in tasks:
          print(task)
      elif choice == "remove":
        index = int(input("Enter the index of the task to remove: "))
        tasks.remove(index)  # Error: Should remove the task at the given index
      elif choice == "complete":
        # Implement logic to mark tasks as complete
        pass
      elif choice == "quit":
        break
      else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()