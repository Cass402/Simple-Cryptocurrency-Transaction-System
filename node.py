''' This file will contain the Node class. The Node class is used to create the nodes in the network that contain the blockchain.
Different nodes will be created for demonstration purposes to simulate a decentralized network.
'''

# importing the necessary libraries
from blockchain import Blockchain # import the Blockchain class from blockchain.py
from transaction import Transaction # import the Transaction class from transaction.py
import random # for generating random numbers

# Node class
class Node:
    def __init__(self, name, blockchain):
        self.name = name # the name of the node
        if (Blockchain.validate_chain): # validate the blockchain before copying it to the node (to ensure the integrity of the blockchain)
            self.chain = blockchain.chain.copy() # copy the blockchain to the node
            self.blockchain = blockchain # reference to the blockchain
        else: # if the blockchain is not valid
            raise Exception('Blockchain is not valid!') # raise an exception
        self.transactions = [] # a list to store the transactions in the node
        blockchain.add_node(self) # add the node to the blockchain
    
    # method to create a new transaction
    def create_transaction(self, receiver, amount):
        transaction = Transaction(self.name, receiver, amount) # create a new transaction with the sender as the node's name
        return transaction.to_dict() # return the transaction as a dictionary
    
    # method to simulate transactions between nodes for demonstration purposes
    def simulate_transactions(self, nodes):
        for i in range(5):
            sender = random.choice(nodes) # select a random sender node
            receiver = random.choice(nodes) # select a random receiver node
            if sender != receiver:
                amount = random.randint(1, 100) # generate a random amount for the transaction
                self.transactions.append(sender.create_transaction(receiver.name, amount)) # create a transaction between the sender and receiver nodes
                print(f'{sender.name} sent {amount} coins to {receiver.name}')
    
    # method to mine a block in the blockchain
    def mine_block(self):
        block = self.blockchain.add_block(self.transactions) # add the transactions to the blockchain and mine a new block
        self.chain.append(block) # add the block to the node's chain
        self.transactions = [] # clear the transactions in the node after mining the block
        print(f'{self.name} mined a new block with index {block.index} and hash {block.hash}') # print a message that the block has been mined
    
    # method to update the blockchain of the node after the original blockchain is updated
    def update_blockchain(self):
        self.chain = self.blockchain.chain.copy() # copy the updated blockchain to the node
        print(f'{self.name} updated the blockchain') # print a message that the blockchain has been updated
    
        
    
    
        