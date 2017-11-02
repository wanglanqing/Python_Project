-- 同步根组织涉及到hydt_ofdb.ofgroup、hydt_ofdb.ofgroupprop、hydt_ofdb.ofgroupuser、hydt_ofdb.ofmucroom、hydt_ofdb.ofmucaffiliation、hydt_ofdb.ofmucroomprop 6张表。
-- 同步group表
INSERT INTO hydt_ofdb.ofgroup VALUES ('AUTO', '证券');
-- 同步hydt_ofdb.ofgroupprop表
INSERT INTO hydt_ofdb.ofgroupprop VALUES ('AUTO', 'sharedRoster.displayName', 'AUTO');
INSERT INTO hydt_ofdb.ofgroupprop VALUES ('AUTO', 'sharedRoster.groupList', '');
INSERT INTO hydt_ofdb.ofgroupprop VALUES ('AUTO', 'sharedRoster.showInRoster', 'onlyGroup');
-- 同步hydt_ofdb.ofgroupuser表
INSERT INTO hydt_ofdb.ofgroupuser VALUES ('AUTO', 'bcm-gw', 0);


-- 同步hydt_ofdb.ofmucroom表
insert into hydt_ofdb.ofmucroom
select '1','10','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO';

-- 同步子组织数据，涉及到hydt_ofdb.ofmucroom、hydt_ofdb.ofmucaffiliation、hydt_ofdb.ofmucroomprop 3张表。
insert into hydt_ofdb.ofmucroom
select '1','11','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='应急指挥中心';
insert into hydt_ofdb.ofmucroom
select '1','12','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='应急处置领导小组办公室';
insert into hydt_ofdb.ofmucroom
select '1','13','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='技术处置工作小组';
insert into hydt_ofdb.ofmucroom
select '1','14','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='交易业务处置工作小组';
insert into hydt_ofdb.ofmucroom
select '1','15','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='客户服务处置工作小组';
insert into hydt_ofdb.ofmucroom
select '1','16','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='精算业务处置工作小组';
insert into hydt_ofdb.ofmucroom
select '1','17','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='后勤保障处置工作小组';
insert into hydt_ofdb.ofmucroom
select '1','18','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD';
insert into hydt_ofdb.ofmucroom
select '1','19','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_HR';
insert into hydt_ofdb.ofmucroom
select '1','20','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_FIN';
insert into hydt_ofdb.ofmucroom
select '1','21','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_BOCC';
insert into hydt_ofdb.ofmucroom
select '1','22','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD_RD1';
insert into hydt_ofdb.ofmucroom
select '1','23','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD_RD2';
insert into hydt_ofdb.ofmucroom
select '1','24','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD_RD1_OLTP';
insert into hydt_ofdb.ofmucroom
select '1','25','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD_RD1_SIT';
insert into hydt_ofdb.ofmucroom
select '1','26','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_RD_RD1_SBC';
insert into hydt_ofdb.ofmucroom
select '1','27','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_BOCC_B1';
insert into hydt_ofdb.ofmucroom
select '1','28','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='AUTO_BOCC_ZC';
insert into hydt_ofdb.ofmucroom
select '1','29','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD';
insert into hydt_ofdb.ofmucroom
select '1','30','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_HR';
insert into hydt_ofdb.ofmucroom
select '1','31','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_FIN';
insert into hydt_ofdb.ofmucroom
select '1','32','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_BOCC';
insert into hydt_ofdb.ofmucroom
select '1','33','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD_RD1';
insert into hydt_ofdb.ofmucroom
select '1','34','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD_RD2';
insert into hydt_ofdb.ofmucroom
select '1','35','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD_RD1_OLTP';
insert into hydt_ofdb.ofmucroom
select '1','36','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD_RD1_SBC';
insert into hydt_ofdb.ofmucroom
select '1','37','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_RD_RD1_SIT'; 
insert into hydt_ofdb.ofmucroom
select '1','38','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_BOCC_B1';
insert into hydt_ofdb.ofmucroom
select '1','39','001452940754512','001453277500858',CONCAT('org_',org_id),org_name,'','000000000000000','001452940754488','0','0','0','0','0','0',NULL,'0','0',NULL,'0','0','0','0' from hydt_bcm.t_organization
where org_name='YY_BOCC_ZC';

-- 同步hydt_ofdb.ofmucaffiliation表,将7替换成上一select查询到的结果
insert into hydt_ofdb.ofmucaffiliation
select roomID,'admin@im.ihydt.com','10' from hydt_ofdb.ofmucroom where roomID between 10 and 99;
insert into hydt_ofdb.ofmucroomprop
select roomID,'roomType','2' from hydt_ofdb.ofmucroom where roomID between 10 and 99;


-- 同步用户，涉及到hydt_ofdb.ofgroupuser,ofmucmember,ofuser,ofuserprop  4张表。
	-- 同步ofuser表
	insert into hydt_ofdb.ofuser
	(username,plainPassword,name,email,creationDate,modificationDate)
	select a.mobile,'admin123',a.user_name,a.email,'001453185456847','001453185456847'
	from hydt_bcm.t_user a
	where user_id >2;

	-- 同步ofgroupuser表
	INSERT INTO hydt_ofdb.ofgroupuser (
		groupName,
		username,
		administrator
	) SELECT
		'AUTO',
		a.mobile,
		0
	FROM
		hydt_bcm.t_user a
	WHERE
		a.user_id > 2;

	-- 同步ofuserprop
	insert into hydt_ofdb.ofuserprop
	(username,name,propValue)
	select a.mobile,'userId',a.user_id from hydt_bcm.t_user a where a.user_id >2;

	insert into hydt_ofdb.ofuserprop
	(username,name,propValue)
	select a.mobile,'rootOrgId',a.root_org_id from hydt_bcm.t_user a where a.user_id >2;
	

-- 同步ofmucmember，使用Python脚本同步,详细见add_ofmucmember方法
-- 添加用户头像，添加的都是默认的蓝色图标的头像。
	update hydt_bcm.t_user set head_path='/group1/M00/00/00/ezk4eVaoM4CAGUq1AAAN6hFsbNY750.png'
	where user_id>2;
	-- 将用户头像信息同步到ofuserprop表中
		insert into hydt_ofdb.ofuserprop
	(username,name,propValue)
	select a.mobile,'head',a.head_path from hydt_bcm.t_user a where a.user_id >2;
	