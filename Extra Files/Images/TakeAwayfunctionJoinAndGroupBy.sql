USE TakeAwayDBCA1
GO

-- Function that get Order list by Date Range
CREATE FUNCTION function_Orderlist_by_DateRange (@start as Date,@end as Date)
returns TABLE
AS
return 
	SELECT * FROM tbl_Order c
	WHERE c.OrderDate BETWEEN  @start AND @end
GO

-- SELECT Query with JOIN
SELECT tbl_MenuItem.MenuName, tbl_MenuItem.MenuPrice, tbl_MenuItem.CategoryID, tbl_Category.CategoryName
FROM tbl_MenuItem
INNER JOIN tbl_Category
ON tbl_MenuItem.CategoryId = tbl_Category.CategoryID

-- SELECT Query with Group BY and Order BY 
SELECT PaymentStatus, AgentID, OrderAmount
FROM tbl_Order
WHERE PaymentStatus = 'Paid'
GROUP BY AgentID,PaymentStatus,OrderAmount
ORDER BY OrderAmount;








AS
BEGIN
	DECLARE @duration as int
	SET @duration = DateDiff(month, @start, @end)
	return @duration
END
GO
SELECT dbo.fn_CourseDurartion('2022-09-01', '2023-05-30') 
AS [course duration in months]


