# Write your MySQL query statement below


#

select e.employee_id,e.department_id
from Employee e
where e.primary_flag='Y' or (employee_id,department_id) IN
(select d.employee_id,d.department_id
from Employee d
group by employee_id
having count(d.employee_id)=1);


