-- 18. Temperatures #0
use hbtn_0c_0;
source temperatures.sql;
SELECT city, value 'average' FROM temperatures ORDER BY value DESC;
