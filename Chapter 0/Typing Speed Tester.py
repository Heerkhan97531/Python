import time
text = "Good habits lead to a brihter future. keep learning. keep goin!"
input("Press Enter when you're ready...")
start_time = time.time()
user_input = input("Type the text: \n")
end_time = time.time()
time_taken = end_time - start_time

#Calculate results
words = len(text.split())
wpm = (words / time_taken) *60

#Count mistakes 
mistakes = sum(1 for a, b in zip(text, user_input) if a!=b)
accuracy = (1 - mistakes / len(text) *100)

print(f"\nWPM: {wpm:.1f}")
print(f"Accuracy: {accuracy:.1f}")
print(f"Mistakes: {mistakes}")
print(f"Time taken: {time_taken: .1f} seconds")
