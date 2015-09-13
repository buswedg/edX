-- Retrieve total sales by product
SELECT Name,SUM(LineTotal) AS TotalRevenue
FROM SalesLT.SalesOrderDetail AS SOD
JOIN SalesLT.Product AS P ON SOD.ProductID=P.ProductID
GROUP BY P.Name
ORDER BY TotalRevenue DESC;

-- Filter the product sales list to include only products that cost over $1,000
SELECT Name,SUM(LineTotal) AS TotalRevenue
FROM SalesLT.SalesOrderDetail AS SOD
JOIN SalesLT.Product AS P ON SOD.ProductID=P.ProductID
WHERE P.ListPrice > 1000
GROUP BY P.Name
ORDER BY TotalRevenue DESC;

-- Filter the product sales groups to include only total sales over $20,000
SELECT Name,SUM(LineTotal) AS TotalRevenue
FROM SalesLT.SalesOrderDetail AS SOD
JOIN SalesLT.Product AS P ON SOD.ProductID=P.ProductID
WHERE P.ListPrice > 1000
GROUP BY P.Name
HAVING SUM(LineTotal) > 20000
ORDER BY TotalRevenue DESC;