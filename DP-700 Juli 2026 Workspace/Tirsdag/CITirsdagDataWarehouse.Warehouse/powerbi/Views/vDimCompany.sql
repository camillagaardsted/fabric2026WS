-- Auto Generated (Do not modify) DADAD34444A765A23E6AAB6417A8DB6EC21EF3FF1128521D8A270A4982618175


-- firma dim tabel
-- med geografisk info

CREATE VIEW [powerbi].[vDimCompany] AS
    SELECT      CC.company_id
                , CC.name AS CompanyName
                , G.country_txt_dk AS Country 
                , R.region_txt AS Region
                , GC.city_name AS City
                , GC.postal_code AS Zipcode
    FROM        cust.company CC                 
                INNER JOIN geo.city GC ON GC.country_id = CC.country_id AND GC.postal_code=CC.postal_code
                INNER JOIN geo.country G ON G.country_id = CC.country_id
                LEFT OUTER JOIN geo.region R ON R.region_id = GC.region_id

-- vi laver vores fact tabel med ordrer og ordrelinje og beslutter at fragt deles ligeligt ud på alle ordrelinjer for en ordre