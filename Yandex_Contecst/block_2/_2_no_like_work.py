# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node: Node, idx):
    if idx == 0:
        return node.next_item
    current = node
    for _ in range(idx - 1):
        current = current.next_item
    if current.next_item is not None:
        current.next_item = current.next_item.next_item
    return node

# def test():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     new_head = solution(node0, 1)
#     assert new_head is node0
#     assert new_head.next_item is node2
#     assert new_head.next_item.next_item is node3
#     assert new_head.next_item.next_item.next_item is None
#     # result is node0 -> node2 -> node3


# if __name__ == '__main__':
#     test()
