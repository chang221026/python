# 14 Queues

# https://docs.python.org/3.8/library/collections.html#collections.deque
# 清空队列
# 队列：先进先出（FIFO - First In, First Out）

from collections import deque

list_queue = deque([])
list_queue.append(1)
list_queue.append(2)
list_queue.append(3)
list_queue.append(4)

list_queue.popleft()
print(list_queue)

if not list_queue: # 如果队列为空则输出 "Empty"
    print("Empty")