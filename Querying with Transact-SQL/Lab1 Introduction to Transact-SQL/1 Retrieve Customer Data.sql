-- Retrieve customer details
SELECT * FROM SalesLT.Customer;


-- Retrieve customer name data
SELECT Title, FirstName, MiddleName, LastName, Suffix
FROM SalesLT.Customer;


-- Retrieve customer names and phone numbers
SELECT Salesperson, Title + ' ' + LastName AS CustomerName, Phone
FROM SalesLT.Customer;