USE TakeAwayDBCA1
GO
INSERT INTO tbl_Category VALUES 
('cat1','Drinks'),
('cat2', 'Vegetarian'),
('cat3', 'Noodles'),
('cat4', 'Starter'),
('cat5','Desserts')

GO
INSERT INTO tbl_Supplier VALUES 
('supplyer1','Dyle Enterprise','pdeborah@gmail.com','53899612532','<?xml version="1.0"?>
<office_address>
    <officeaddress>
        <cityname>Dublin</cityname>
        <postcodedetails>D07 D3C5</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Cork</cityname>
        <postcodedetails>C11 G7C5</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Baywood</cityname>
        <postcodedetails>B03 H7R5</postcodedetails>
    </officeaddress>
</office_address>',GETDATE()),
('supplyer2', 'Paschal Marchant','dpaschal@gmail.com','53899676532','<?xml version="1.0"?>
<office_address>
    <officeaddress>
        <cityname>Dublin</cityname>
        <postcodedetails>D05 DJC5</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Gallway</cityname>
        <postcodedetails>G11 G7T5</postcodedetails>
    </officeaddress>
</office_address>',GETDATE()),
('supplyer3', 'Livinus Industries limited','elivinus@gmail.com','53899632233','<?xml version="1.0"?>
<office_address>
    <officeaddress>
        <cityname>Gallway</cityname>
        <postcodedetails>G05 D3Y5</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Cork</cityname>
        <postcodedetails>C05 G8C5</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Baywood</cityname>
        <postcodedetails>B12 A7R5</postcodedetails>
    </officeaddress>
</office_address>',GETDATE()),
('supplyer4', 'Perry Ventures','pperry@gmail.com','53899648832','<?xml version="1.0"?>
<office_address>
    <officeaddress>
        <cityname>Gallway</cityname>
        <postcodedetails>G3 D5Y2</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Cork</cityname>
        <postcodedetails>C15 G8C4</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Baywood</cityname>
        <postcodedetails>B12 A7S5</postcodedetails>
    </officeaddress>
	<officeaddress>
        <cityname>Gitall</cityname>
        <postcodedetails>GI12 A7R5</postcodedetails>
    </officeaddress>
</office_address>',GETDATE()),
('supplyer5','Peterno Holdings','ppeterno@gmail.com','53899634847','<?xml version="1.0"?>
<office_address>
    <officeaddress>
        <cityname>Churchhill</cityname>
        <postcodedetails>C09 G2C4</postcodedetails>
    </officeaddress>
    <officeaddress>
        <cityname>Baywood</cityname>
        <postcodedetails>B03 A7X5</postcodedetails>
    </officeaddress>
	<officeaddress>
        <cityname>Gitall</cityname>
        <postcodedetails>GI01 Q7P5</postcodedetails>
    </officeaddress>
</office_address>',GETDATE())

GO
INSERT INTO tbl_Ingredient VALUES 
('ing1','Flower',15.0,GETDATE(),'supplyer3'),
('ing2','Vegetable Oil',25.0,GETDATE(),'supplyer2'),
('ing3','Frozen Beef',34.0,GETDATE(),'supplyer1'),
('ing4','Food Seasoning',20.5,GETDATE(),'supplyer5'),
('ing5','Salt',45.8,GETDATE(),'supplyer4')

GO
INSERT INTO tbl_Recipe VALUES 
('recipe1','Flower Recipe','This recipe is for Flower',GETDATE(),'ing1'),
('recipe2','Vegetable Oil Recipe','This recipe is for Vegitable Oil',GETDATE(),'ing2'),
('recipe3','Frozen Beef Recipe','This recipe is for Frozen Beef',GETDATE(),'ing3'),
('recipe4','Food Seasoning Recipe','This recipe is for Seasoning',GETDATE(),'ing4'),
('recipe5','Table Salt Recipe','This recipe is for table salt',GETDATE(),'ing5')

GO
insert into tbl_MenuItem (MenuItemID,MenuName,MenuPrice,CategoryID,RecipeID,MenuDescription,MenuImage,Alegies) 
SELECT 'menu1','Spring Rolls',5,'cat4','recipe1','Spring roll is a traditional Chinese savory snack where a pastry sheet is filled with vegetables, rolled & fried.',BulkColumn,'' 
FROM Openrowset( Bulk 'C:\imgs\springrolls.png', Single_Blob) as img

insert into tbl_MenuItem (MenuItemID,MenuName,MenuPrice,CategoryID,RecipeID,MenuDescription,MenuImage,Alegies) 
SELECT 'menu2', 'Roast Pork with Cracle',7,'cat5','recipe2','Transfer pork to a roasting dish and roast for 50 minutes, or until the rind crackles.',BulkColumn,''
FROM Openrowset( Bulk 'C:\imgs\roast-pork-with-cracle.png', Single_Blob) as img 

insert into tbl_MenuItem (MenuItemID,MenuName,MenuPrice,CategoryID,RecipeID,MenuDescription,MenuImage,Alegies) 
SELECT 'menu3', 'Coca Cola',2,'cat1','recipe3','Coca-Cola, or Coke, is a carbonated soft drink manufactured by the Coca-Cola Company.',BulkColumn,''
FROM Openrowset( Bulk 'C:\imgs\coca-cola.png', Single_Blob) as img

insert into tbl_MenuItem (MenuItemID,MenuName,MenuPrice,CategoryID,RecipeID,MenuDescription,MenuImage,Alegies) 
SELECT 'menu4', 'Crispy Chilli Chicken Udon',10,'cat2','recipe4','Chilli Chicken Udon Noodle Soup by Chef Kwanghi Chan.',BulkColumn,''
FROM Openrowset( Bulk 'C:\imgs\crispy-chilli-chicken-udon.png', Single_Blob) as img

insert into tbl_MenuItem (MenuItemID,MenuName,MenuPrice,CategoryID,RecipeID,MenuDescription,MenuImage,Alegies) 
SELECT 'menu5','Teriyaki Sauce Japanese Style',9,'cat3','recipe5','Teriyaki is a Japanese cooking technique used to cook and glaze proteins with a savory-sweet sauce.',BulkColumn,''
FROM Openrowset( Bulk 'C:\imgs\teriyaki-sauce-japanese-style.png', Single_Blob) as img

GO
INSERT INTO tbl_Customer VALUES 
('cust1','John','Gowel','gjohn@gmail.com','353899634532','G2T4','Dublin','No 23, Shagan Avenue',GETDATE(),'P@ssJ0hn#'),
('cust2', 'Michael','Doyle','dmichael@gmail.com','353899635532','N2G2','Dublin','No 33 Tayak Road',GETDATE(),'P@ss@D0ylE#'),
('cust3', 'Livinus','Enoja','elivinus@gmail.com','353899634533','Y2f5','Cork','No 67 Bijock Avenue',GETDATE(),'en0j@P@ss#'),
('cust4', 'Ebele','Onyeka','oebele@gmail.com','353899644532','B3Y4','Dublin','89 Asuka Avenue',GETDATE(),'0ny3k@PAss#'),
('cust5','Jackson','Peters','pjackson@gmail.com','353899634536','H7D3','Baywood','44 Badeye Cross Road',GETDATE(),'P3t3rzP@ss#')
GO
INSERT INTO tbl_DeliveryAgent VALUES 
('agent1','Deborah','Packer','pdeborah@gmail.com','353899656532','G2K4','CorK','No 24, Fagan Avenue',GETDATE()),
('agent2', 'Samuel','Doyle','dsamuel@gmail.com','353899622532','N5G2','Dublin','No 33 Buyak Road',GETDATE()),
('agent3', 'Donald','Bugger','bdonald@gmail.com','353899564533','Y2f7','Cork','No 57 Bigulpa Avenue',GETDATE()),
('agent4', 'Jerry','Pawn','pjerry@gmail.com','353899647832','G3Y4','Draway','79 Yanuka Avenue',GETDATE()),
('agent5','Bruno','James','jbruno@gmail.com','353899634567','Q7W3','Baywood','49 Goodeye Cross Road',GETDATE())

GO
INSERT INTO tbl_Staff VALUES 
('staff1','Dyle','Jacob','pdeborah@gmail.com','353899612532','Y2K4','CorK','No 24, Hagan Avenue',GETDATE()),
('staff2', 'Paschal','Doyle','dpaschal@gmail.com','353899676532','N5G2','Dublin','No 33 Beer Road',GETDATE()),
('staff3', 'Livinus','Enoja','elivinus@gmail.com','353899632233','Y2f5','Cork','No 67 Jock Avenue',GETDATE()),
('staff4', 'Perry','Poter','pperry@gmail.com','353899648832','G3Y4','Draway','79 Sanuka Avenue',GETDATE()),
('staff5','Peterno','Pecky','ppeterno@gmail.com','353899634847','Q7W3','Baywood','49 Codeye Cross Road',GETDATE())

GO
INSERT INTO tbl_Order VALUES 
(GETDATE(),40.0,'Delivered','order1','Paid','agent2','staff3','cust3'),
(GETDATE(),30.0,'Progress','order2','Paid','agent3','staff2','cust4'),
(GETDATE(),19.0,'Delivered','order3','Not Paid','agent1','staff4','cust1'),
(GETDATE(),45.0,'Delivered','order4','Paid','agent4','staff1','cust2'),
(GETDATE(),50.0,'Progress','order5','Not Paid','agent5','staff5','cust5')

GO
INSERT INTO tbl_OrderDetail VALUES 
('orderd1',5,35.0,GETDATE(),'menu2','order1'),
('orderd2',5,25.0,GETDATE(),'menu1','order2'),
('orderd3',7,14.0,GETDATE(),'menu3','order3'),
('orderd4',4,40.0,GETDATE(),'menu5','order4'),
('orderd5',5,45.0,GETDATE(),'menu4','order5')

