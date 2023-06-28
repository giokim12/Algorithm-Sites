-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, I.NAME 
FROM ANIMAL_INS I JOIN ANIMAL_OUTS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.SEX_UPON_INTAKE LIKE '%Intact%' AND
O.SEX_UPON_OUTCOME not LIKE '%Intact%'
