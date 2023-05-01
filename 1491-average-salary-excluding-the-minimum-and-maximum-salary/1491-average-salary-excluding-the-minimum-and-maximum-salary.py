class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        salary.remove(min_salary)
        salary.remove(max_salary)
        return sum(salary) / len(salary)
        