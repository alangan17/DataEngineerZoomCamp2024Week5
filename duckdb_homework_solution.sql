-- Q4
with
base as (
    SELECT 
    CAST(dropOff_datetime AS DATE) AS date_only,
    dropOff_datetime,
    pickup_datetime,
    (EXTRACT(EPOCH FROM dropOff_datetime - pickup_datetime) / 3600) AS hours_difference
    FROM read_parquet("data/fhv_201910_repartition/*.parquet")
    WHERE 1=1
),
pick
select
    date_only,
    hours_difference
from base
order by hours_difference desc
;