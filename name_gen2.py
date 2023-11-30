def has_consecutive_vowels_or_consonants(s):
    vowels = "AEIOUaeiou"
    consecutive_chars = 0
    last_char = ''
    for char in s:
        if char.isalpha():
            if char in vowels == last_char in vowels:
                consecutive_chars += 1
                if consecutive_chars >= 2:
                    return True
            elif char not in vowels == last_char not in vowels:
                consecutive_chars += 1
                if consecutive_chars >= 2:
                    return True
            else:
                consecutive_chars = 0
        else:
            consecutive_chars = 0
        last_char = char
    return False

def character_combinations(s):
    if len(s) <= 1:
        return {s}

    combinations = set()
    for i, char in enumerate(s):
        remaining_chars = s[:i] + s[i + 1:]
        for combo in character_combinations(remaining_chars):
            if not has_consecutive_vowels_or_consonants(char + combo):
                combinations.add(char + combo)

    return combinations

# Function to write combinations to a file with grouped first five letters
def write_combinations_to_file(combinations):
    combinations_dict = {}
    for combination in combinations:
        key = combination[:5].upper()
        if key not in combinations_dict:
            combinations_dict[key] = []
        combinations_dict[key].append(combination)

    with open("combinations_3seqVC.txt", "w") as file:
        for key, value in combinations_dict.items():
            file.write(f"----- {key} -----\n")
            for combo in value:
                file.write(combo + "\n")
            file.write("\n")  # Add an empty line after each group


# Example usage:
input_string = input("Enter a string: ")
print("Calculating all possible character combinations")
result = character_combinations(input_string)

write_combinations_to_file(result)
print("Combinations written to 'combinations_3seqVC.txt'")
