-- Write your query below
-- MYSQL
-- select employee_id, IF( employee_id %2 !=0 and name NOT like 'M%', salary ,0 ) as bonus
-- from employees
-- order by employee_id;
-- PostgreSQL we use Case when
select employee_id,
case
    when employee_id %2 !=0 and name NOT like 'M%' then salary
    else 0
end as Bonus
from employees
order by employee_id;