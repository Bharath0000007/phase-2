CREATE TABLE suppliers (
    supplier_id INT,
    supplier_name VARCHAR(100)
);

CREATE TABLE purchase_orders (
    po_id INT,
    po_number VARCHAR(50),
    supplier_id INT
);

CREATE TABLE shipments (
    shipment_id VARCHAR(20),
    carrier VARCHAR(50),
    origin VARCHAR(50),
    destination VARCHAR(50),
    delay_days INT,
    po_id INT
);

INSERT INTO suppliers (supplier_id, supplier_name) VALUES
(1, 'ABC Supplies'),
(2, 'Global Components'),
(3, 'TechParts Ltd');


INSERT INTO purchase_orders (po_id, po_number, supplier_id) VALUES
(101, 'PO-1001', 1),
(102, 'PO-1002', 2),
(103, 'PO-1003', 3);


INSERT INTO shipments
    (shipment_id, carrier, origin, destination, delay_days, po_id)
VALUES
('S001', 'FastFreight', 'Hyderabad', 'Bangalore', 0, 101),
('S002', 'QuickShip', 'Mumbai', 'Delhi', 2, 102),
('S003', 'FastFreight', 'Chennai', 'Hyderabad', 5, 103),
('S004', 'QuickShip', 'Pune', 'Mumbai', 1, 101),
('S005', 'FastFreight', 'Delhi', 'Chennai', 3, 102);

-- 1. Filtering: find delayed shipments

SELECT shipment_id, carrier, delay_days
FROM shipments
WHERE delay_days > 0;


-- 2. Joining: which supplier does each shipment's PO belong to?

SELECT s.shipment_id, po.po_number, sup.supplier_name
FROM shipments s
JOIN purchase_orders po ON s.po_id = po.po_id
JOIN suppliers sup ON po.supplier_id = sup.supplier_id;

-- 3. Aggregating: average delay per carrier

SELECT carrier,
       AVG(delay_days) AS avg_delay,
       COUNT(*) AS shipment_count
FROM shipments
GROUP BY carrier
ORDER BY avg_delay DESC;