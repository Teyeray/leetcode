import sys
#exp1
students = ["1/N", "2/Y", "3/N", "4/Y"]
#exp2
#students = ["1/N", "2/Y", "3/N", "4/Y", "5/Y", "6/Y", "7/N", "8/Y"]

input_list = []
for student in students:
    id, is_same_class = student.split("/")
    try:
        id = int(id)
    except ValueError:
        print('ERROR')
        sys.exit()
    if is_same_class == "N":
        input_list.append((id, 0))
    elif is_same_class == "Y":
        input_list.append((id, 1))
    else:
        print('ERROR')
        sys.exit()

result = [i for i in range(len(input_list)+1)]
#print(f'input_list:{input_list}, result:{result}')

def set_parent(student_id, result):
    if result[student_id] != student_id:
        result[student_id] = set_parent(result[student_id], result)
    return result[student_id]

prev = None
for student in input_list:
    student_id, is_same_class = student
    if is_same_class == 1:
        #print(f'student_id: {student_id}, prev: {prev}')
        result[student_id] =  prev if prev is not None else student_id
        #print(f'result: {result}\n')
        result[student_id] = set_parent(student_id, result)
    prev = student_id

# prev = 0
# for class_id in result:
#     if class_id != prev:

klass = {}
for id, cls in enumerate(result):
    if id == 0:
        continue
    if cls not in klass:
        klass[cls] = []
    klass[cls].append(id)
#print(f'klass:{klass}')


#print(f'{result}')
for members in klass.values():
    print(*members)