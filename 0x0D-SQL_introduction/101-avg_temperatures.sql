-- script that displays the average temperatures(Fahrenheit) by city ordered
--by temperatures descending
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
