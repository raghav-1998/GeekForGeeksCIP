# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=smallHead=ListNode(0)
        higher=higherHead=ListNode(0)
        
        while(head):
            if(head.val<x):
                smallHead.next=head
                smallHead=smallHead.next
            else:
                higherHead.next=head
                higherHead=higherHead.next
            
            head=head.next
        
        smallHead.next=higher.next
        higherHead.next=None
        
        return small.next