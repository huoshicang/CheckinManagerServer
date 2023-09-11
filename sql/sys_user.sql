-- `sys_user`
create table if not exists `sys_user`
(
`id` int not null auto_increment comment 'id' primary key,
`username` varchar(10) not null comment '用户名',
`phone` varchar(11) not null comment '手机号',
`password` varchar(12) not null comment '用户名',
`token` longtext null,
`role` varchar(5)  default 'user'  not null comment '角色',
`gxy_info` varchar(5) not null comment '用户名',
`is_deleted` varchar(5) default 'false'  not null comment '是否删除'
) comment '`sys_user`';



insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (1, '管理员', '17097780811', 'sj4qO', 'admin', 'true', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (2, '彭思聪', '14711003249', 'X82G', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (3, '韩智辉', '17789772547', 'Ol0ze', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (4, '董伟祺', '15341369862', '5t3M', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (5, '孙烨华', '17701957286', 'WP', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (6, '魏越彬', '17046219853', 'D5', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (7, '赵伟诚', '17296220778', 'ZB', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (8, '阎越彬', '17237373391', '1sz8', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (9, '沈鸿涛', '15813041654', 'ZRKow', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (10, '汪炫明', '15941044042', 'Nq', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (11, '梁哲瀚', '17728796032', 'xjU', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (12, '阎明辉', '17652027963', 'Ki0Wr', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (13, '陆哲瀚', '17157284756', 'SVV2', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (14, '崔鸿煊', '15776502343', 'k3PX', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (15, '孔鸿煊', '17860780294', 'DVr', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (16, '邓擎苍', '15988081996', 'jr', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (17, '雷正豪', '17270731647', '70Bz', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (18, '曾健雄', '17612337186', 'q9J5P', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (19, '龙鹏涛', '15028694899', 'Plx', 'user', 'false', 'false');
insert into `sys_user` (`id`, `username`, `phone`, `password`, `role`, `gxy_info`, `is_deleted`) values (20, '贾懿轩', '15689438888', 'nDh', 'user', 'false', 'false');


