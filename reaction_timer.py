import time
import random

print("Reaction Timer Game")
print("When you see 'GO!', press Enter as quickly as you can.")
input("Press Enter to start...")

# Odota random aika
wait_time = random.uniform(3, 7)
print("Get ready...")
time.sleep(wait_time)

print("Go!")
start_time = time.time()

input() # Odota että painetaan Enter

end_time = time.time()
reaction_time = end_time - start_time

print(f"Your reaction time is {reaction_time:.3f} seconds.")