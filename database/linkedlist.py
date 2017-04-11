class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList(object):
    head = 0
    lens = 0
    
    def __init__(self):
        self.head = 0
        
    def BuildWithArray(self,array):
        lens = len(array)
        if lens == 0:
            pass

        self.head = ListNode(array[0])
        current = self.head
        
        for i in range(1,lens):
            new_node = ListNode(array[i])
            # 设置指针
            current.next = new_node
            #  更新当前指针
            current = new_node
            
        self.lens = lens
    # print 函数
    
    def PrintList(self):
        current = self.head
        for i in range(self.lens):
            print(current.val,end=' ')
            current = current.next
    
    def IsEmpty(self):
        return self.lens == 0
    
    # 在第i位置上插入一个数
    def Insert(self, index, val):
        if index < 0 or index > self.lens:
            print('the index is wrong, please input the suitable index')       
            return
        
        current = self.head
        new_node =  ListNode(val)
        
        if index == 0:

            new_node.next = self.head
            self.head = new_node

        elif index == self.lens:
            while(current.next != None):
                current = current.next                
            current.next = new_node

        else:
            current = self.head
            for i in range(index-1):
                current = current.next
            # new node should insert in current and current.next
            nextnode = current.next
            current.next = new_node
            new_node.next = nextnode
            
        self.lens += 1
        
        # 删去第i个数，并返回
    def Delete(self,index):
        if self.lens == 0:
            print('can not delete anything in an empty linklist')
            
        if index < 0 or index >= self.lens :
            print('the index is wrong, please input the suitable index')       
            return
        
        current = self.head
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(index-1):
                current = current.next
                
            nextnode = current.next
            current.next = nextnode.next           
        self.lens -= 1
            

 
