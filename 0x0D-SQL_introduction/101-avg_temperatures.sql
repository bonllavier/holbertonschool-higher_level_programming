-- 18. Temperatures #0
use hbtn_0c_0;
source temperatures.sql;
SELECT city, AVG(value) 'avg_temp' FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
