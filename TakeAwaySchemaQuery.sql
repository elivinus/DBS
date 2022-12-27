USE TakeAwayDBCA1
GO
CREATE XML SCHEMA COLLECTION SupplierAddressCollection
AS
'<?xml version="1.0"?>
<xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
	<xsd:element name="office_address">
			<xsd:complexType>
				<xsd:sequence>
					<xsd:element ref="officeaddress" minOccurs="1" maxOccurs="unbounded" />
				</xsd:sequence>
			</xsd:complexType>
	</xsd:element>
	<xsd:element name="officeaddress">
			<xsd:complexType>
				<xsd:sequence>
                    <xsd:element name="cityname" type="xsd:string" />
					<xsd:element name="postcodedetails" type="xsd:string" />
				</xsd:sequence>
			</xsd:complexType>
	</xsd:element>
</xsd:schema>'