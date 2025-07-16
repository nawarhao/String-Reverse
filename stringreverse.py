class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# Take input from the user
user_input = input("Enter a string: ")

# Create an instance of the class with user input
rev = Reverse(user_input)

# Print the reversed string
print("Reversed string:", rev.reverse_string())
