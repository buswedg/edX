-- Retrieve a list of cities
SELECT DISTINCT City, StateProvince
FROM SalesLT.Address


-- Retrieve the heaviest products
SELECT TOP 10 PERCENT Name FROM SalesLT.Product ORDER BY Weight DESC;


-- Retrieve the heaviest 100 products not including the heaviest ten
SELECT Name FROM SalesLT.Product ORDER BY Weight DESC
OFFSET 10 ROWS FETCH NEXT 100 ROWS ONLY;