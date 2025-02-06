import unittest

class ListNode:
    def __init__(self, ssn, age, full_name):
        self.ssn = ssn
        self.age = age
        self.full_name = full_name
        self.next = None

def merged_sorted_lists(head1, head2):
    dummy = ListNode(0, 0, "")
    current = dummy

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    if head1:
        current.next = head1
    if head2:
        current.next = head2

    return dummy.next

class TestMergeLists(unittest.TestCase):
    def list_to_array(self, head):
        arr = []
        while head:
            arr.append((head.ssn, head.age, head.full_name))
            head = head.next
        return arr

    def test_merged_sorted_lists(self):
        head1 = ListNode(101, 30, "Alice")
        head1.next = ListNode(150, 25, "Bob")
        head1.next.next = ListNode(200, 40, "Charlie")

        head2 = ListNode(120, 35, "David")
        head2.next = ListNode(170, 28, "Eve")
        head2.next.next = ListNode(250, 50, "Frank")

        
        merged_head = merged_sorted_lists(head1, head2)
        result = self.list_to_array(merged_head)

        expected = [
            (101, 30, "Alice"), (120, 35, "David"),
            (150, 25, "Bob"), (170, 28, "Eve"),
            (200, 40, "Charlie"), (250, 50, "Frank")
        ]

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
