WITH TARGET_CODE AS (
    SELECT 
        (SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End') AS total_front,
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') AS python_code,
        (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') AS csharp_code
)
SELECT 
    CASE
        WHEN (D.SKILL_CODE & TC.total_front) != 0 AND (D.SKILL_CODE & TC.python_code) != 0 THEN 'A'
        WHEN (D.SKILL_CODE & TC.csharp_code) = TC.csharp_code THEN 'B'
        ELSE 'C'
    END AS GRADE,
    D.ID,
    D.EMAIL
FROM DEVELOPERS D, TARGET_CODE TC
WHERE (D.SKILL_CODE & TC.csharp_code) = TC.csharp_code
    OR (D.SKILL_CODE & TC.total_front) != 0
ORDER BY 1, 2;