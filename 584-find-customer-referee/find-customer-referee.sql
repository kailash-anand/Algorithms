-- Write your PostgreSQL query statement below
SELECT NAME
FROM CUSTOMER
WHERE REFEREE_ID IS NULL OR REFEREE_ID != 2;