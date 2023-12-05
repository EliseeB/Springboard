-- write your queries here


SELECT 
    owners.id,
    owners.first_name,
    owners.last_name, 
    vehicles.id, 
    vehicles.make, 
    vehicles.model, 
    vehicles.year,
    vehicles.price, 
    vehicles.owner_id
FROM 
    owners
FULL JOIN 
    vehicles ON owners.id = vehicles.owner_id;




SELECT 
    owners.first_name fn, 
    owners.last_name ln, 
    COUNT(vehicles.owner_id)
FROM 
    owners
JOIN 
    vehicles ON owners.id = vehicles.owner_id
GROUP BY 
    fn, ln
ORDER BY 
    fn;



SELECT 
    owners.first_name first_name, 
    owners.last_name last_name, 
    CAST( AVG(vehicles.price) AS INTEGER ) average_price, 
    COUNT(vehicles.owner_id)
FROM 
    owners
JOIN 
    vehicles ON owners.id = vehicles.owner_id
GROUP BY 
    first_name, last_name
HAVING 
    AVG(vehicles.price) > 10000 AND COUNT(vehicles.owner_id) > 1
ORDER BY 
    first_name DESC;