"""
__author__ : Sureya Sathiamoorthi

"""
import random
import requests


def get_words(min_word_length=4):
    """
    Alter the function to populate words as per your requirements

    """
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    r = requests.get(url)
    response = r.content.decode('utf-8')
    words = response.splitlines()
    filtered = [word for word in words if len(word) >= min_word_length]
    print("Considering {} words to pick a word for you mate !".format(len(filtered)))
    return filtered


def validate_input(input_letter):
    """
    input_letter : character => Validates if given input is a valid letter.

    """
    if len(input_letter) == 1 and input_letter.isalpha():
        return True
    else:
        return False


class Hangman:

    """
    Implements Hangman game with 7 chances, one object per word / game

    """

    def __init__(self, word):
        self.word = word
        self.chances = 7
        self.show = ["-"]*len(self.word)

        print("length = {}".format(len(self.word)), "\n", self._output_word())

        self._game()

    def _output_word(self):
        return " ".join(self.show)

    def guess(self, guessed_letter):
        if guessed_letter in self.word:
            idxs = [i for i, ltr in enumerate(self.word) if ltr == guessed_letter]
            return idxs

        else:
            return []

    def _game(self):
        while self.chances > 0 and self.show.count("-") > 0:
            letter = input("Make a guess : ")

            if validate_input(letter):
                idxs = self.guess(letter)

                if len(idxs) > 0:
                    for index in idxs:
                        self.show[index] = self.word[index]

                    print("Lovely! {} chances remaining".format(self.chances))
                    print(self._output_word())

                else:
                    self.chances -= 1
                    print("Oops! No {} chances remaining".format(self.chances))
                    print(self._output_word())

            else:
                print("Invalid input Try again")

        if self.chances == 0 and self.show.count("-") > 0:
            print("Sorry the word is {}".format(self.word))

        elif self.chances > 0:
            print("Congrats you Won the game!")

if __name__ == '__main__':

    Hangman(random.choice(get_words()))
"""
__author__ : Sureya Sathiamoorthi

"""
import random
import requests


def get_words(min_word_length=4):
    """
    Alter the function to populate words as per your requirements

    """
    url = "https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    r = requests.get(url)
    response = r.content.decode('utf-8')
    words = response.splitlines()
    filtered = [word for word in words if len(word) >= min_word_length]
    print("Considering {} words to pick a word for you mate !".format(len(filtered)))
    return filtered


def validate_input(input_letter):
    """
    input_letter : character => Validates if given input is a valid letter.

    """
    if len(input_letter) == 1 and input_letter.isalpha():
        return True
    else:
        return False


class Hangman:

    """
    Implements Hangman game with 7 chances, one object per word / game

    """

    def __init__(self, word):
        self.word = word
        self.chances = 7
        self.show = ["-"]*len(self.word)

        print("length = {}".format(len(self.word)), "\n", self._output_word())

        self._game()

    def _output_word(self):
        return " ".join(self.show)

    def guess(self, guessed_letter):
        if guessed_letter in self.word:
            idxs = [i for i, ltr in enumerate(self.word) if ltr == guessed_letter]
            return idxs

        else:
            return []

    def _game(self):
        while self.chances > 0 and self.show.count("-") > 0:
            letter = input("Make a guess : ")

            if validate_input(letter):
                idxs = self.guess(letter)

                if len(idxs) > 0:
                    for index in idxs:
                        self.show[index] = self.word[index]

                    print("Lovely! {} chances remaining".format(self.chances))
                    print(self._output_word())

                else:
                    self.chances -= 1
                    print("Oops! No {} chances remaining".format(self.chances))
                    print(self._output_word())

            else:
                print("Invalid input Try again")

        if self.chances == 0 and self.show.count("-") > 0:
            print("Sorry the word is {}".format(self.word))

        elif self.chances > 0:
            print("Congrats you Won the game!")

if __name__ == '__main__':

    Hangman(random.choice(get_words()))
