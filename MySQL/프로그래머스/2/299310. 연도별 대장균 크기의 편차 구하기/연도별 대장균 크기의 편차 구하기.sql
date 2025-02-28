WITH SIZE_CTE AS (
    SELECT 
        YEAR(DIFFERENTIATION_DATE) AS YEAR,
        MAX(SIZE_OF_COLONY) AS MAX_SIZE
    FROM ECOLI_DATA
    GROUP BY YEAR(DIFFERENTIATION_DATE)
)
SELECT
    YEAR(ED.DIFFERENTIATION_DATE) AS YEAR,
    (SC.MAX_SIZE - ED.SIZE_OF_COLONY) AS YEAR_DEV,
    ED.ID AS ID
FROM ECOLI_DATA ED
LEFT JOIN SIZE_CTE SC ON YEAR(ED.DIFFERENTIATION_DATE) = SC.YEAR
ORDER BY 1, 2