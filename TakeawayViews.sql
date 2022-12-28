USE TakeAwayDBCA1
GO
--View All Orders
CREATE VIEW Allorders
AS
SELECT * FROM tbl_Order
GO

--View All Orders Paid
CREATE VIEW Paidorders
AS
SELECT tbl_Order.OrderDate, tbl_Order.OrderID, tbl_Order.OrderStatus, tbl_Order.PaymentStatus FROM tbl_Order 
WHERE tbl_Order.PaymentStatus = 'Paid'
GO

--View All Orders not Delivered
CREATE VIEW NotDeliveredOrders
AS
SELECT tbl_Order.OrderDate, tbl_Order.OrderID, tbl_Order.OrderStatus, tbl_Order.PaymentStatus FROM tbl_Order 
WHERE tbl_Order.OrderStatus != 'Delivered'
GO

