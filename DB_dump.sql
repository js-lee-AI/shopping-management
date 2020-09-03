drop database postshop;
create database postshop;
use postshop;


create table MEMBERSHIPLEVEL(
   mem_ID integer not null primary key,
    mem_condition integer not null,
    mem_name varchar(10) not null);
    
    
create table CUSTOMER(
   customer_ID varchar(20) not null primary key,
    mem_ID integer not null,
    customer_pw varchar(20) not null,
    customer_name varchar(10) not null,
    customer_address varchar(50) not null,
    customer_phone varchar(15) not null,
    customer_gender varchar(5) not null,
    customer_mileage integer,
    foreign key(mem_ID) references MEMBERSHIPLEVEL(mem_ID));
    
    
create table delivery(
   delivery_num integer not null primary key,
    delivery_shipcost integer not null,
    delivery_date integer not null,
    delivery_code varchar(5) not null);
    
    
create table warehouse(
   warehouse_code integer not null primary key,
    warehouse_locat varchar(50) not null,
    warehouse_phone integer not null);
    
    
create table provider(
   provider_num integer not null primary key,
    provider_phone integer not null,
    provider_addr varchar(50) not null,
    provider_account integer not null,
    provider_name varchar(20) not null,
    provider_contract_due integer not null);
    
    
create table product(
   product_code integer not null primary key,
    provider_num integer not null,
    product_kind varchar(10) not null,
    product_price integer not null,
    warehouse_code integer not null,
    product_name varchar(20) not null,
    product_stock integer not null,
    product_disrate integer,
    foreign key(provider_num) references provider(provider_num) ON UPDATE CASCADE, 
    foreign key(warehouse_code) references warehouse(warehouse_code) ON DELETE CASCADE ON UPDATE CASCADE
    ) ;   
    
    
create table orders(
   order_code integer not null primary key,
    customer_ID varchar(20) not null,
    delivery_num integer not null,
    order_date integer not null,
    order_price integer not null,
    order_status varchar(10) not null,
    product_code integer not null,
    foreign key(product_code) references product(product_code) ON DELETE CASCADE ON UPDATE CASCADE,
    foreign key(customer_ID) references CUSTOMER(customer_ID)  ON UPDATE CASCADE,
    foreign key(delivery_num) references delivery(delivery_num) 
   
    );
    
    
create table basket(
	basket_id integer not null,
    customer_ID varchar(20) not null,
    product_name varchar(20) not null,
    primary key(basket_id, customer_ID),
    foreign key(customer_ID) references customer(customer_ID));


insert into MEMBERSHIPLEVEL values(1000, 0, "NORMAL");
insert into MEMBERSHIPLEVEL values(1010, 50, "VIP");
insert into MEMBERSHIPLEVEL values(1020, 100, "VVIP");
insert into MEMBERSHIPLEVEL values(1030, 150, "SVIP");
insert into CUSTOMER values("kcs11", 1010, "asd", "김철수", "서울시 중구...", "01011112222", "M", 5000);
insert into CUSTOMER values("lgh22", 1030, "zxc", "이건희", "서울시 서초구...", "01033334444", "M", 10200);
insert into CUSTOMER values("jnr33", 1020, "qwe", "장나라", "서울시 마포구...", "01055556666", "F", 1000);
insert into CUSTOMER values("operator", 1030, "asd", "비공개", "비공개", "비공개", "M", 1000000);
insert into delivery values(159102, 5000, 20191016, "S");
insert into delivery values(192852, 2500, 20191018, "N");
insert into delivery values(192853, 5000, 20191018, "S");
insert into delivery values(214002, 2500, 20191020, "N");
insert into delivery values(222402, 5000, 20191021, "S");
insert into delivery values(249182, 20000, 20191023, "S");
insert into provider values(101044, 01032143124, "서울시 용산구...", 1104928492, "넝협 특산물전문", 20140322);
insert into provider values(101402, 01009120912, "서울시 동대문구...", 1302901213, "동국 음식", 20150117);
insert into provider values(124599, 01057895789, "서울시 강남구...", 1078928561, "동국 가구", 20150703);
insert into warehouse values(55609, "경기도 이천시...", 0310449293);
insert into warehouse values(59201, "경기도 포천시...", 0319874302);
insert into warehouse values(77209, "대구 광역시...", 0532948239);
insert into product values(1, 101044, "local", 40000, 55609, "이천쌀", 1024, 10);
insert into product values(2, 101044, "local", 100000, 55609, "이천도자기", 21, 25);
insert into product values(3, 101044, "local", 50000, 55609, "포항과메기", 304, 10);
insert into product values(4, 101402, "food", 30000, 59201, "참치캔", 978, 20);
insert into product values(5, 101402, "food", 30000, 59201, "식용유", 978, 35);
insert into product values(6, 101402, "food", 35000, 59201, "스팸", 978, 20);
insert into product values(7, 124599, "fur", 200000, 77209, "침대", 978, 0);
insert into product values(8, 124599, "fur", 150000, 77209, "책상", 978, 60);
insert into product values(9, 124599, "fur", 70000, 77209, "의자", 978, 10);
insert into orders values(19101501, "lgh22", 0159102, 20191015, 40000, "배송완료", 1); 
insert into orders values(19101611, "kcs11", 0192852, 20191016, 30000,"배송중", 5); 
insert into orders values(19101627, "lgh22", 0192853, 20191016, 30000, "배송중", 4); 
insert into orders values(19101702, "jnr33", 0214002, 20191017, 200000, "배송준비", 7);
insert into orders values(19101711, "kcs11", 0222402, 20191017, 40000,"배송준비", 1); 
insert into orders values(19101911, "kcs11", 0249182, 20191019, 100000,"배송준비", 2); 

