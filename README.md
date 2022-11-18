# About
This program intergrates data sources into target systems then verifies data  quality by conducting a range of quality checks on staged data in the billing-datawarehouse by looking for missing values and dublicated records.The program achieves the objective of decoupling processing from source systems, helpnig to miniimize data corruption and acting as an archive at the same time.


 
# Table of Content:
1. Design and implement billing-datawarehouse schema.
2. Load Customer and Month dimension tables.
3. Load data into the FactBilling fact table. 
4. Verify loaded data.
5. Perform data quality checks
    
    5.1 Check Null values

    5.2 Check Duplicate values

    5.3 Check Min Max
    
    5.4 Check Invalid values
    
6. Generate a report on data quality.
