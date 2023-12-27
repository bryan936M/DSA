from main import Stack


class StringReverse(Stack):
  def __init__(self):
    super().__init__()
    
  def reverse(self, string):
    for char in string:
      self.push(char)
      
    reversed_string = ''
    
    while not self.is_empty():
      reversed_string += self.pop()
      
    return reversed_string



if __name__ == '__main__':
  string_reverse = StringReverse()
  print(string_reverse.reverse('Hello World'))