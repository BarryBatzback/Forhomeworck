grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
AR = {}
abc = sorted(students)
for k, v in zip(abc, grades):
    AR[k] = v
numbers = AR.get('Aaron')
L0 = sum(numbers) / len(numbers)
numbers = AR.get('Bilbo')
L1 = sum(numbers) / len(numbers)
numbers = AR.get('Johnny')
L2 = sum(numbers) / len(numbers)
numbers = AR.get('Khendrik')
L3 = sum(numbers) / len(numbers)
numbers = AR.get('Steve')
L4 = sum(numbers) / len(numbers)
LO = [L0,L1,L2,L3,L4]
for k, v in zip(abc, LO):
    AR[k] = v
print(AR)