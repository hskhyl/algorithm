SELECT
    ED_p.ID AS ID,
    COUNT(ED_c.ID) AS CHILD_COUNT
FROM ECOLI_DATA ED_p
LEFT JOIN ECOLI_DATA ED_c ON ED_p.ID = ED_c.PARENT_ID
GROUP BY ED_p.ID
ORDER BY 1 ASC;