from lib2to3.pytree import LeafPattern


def translate(phrase):
    translate=""
    for letter in phrase:
        if letter in "AEIOU aeiou":
            translation = translation + "g"
        else:
            translation = translation + letter

        return translation
print(translate(input("enter a phrase: ")))