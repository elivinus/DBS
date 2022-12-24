USE TakeAwayDBCA1
GO 

CREATE TABLE tbl_Category
(
CategoryName varchar(20) not null,
PRIMARY KEY (CategoryName),
)
GO

CREATE TABLE tbl_MenuItem
(
MenuItemID	varchar(30) not null,
MenuName	varchar(50) not null,
MenuPrice	int	not null,
CategoryName	varchar(20) not null,
MenuDescription	varchar(50) not null,
MenuImage	image	not null,
Alegies	varchar(50)	not null,
PRIMARY KEY	(MenuItemID),
FOREIGN KEY	(CategoryName)	REFERENCES	tbl_Category(CategoryName),
)
Go


CREATE TABLE tbl_Customer
(
CustomerID	varchar(30) not null,
CustomerFirstName varchar(20) not null,
CustomerLastName varchar(20) not null,
CustomerEmailAddress varchar(50) not null,
CustomerMobileNumber int not null,
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
AgentMobileNumber int not null,
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
StaffMobileNumber int not null,
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
OrderAmount varchar(50) not null,
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
OrderDetailID int not null,
OrderQuantity int not null,
TotalAmount float not null,
OrderDate date not null,
MenuItemID	varchar(30) not null,
OrderID	varchar(100) not null,
PRIMARY KEY (OrderDetailID),
FOREIGN KEY (MenuItemID) REFERENCES tbl_MenuItem (MenuItemID),
FOREIGN KEY (OrderID) REFERENCES tbl_Order (OrderID),
)
GO

CREATE TABLE tbl_Supplier
(
SupplierID varchar(30) not null,
SupplierName varchar(20) not null,
SupplierEmailAddress varchar(50) not null,
SupplierMobileNumber int not null,
SupplierAddress  xml (SupplierAddressCollection),
SupplierCreateDate  date not null
PRIMARY KEY (SupplierID),
)
GO

CREATE TABLE tbl_Ingredient
(
IngredientID varchar(30) not null,
IngredientName varchar(20) not null,
IngredientPrice float not null,
IngredientCreateDate  date not null,
PRIMARY KEY (IngredientID)
)
GO
CREATE TABLE tbl_Recipe
(
RecipeName varchar(20) not null,
RecipeDescription varchar(100) not null,
RecipeCreateDate  date not null,
Ingredient1 varchar (30),
Ingredient2 varchar (30),
Ingredient3 varchar (30),
Ingredient4 varchar (30),
Ingredient5 varchar (30),
Ingredient6 varchar (30),
Ingredient7 varchar (30),
Ingredient8 varchar (30),
Ingredient9 varchar (30),
Ingredient10 varchar (30),
PRIMARY KEY (RecipeName),
FOREIGN KEY (Ingredient1) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient2) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient3) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient4) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient5) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient6) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient7) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient8) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient9) REFERENCES tbl_Ingredient (IngredientID),
FOREIGN KEY (Ingredient10) REFERENCES tbl_Ingredient (IngredientID),
)
