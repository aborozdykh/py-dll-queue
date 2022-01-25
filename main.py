from CustomQueue import CustomQueue
from DoubleLink import DoublyLinkedList

if __name__ == '__main__':
    new_linked_list = DoublyLinkedList()
    print('Insert in empty list')
    new_linked_list.insert_in_emptylist(50)
    new_linked_list.traverse_list()
    print('Insert at the start')
    new_linked_list.insert_at_start(10)
    new_linked_list.insert_at_start(5)
    new_linked_list.insert_at_start(18)
    new_linked_list.traverse_list()
    print('Insert at the end')
    new_linked_list.insert_at_end(29)
    new_linked_list.insert_at_end(39)
    new_linked_list.insert_at_end(49)
    new_linked_list.traverse_list()
    print('Insert after item 50')
    new_linked_list.insert_after_item(50, 65)
    new_linked_list.traverse_list()
    print('Insert before item 29')
    new_linked_list.insert_before_item(29, 100)
    new_linked_list.traverse_list()
    print('Delete at start')
    new_linked_list.delete_at_start()
    new_linked_list.traverse_list()

    print('Delete at end')
    new_linked_list.delete_at_end()
    new_linked_list.traverse_list()

    print('Delete by value')
    new_linked_list.delete_element_by_value(100)
    new_linked_list.traverse_list()

    print('Reverse list')
    print('Original list')
    new_linked_list.traverse_list()
    new_linked_list.reverse_linked_list()
    print('Reversed list')
    new_linked_list.traverse_list()


    # q = CustomQueue()
    #
    # q.push('First')
    # q.push('Second')
    # q.push('Third')
    # print(q.queue)
    # print('Queue size is ', q.size())
    #
    # q.pop()
    # print(q.queue)
    # print('Queue size is ', q.size())
    # q.pop()
    # print(q.queue)
    # print('Queue size is ', q.size())
    # q.pop()
    # print(q.queue)
    # print('Queue size is ', q.size())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


