# use py 3.10 or later
def count_words(prompt: str):
    count = sum(1 for x in prompt.strip() if x== " ")
    return count

def count_vowel(vow: str, prompt: str):
    count = sum(1 for x in prompt if x == vow)
    return count

def starts_with_uppercase(prompt: str): return True if prompt[0].isupper() else False

def main():
    try:
        text = input("enter phrase\n--> ")
        vowel = input("enter vowel\n--> ")
        print(
            f"the phrase contains {count_words(text)} words\n"
            f"the phrase contains {count_vowel(vowel, text)} target vowels"
            "the phrase starts with capital letter" if starts_with_uppercase(text)  else "does not start with capital letter"
        )
    except ValueError: print("invalid input")

if __name__ == "__main__": main()