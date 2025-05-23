SELECT UGU.USER_ID, UGU.NICKNAME, TARGET_ID.TOTAL_SALES
FROM (
    SELECT WRITER_ID, SUM(PRICE) AS TOTAL_SALES
    FROM USED_GOODS_BOARD
    WHERE STATUS = 'DONE'
    GROUP BY WRITER_ID
    HAVING SUM(PRICE) >= 700000
) TARGET_ID
INNER JOIN USED_GOODS_USER UGU
ON TARGET_ID.WRITER_ID = UGU.USER_ID
ORDER BY TARGET_ID.TOTAL_SALES ASC