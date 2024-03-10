import hashlib as hasher
from datetime import datetime


# Define what a Snakecoin block is
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8'))
        return sha.hexdigest()


# Generate genesis block
def create_genesis_block():
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(0, datetime.now(), {
        "proof-of-work": 9,
        "transactions": None
    }, "0")


# Generate all later blocks in the blockchain
def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = datetime.now()
    this_data = last_block.data
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)
