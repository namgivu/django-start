drop database if exists `django_start`;
create database `django_start` default character set utf8;

drop user if exists `django_start`;
create user `django_start`@'%' identified by 'django_start';
grant all on *.* to `django_start`@'%';
