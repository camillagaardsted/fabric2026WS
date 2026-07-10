CREATE TABLE [bronze].[raspdataFromDatalake] (

	[sensorid] bigint NULL, 
	[timestamp] datetime2(6) NULL, 
	[temperature_from_humidity] float NULL, 
	[temperature_from_pressure] float NULL, 
	[humidity] float NULL, 
	[pressure] float NULL
);