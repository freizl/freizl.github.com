select * from chart_data
where time like '2010-11-10%'

delete from chart_data where time like '2010-11-10%'


delete cd from chart_data cd 
join chart_rows cr on cd.row_id = cr.row_id
join chart ch on cr.chart_id = ch.chart_id
join department d on ch.department_id = d.department_id
where d.department_name = 'UPT-CRDC'
