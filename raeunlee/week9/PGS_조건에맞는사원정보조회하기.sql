-- 코드를 작성해주세요
select sum(g.score) as score, e.emp_no, e.emp_name, e.position, e.email
from hr_department d join hr_employees e on d.dept_id = e.dept_id
join hr_grade g on e.emp_no = g.emp_no
group by emp_no
order by score desc
limit 1