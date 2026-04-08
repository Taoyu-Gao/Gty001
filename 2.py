student = {
    'name': 'Alice',           # 键：'name'，值：'Alice'
    'scores': [85, 92, 78],    # 键：'scores'，值：[85, 92, 78]
    'info': {'age': 20, 'major': 'Bio'}  # 键：'info'，值：{'age': 20, 'major': 'Bio'}
}
print(student['name'])       # 输出：Alice
print(student['scores'])     # 输出：[85, 92, 78]   
print(student['info'])       # 输出：{'age': 20, 'major': 'Bio'}
print(student['info']['age'])  # 输出：20