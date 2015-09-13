-- Retrieve product details for product model 1
SELECT Name, Color, Size
FROM SalesLT.Product
WHERE ProductModelID = 1;


-- Filter products by color and size
SELECT ProductNumber, Name
FROM SalesLT.Product
WHERE Color IN ('Black','Red','White') and Size IN ('S','M');


-- Filter products by product number
SELECT ProductNumber, Name, ListPrice
FROM SalesLT.Product 
WHERE ProductNumber LIKE 'BK-%';


-- Retrieve specific products by product number
SELECT ProductNumber, Name, ListPrice
FROM SalesLT.Product 
WHERE ProductNumber LIKE 'BK-[^R]%-[0-9][0-9]';