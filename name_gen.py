def character_combinations(s):
    if len(s) <= 1:
        return {s}

    combinations = set()
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        for combo in character_combinations(remaining_chars):
            combinations.add(char + combo)

    return combinations

# Example usage:
input_string = input("Enter a string: ")
print("All possible character combinations:")
result = character_combinations(input_string)
for combination in result:
    print(combination)
print("Number of combinations: "+str(len(combination)))
