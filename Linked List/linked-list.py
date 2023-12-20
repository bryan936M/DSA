class Node:
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next
    
  def __str__(self):
    return str(self.data)


class LinkedList:
  def __init__(self):
    self.head = None
    
  def insert_at_bgn(self, data):
    node = Node(data, self.head)
    self.head = node
    
  def show_my_LinkedList(self):
    if self.head is None:
      print("Linked List is empty")
      return
    
    itr = self.head
    ll = ''
    
    while itr:
      ll += str(itr.data) + '-->'
      itr = itr.next
    print(ll+'None')

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None)
      return
      
    itr = self.head
    while itr.next:
      itr = itr.next
    
    itr.next = Node(data, None)

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)
  
  def get_length(self):
    count = 0
    itr = self.head
    
    while itr:
      count += 1
      itr = itr.next
    return count
  
  def rmv_at(self, index):
    if type(index) != int or index < 0 or index >= self.get_length():
      raise Exception("Invalid index")
    
    if index == 0:
      self.head = self.head.next
      return
    
    itr = self.head
    count = 0
    while count < index - 1:
      itr = itr.next
      count += 1
      
    itr.next = itr.next.next
    
  def insert_at(self, index, data):
    if type(index) != int or index < 0 or index >= self.get_length():
      raise Exception("Invalid index")
    
    if index == 0:
      self.insert_at_bgn(data)
      return
    
    itr = self.head
    count = 0
    while count < index - 1:
      itr = itr.next
      count += 1
      
    itr.next = Node(data, itr.next)
    
  def insert_after_value(self, data_after, data_to_insert):
    if self.head is None:
      raise Exception('Empty Linked..')
    
    itr = self.head
    count = 0
    while itr:
      if itr.data == data_after:
        self.insert_at(count+1, data_to_insert)
        return
      itr = itr.next
      count += 1
    


if __name__ == "__main__":
  ll = LinkedList()
  # ll.insert_at_bgn(5)
  # ll.insert_at_bgn(89)
  # ll.insert_at_bgn(90)
  # ll.insert_at_bgn(23)
  # ll.insert_at_bgn(12)
  # ll.insert_at_end(100)
  # ll.show_my_LinkedList()
  
  ll.insert_values(["banana","mango","grapes","orange"])
  ll.show_my_LinkedList()
  print("Length of Linked List: ", ll.get_length())
  
  # ll.rmv_at(0)
  # ll.show_my_LinkedList()
  # print("Length of updated Linked List: ", ll.get_length())
  
  ll.insert_at(2, "figs")
  ll.insert_after_value("mango", "apple")
  print("Length of updated Linked List: ", ll.get_length())
  ll.show_my_LinkedList()