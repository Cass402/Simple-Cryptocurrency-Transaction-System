'''This python file contains the Transaction class of the blockchain. The Transaction class is used to create the transactions
that contain sender, receiver, amount and timestamp.
'''
# importing the necessary libraries
from time import time # for timestamping the transactions

# Transaction class
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender # the sender of the transaction
        self.receiver = receiver # the receiver of the transaction
        self.amount = amount # the amount of the transaction
        self.timestamp = time() # the timestamp of the transaction
