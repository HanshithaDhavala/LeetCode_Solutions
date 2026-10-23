# Write your MySQL query statement below
UPDATE Salary
SET sex = CASE
When sex = 'm' THEN 'f'
else 'm'
END;