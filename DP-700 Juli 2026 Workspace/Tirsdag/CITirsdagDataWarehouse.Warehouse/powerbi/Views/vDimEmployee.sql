-- Auto Generated (Do not modify) 9EAEC4310DE5404C2BAF46848E4D072DAC6EC2A11C0611B4C3E1E259DF384DB2
--CREATE SCHEMA powerbi


CREATE VIEW [powerbi].[vDimEmployee] AS
SELECT      CONCAT(HE.first_name,' ',HE.last_name) AS EmployeeName
            , HE.employee_id
            , HD.name AS Department   
            FROM hr.employee HE INNER JOIN hr.department HD ON HD.dept_id=HE.dept_id