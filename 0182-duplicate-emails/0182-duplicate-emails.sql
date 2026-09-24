# Write your MySQL query statement below
SELECT email AS Email FROM Person
GROUP BY email Having count(email)>1; 