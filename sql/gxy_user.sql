# -- auto-generated definition
# create table gxy_user
# (
#     id        int(255) unsigned auto_increment comment 'id'
#         primary key,
#     enable    varchar(5) default 'true'    not null comment '启停',
#     name      varchar(10)                  not null comment '姓名',
#     phone     varchar(11)                  not null comment '手机号',
#     password  varchar(15)                  not null comment '密码',
#     token     varchar(400)                 null comment '个人标识',
#     userId    varchar(30)                  null comment '个人Id',
#     planId    varchar(40)                  null comment '计划Id',
#     country   varchar(2) default '中国'    not null comment '国家',
#     province  varchar(10)                  not null comment '省份',
#     city      varchar(10)                  not null comment '城市',
#     area      varchar(10)                  not null comment '区/县',
#     address   varchar(255)                 not null comment '详细地址',
#     longitude varchar(20)                  null comment '经度',
#     latitude  varchar(20)                  null comment '纬度',
#     note      varchar(255)                 null comment '打卡备注',
#     type      char(20)   default 'android' not null comment '签到设备',
#     pushKey   varchar(50)                  not null comment '推送token',
#     save_time datetime                     null comment '签到时间'
# )
#     charset = utf8;
#






-- `gxy_user`
create table if not exists `gxy_user`
(
`id` int not null auto_increment comment 'id' primary key,
`enable` varchar(5) default 'true' not null comment '启停',
`name` varchar(10) not null comment '姓名',
`phone` varchar(11) not null comment '手机号',
`password` varchar(15) not null comment '密码',
`token` varchar(400) null comment '个人标识',
`userId` varchar(30) null comment '个人Id',
`planId` varchar(40) null comment '计划Id',
`country` varchar(2) default '中国' not null comment '国家',
`province` varchar(10) not null comment '省份',
`city` varchar(10) not null comment '城市',
`area` varchar(10) not null comment '区/县',
`address` varchar(255) not null comment '详细地址',
`longitude` varchar(20) null comment '经度',
`latitude` varchar(20) null comment '纬度',
`note` varchar(255) null comment '打卡备注',
`type` char(20) default 'android' not null comment '签到设备',
`pushKey` varchar(50) not null comment '推送token',
`save_time` datetime null comment '签到时间'
) comment '`gxy_user`';

insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('魏正豪', '15750480195', '123', '内蒙古', '辉县市', '计算机科学与技术', 'www.jean-dietrich.org', '83699.65', '58587.9', '184.254.24.150', 'RN', '2022-12-21 15:01:06');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('罗志泽', '15886896249', '123', '台湾', '威海市', '软件工程', 'www.milford-mcclure.com', '71817.0', '8397.049', '147.242.148.103', 'Fg8sV', '2022-01-31 23:12:19');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('彭哲瀚', '17511028467', '123', '台湾', '峨眉山市', '软件工程', 'www.kayla-gleichner.io', '3724.5571', '80438.29', '218.10.82.61', '0d', '2022-06-29 17:12:40');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('马越彬', '15007787787', '123', '广东', '文山市', '软件工程', 'www.valene-walsh.com', '37711.16', '17713.959', '14.190.249.71', 'dMY', '2022-03-07 00:50:18');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('王弘文', '15178786715', '123', '福建', '都匀市', '计算机科学与技术', 'www.garfield-wehner.co', '93168.25', '12003.397', '153.165.145.232', '6LTyz', '2022-08-23 22:02:39');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('黎乐驹', '14599598908', '123', '湖北', '西安市', '大数据科学与技术', 'www.mariam-funk.info', '27123.809', '4603.2427', '218.250.85.44', 'UB7Dg', '2022-04-05 19:43:44');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('陈煜祺', '17099892684', '123', '海南', '临江市', '计算机科学与技术', 'www.douglas-ratke.io', '79008.92', '10849.16', '78.209.3.121', 'GaV0', '2022-07-09 16:17:27');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('孟烨霖', '14526274175', '123', '湖南', '厦门市', '计算机科学与技术', 'www.daria-abernathy.name', '54846.863', '14355.1', '4.35.30.61', '10', '2022-08-05 04:06:29');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('方潇然', '17108687419', '123', '青海', '库尔勒市', '计算机科学与技术', 'www.marcus-nader.com', '1348.1796', '66711.85', '132.112.77.209', 'yw', '2022-11-14 18:18:02');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('罗明', '17869468901', '123', '上海', '锡林浩特市', '大数据科学与技术', 'www.hyun-christiansen.com', '84439.35', '8484.482', '118.107.151.232', 'WAf', '2022-02-15 20:59:42');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('方志泽', '15616764817', '123', '云南', '麻城市', '软件工程', 'www.eula-labadie.biz', '86571.52', '9579.658', '37.200.163.33', 'LyKjr', '2022-03-03 10:38:30');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('李智辉', '14593473373', '123', '河北', '华阴', '计算机科学与技术', 'www.freddie-dooley.info', '50585.35', '70508.984', '245.168.28.12', '5mF0', '2022-05-24 22:18:24');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('董煜祺', '15605944073', '123', '新疆', '恩平市', '软件工程', 'www.dong-hintz.name', '60783.434', '5969.8164', '252.224.133.25', '2Ctdi', '2022-09-30 16:05:36');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('吕天宇', '15319743328', '123', '河北', '阆中市', '软件工程', 'www.elana-glover.net', '60336.33', '176.48935', '23.39.79.200', 'QcaT', '2022-11-29 20:24:00');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('董博涛', '15587066844', '123', '江西', '南昌市', '软件工程', 'www.deadra-yundt.io', '11996.973', '95754.266', '16.85.255.254', 'Jy4Zs', '2022-12-29 02:29:57');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('雷鹏飞', '15304132360', '123', '内蒙古', '香港', '软件工程', 'www.courtney-nicolas.org', '21930.873', '65936.26', '161.96.36.156', 'EaJ1', '2022-05-10 18:16:26');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('罗博超', '15953116887', '123', '澳门', '吉林市', '软件工程', 'www.clement-hill.name', '17958.004', '19556.541', '11.209.250.219', 'Kk', '2022-07-28 12:48:23');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('唐伟祺', '15196061547', '123', '上海', '长治市', '大数据科学与技术', 'www.julio-bashirian.io', '36803.84', '76968.1', '210.242.213.189', 'ww93', '2022-07-26 15:12:44');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('程懿轩', '17274144320', '123', '甘肃', '运城市', '计算机科学与技术', 'www.margorie-luettgen.co', '95676.805', '90401.016', '49.209.18.195', 'H4D', '2022-10-26 16:28:41');
insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`, `save_time`) values ('孔明轩', '15036859054', '123', '湖北', '北海市', '大数据科学与技术', 'www.youlanda-wolff.org', '38625.844', '84423.086', '59.153.115.211', '9Wh', '2022-08-04 06:28:35');
















