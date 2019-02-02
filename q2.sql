# written by Lingzhi Zhang
# sql query to answer certain questions

## question 1
# 在users表中查询注册时间最早的十条会员信息。
select * from users where cdate order by cdate limit 10;

## question 2
# 从两个表中查询点赞数最高的5条博客信息，要求显示字段：（博文id，标题，点赞数，会员名）
select blog.id, blog.title, blog.pcount, users.name
from blog 
left join users on users.id = blog.uid 
order by pcount desc 
limit 5;

 ## question 3
 # 统计每个会员的发表博文数量（降序），要求显示字段（会员id号，姓名，博文数量）
select users.id,users.name,count(blog.id) as numOfBlog
from users 
inner join blog 
on users.id = blog.uid 
group by blog.uid;

## question 4
# 获取会员的博文平均点赞数量最高的三位。显示字段（会员id，姓名，平均点赞数）
select users.id, users.name, avg(blog.pcount) as avgPoke 
from users 
inner join blog 
on users.id = blog.uid 
group by blog.uid;

## question 5
# 删除没有发表博文的所有会员信息。
delete users, blog
from users inner join blog 
on users.id = blog.id 
where users.id not in 
(select * from 
	(select blog.uid from blog ) as b);


