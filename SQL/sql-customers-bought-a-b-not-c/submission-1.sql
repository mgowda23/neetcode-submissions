-- Write your query below
select c.customer_id, c.customer_name
from customers c
join orders o1
    on c.customer_id = o1.customer_id and o1.product_name in ('A', 'B') 
left join orders o2
    on c.customer_id = o2.customer_id and o2.product_name ='C'
where o2.customer_id is NULL
group by c.customer_id
HAVING COUNT(Distinct o1.product_name) = 2
order by c.customer_name;