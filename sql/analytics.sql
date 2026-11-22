-- Count all records
SELECT COUNT(*) AS total_records
FROM ridership;

-- Total ridership by borough
SELECT
    borough,
    SUM(ridership) AS total_ridership
FROM ridership
GROUP BY borough
ORDER BY total_ridership DESC;

-- Average ridership by hour
SELECT
    hour,
    AVG(ridership) AS avg_ridership
FROM ridership
GROUP BY hour
ORDER BY hour;
