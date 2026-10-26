# Write your MySQL query statement below
SELECT * FROM CINEMA 
WHERE (id mod 2 != 0) and description != "boring"
order by rating desc;