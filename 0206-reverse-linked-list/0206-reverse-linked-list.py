# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead=None
        while head!=None:
            next=head.next             #Point to the immediate next.
            head.next=newHead          #head.next point to the dummy node.
            newHead=head               #dummy node move to the head.
            head=next                  #head move to the next
        return newHead                 #our dummy node is new head of our linked list do return that.