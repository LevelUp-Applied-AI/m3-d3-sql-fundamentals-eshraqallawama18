import sqlite3

# ===============================
# Task 1 — Aggregation
# ===============================
def top_departments(db_path):
    """
    Returns the top 3 departments by total salary expenditure.
    Output: [(dept_name, total_salary), ...]
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT d.name, SUM(e.salary) as total_salary
    FROM departments d
    JOIN employees e ON d.dept_id = e.dept_id
    GROUP BY d.name
    ORDER BY total_salary DESC
    LIMIT 3;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results


# ===============================
# Task 2 — JOIN
# ===============================
def employees_with_projects(db_path):
    """
    Returns a list of tuples [(employee_name, project_name), ...]
    for all employees assigned to at least one project
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT e.name, p.name
    FROM employees e
    JOIN project_assignments pa ON e.emp_id = pa.emp_id
    JOIN projects p ON pa.project_id = p.project_id;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results


# ===============================
# Task 3 — Window Function
# ===============================
def salary_rank_by_department(db_path):
    """
    Returns [(employee_name, dept_name, salary, rank), ...]
    Rank by salary within each department
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT 
        e.name,
        d.name,
        e.salary,
        RANK() OVER(PARTITION BY d.dept_id ORDER BY e.salary DESC) as rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY d.name, rank;
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results


# ===============================
# Optional: test functions
# ===============================
if __name__ == "__main__":
    db_path = r"C:\Users\eshraq allawama\m3-d3-sql-fundamentals-eshraqallawama18\drill.db"

    print("Top Departments:")
    print(top_departments(db_path))
    print("\nEmployees with Projects:")
    print(employees_with_projects(db_path))
    print("\nSalary Rank by Department:")
    print(salary_rank_by_department(db_path))