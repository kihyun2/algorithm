SELECT PRODUCT_CODE, (price*sum_sales_amount) as SALES
from product a join (select product_id, sum(sales_amount) as sum_sales_amount
                  from offline_sale
                  group by product_id ) b on a.product_id = b.product_id
group by product_code
order by SALES desc, product_code asc
