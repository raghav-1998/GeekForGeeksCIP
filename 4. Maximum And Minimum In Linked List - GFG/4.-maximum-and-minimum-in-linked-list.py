#User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
def maximum(head):
    #code here
    temp=head
    maxVal=temp.data
    
    while(temp!=None):
        if(temp.data>maxVal):
            maxVal=temp.data
        temp=temp.next
    
    return maxVal
    
def minimum(head):
    #code here
    temp=head
    minVal=temp.data
    
    while(temp!=None):
        if(temp.data<minVal):
            minVal=temp.data
        temp=temp.next
    
    return minVal

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import io
import sys

    
# Node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # append at the end of the list
    def append(self,new_node):
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node
        self.tail = self.tail.next

if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        n=int(input())
        a=LinkedList()
        nodes=list(map(int,input().strip().split())) #list containing nodes
        for x in nodes:
            node=Node(x) # create a new node
            a.append(node)
        print(maximum(a.head), end = " ")
        print(minimum(a.head))
# } Driver Code Ends