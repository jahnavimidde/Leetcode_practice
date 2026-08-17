select max(e.salary) as SecondHighestSalary
from employee e
where exists(
    select 1
    from employee e2
    where e2.salary>e.salary
) and not exists(
    select 1 
    from employee e3
    where e3.salary>e.salary
    and exists(
        select 1 
        from employee e4
        where e4.salary>e3.salary
    )
);



#  Aggregate functions always return one row;   so use max(e.salary)