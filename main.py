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
    node_Alice = Node('Alice', blockchain) # create a node with name 'Alice'
    node_Bob = Node('Bob', blockchain) # create a node with name 'Bob'
    node_Charlie = Node('Charlie', blockchain) # create a node with name 'Charlie'

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

    # update the chain of one of the nodes to simulate a conflict and resolve it (for demonstration purposes)
    node_Alice.simulate_transactions(nodes) # simulate transactions for Alice
    node_Alice.mine_block() # mine a block for Alice
    #delete the last block of the blockchain
    blockchain.chain.pop()

    # call the resolve_conflicts method to resolve the conflict
    if blockchain.resolve_conflicts():
        print('Conflict resolved!')
    else:
        print('Conflict not resolved!')
    
    # print the blockchain after resolving the conflict
    for block in blockchain.chain:
        print(block)
    
    print("Alice's chain after resolving the conflict:")
    # print the chain of Alice after resolving the conflict
    for block in node_Alice.chain:
        print(block)
    

# run the main function
if __name__ == '__main__':
    main()


