from collections import deque

class Stack:
  
  def __init__(self):
    self.container = deque()
    
  def push(self, val):
    self.container.append(val)
    
  def pop(self):
    if self.is_empty():
      return None
    
    return self.container.pop()  # Added return statement
  
  def peek(self):
    if self.is_empty():
      return None
    
    return self.container[-1]  # Added return statement
  
  def is_empty(self):
    return len(self.container) == 0
  
  def size(self):
    return len(self.container)


if __name__ == '__main__':
  s = Stack()
  s.push(5)
  s.push(6)
  s.push(7)
  s.push(8)
  s.push(9)
  s.push(10)
  print(s.size())
  print(s.is_empty())
  print(s.peek())
  print(s.pop())
  print(s.peek())
  print(s.size())
