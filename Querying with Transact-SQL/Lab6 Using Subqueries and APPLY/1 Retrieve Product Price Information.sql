-- Retrieve products whose list price is higher than the average unit price
SELECT ProductID, Name, ListPrice from SalesLT.Product
WHERE ListPrice >
(SELECT AVG(UnitPrice) FROM SalesLT.SalesOrderDetail)
ORDER BY ProductID;


-- Retrieve Products with a list price of $100 or more that have been sold for less than $100
SELECT ProductID, Name, ListPrice FROM SalesLT.Product
WHERE ProductID IN
(SELECT ProductID from SalesLT.SalesOrderDetail
 WHERE UnitPrice < 100.00)
AND ListPrice >= 100.00
ORDER BY ProductID;


-- Retrieve the cost, list price, and average selling price for each product
SELECT ProductID, Name, StandardCost, ListPrice,
	(SELECT AVG(UnitPrice)
	 FROM SalesLT.SalesOrderDetail AS SOD
	 WHERE P.ProductID = SOD.ProductID) AS AvgSellingPrice
FROM SalesLT.Product AS P
ORDER BY P.ProductID;


-- Retrieve products that have an average selling price that is lower than the cost
SELECT ProductID, Name, StandardCost, ListPrice,
(SELECT AVG(UnitPrice)
 FROM SalesLT.SalesOrderDetail AS SOD
 WHERE P.ProductID = SOD.ProductID) AS AvgSellingPrice
FROM SalesLT.Product AS P
WHERE StandardCost >
(SELECT AVG(UnitPrice)
 FROM SalesLT.SalesOrderDetail AS SOD
 WHERE P.ProductID = SOD.ProductID)
ORDER BY P.ProductID;