#1
SELECT ticket_client
FROM tickets
WHERE csat < 3;   #Только те тикеты, где оценка csat меньше 3

#2
SELECT ticket_id
FROM tickets
WHERE LOWER(text) LIKE '%отлично%' #Ищем тикеты, в которых встречается слово "отлично" (независимо от регистра)
ORDER BY csat DESC;   #Сортируем по оценке csat в порядке убывания

#3
SELECT orders.order_client_id AS frequent_customer, MAX(orders.price) AS max_sum  #Выбираем ID клиента и максимальную сумму заказа
FROM orders
JOIN clients ON orders.order_client_id = clients.client_id  #Соединяем таблицу заказов с таблицей клиентов
WHERE orders.place IN ('Теремок', 'Вкусно и точка')
AND orders.price BETWEEN 2000 AND 10000
GROUP BY orders.order_client_id  #Группируем по клиентам
HAVING COUNT(orders.order_id) > 5;  #Убираем клиентов, у которых менее 5 заказов

#4
SELECT orders.*, clients.username, clients.name, clients.age, clients.city, tickets.csat, tickets.text  #Выбираем все данные о заказах, клиентах и тикетах
FROM orders
JOIN clients ON orders.order_client_id = clients.client_id
JOIN tickets ON orders.order_client_id = tickets.ticket_client  #Соединяем таблицы
LIMIT 1000;
