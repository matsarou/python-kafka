SELECT ad_type,SUM(margin_func(price, payment_cost))
FROM  Classifieds
WHERE created_at BETWEEN '2020-04-08T18:07:32.1688783Z' AND '2020-04-09T00:57:32.5045605Z'
GROUP BY ad_type;

SELECT payment_type,SUM(margin_func(price, payment_cost))
FROM  Classifieds
WHERE created_at BETWEEN '2020-04-08T18:07:32.1688783Z' AND '2020-04-09T00:57:32.5045605Z'
GROUP BY payment_type;