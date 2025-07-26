import random

def get_word_list(prompt):
    user_input = input(prompt).strip()
    # Split on commas, strip extra spaces, discard empties
    return [w.strip() for w in user_input.split(',') if w.strip()]

def generate_band_name(adjectives, nouns):
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def main():
    print("🎸 Band Name Generator 🎤")
    adjectives = get_word_list("Enter some adjectives (comma-separated): ")
    nouns      = get_word_list("Enter some nouns (comma-separated): ")
    if not adjectives or not nouns:
        print("Need at least one adjective and one noun. Restart and try again.")
        return

    while True:
        print("\nYour band name:", generate_band_name(adjectives, nouns))
        again = input("Generate another? (y/n): ").strip().lower()
        if again != 'y':
            print("Have fun rocking out! 🤘")
            break

if __name__ == "__main__":
    main()
