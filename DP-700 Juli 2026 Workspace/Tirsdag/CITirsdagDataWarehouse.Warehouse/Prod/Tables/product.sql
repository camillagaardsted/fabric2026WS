CREATE TABLE [Prod].[product] (

	[product_id] smallint NULL, 
	[recipe_id] smallint NULL, 
	[product_name_dk] varchar(8000) NULL, 
	[product_name_uk] varchar(8000) NULL, 
	[quantity_g] int NULL, 
	[quantity_oz] decimal(5,2) NULL, 
	[product_subcategory_id] smallint NULL, 
	[retail_price] decimal(9,2) NULL, 
	[cost_price] decimal(9,2) NULL
);