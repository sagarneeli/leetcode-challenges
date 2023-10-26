class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students, sandwiches = deque(students), deque(sandwiches)
        while sandwiches:
            student = students[0]
            if student == sandwiches[0]:
                sandwiches.popleft()
            else:
                if sandwiches[0] not in students:
                    break
                students.append(student)
            students.popleft()
        return len(students)