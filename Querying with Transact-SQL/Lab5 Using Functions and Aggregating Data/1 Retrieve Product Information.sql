-- Retrieve the year and month in which products were first sold
SELECT YEAR(SellStartDate) SellStartYear, DATENAME(mm,SellStartDate) SellStartMonth,
	   ProductID, Name
FROM SalesLT.Product
ORDER BY SellStartYear;


-- Extract product types from product numbers
SELECT Name, ProductNumber, LEFT(ProductNumber, 2) AS ProductType
FROM SalesLT.Product;