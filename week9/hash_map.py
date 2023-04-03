#!/usr/bin/env python
prehash = hash

def hash(obj):
    num = prehash(obj)
    return num%10

class KeyNotFoundError(Exception):
    pass


class HashMap:
    def __init__(self):
        self.hash_table = list()
        for i in range(10):
            self.hash_table.append(list())
        

    @staticmethod
    def from_list(arr):
        h_map = HashMap()
        for key, value in arr:
            h_map[key] = value
        return h_map
            
    def __getitem__(self, key):
        slot = self.hash_table[hash(key)]
        if slot:
            for _key, _item in slot:
                if key == _key:
                    return _item
        raise KeyNotFoundError

    def __setitem__(self, key, value):
        index = hash(key)
        try:
            self[key]
        except KeyNotFoundError:
            self.hash_table[index].append((key, value))
        else:
            for _key, _value in self.hash_table[index]:
                if _key == key:
                    self.hash_table[index].remove((_key,_value))
                    self.hash_table[index].append((key, value))

    def __delitem__(self, key):
        index = hash(key)
        slot = self.hash_table[index]
        if slot:
            for _key, _value in slot:
                if _key == key:
                    slot.remove((_key, _value))
                    return
        raise KeyNotFoundError

if __name__ == "__main__":
    h_map = HashMap.from_list([[1,2],[2,1],[3,4],[1,3],[2,4],[11,4]])
    print(h_map.hash_table)
    print(h_map[2])
    del h_map[11]
    print(h_map.hash_table)
