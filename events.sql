DECLARE year_events INT64;
SET year_events = 2021;

SELECT 
   period,STRING_AGG(CONCAT(type,"=",counts),",") AS event 
FROM (
    SELECT 
      CONCAT("Q",CAST(EXTRACT(QUARTER FROM dt) AS STRING),"'",SUBSTRING(CAST(EXTRACT(YEAR FROM dt) AS STRING),3,2)) AS period,
      type,
      COUNT(type) AS counts
    FROM `PROJECT.ProcessData.events` 
    WHERE EXTRACT(YEAR FROM dt) = year_events
    GROUP BY 1,2) agg_events
GROUP BY period
ORDER BY period,event asc