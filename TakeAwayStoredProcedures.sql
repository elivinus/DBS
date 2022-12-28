

CREATE PROCEDURE GetSupplier_withparameters
(@SupplierID varchar)
AS
BEGIN
SET NOCOUNT ON

SELECT m.SupplierName, m.SupplierEmailAddress, m.SupplierAddress,
m.SupplierAddress.value('(/office_address/officeaddress[2]/postcodedetails)[1]', 'varchar(50)') as postcode
FROM tbl_Supplier m
WHERE m.SupplierID=@SupplierID
END


CREATE PROCEDURE UpdateSupplier_withparameters
(@SupplierID varchar)
AS
BEGIN
SET NOCOUNT ON

UPDATE tbl_Supplier
SET SupplierAddress.modify('insert (<officeaddress><cityname>Berlin</cityname><postcodedetails>A09 F3X8</postcodedetails></officeaddress>) after (/office_address/officeaddress)[3]' )
WHERE SupplierID = @SupplierID
END


SELECT m.SupplierName, m.SupplierEmailAddress, m.SupplierAddress
FROM tbl_Supplier m
WHERE m.SupplierID='supplyer3'
