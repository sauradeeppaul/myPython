class node:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        self.parent=None
        self.height=0
        
class tree:
    def __init__(self):
        '''This is the constructor method for the tree'''
        self.root=None
        
    def insert_node(self,key):
        '''This inserts a node of the given key into the tree'''
        current_node=self.root
        new_node=node(key)
        while current_node!=None:
            if key<current_node.key:
                if current_node.left!=None:
                    current_node=current_node.left
                else:
                    current_node.left=new_node
                    new_node.parent=current_node
                    new_node.height=current_node+1
            else:
                if current_node.right!=None:
                    current_node=current_node.right
                else:
                    current_node.right=new_node
                    new_node.parent=current_node
                    new_node.height=current_node+1
                    
    def rotate_right(node):
        
        
    def rotate_left(node):
        
        
        
    def search_node(self,value):
        '''This seraches for the node of the given value in the tree'''
        current_node=self.root
        while current_node.key!=value:
            if current_node==None:
                return None
            elif value==current_node.key:
                return current_node
            elif value<current_node.key:
                current_node=current_node.left
            elif value>current_node.key:
                current_node=current_node.right
    
    def delete_node_0(self,del_node):
        '''This is called when the node to be deleted has no children'''
        if del_node.parent.right==del_node:
            del_node.parent.right==None
        else:
            del_node.parent.left==None
        del(del_node)
                    
    def delete_node_1(self, del_node):
        '''This is called when the node to be deleted has one child'''
        if del_node.left!=None and del_node.right==None:
            if del_node.parent.right==del_node:
                del_node.parent.right==del_node.left
                del_node.left.parent=del_node.parent
            else:
                del_node.parent.left==del_node.left
                del_node.roght.parent.del_node.parent
        else:
            if del_node.parent.right==del_node:
                del_node.parent.right==del_node.right
                del_node.left.parent=del_node.parent
            else:
                del_node.parent.left==del_node.right
                del_node.roght.parent.del_node.parent
        del(del_node)
        
    def delete_node_2(self, del_node):
        '''This is called when the node to be deleted has two children'''            
        if del_node.parent.left==del_node:
            self.rotate_right(del_node.parent)
        else:
            self.rotate_left(del_node.parent)
            
    def delete_node(self,value):
        '''This is called to delete the node of the given value'''
        del_node=self.search_node(value)
        if del_node==None:
            return 'Node not in tree'
        else:
            if del_node.left==None and del_node.right==None:
                self.delete_node_0(del_node)
            elif del_node.left!=None and del_node.right!=None:
                self.delete_node_2(del_node)
            else:
                self.delete_node_1(del_node)