-- insert into basket values(1, "kcs11", "식용유");
-- insert into basket values(2, "kcs11", "스팸");

select mem_name
from MEMBERSHIPLEVEL
where mem_condition > 100;
select product_name
from product
where product_disrate > 30;
select customer_name, m.mem_name
from customer as c, membershiplevel as m
where c.mem_ID = m.mem_ID;
select o.delivery_num, customer_id, delivery_shipcost
from orders as o, delivery as d
where o.delivery_num = d.delivery_num;
select product_name
from product
where product_disrate>30
union
(select product_name
from product
where product_stock>500);
select customer_ID
from orders
where order_price > 100000
union
(select customer_ID
from orders
where order_status = "배송중");
select mem_name, count(*) as cnt
from membershiplevel
group  by mem_name;
select order_status, count(*) as cnt
from orders
group by order_status
order by cnt;
select customer_name, customer_mileage
from customer
where customer_id in (select customer_id
from orders
where order_status = "배송중");
select provider_name
from provider
where provider_num in (select provider_num
from product
where product_stock > 900);
select mem_ID, mem_name
from membershiplevel as m
where exists(select * 
			 from customer as c 
			 where m.mem_id = c.mem_id and
				   customer_gender = 'F');
select order_code, order_status
from orders as o
where exists(select *
			 from customer as c
             where o.customer_id = c.customer_id and
                   customer_phone = 1011112222 );
SET SQL_SAFE_UPDATES = 0;
update product
set product_disrate = 15
where product_name = "이천쌀";
select product_name,product_disrate
from product
where product_name = "이천쌀";
update orders
set order_status = "배송완료"
where order_code = 19101611;
-- join
select customer_name, customer_address, order_status
from customer as c
join orders as o
on c.customer_id = o.customer_id;
-- order by
select order_price, customer_ID
from orders
order by order_price desc;
-- any
select distinct c.customer_name
from customer as c
where c.customer_id = any(select o.customer_id from orders as o where o.order_status="배송완료");
-- not in
insert into provider values(125689, 01041554155, "서울시 관악구...", 1948273915, "동국제약", 20180421);
select provider_name
from provider as v
where v.provider_num not in(select d.provider_num from product as d);
-- distinct
select distinct(customer_name)
from customer
where customer_ID IN (select o.customer_id
					  from orders o);
                      
                      use postshop;

DELIMITER // 
	drop procedure if exists total_revenue;
	CREATE PROCEDURE total_revenue(OUT t_revenue INTEGER) 
    BEGIN 
		SELECT SUM(order_price) INTO t_revenue 
        FROM orders;
    END //
DELIMITER ;  

call total_revenue(@a);


DELIMITER //
	drop function if exists status_delivery;

	create function status_delivery(o_code integer) 
    returns table
	BEGIN
		declare d_status varchar(10);
		set d_status = null;
		
		select order_status INTO d_status from orders where order_code=o_code;
		return d_status;
		
	END //
DELIMITER ;

select status_delivery(19101627);

-- SET GLOBAL log_bin_trust_function_creators = 1;
-- from `order`;
                 