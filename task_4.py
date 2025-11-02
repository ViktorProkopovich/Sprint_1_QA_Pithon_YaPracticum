new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

completed_tasks.insert(0, new_tasks.pop())
print(completed_tasks)

new_tasks.pop(2)
print(new_tasks)

print('Заказчик поднял приеоритет задачи -', new_tasks[2] +', срочно взять в работу!' )