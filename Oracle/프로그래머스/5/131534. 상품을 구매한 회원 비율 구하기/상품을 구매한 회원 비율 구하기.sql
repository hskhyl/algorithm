SELECT 
    EXTRACT(YEAR FROM SALES_DATE) AS YEAR, 
    EXTRACT(MONTH FROM SALES_DATE) AS MONTH,
    COUNT(DISTINCT USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT USER_ID) / (SELECT COUNT(DISTINCT UI.USER_ID)
                             FROM USER_INFO UI
                             WHERE EXTRACT(YEAR FROM UI.JOINED) = 2021), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID IN (SELECT DISTINCT USER_ID FROM USER_INFO WHERE EXTRACT(YEAR FROM JOINED) = 2021)
GROUP BY EXTRACT(YEAR FROM SALES_DATE), EXTRACT(MONTH FROM SALES_DATE)
ORDER BY 1, 2;
          