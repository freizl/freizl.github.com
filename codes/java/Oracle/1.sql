SQL-Scripts
---
show parameter instance_name;

--- Session
select sid, username, command, machine, osuser, status, module from v$session;

--- log in as DBA
connect system/system as sysdba
connect sys/sys as sysdba

-- create user weblogic identified by weblogic;
grant CONNECT, RESOURCE to weblogic;

--
select table_name from all_tables where table_name like '%ETORDERFROMRMS%';
select view_name from all_views where view_name like '%ETORDERFROMRMS%';

--
SQLPLUS dev23_soainfra/weblogic@10.2.5.22/opus  @console.sql

--
SET LINESIZE 150;
SET WRAP OFF;
COLUMN QUEUE FORMAT A20;
COLUMN DEQ_TIME FORMAT A20;
COLUMN ENQ_TIME FORMAT A20;