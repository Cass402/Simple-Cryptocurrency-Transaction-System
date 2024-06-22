''' This file contains the Block and Blockchain classes. The Block class is used to create the blocks that contain
index, timestamp, previous hash, hash of the block and other relevant data. The Blockchain class is used to create the
blockchain and contains methods to add blocks to the blockchain, validate the blockchain and mine blocks.
'''

import hashlib # for hashing the blocks using SHA-256
import json # for encoding the blocks to JSON format
from time import time # for timestamping the blocks
from urllib.parse import urlparse # for parsing the URLs of the nodes in the network
import requests # for sending HTTP requests to the nodes in the network

# Block class
class Block: 
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # method to calculate the hash of the current block
    def calculate_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True) # encode the block with its instance variables in dictionary format to JSON format
        return hashlib.sha256(block_string.encode()).hexdigest() # hash the block using SHA-256 and return the value of hash in hexadecimal format
    
# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [] # a list to store the blocks in the blockchain
        self.nodes = set() # a set to store the nodes in the network
        self.create_block(1, '0') # create the genesis block with index 1 and previous hash '0'
    
    # method to create a new block in the blockchain
    def create_block(self, index, previous_hash):
        block = Block(index, time(), self.chain[-1] if self.chain else 'Genesis Block', previous_hash) # create a new block with the given index, timestamp, data and previous hash
        self.chain.append(block.__dict__) # add the block to the blockchain
        return block # return the block
    