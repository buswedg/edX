-- Throw an error for non-existent orders
DECLARE @SalesOrderID int = 0

SELECT @SalesOrderID = MIN(SalesOrderID) FROM SalesLT.SalesOrderHeader; 

BEGIN TRY
	-- Handle errors
	IF NOT EXISTS (SELECT * FROM SalesLT.SalesOrderHeader
				   WHERE SalesOrderID = @SalesOrderID)
	BEGIN
		DECLARE @error varchar(25);
		SET @error = 'Order #' + cast(@SalesOrderID as varchar) + ' does not exist';
		THROW 50001, @error, 0
	END
	ELSE
	BEGIN
		DELETE FROM SalesLT.SalesOrderDetail
		WHERE SalesOrderID = @SalesOrderID;

		DELETE FROM SalesLT.SalesOrderHeader
		WHERE SalesOrderID = @SalesOrderID;
	END
END TRY
BEGIN CATCH
	PRINT  ERROR_MESSAGE();
END CATCH