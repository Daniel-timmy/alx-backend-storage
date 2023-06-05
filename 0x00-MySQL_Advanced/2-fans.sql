-- a SQL script that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
CREATE OR REPLACE VIEW v1 AS SELECT origin AS origin,SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY SUM(fans) DESC;
SELECT * FROM v1;
