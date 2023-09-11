-- `sys_user`
create table if not exists `sys_user`
(
`id` int not null auto_increment comment 'id' primary key,
`username` varchar(10) not null comment '用户名',
`phone` varchar(11) not null comment '手机号',
`password` varchar(12) not null comment '密码',
`token` longtext null comment 'token',
`role` varchar(5) default 'user' not null comment '角色',
`gxy_info` varchar(5) default 'fasle' not null comment '用户名',
`is_deleted` tinyint default 0 not null comment '是否删除',
`update_time` datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间'
) comment '`sys_user`';


insert into `sys_user` (`username`, `phone`, `password`) values ('卢擎苍', '15751122669', 'UJzHC');
insert into `sys_user` (`username`, `phone`, `password`) values ('胡梓晨', '15847531353', 'lxIr');
insert into `sys_user` (`username`, `phone`, `password`) values ('范俊驰', '17242316426', 'uD');
insert into `sys_user` (`username`, `phone`, `password`) values ('廖彬', '17820176778', 'LXYvj');
insert into `sys_user` (`username`, `phone`, `password`) values ('彭鸿煊', '14557964776', 'Wv');
insert into `sys_user` (`username`, `phone`, `password`) values ('史耀杰', '15717610631', 'S9');
insert into `sys_user` (`username`, `phone`, `password`) values ('邱博文', '17238559379', '7A');
insert into `sys_user` (`username`, `phone`, `password`) values ('韦立果', '17211941809', 'fzf');
insert into `sys_user` (`username`, `phone`, `password`) values ('尹烨霖', '17559501805', 'wT3mq');
insert into `sys_user` (`username`, `phone`, `password`) values ('余荣轩', '15395271133', 'S9UDR');
insert into `sys_user` (`username`, `phone`, `password`) values ('程君浩', '17154209708', 'gEFod');
insert into `sys_user` (`username`, `phone`, `password`) values ('郭绍齐', '14735596327', 'rbf');
insert into `sys_user` (`username`, `phone`, `password`) values ('贾越泽', '15955514339', 'Shasf');
insert into `sys_user` (`username`, `phone`, `password`) values ('韦越彬', '15639551731', 'cV');
insert into `sys_user` (`username`, `phone`, `password`) values ('叶楷瑞', '17232024152', 'Nwbly');
insert into `sys_user` (`username`, `phone`, `password`) values ('覃弘文', '17736706303', 'fI');
insert into `sys_user` (`username`, `phone`, `password`) values ('沈明杰', '15768348113', 'jsoTa');
insert into `sys_user` (`username`, `phone`, `password`) values ('黄哲瀚', '17591915284', 'bY');
insert into `sys_user` (`username`, `phone`, `password`) values ('秦振家', '14736946304', 'baQ');
insert into `sys_user` (`username`, `phone`, `password`) values ('杨语堂', '17279666113', '0Xjl');