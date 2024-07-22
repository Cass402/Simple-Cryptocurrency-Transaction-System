''' This file is the main file that will be used to run the blockchain simulation. It will create multiple nodes in the network,
which will generate transactions and add blocks to the blockchain. The nodes will communicate with each other to synchronize
the blockchain and maintain a decentralized network.    
'''
# importing the necessary libraries
from blockchain import Blockchain # import the Blockchain class from blockchain.py
from node import Node # import the Node class from node.py
import threading # for creating threads for the nodes to mine blocks

# main function to run the blockchain simulation
def main():
    # initialize the blockchain
    blockchain = Blockchain()

    # create nodes in the network
    node_Alice = Node('Alice') # create a node with name 'Alice'
    node_Bob = Node('Bob') # create a node with name 'Bob'
    node_Charlie = Node('Charlie') # create a node with name 'Charlie'

    # create a list of nodes
    nodes = [node_Alice, node_Bob, node_Charlie]

    # make the nodes simulate transactions
    for node in nodes:
        node.simulate_transactions(nodes)
    
    # create threads for the nodes to mine blocks
    threads = []
    for node in nodes:
        thread = threading.Thread(target=node.mine_block) # create a thread for mining a block
        threads.append(thread) # add the thread to the list of threads
        thread.start() # start the thread
    
    # join the threads
    for thread in threads:
        thread.join() # wait for the thread to finish
    
    # print the blockchain
    for block in blockchain.chain:
        print(block)
    

# run the main function
if __name__ == '__main__':
    main()


