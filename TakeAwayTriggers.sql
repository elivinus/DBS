USE TakeAwayDBCA1  
GO  

-- Trigger to ensure that CustomerID and OrderID Cannot be modified once created
IF EXISTS (SELECT name FROM sys.objects  
      WHERE name = 'customer_edit_alert' AND type = 'TR')  
   DROP TRIGGER [tbl_Order].[customer_edit_alert];  
GO  
CREATE TRIGGER customer_edit_alert  ON [dbo].[tbl_Order]  
AFTER UPDATE   
AS   
IF ( UPDATE (CustomerID) OR UPDATE (OrderID) )  
BEGIN  
RAISERROR (50009, 16, 10)  
END;  
GO

-- Triiger to Ensure All Order with Delivered Status are fully Paid for.

CREATE TRIGGER order_status_update ON [dbo].[tbl_Order] 
AFTER UPDATE
AS 
BEGIN

declare @OrderDAte date;
declare @OrderAmount float;
declare @OrderStatus varchar(50);
declare @OrderID varchar(100);
declare @PaymentStatus varchar(10);
declare @AgentID varchar(30);
declare @StaffID varchar(30);
declare @CustomerID varchar(30);

select @OrderDate = orderlist.OrderDate from inserted orderlist
select @OrderAmount = orderlist.OrderAmount from inserted orderlist
select @OrderStatus = orderlist.OrderStatus from inserted orderlist
select @OrderID = orderlist.OrderID from inserted orderlist
select @AgentID = orderlist.AgentID from inserted orderlist
select @StaffID = orderlist.StaffID from inserted orderlist
select @CustomerID = orderlist.CustomerID from inserted orderlist


IF @OrderStatus = 'Delivered' AND @PaymentStatus != 'Paid' 
	UPDATE tbl_Order
	SET PaymentStatus = 'Paid'
	WHERE @OrderStatus = 'Delivered' AND  @PaymentStatus != 'Paid'

END 
GO