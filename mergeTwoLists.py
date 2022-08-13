# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print_list(self):
        #if self.next == None:
        #    return
        #else:
        #    print(self.val)
        #    self.next.print_list()

        current = self
        while current != None:
            print(current.val, current.next)
            current = current.next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
                """

class Solution:
    def mergeTwoLists(self, list1, list2):
        start = None
        last = None
        if list1 == None:
            return list2
        elif list2 == None:
            return list1

        if list1.val < list2.val:
            start = list1
            last = list1
            list1 = list1.next
        else:
            start = list2
            last = list2
            list2 = list2.next

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                last.next = list1
                list1 = list1.next
                last = last.next
            else:
                last.next = list2
                list2 = list2.next
                last = last.next

        while list1 != None:
            last.next = list1
            list1 = list1.next
            last = last.next
        while list2 != None:
            last.next = list2
            list2 = list2.next
            last = last.next

        return start

"""    
    def mergeTwoLists(self, list1, list2):
        if list1 != None and list2 == None:
            return list1
        elif list1 == None and list2 != None:
            return list2
        elif list1 == None and list2 == None:
            return None
        elif list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        else:
            return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
"""

list1 = ListNode(val = 1, next = ListNode( val = 2, next = ListNode(val = 4, next = None)))
list2 = ListNode(val = 1, next = ListNode(val = 3, next = ListNode(val = 4, next = None)))
sol = Solution()
s = sol.mergeTwoLists(list1, list2)
s.print_list()

