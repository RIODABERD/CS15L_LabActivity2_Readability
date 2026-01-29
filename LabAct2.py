# Object-Oriented Programming

def main():
    try:
        text = input("Text: ")

        letters = countinger.count_letters(text)
        words = countinger.count_words(text)
        sentences = countinger.count_sentences(text)
    except Exception as e:
        print(f"An error has occurred ", e)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    grade = round(index)

    if grade < 0:
        print("Before Grade 1")
    elif grade >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")

class countinger(): # One class with user-defined attributes
    def count_letters(text):
        count = 0
        for char in text:
            if char.isalpha():
                count += 1
        return count


    def count_words(text):
        count = 0
        word = False
        for char in text:
            if char.isalnum():
                word = True
            if char.isspace() and word == True:
                word = False
                count += 1
        if word == True:
            count += 1
        return count


    def count_sentences(text):
        count = 0
        for char in text:
            if char in [".", "?", "!"]:
                count += 1
        return count

main()