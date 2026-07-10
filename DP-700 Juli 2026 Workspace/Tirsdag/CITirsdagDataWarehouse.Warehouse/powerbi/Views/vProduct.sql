-- Auto Generated (Do not modify) BC303DA9A859C12816BE791013BD27E2439350F5F2E8F43DB0344B00C348A5C5




CREATE VIEW [powerbi].[vProduct] AS
SELECT      pp.product_name_dk AS Product 
            , pp.product_id 
            , pc.product_category_name_dk AS Category
            , ps.product_subcategory_name_dk AS Subcategory
            , pp.retail_price
            ,pp.cost_price
FROM        prod.product pp
            INNER JOIN prod.product_subcategory ps ON pp.product_subcategory_id=ps.product_subcategory_id
            INNER JOIN prod.product_category pc ON pc.product_category_id = ps.product_category_id