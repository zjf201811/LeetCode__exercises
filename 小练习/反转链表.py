# Author:ZJF
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p=None
        while head:
            q=head
            head=q.next
            q.next=p
            p=q
        return p
print(Solution().reverseList([1,2,3,4,5]))