words = []

length = int(input("Enter the number of words you want in the list: "))

print("Enter words with 5 or 6 letters:")

while len(words) < length:
    word = input(f"Word {len(words) + 1}/{length}: ").strip()
    
    if word.lower() == 'done':
        break
    
    if 5 <= len(word) <= 6:
        words.append(word)
    else:
        print("Word must have 5 or 6 letters. Try again.")
        
print("\nFinal List of Words:", words)