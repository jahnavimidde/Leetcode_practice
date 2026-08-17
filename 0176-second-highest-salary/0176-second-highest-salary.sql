SELECT MAX(e.salary) AS SecondHighestSalary
FROM Employee e
WHERE e.salary < (
    SELECT MAX(e2.salary)
    FROM Employee e2
);