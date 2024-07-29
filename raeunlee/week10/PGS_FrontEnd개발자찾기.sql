
select distinct d.id, d.email, d.first_name, d.last_name
from developers as d join skillcodes as s on s.code & d.skill_code
where s.category = 'Front End'
order by d.id