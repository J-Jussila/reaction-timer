import time
import random

best_time = None

while True:

    print("Reaction Timer Game")
    print("When you see 'GO!', press Enter as quickly as you can.")
    input("Press Enter to start...")

    # Odota random aika
    wait_time = random.uniform(3, 7)
    print("Get ready...")
    time.sleep(wait_time)

    ready_time = time.time()
    print("Go!")

    start_time = time.time()

    input() # Odota että painetaan Enter

    end_time = time.time()

    # Anticheat
    if end_time - ready_time < 0.1:
        print("Too early! You pressed before or instantly after 'GO!'")
    else:
        reaction_time = end_time - start_time
        print(f"Your reaction time is {reaction_time:.3f} seconds.")

        # Päivitä paras aika jos uusi aika on parempi
        if best_time is None or reaction_time < best_time:
            best_time = reaction_time
            print("New Personal best!")
        print(f"Best time: {best_time:.3f} seconds\n")

    again = input("Play again? (y/n): ")
    if again.lower() != 'y':
        break