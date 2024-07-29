SELECT 
    e.emp_no, 
    e.emp_name, 
    CASE 
        WHEN avg(g.score) >= 96 THEN 'S'
        WHEN avg(g.score) >= 90 THEN 'A'
        WHEN avg(g.score) >= 80 THEN 'B'
        ELSE 'C'
    END AS grade,
    
    CASE 
        WHEN avg(g.score) >= 96 THEN e.sal * 0.2
        WHEN avg(g.score) >= 90 THEN e.sal * 0.15
        WHEN avg(g.score) >= 80 THEN e.sal * 0.1
        ELSE e.sal * 0
    END AS bonus
    
FROM 
    hr_employees AS e 
    JOIN hr_department AS d ON e.dept_id = d.dept_id
    JOIN hr_grade AS g ON e.emp_no = g.emp_no
    
GROUP BY 
    e.emp_no, e.emp_name

ORDER BY e.emp_no ASC;