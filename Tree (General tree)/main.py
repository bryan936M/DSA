

class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None
    
  def add_child(self,  child) -> None:
    child.parent = self
    self.children.append(child)
    return
    

def build_tree_node() -> TreeNode:
  root  = TreeNode('Electronics')
  
  cellphone = TreeNode("Cell phone")
  cellphone.add_child(TreeNode("Iphone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Vivo"))
  
  tv = TreeNode("TV")
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))
  
  root.add_child(cellphone)
  root.add_child(TreeNode(tv))
  
  return root


if __name__ == "__main__":
  root = build_tree_node()