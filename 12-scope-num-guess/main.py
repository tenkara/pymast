enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1  # this is a local variable

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@RajNakka"


