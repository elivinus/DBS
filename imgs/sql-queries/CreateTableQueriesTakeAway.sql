USE TakeAwayDBCA1
GO 

CREATE TABLE tbl_Category
(
CategoryID   varchar(20) not null,
CategoryName varchar(20) not null,
PRIMARY KEY (CategoryID),
)

GO
CREATE TABLE tbl_Supplier
(
SupplierID varchar(30) not null,
SupplierName varchar(50) not null,
SupplierEmailAddress varchar(50) not null,
SupplierMobileNumber varchar(14) not null,
SupplierAddress  xml (SupplierAddressCollection),
SupplierCreateDate  date not null,
PRIMARY KEY (SupplierID),
)
GO

CREATE TABLE tbl_Ingredient
(
IngredientID varchar(30) not null,
IngredientName varchar(20) not null,
IngredientPrice float not null,
IngredientCreateDate  date not null,
SupplierID varchar(30) not null,
PRIMARY KEY (IngredientID),
FOREIGN KEY (SupplierID) REFERENCES tbl_Supplier (SupplierID),
)
GO
CREATE TABLE tbl_Recipe
(
RecipeID   varchar(20) not null,
RecipeName varchar(50) not null,
RecipeDescription varchar(100) not null,
RecipeCreateDate  date not null,
IngredientID varchar (30),
PRIMARY KEY (RecipeID),
FOREIGN KEY (IngredientID) REFERENCES tbl_Ingredient (IngredientID),
)

GO

CREATE TABLE tbl_MenuItem
(
MenuItemID	varchar(30) not null,
MenuName	varchar(50) not null,
MenuPrice	float	not null,
CategoryID	varchar(20) not null,
RecipeID	varchar(20) not null,
MenuDescription	varchar(200) not null,
MenuImage	image,
Alegies	varchar(50),
PRIMARY KEY	(MenuItemID),
FOREIGN KEY	(CategoryID)	REFERENCES	tbl_Category(CategoryID),
FOREIGN KEY	(RecipeID)	REFERENCES	tbl_Recipe(RecipeID),
)
Go

CREATE TABLE tbl_Customer
(
CustomerID	varchar(30) not null,
CustomerFirstName varchar(20) not null,
CustomerLastName varchar(20) not null,
CustomerEmailAddress varchar(50) not null,
CustomerMobileNumber varchar(14) not null,
CustomerPostCode varchar(10) not null,
CustomerCity varchar(10) not null,
CustomerHomeAddress varchar(100) not null,
CustomerCreateDate  date not null,
CustomerPassword varchar(100) not null
PRIMARY KEY (CustomerID),
)
GO

CREATE TABLE tbl_DeliveryAgent
(
AgentID	varchar(30) not null,
AgentFirstName varchar(20) not null,
AgentLastName varchar(20) not null,
AgentEmailAddress varchar(50) not null,
AgentMobileNumber varchar(14) not null,
AgentPostCode varchar(10) not null,
AgentCity varchar(10) not null,
AgentHomeAddress varchar(100) not null,
AgentCreateDate  date not null
PRIMARY KEY (AgentID),
)
GO

CREATE TABLE tbl_Staff
(
StaffID	varchar(30) not null,
StaffFirstName varchar(20) not null,
StaffLastName varchar(20) not null,
StaffEmailAddress varchar(50) not null,
StaffMobileNumber varchar(14) not null,
StaffPostCode varchar(10) not null,
StaffCity varchar(10) not null,
StaffHomeAddress varchar(100) not null,
StaffCreateDate  date not null
PRIMARY KEY (StaffID),
)
GO

CREATE TABLE tbl_Order
(
OrderDate date not null,
OrderAmount float not null,
OrderStatus varchar(50) not null,
OrderID varchar(100) not null,
PaymentStatus varchar(10) not null,
AgentID	varchar(30),
StaffID	varchar(30),
CustomerID	varchar(30) not null,
PRIMARY KEY (OrderID),
FOREIGN KEY (AgentID) REFERENCES tbl_DeliveryAgent (AgentID),
FOREIGN KEY (StaffID) REFERENCES tbl_Staff (StaffID),
FOREIGN KEY (CustomerID) REFERENCES tbl_Customer (CustomerID),
)

GO
CREATE TABLE tbl_OrderDetail
(
OrderDetailID varchar(30) not null,
OrderQuantity int not null,
TotalAmount float not null,
OrderDate date not null,
MenuItemID	varchar(30) not null,
OrderID	varchar(100) not null,
PRIMARY KEY (OrderDetailID),
FOREIGN KEY (MenuItemID) REFERENCES tbl_MenuItem (MenuItemID),
FOREIGN KEY (OrderID) REFERENCES tbl_Order (OrderID),
)


