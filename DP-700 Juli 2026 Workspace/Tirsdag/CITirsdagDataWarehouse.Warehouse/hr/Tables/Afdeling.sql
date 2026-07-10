CREATE TABLE [hr].[Afdeling] (

	[AfdID] int NOT NULL, 
	[Navn] varchar(25) NOT NULL, 
	[Salgsmaal] int NULL
);


GO
ALTER TABLE [hr].[Afdeling] ADD CONSTRAINT PK_Afdeling_AfdId primary key NONCLUSTERED ([AfdID]);