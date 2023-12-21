class HashTable:
    def __init__(self):
      self.MAX = 100
      self.arr = [[] for i in range(self.MAX)]
    
    def get_hash(self, key):
      h = 0
      
      # convert each key to ascii and add it to h
      for char in key:
        h += ord(char)
        
      return h % self.MAX

    

    def __setitem__(self, key, value):
      h = self.get_hash(key)
      print(h)
      
      # if key already exists, update the vale
      for idx, element in enumerate(self.arr[h]):
        if len(element) == 2 and element[0] == key:
          self.arr[h][idx] = (key, value)
          return
      
      # if key does not exist, append
      self.arr[h].append((key, value))
    
if __name__ == '__main__':
  t = HashTable()
  t['ab c'] = 123
  t['bc a'] = 321
  print(t.arr)
  