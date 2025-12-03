
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        for pair in self.table[key_hash]:
            if pair[0] == key:
                pair[1] = value
                return True
        self.table[key_hash].append(key_value)
        return True

    def get(self, key):
        key_hash = self.hash_function(key)
        for pair in self.table[key_hash]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                # delete element from list by index
                bucket.pop(i)
                return True
        return False

# Testing:

# Create a table and add data
H = HashTable(5)
H.insert("apple", 10)
H.insert("orange", 20)
H.insert("banana", 30)

print("Before deletion:")
print(H.get("apple"))    # 10
print(H.get("orange"))   # 20
print(H.get("banana"))   # 30
print()

# Test deleting an existing key
print("Deleting 'apple':", H.delete("apple"))
print("After deleting 'apple':")
print(H.get("apple"))    # None
print(H.get("orange"))   # 20
print(H.get("banana"))   # 30
print()

# Testing deletion of non-exist key
print("Deleting non-existent 'grape':", H.delete("grape"))  # False
print("After attempt of deleting 'grape':")
print(H.get("orange"))   # 20
print(H.get("banana"))   # 30
print()

# Deleting one more key
print("Deleting 'banana':", H.delete("banana"))
print("Final stage:")
print(H.get("apple"))    # None
print(H.get("orange"))   # 20
print(H.get("banana"))   # None
