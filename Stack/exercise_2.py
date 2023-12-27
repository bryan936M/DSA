from main import Stack

# # ---------------------- My Solution ----------------------

# open_parantheses = ['(', '[', '{']
# closed_parantheses = [')', ']', '}']


# def is_balanced(string):
#   s = Stack()
  
#   for char in string:
    
#     if char in open_parantheses:
#       s.push(char)
        
#     if char in closed_parantheses:
#       if s.is_empty():
#         return False
      
#       top = s.pop()
      
#       if closed_parantheses.index(char) != open_parantheses.index(top):
#         return False
      
#   return s.is_empty()

# ---------------------- Another Solution ----------------------

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0



if __name__ == '__main__':
  print(is_balanced('({a+b})'))
  print(is_balanced('))((a+b}{'))
  print(is_balanced('((a+b))'))
  print(is_balanced('))'))
  print(is_balanced('[a+b]*(x+2y)*{gg+kk}'))
