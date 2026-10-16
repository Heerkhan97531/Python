#Mini Project – Countdown Timer (with 1-second gap)
#Goal:
# Print a countdown before something “exciting” happens (like “Launching…” or
# “Happy New Year!”).

# take ountdown input from user
import time
count = int(input("Enter a countdown number:"))

print(" \nCountdown starts Now:")
for i in range(count, 0, -1):
    print(i)
    time.sleep(1)
print(" \n Wohoo, Happy new year!")


