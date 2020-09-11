import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', password='950205', charset='utf8',db='postshop', port= 3306)

# Connection 으로부터 Cursor 생성
curs = conn.cursor()

# Where statement에 대한 쿼리문
print('\n\nShow all product names with discount rate over 30%(30).')
sql = """
select product_name
from product
where product_disrate > 30;"""
num = curs.execute(sql) # 위의 sql 구문을 execute.
where_host = curs.fetchall() # 'where_host' 이름을 가진 Host Variable에 sql 결과 삽입.

print("====================================================================")
for i in range(num):
    print('\t'+str(i)+'\t\t\t'+where_host[i][0])
print("====================================================================")

#From statement에 대한 쿼리문
print('\n\nShow membership levels for all customers.')
sql = """
select customer_name, m.mem_name
from customer as c, membershiplevel as m
where c.mem_ID = m.mem_ID;"""

num = curs.execute(sql) # 위의 sql 구문을 execute.
from_host = curs.fetchall() # 'from_host' 이름을 가진 Host Variable에 sql 결과 삽입.

print("====================================================================")
for i in range(num):
    print('\t'+str(i)+'\t\t\t'+from_host[i][0]+'\t\t\t'+from_host[i][1])
print("====================================================================")


#SET operation에 대한 쿼리문
sql = """
select product_name
from product
where product_disrate>30
union
(select product_name
from product
where product_stock>500);"""

num = curs.execute(sql) # 위의 sql 구문을 execute.
set_host = curs.fetchall() # 'set_host' 이름을 가진 Host Variable에 sql 결과 삽입.
print('\n\nShow all the names of products which stock is grater than 500 or a discount rate greater than 30%.')
print("====================================================================")
for i in range(num):
    print('\t'+str(i)+'\t\t\t'+set_host[i][0])
print("====================================================================")


# EXISTS statement에 대한 쿼리문
print('\n\nShow delivery status of customers whose phone number is 1011112222(integer)')
sql = """
select order_code, order_status
from orders as o
where exists(select *
	     from customer as c
             where o.customer_id = c.customer_id and
                    customer_phone = 1011112222 );"""

num = curs.execute(sql) # 위의 sql 구문을 execute.
exists_host = curs.fetchall() # 'exists_host' 이름을 가진 Host Variable에 sql 결과 삽입.
print("====================================================================")
for i in range(num):
    print('\t'+str(i)+'\t\t\t'+str(exists_host[i][0])+'\t\t\t'+exists_host[i][1])
print("====================================================================")


#### 2-1 procedure ####
print('\n\n')
sql = ["call total_revenue(@a);",
       "select @a;"]

for i in sql:
    curs.execute(i)# 위의 sql 구문을 execute.
procedure_host = curs.fetchall()

print("Define a procedure which shows total revenue. And use it.")
print("====================================================================")
print('\t'+str(1)+'\t\t\t'+str(procedure_host[0][0]))
print("====================================================================")
##################



#### 2-2 function ####
print("\n\nDefine a function which shows the status of delivery given 'order_code'. And use it when 'order_code' is '1910627'.")
sql = """
SELECT status_delivery(19101627);
"""

curs.execute(sql)# 위의 sql 구문을 execute.
function_host = curs.fetchall()

print("====================================================================")
print('\t'+'1'+'\t\t\t'+function_host[0][0])
print("====================================================================")
##################

print('\n\n\n\n')


####### 2-3 #########
print("1. Check Total Revenue.")
print("2. Check whether the order can be canceled or not.")
print("3. Cancel Order \n\n")

menu = input("Select num >> ")
menu = int(menu)
if menu == 1:
    #### 2-1 procedure ####
    print('\n\n')
    sql = ["call total_revenue(@a);",
           "select @a;"]

    for i in sql:
        curs.execute(i)  # 위의 sql 구문을 execute.
    procedure_host = curs.fetchall()

    print("Define a procedure which shows total revenue. And use it.")
    print("====================================================================")
    print('\t' + str(1) + '\t\t\t' + str(procedure_host[0][0]))
    print("====================================================================")

elif menu == 2:
    #### 2-2 function ####
    print(
        "\n\nDefine a function which shows the status of delivery given 'order_code'. And use it when 'order_code' is '1910627'.")
    sql = """
    SELECT status_delivery(19101627);
    """

    curs.execute(sql)  # 위의 sql 구문을 execute.
    function_host = curs.fetchall()

    print("====  Check whether the order can be canceled or not. ====")
    ord_code = input("Input the Order_code >>")

    if( (function_host[0][0] == '배송중')):
        print("{} is Can not Cancel the order! (Already Shipping)".format(ord_code))
    elif( (function_host[0][0] == '배송완료')):
        print("{} is Can not Cancel the order! (Already Delivered)".format(ord_code))
    else:
        print("{} is Can be canceled !".format(ord_code))


    print("====================================================================")
    print('\t' + '1' + '\t\t\t' + function_host[0][0])
    print("====================================================================")

elif menu == 3:
    ord_code = input("Input the Order_code >>")
    print(" {th} Cancel is successful\n\n. ".format(th=ord_code))

    sql = "delete from order where order_code = {tn}".format(tn=int(ord_code))
    curs.execute(sql)  # 위의 sql 구문을 execute.
    print(" {th} Cancel is successful ".format(th=ord_code))
