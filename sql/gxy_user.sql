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
`enable` varchar(5) default 'false' not null comment '启停',
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
`save_time` datetime null comment '签到时间',
`is_deleted` tinyint default 1 not null comment '是否删除',
`create_time` datetime default CURRENT_TIMESTAMP not null comment '创建时间',
`update_time` datetime default CURRENT_TIMESTAMP not null on update CURRENT_TIMESTAMP comment '更新时间'
) comment '`gxy_user`';

insert into `gxy_user` (`name`, `phone`, `password`, `province`, `city`, `area`, `address`, `longitude`, `latitude`, `note`, `pushKey`) values
('胡梓晨', '12345678901', 'password1', '北京市', '北京市', '朝阳区', '北京市 · 朝阳区 · 示例地址1', '123.45', '67.89', '示例备注1', '推送Key1'),
('范俊驰', '98765432109', 'password2', '上海市', '上海市', '浦东新区', '上海市 · 浦东新区 · 示例地址2', '234.56', '78.90', '示例备注2', '推送Key2'),
('廖彬', '13579246801', 'password3', '广州市', '广州市', '天河区', '广州市 · 天河区 · 示例地址3', '345.67', '89.01', '示例备注3', '推送Key3'),
('彭鸿煊', '56789012345', 'password4', '深圳市', '深圳市', '南山区', '深圳市 · 南山区 · 示例地址4', '456.78', '90.12', '示例备注4', '推送Key4'),
('史耀杰', '32109876543', 'password5', '杭州市', '杭州市', '西湖区', '杭州市 · 西湖区 · 示例地址5', '567.89', '12.34', '示例备注5', '推送Key5'),
('邱博文', '65432109876', 'password6', '成都市', '成都市', '锦江区', '成都市 · 锦江区 · 示例地址6', '678.90', '23.45', '示例备注6', '推送Key6'),
('韦立果', '23456789012', 'password7', '南京市', '南京市', '鼓楼区', '南京市 · 鼓楼区 · 示例地址7', '789.01', '34.56', '示例备注7', '推送Key7'),
('尹烨霖', '78901234567', 'password8', '武汉市', '武汉市', '江汉区', '武汉市 · 江汉区 · 示例地址8', '890.12', '45.67', '示例备注8', '推送Key8'),
('余荣轩', '45678901234', 'password9', '重庆市', '重庆市', '渝中区', '重庆市 · 渝中区 · 示例地址9', '901.23', '56.78', '示例备注9', '推送Key9'),
('程君浩', '89012345678', 'password10', '郑州市', '郑州市', '中原区', '郑州市 · 中原区 · 示例地址10', '12.34', '67.89', '示例备注10', '推送Key10'),
('郭绍齐', '12345678901', 'password11', '西安市', '西安市', '雁塔区', '西安市 · 雁塔区 · 示例地址11', '23.45', '78.90', '示例备注11', '推送Key11'),
('贾越泽', '56789012345', 'password12', '青岛市', '青岛市', '市南区', '青岛市 · 市南区 · 示例地址12', '34.56', '89.01', '示例备注12', '推送Key12'),
('韦越彬', '32109876543', 'password13', '大连市', '大连市', '中山区', '大连市 · 中山区 · 示例地址13', '45.67', '90.12', '示例备注13', '推送Key13'),
('叶楷瑞', '65432109876', 'password14', '厦门市', '厦门市', '思明区', '厦门市 · 思明区 · 示例地址14', '56.78', '12.34', '示例备注14', '推送Key14'),
('覃弘文', '23456789012', 'password15', '苏州市', '苏州市', '姑苏区', '苏州市 · 姑苏区 · 示例地址15', '67.89', '23.45', '示例备注15', '推送Key15'),
('沈明杰', '78901234567', 'password16', '杭州市', '杭州市', '西湖区', '杭州市 · 西湖区 · 示例地址16', '78.90', '34.56', '示例备注16', '推送Key16'),
('黄哲瀚', '45678901234', 'password17', '宁波市', '宁波市', '江北区', '宁波市 · 江北区 · 示例地址17', '89.01', '45.67', '示例备注17', '推送Key17'),
('秦振家', '89012345678', 'password18', '无锡市', '无锡市', '锡山区', '无锡市 · 锡山区 · 示例地址18', '90.12', '56.78', '示例备注18', '推送Key18'),
('杨语堂', '12345678901', 'password19', '常州市', '常州市', '钟楼区', '常州市 · 钟楼区 · 示例地址19', '12.34', '67.89', '示例备注19', '推送Key19');
















