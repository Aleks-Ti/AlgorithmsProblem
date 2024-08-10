# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def _parse_linked_list(self, instance: ListNode) -> int:
        result = ""
        while True:
            if (value := instance.val) is not None:
                result += str(value)
            if instance.next is None:
                break
            instance = instance.next

        return int(result[::-1])

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        parsed_l1 = self._parse_linked_list(l1)  # 342  integer
        parsed_l2 = self._parse_linked_list(l2)  # 465  integer
        result = (str(parsed_l1 + parsed_l2))[::-1]
        new_linked_list = ListNode(",".join([x for x in result]))
        return new_linked_list


if __name__ == "__main__":
    linked_list_1 = ListNode(2, ListNode(4, ListNode(3, None)))
    linked_list_2 = ListNode(5, ListNode(6, ListNode(4, None)))

    Solution().addTwoNumbers(linked_list_1, linked_list_2)
