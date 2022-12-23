CREATE TABLE tbl_MenuItem
(
MenuName   varchar(10) not null,
MenuPrice    int not null UNIQUE,
MenuDescription varchar(50) not null,
MenuImage  image not null,
Alegies     varchar(50) not null,
CONSTRAINT category_pk PRIMARY KEY (MenuName)
)
GO
CREATE TABLE tbl_Category
(
CategoryName varchar(10) not null
)

GO
CREATE TABLE tbl_Customer
(
CustomerFirstName varchar(20) not null,
CustomerLastName varchar(20) not null,
CustomerEmailAddress varchar(50) not null,
CustomerMobileNumber int not null,
CustomerPostCode varchar(10) not null,
CustomerCity varchar(10) not null,
CustomerHomeAddress varchar(100) not null,
CustomerCreateDate  date not null,
CustomerPassword varchar(100) not null
)
GO
CREATE TABLE tbl_Order
(
OrderDate date not null,
OrderAmount varchar(50) not null,
OrderStatus varchar(50) not null,
TransactionId varchar(100) not null,
PaymentStatus varcchar(10) not null,
CONSTRAINT delivery_agent_fk FOREIGN KEY (TransactioId)
CONSTRAINT staff_fk FOREIGN KEY (TransactioId)
CONSTRAINT customer_fk FOREIGN KEY (TransactioId)
)
GO
CREATE TABLE tbl_DeliveryAgent
(
AgentFirstName varchar(20) not null,
AgentLastName varchar(20) not null,
AgentEmailAddress varchar(50) not null,
AgentMobileNumber int not null,
AgentPostCode varchar(10) not null,
AgentCity varchar(10) not null,
AgentHomeAddress varchar(100) not null,
AgentCreateDate  date not null
)
GO
CREATE TABLE tbl_OrderDetail
(
OrderQuantity int not null,
TotalAmount float not null,
OrderDate date not null,
CONSTRAINT menuitem_fk FOREIGN KEY (OrderQuantity)
CONSTRAINT order_fk FOREIGN KEY (OrderQuantity)
)
GO
CREATE TABLE tbl_Staff
(
StaffFirstName varchar(20) not null,
StaffLastName varchar(20) not null,
StaffEmailAddress varchar(50) not null,
StaffMobileNumber int not null,
StaffPostCode varchar(10) not null,
StaffCity varchar(10) not null,
StaffHomeAddress varchar(100) not null,
StaffCreateDate  date not null
)
GO
CREATE TABLE tbl_Supplier
(
SupplierName varchar(20) not null,
SupplierEmailAddress varchar(50) not null,
SupplierMobileNumber int not null,
SupplierAddress  xml (SupplierAddressCollection),
SupplierCreateDate  date not null
)
GO
CREATE TABLE tbl_Ingredient
(
IngredientName varchar(20) not null,
IngredientPrice float not null,
IngredientCreateDate  date not null,
CONSTRAINT recipe_fk FOREIGN KEY (IngredientName)
CONSTRAINT supplier_fk FOREIGN KEY (IngredientName)
)
GO
CREATE TABLE tbl_Recipe
(
RecipeName varchar(20) not null,
RecipeDescription varchar(100) not null,
RecipeCreateDate  date not null,
CONSTRAINT menuitem_fk FOREIGN KEY (RecipeName)
)