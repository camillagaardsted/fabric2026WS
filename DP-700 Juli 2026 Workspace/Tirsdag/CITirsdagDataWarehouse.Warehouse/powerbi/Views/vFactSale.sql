-- Auto Generated (Do not modify) 889A3F214BB9CA3C3F68E3B8331516D4BBD5CA228968466586ACBC1AA6C6DA24
CREATE   VIEW [powerbi].[vFactSale] AS
SELECT      --I.order_id,
             CAST(I.order_date AS DATE)	AS order_date
            , CAST(I.ship_date AS DATE)		AS ship_date
            , I.employee_id            
            , SO.product_id
            , SO.quantity
            , SO.discount_pct
			,7 AS company_id
			-- her bruger vi en window function
            , 1.0*I.freight_dkk/COUNT(*) OVER (PARTITION BY I.order_id) AS FreightPart             
FROM        sale.order_company_internet I 
            INNER JOIN sale.order_line SO ON I.order_id=SO.order_id
--            INNER JOIN cust.company_contact CC ON CC.company_contact_id=I.company_contact_id
WHERE		SO.order_type = 2 -- for internet_ordre