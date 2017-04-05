"""
__author__ : Sureya Sathiamoorthi

"""
import random


def get_words():
    """
    Alter the function to populate words as per your requirements
    
    """
    return ["plausible", "eccentric"]


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





