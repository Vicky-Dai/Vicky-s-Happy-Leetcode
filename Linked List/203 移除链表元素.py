#（版本一）虚拟头节点法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head)
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next
    

#方法二 双指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummyhead = ListNode(0, head)
        pre, cur = dummyhead, head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummyhead.next
