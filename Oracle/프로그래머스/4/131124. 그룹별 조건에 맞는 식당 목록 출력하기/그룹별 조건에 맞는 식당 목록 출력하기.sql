SELECT MP.MEMBER_NAME, RR.REVIEW_TEXT, TO_CHAR(RR.REVIEW_DATE, 'YYYY-MM-DD') AS REVIEW_DATE
FROM MEMBER_PROFILE MP
INNER JOIN REST_REVIEW RR
ON MP.MEMBER_ID = RR.MEMBER_ID
WHERE MP.MEMBER_ID = (SELECT MEMBER_ID
                  FROM REST_REVIEW
                  GROUP BY MEMBER_ID
                  ORDER BY COUNT(REVIEW_ID) DESC
                  FETCH FIRST 1 ROW ONLY)
ORDER BY RR.REVIEW_DATE ASC, RR.REVIEW_TEXT ASC;