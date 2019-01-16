import hashlib as hasher
import datetime


class Block:
    def __init__ (self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha.hexdigest()

def create_genesis_block():
    return Block(0,datetime.datetime.now(), "Genesis Block", "0")

def next_block(last_block, data):
    this_index = last_block.index + 1
    this_timestamp = datetime.datetime.now()
    this_data = data
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def main():
    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]
    num_blocks = int(input("How many blocks do you want to create? "))
    for i in range(num_blocks):
        data = input("What would you like to put in this block? ")
        block_to_add = next_block(previous_block, data)
        blockchain.append(block_to_add)
        previous_block = block_to_add

        print("Block #{} has been added to the blockchain!".format(block_to_add.index))
        print ("Hash: {}".format(block_to_add.hash))

main()

