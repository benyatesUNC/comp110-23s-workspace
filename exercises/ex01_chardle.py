"""Chardle - A cute step toward wordle"""

_author_ = "730479956"

_word_: str = input ("Enter a 5-character word: ")
if(len(_word_) < 5):
    print("Error: Word must contain 5 characters")
    exit()
if(len(_word_) > 5):
    print("Error: Word must contain 5 characters")
    exit()

_letter_: chr = input ("Enter a single character: ")
if(len(_letter_) > 1):
    print("Error: Character must be a single character.")
    exit()
if(len(_letter_) < 1):
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + _letter_ + " in " + _word_ )
if( _word_[0] == _letter_):
    print( _letter_ + "found at index 0")
if( _word_[1] == _letter_):
    print( _letter_ + " found at index 1")
if( _word_[2] == _letter_):
    print( _letter_ + " found at index 2")
if( _word_[3] == _letter_):
    print( _letter_ + " found at index 3")
if( _word_[4] == _letter_):
    print( _letter_ + " found at index 4")

str = _word_ 
sub = _letter_ 
if(str.count(sub) > 0 ):
    print(str.count(sub),  " instances of " + _letter_ + " found in " + _word_)
else:
    print("No instances of " + _letter_ + " found in " + _word_)



