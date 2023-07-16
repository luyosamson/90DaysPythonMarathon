def maximum_draws(n):
    # To guarantee a matching pair, you need to remove n-1 socks
    return n + 1


# Read the number of colors of socks from the user
n = int(input("Enter the number of colors of socks: "))

# Find the minimum number of socks to remove for a matching pair
min_socks_to_remove = maximum_draws(n)

# Print the result
print("The minimum number of socks to remove to guarantee a matching pair is:",
      min_socks_to_remove)
