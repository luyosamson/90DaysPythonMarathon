def sort_vowels_consonants_numbers(data):
    # Define vowels
    vowels = "AEIOUaeiou"

    # Separate vowels, consonants, and numbers
    vowels_list = [char for char in data if char in vowels]
    consonants_list = [char for char in data if char.isalpha() and char not in vowels]
    numbers_list = [char for char in data if char.isdigit()]

    # Sort each list
    vowels_list.sort()
    consonants_list.sort()
    numbers_list.sort()

    # Combine the sorted lists
    sorted_data = vowels_list + consonants_list + numbers_list

    return ''.join(sorted_data)

# Example usage:
input_data = input("Enter character to sort:  ")
sorted_result = sort_vowels_consonants_numbers(input_data)
print(sorted_result)  # Output: "EIOUabcd1234"
