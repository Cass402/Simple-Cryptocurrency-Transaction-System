''' This file contains the Block and Blockchain classes. The Block class is used to create the blocks that contain
index, timestamp, previous hash, hash of the block and other relevant data. The Blockchain class is used to create the
blockchain and contains methods to add blocks to the blockchain, validate the blockchain and mine blocks.
'''

import hashlib # for hashing the blocks using SHA-256
import json # for encoding the blocks to JSON format
from time import time # for timestamping the blocks

# Block class
class Block: 
    def __init__(self, index, timestamp, data, previous_hash, nonce=None):
        self.index = index # the index of the block in the blockchain
        self.timestamp = timestamp # the timestamp of the block when it was created
        self.data = data # the data that the block contains (e.g., transactions)
        self.previous_hash = previous_hash # the hash of the previous block in the blockchain
        if nonce is None: # if no nonce value is provided
            self.nonce = 0 # set the nonce value to 0
        else: # if a nonce value is provided
            self.nonce = nonce
        self.hash = self.calculate_hash() # the hash of the current block

    # method to calculate the hash of the current block
    def calculate_hash(self):
        block_string = json.dumps({'index': self.index, 'timestamp': self.timestamp, 'data': self.data, 'previous_hash': self.previous_hash, 'nonce': self.nonce}, sort_keys=True) # encode the block to JSON format and sort the keys
        return hashlib.sha256(block_string.encode()).hexdigest() # hash the block using SHA-256 and return the value of hash in hexadecimal format
    
    # method to perform proof of work and mine the block
    def proof_of_work(self, difficulty):
        target_difficulty = '0' * difficulty # the number of leading zeros in the hash of the block required for proof of work
        while self.hash[:difficulty] != target_difficulty: # repeat the process until the hash of the block has the required number of leading zeros
            self.nonce += 1 # increment the nonce value to change the hash of the block
            self.hash = self.calculate_hash() # calculate the hash of the block with the new nonce value

    # method to convert the block dictionary back to a Block object
    @classmethod # decorator to define a class method
    def from_dict(cls, block_dict):
        return cls(block_dict['index'], block_dict['timestamp'], block_dict['data'], block_dict['previous_hash']) # return a new Block object with the values from the block dictionary
    
# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [] # a list to store the blocks in the blockchain
        self.nodes = set() # a set to store the nodes in the network
        self.difficulty = 2 # the difficulty level for proof of work (easier for demonstration purposes)
        self.create_block(1, '0', 'Genesis Block') # create the genesis block with index 1 and previous hash '0' and data 'Genesis Block'
    
    # method to create a new block in the blockchain
    def create_block(self, index, previous_hash, data):
        block = Block(index, time(), data, previous_hash) # create a new block with the given index, timestamp, data and previous hash
        block.proof_of_work(self.difficulty) # mine the block using proof of work to find the valid hash
        self.chain.append(block.__dict__) # add the block to the blockchain as a dictionary
        return block # return the block
    
    # method to add a new block to the blockchain
    def add_block(self, data):
        previous_block = self.chain[-1] # get the last block in the blockchain
        new_block = self.create_block(previous_block['index'] + 1, previous_block['hash'], data) # create a new block with a index incremented by 1, previous hash as the hash of the previous block and the given data
        for node in self.nodes: # iterate over the nodes in the network
            node.update_blockchain() # update the blockchain of each node to synchronize the network
        return new_block # return the new block
    
    # method to validate the blockchain
    def validate_chain(self, chain=None):
        if chain is None: # if no chain is provided
            chain = self.chain # use the current chain of the blockchain
        # iterate over the blocks in the blockchain starting from the second block (ignoring the genesis block)
        for index in range(1, len(chain)):
            current_block_dict = chain[index] # get the current block as a dictionary
            previous_block_dict = chain[index - 1] # get the previous block as a dictionary
            current_block = Block.from_dict(current_block_dict) # convert the current block dictionary to a Block object
            previous_block = Block.from_dict(previous_block_dict) # convert the previous block dictionary to a Block object
            current_block.proof_of_work(self.difficulty) # mine the current block to validate the hash

            # check if the hash of the current block is valid (to ensure the integrity of the block in the blockchain)
            if current_block_dict['hash'] != current_block.hash:
                return False
            
            # check if the previous hash of the current block matches the hash of the previous block (to ensure the continuity of the blockchain)
            if current_block_dict['previous_hash'] != previous_block.hash:
                return False
            
        return True # return True if the blockchain is valid
    
    # method to add a new node to the network
    def add_node(self, node):
        self.nodes.add(node) # add the node to the set of nodes in the network

    # method to resolve conflicts in the blockchain by reaching consensus among the nodes
    def resolve_conflicts(self):
        new_chain = None # variable to store the new chain
        max_length = len(self.chain) # variable to store the length of the longest chain (initially set to the length of the current chain)

        # iterate over the nodes in the network
        for node in self.nodes:
                chain = node.chain # get the chain of the node
                length = len(chain) # get the length of the blockchain

                # check if the length of the blockchain is greater than the current length and the blockchain is valid
                if length > max_length:
                    max_length = length # update the maximum length
                    new_chain = chain # update the new chain
                
        if new_chain: # if a new chain is found (not None)
            self.chain = new_chain # update the blockchain with the new chain
            return True # return True if the blockchain is updated and conflicts are resolved
        
        return False