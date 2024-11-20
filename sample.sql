-- intersect
select customer_id from sales_2015
intersect all
select customer_id from customer_20_60

select customer_id from sales_2015 order by customer_id
select customer_id from customer_20_60 order by customer_id

-- except
select customer_id from sales_2015 where customer_id like 'A%'
except
select customer_id from customer_20_60
order by customer_id

-- union, must have the same number of fields/columns/attributes
select customer_id from sales_2015
union
select customer_id from customer_20_60
order by customer_id limit 10

-- exercise 10 number 1
select customer_20_60.state, sum(sales_2015.sales)
from customer_20_60
left join sales_2015
on customer_20_60.customer_id = sales_2015.customer_id
group by customer_20_60.state

-- number 2
select product.product_id, product_name, category, sum(sales.sales) as "Total Sales"
from product
left join sales
on product.product_id = sales.product_id
group by product.product_id

-- subqueries
select *, age from sales, customer where customer.customer_id in
(select customer.customer_id from customer where age > 60)

select a.product_id, a.product_name, b."Quantiy of Product"
from product as a
left join (select product_id, sum(quantity) as "Quantiy of Product" from sales group by product_id) as b
on a.product_id = b.product_id
order by b."Quantiy of Product" desc;

select *, age from sales
left join customer
on sales.customer_id = customer.customer_id
order by sales.customer_id desc;

select * from sales
left join (select customer_id, customer_name, age from customer) as b
on sales.customer_id = b.customer_id

-- Exercise 11 took a while to figure it out lol
select sales.*, cus.customer_name, cus.age,
p.product_name, p.category
from customer as cus,
product as p, sales
-- left join sales
-- on sales.product_id = p.product_id

-- Exercise 11 2nd approach
select sales.*, customer_name, age, p.product_name, p.category from (select * from sales
left join customer on sales.customer_id = customer.customer_id),
product as p
left join sales
on sales.product_id = p.product_id

create view logistics as 
select a.order_line, a.order_id, b.customer_name, b.city, b.state, b.country
from sales as a
left join customer as b
on a.customer_id = b.customer_id
order by a.order_line;