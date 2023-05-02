
q1 = ''' SELECT d.department, j.job,
            COUNT(e.id) FILTER (WHERE e.datetime >= '2021-01-01' AND e.datetime < '2021-04-01') AS Q1,
            COUNT(e.id) FILTER (WHERE e.datetime >= '2021-04-01' AND e.datetime < '2021-07-01') AS Q2,
            COUNT(e.id) FILTER (WHERE e.datetime >= '2021-07-01' AND e.datetime < '2021-10-01') AS Q3,
            COUNT(e.id) FILTER (WHERE e.datetime >= '2021-10-01' AND e.datetime < '2022-01-01') AS Q4
        FROM bronze.hired_employees e
        JOIN bronze.departments d ON e.department_id = d.id
        JOIN bronze.jobs j ON e.job_id = j.id
        WHERE e.datetime >= '2021-01-01' AND e.datetime < '2022-01-01'
        GROUP BY d.department, j.job
        ORDER BY d.department, j.job'''


q2 = '''WITH dept_avg AS (
            SELECT department_id, AVG(CASE WHEN date_trunc('year', datetime) = '2021-01-01' THEN 1 ELSE 0 END) AS avg_hires
            FROM bronze.hired_employees
            GROUP BY department_id
        ), dept_counts AS (
            SELECT department_id, COUNT(*) AS num_hires
            FROM bronze.hired_employees
            WHERE date_trunc('year', datetime) = '2021-01-01'
            GROUP BY department_id
        ), dept_filtered AS (
            SELECT department_id, num_hires
            FROM dept_counts
            WHERE num_hires > (SELECT AVG(avg_hires) FROM dept_avg)
        )
        SELECT dept_filtered.department_id, departments.department, COUNT(*) AS num_employees_hired
        FROM dept_filtered
        JOIN bronze.hired_employees ON dept_filtered.department_id = hired_employees.department_id
        JOIN bronze.departments ON dept_filtered.department_id = departments.id
        GROUP BY dept_filtered.department_id, departments.department
        ORDER BY num_employees_hired DESC'''

sql = {"q1":q1, "q2": q2}