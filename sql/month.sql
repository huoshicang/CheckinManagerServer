-- 月报信息
create table if not exists `monthdata`
(
`month_id` int not null auto_increment comment '月报信息id' primary key,
`username` varchar(5) not null comment '用户名',
`title` longtext not null comment '月报标题',
`content` longtext not null comment '月报内容',
`month_time` datetime not null comment '月报提交时间',
`sub` tinyint(1) default 0 not null comment '是否已交',
`is_deleted` tinyint(1) default 0 not null comment '是否删除',
`enable` varchar(5) default 'true' not null comment '是否启用',
`create_time` datetime default CURRENT_TIMESTAMP not null comment '创建时间',
`update_time` datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间'
) comment '月报信息';


# insert into `monthdata` (`username`, `title`, `content`, `weekly_time`) values
# ('胡梓晨', '月报标题1', '月报内容1', '2023-09-20 09:30:00'),
# ('范俊驰', '月报标题2', '月报内容2', '2023-09-21 14:45:00'),
# ('廖彬', '月报标题3', '月报内容3', '2023-09-22 11:20:00'),
# ('彭鸿煊', '月报标题4', '月报内容4', '2023-09-23 16:55:00'),
# ('史耀杰', '月报标题5', '月报内容5', '2023-09-24 08:10:00'),
# ('邱博文', '月报标题6', '月报内容6', '2023-09-25 10:05:00'),
# ('韦立果', '月报标题7', '月报内容7', '2023-09-26 12:40:00'),
# ('尹烨霖', '月报标题8', '月报内容8', '2023-09-27 17:15:00'),
# ('余荣轩', '月报标题9', '月报内容9', '2023-09-28 09:50:00'),
# ('程君浩', '月报标题10', '月报内容10', '2023-09-29 13:25:00'),
# ('郭绍齐', '月报标题11', '月报内容11', '2023-09-30 15:00:00'),
# ('贾越泽', '月报标题12', '月报内容12', '2023-10-01 07:35:00'),
# ('韦越彬', '月报标题13', '月报内容13', '2023-10-02 10:20:00'),
# ('叶楷瑞', '月报标题14', '月报内容14', '2023-10-03 11:45:00'),
# ('覃弘文', '月报标题15', '月报内容15', '2023-10-04 14:30:00'),
# ('沈明杰', '月报标题16', '月报内容16', '2023-10-05 16:05:00'),
# ('黄哲瀚', '月报标题17', '月报内容17', '2023-10-06 08:40:00'),
# ('秦振家', '月报标题18', '月报内容18', '2023-10-07 11:15:00'),
# ('杨语堂', '月报标题19', '月报内容19', '2023-10-08 12:50:00');


-- 为每个用户插入随机数量的月报，最少1篇，最多5篇
insert into `monthdata` (`username`, `title`, `content`, `month_time`)
select
  `username`,
  CONCAT('月报标题', FLOOR(RAND() * 5) + 1), -- 随机生成1到5之间的整数作为标题后缀
  CONCAT('月报内容', FLOOR(RAND() * 5) + 1), -- 随机生成1到5之间的整数作为内容后缀
  DATE_ADD('2022-02-05 06:15:42', INTERVAL FLOOR(RAND() * 30) DAY) -- 随机生成从2022-02-05开始的30天内的日期
from (
  select '黄昊天' as `username` union
  select '胡梓晨' union
  select '范俊驰' union
  select '廖彬' union
  select '彭鸿煊' union
  select '史耀杰' union
  select '邱博文' union
  select '韦立果' union
  select '尹烨霖' union
  select '余荣轩' union
  select '程君浩' union
  select '郭绍齐' union
  select '贾越泽' union
  select '韦越彬' union
  select '叶楷瑞' union
  select '覃弘文' union
  select '沈明杰' union
  select '黄哲瀚' union
  select '秦振家' union
  select '杨语堂'
) AS Users;

