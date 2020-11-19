import mmh3
import struct

local_file_name='doc'
key_size=96
hash_size=2147483640
dim=64
with open(local_file_name, 'rb') as bin_file:
    while True:
        key = bin_file.read(key_size)
        if len(key) < key_size:
            break
        key = key.strip(b'\x00').decode('utf-8')
        #decode('utf-8')
        vector = bin_file.read(dim*4)
        vector = struct.unpack("{}f".format(dim), vector) # vector type is tuple
        ## mmh3.hash(key) return a signed 32 int, may < 0. need & 0xffffffff
        hash_value = (mmh3.hash(key) & 0xffffffff) % hash_size
        print (key + "\t" + str(hash_value))
