from collections import deque

dq = deque()
dq.append("queue_item")
dq.appendleft("stack_item")

print("Popped from stack:", dq.popleft())
print("Next queue item:", dq.pop())
