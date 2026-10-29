class Solution:
    def average(self, salary: list[int]) -> float:
        a=sum(salary)-(max(salary)+min(salary))
        return a/(len(salary)-2)
          
