#1
SELECT ticket_client
FROM tickets
WHERE csat < 3;

#2
SELECT ticket_id
FROM tickets
WHERE LOWER(text) LIKE '%отлично%'
ORDER BY csat DESC;

#3
SELECT orders.order_client_id AS frequent_customer, MAX(orders.price) AS max_sum
FROM orders
JOIN clients ON orders.order_client_id = clients.client_id
WHERE orders.place IN ('Теремок', 'Вкусно и точка')
AND orders.price BETWEEN 2000 AND 10000
GROUP BY orders.order_client_id
HAVING COUNT(orders.order_id) > 5;

#4
SELECT orders.*, clients.username, clients.name, clients.age, clients.city, tickets.csat, tickets.text
FROM orders
JOIN clients ON orders.order_client_id = clients.client_id
JOIN tickets ON orders.order_client_id = tickets.ticket_client
LIMIT 1000;

