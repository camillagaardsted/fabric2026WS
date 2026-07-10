CREATE TABLE [hr].[Ansat] (

	[AnsatID] int NOT NULL, 
	[Fornavn] varchar(25) NOT NULL, 
	[Efternavn] varchar(25) NOT NULL, 
	[Salgsmaal] int NULL, 
	[ChefID] int NULL, 
	[Foedt] date NULL, 
	[AnsatDato] date NULL, 
	[AfdID] int NOT NULL, 
	[Tlf] int NULL
);