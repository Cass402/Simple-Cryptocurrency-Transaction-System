# Simple-Cryptocurrency-Transaction-System

Beginner Project on Blockchain

This project uses a virtual Python environment to localize dependencies. Follow these steps to set up and activate the environment, and to install the necessary dependencies:

1. **Create a virtual environment** (skip if you already have one):

   - Open the terminal.
   - Navigate to the project directory.
   - Run `python3 -m venv venv` to create a virtual environment named `venv`.

2. **Activate the virtual environment**:

   - On macOS or Linux, run `source venv/bin/activate`.
   - Your terminal prompt will change to indicate that the virtual environment is activated.

3. **Install dependencies**:

   - With the virtual environment activated, install the project dependencies by running `pip install -r requirements.txt`.

4. **Deactivate the virtual environment** (when done working on the project):
   - Run `deactivate` to exit the virtual environment.

# How the Application Works

The Simple-Cryptocurrency-Transaction-System is a beginner-friendly project that demonstrates the foundational concepts of blockchain technology through a simplified cryptocurrency transaction system. The application is structured around two main components: the blockchain itself and the transactions that occur within it. Below is an overview of how these components interact within the system.

## Blockchain

At the heart of the application is the blockchain, implemented in [`blockchain.py`](blockchain.py). The blockchain is a chain of blocks, where each block contains data, a timestamp, a hash of the previous block (linking it to the previous block), and its own unique hash. The unique hash is calculated based on the block's content, ensuring the integrity of the entire blockchain.

### Block

The [`Block`](blockchain.py) class represents the individual blocks in the blockchain. Each block includes:

- An index to indicate its position within the chain.
- A timestamp marking when the block was created.
- The data it contains, which, in the context of this application, are transactions.
- The hash of the previous block, creating a link in the chain.
- A nonce value used for the proof-of-work algorithm.
- Its own hash, calculated from its contents, ensuring data integrity.

The class also has two methods - one for hashing the block using the SHA256 algorithm in the hashlib library; another method for implementing the proof of work algorithm that finds a valid hash for the
block with a set difficulty.

### Blockchain

The [`Blockchain`](blockchain.py) class manages the chain of blocks. It initializes with a genesis block (the first block in the chain) and provides functionality to:

- Add new blocks to the chain with `create_block` and `add_block` methods.
- Validate the integrity of the chain using the `validate_chain` method
- A method to add new nodes to the blockchain network.
- Resolve conflicts in the blockchain by reaching consensus among nodes with the `resolve_conflicts` method.

## Transactions

Transactions represent the transfer of cryptocurrency between parties. They are implemented in [`transaction.py`](transaction.py) and include the sender, receiver, amount, and timestamp. Transactions are the data part of the blocks in the blockchain.

## Network Nodes

The system also includes a network of nodes, represented as a set within the `Blockchain` class. These nodes are crucial for the decentralized nature of the blockchain, allowing for the distribution and verification of the chain across multiple participants.

## Proof of Work

To add a new block to the chain, a proof-of-work algorithm is employed. This algorithm requires finding a value (nonce) that, when hashed with the block's contents, produces a hash that meets certain criteria (e.g., a specific number of leading zeros). This process secures the network and prevents tampering with the blockchain.

## Summary

This Simple-Cryptocurrency-Transaction-System project provides a hands-on approach to understanding blockchain technology. Through the implementation of blocks, transactions, and proof-of-work, users can grasp the core concepts that underpin cryptocurrencies and blockchain networks. The project is designed to be beginner-friendly, offering a step-by-step guide to setting up and interacting with a basic blockchain system.
