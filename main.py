# Foothill College
# CS 03B Python 2, Fall 2023
# Lab 1, week 1
# Prepared by Jorge Pont
# email: jorgefpont@gmail.com

#from collections.abc import ItemsView
import random


def print_stuff():
  """
  Program must print:
  Your full name
  Your student Id
  Your email address
  3 discussed the policies of our class
  """
  
  name = "Jorge Pont"
  student_id = 10949994
  student_email = "jorgefpont@gmail.com"
  
  print("Name: ", name)
  print()
  print("Student ID: ", student_id)
  print()
  print("Student_email: ", student_email)
  print()
  #print("Enrollment: It is the students’ responsibility to drop themselves from the class. At any point in time, if you feel that this class is not what you are looking for, you are responsible for dropping yourself. Simply being absent from all the class activities will result in a final grade of F. I will not handle any dropping petition. If the drop date is passed, please contact the registrar office or consult your academic advisors for appropriate action.\n")

  #print("Late Submission: up to 1 week late, 15% penalty. Each assignment has a due date and a cut-off date; once the cut-off date is passed, you will no longer be able to submit your assignment. Please make sure that you submit your assignment before the cut-off date.\n")

  #print("Regrade: Grading is a difficult task, and errors or misjudgments occasionally occur. Any student who feels that his or her work has not been graded properly may request a regrade. However, all such requests must be made no later than one week after the assignment has been returned.\n\n")
  
# ---------------------------------------------
"""
Create a deck of cards class. Internally, the deck of cards
should use another class, a card class. Your requirements are:
--The Deck class should have a deal method to deal a single card
from the deck
--After a card is dealt, it is removed from the deck.
-- There should be a shuffle method which makes sure the deck of 
cards has all 52 cards and then rearranges them randomly.
-- The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
"""

class Card:

  suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
  ranks = ['Ace','2','3','4','5','6','7','8','9','10',
           'Jack','Queen','King']
  
  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank
  
  def __str__(self):
    return f'{Card.ranks[self.rank]} of {Card.suits[self.suit]}'

class Deck(Card):

  def __init__(self):
    # create deck
    self.deck = []
    for suit in range(len(Card.suits)):
      for rank in range(len(Card.ranks)):
        card = Card(suit, rank)
        self.deck.append(card)

  def shuffle_deck(self):
    random.shuffle(self.deck)

  def deal_card(self):
    card = self.deck.pop()
    return card

  def __str__(self):
    adeck = []
    for item in self.deck:
      adeck.append(str(item))
      
    res = ', '.join(adeck)
    return res

# ----------------------------------

def main():

  print_stuff()

  print('######\n\n')
  
  deck1 = Deck()
  print('Unshuffled deck\n')
  print(deck1)
  print('\n------\n')
  Deck.shuffle_deck(deck1)
  print('Shuffled deck\n')
  print(deck1)
  print('\n------\n')
  acard = Deck.deal_card(deck1)
  print('Deal one card\n')
  print(acard)
  print('\n------\n')
  print('Deck without the dealt card\n')
  print(deck1)
  

if __name__ == "__main__":
    main()
  