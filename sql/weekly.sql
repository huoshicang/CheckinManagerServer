-- 周报信息
create table if not exists `weeklydata`
(
`weekly_id` int not null auto_increment comment '周报信息id' primary key,
`username` varchar(5) not null comment '用户名',
`title` longtext not null comment '周报标题',
`content` longtext not null comment '周报内容',
`weekly_time` datetime not null comment '周报提交时间',
`sub` tinyint(1) default 0 not null comment '是否已交',
`is_deleted` tinyint(1) default 0 not null comment '是否删除',
`enable` tinyint(1) default 0 not null comment '是否启用',
`create_time` datetime default CURRENT_TIMESTAMP not null comment '创建时间',
`update_time` datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间'
) comment '周报信息';


insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (1, '黄昊天', '首当其冲', '蔡徐坤', '2022-02-05 06:15:42');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (2, '方博涛', '先发制人', '练习', '2022-04-24 22:50:27');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (3, '金苑博', '意想不到', '鸡', '2022-01-12 17:50:14');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (4, '赵烨霖', '奋发有为', '太', '2022-12-24 00:37:36');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (5, '蔡峻熙', '无可厚非', '唱', '2022-11-22 06:46:27');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (6, '黄弘文', '任重道远', '美', '2022-05-24 23:45:00');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (7, '魏修洁', '继往开来', '篮球', '2022-05-08 12:26:32');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (8, '陆弘文', '触目惊心', '你', '2022-04-20 05:56:36');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (9, '吴旭尧', '见义勇为', '个人练习生', '2022-07-08 03:57:49');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (10, '林嘉懿', '可乘之机', '练习', '2022-06-27 16:50:23');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (11, '史弘文', '排忧解难', 'rap', '2022-01-07 07:14:11');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (12, '罗立轩', '四面八方', '两年半', '2022-10-01 22:15:38');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (13, '萧弘文', '深入人心', '时长', '2022-09-11 07:38:39');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (14, '吴凯瑞', '一举一动', '你', '2022-04-15 13:41:39');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (15, '史鑫鹏', '未雨绸缪', '唱', '2022-04-19 02:12:03');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (16, '韩智渊', '脱颖而出', 'rap', '2022-06-10 08:59:18');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (17, '曹煜城', '名列前茅', '两年半', '2022-03-16 05:15:07');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (18, '李智渊', '引人注目', 'music', '2022-10-31 08:13:26');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (19, '韩思聪', '可见一斑', 'music', '2022-05-18 03:47:25');
insert into `weeklydata` (`weekly_id`, `username`, `title`, `content`, `weekly_time`) values (20, '陈正豪', '可见一斑', '你', '2022-06-25 05:53:41');

