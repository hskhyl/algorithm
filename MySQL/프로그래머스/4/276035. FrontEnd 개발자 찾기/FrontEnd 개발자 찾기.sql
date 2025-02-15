SELECT DISTINCT D.ID, D.EMAIL, D.FIRST_NAME, D.LAST_NAME
FROM SKILLCODES S
INNER JOIN DEVELOPERS D
ON (S.CODE & D.SKILL_CODE) = S.CODE
WHERE S.CATEGORY = 'Front End'
ORDER BY 1 ASC;
