-- This creates a superuser and 3 users
-- Argument Order: (id, password, last_login, is_superuser, username, first_name, email, is_staff, is_active, date_joined, last_name)
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$JAv11ttb79G1$WCfyLxs8i7hMnSHk7azyaow92SvORUaCu/oX1RwGv1M=', "2019-02-08 17:26:06.739338", 1, 'AdminDillon', 'Dillon', 'dillonwilliamsail@gmail.com', 1, 1, '2019-02-08 17:25:43', 'Williams');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$TH14Dm7ojtWQ$ArXT7OjsyiZ5Qxpr3Z8mFIp7Hh10m0qhDh0vtjsG4Dk=', "2019-02-08 17:29:12", 0,'cust1', 'User', 'exampleUser@gmail.com', 0, 1, '2019-02-08 17:28:14', 'One');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$aFwSrAL7i2fp$n+f+gG9Rx37PDzYT7E2v6WMUHPXmUKPWdQjOywBfW3o=', "2019-02-08 17:49:01", 0, 'cust2', 'User', 'user2@gmail.com', 0, 1, '2019-02-08 17:46:56', 'Two');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$wuZz8vSAxYxr$GXNEva0KNibqZnHkIvlcF0ie4ikjqrCMr2GA+wuDwPA=', "2019-02-08 17:50:31", 0, 'cust3', 'User', 'user3@gmail.com', 0, 1, '2019-02-08 17:50:04', 'Three');

-- Arguments (id, name, deletedOn)
INSERT INTO website_producttype VALUES (null, "Electronics", null);
INSERT INTO website_producttype VALUES (null, "Appliances", null);
INSERT INTO website_producttype VALUES (null, "Furniture", null);

-- Arguments (id, address, phoneNumber, user_id, deletedOn)
INSERT INTO website_customer VALUES (null, '123 Sesame Street', '615-938-3032', 2, null);
INSERT INTO website_customer VALUES (null, '4444 magnolia Street', '901-858-0122', 3, null);
INSERT INTO website_customer VALUES (null, '615 Acorn Avenue', '422-758-2311', 4, null);

-- Arguments (id, isCompleted, customer_id, paymentType_id, deletedOn)
INSERT INTO website_order VALUES (null, 0, 1, 1, null);
INSERT INTO website_order VALUES (null, 0, 2, 2, null);
INSERT INTO website_order VALUES (null, 0, 3, 3, null);

-- Arguments (id, name, accountNumber, customer_id, deletedOn)
INSERT INTO website_paymenttype VALUES (null, 'Visa Debit Card', 9384750384761023, 1, null);
INSERT INTO website_paymenttype VALUES (null, 'Amex Credit Card', 1058395877349245, 2, null);
INSERT INTO website_paymenttype VALUES (null, 'Mastercard Platinum', 9983632319577443, 3, null);

-- Arguments (id, title, description, price, quantity, customer_id, productType_id, deletedOn)
INSERT INTO website_product VALUES (null, "Computer", "2014 Macbook Pro: Mint condition (SSD, 256GB, i7 core)", 1500, 1, 1, 1, null);
INSERT INTO website_product VALUES (null, "Refridgerator", "2017 Samsung Smart Refridgerator: never used!", 1200, 1, 2, 2, null);
INSERT INTO website_product VALUES (null, "Office Chairs", "Standard black office chairs with mesh backing", 50, 6, 3, 3, null);

-- Arguments (id, order_id, product_id, deletedOn)
INSERT INTO website_productorder VALUES (null, 1, 1, null);
INSERT INTO website_productorder VALUES (null, 2, 2, null);
INSERT INTO website_productorder VALUES (null, 3, 3, null);

-- =============================================================
-- Below is the code we used to populate when migrations made the delete on key flip

-- INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$JAv11ttb79G1$WCfyLxs8i7hMnSHk7azyaow92SvORUaCu/oX1RwGv1M=', "2019-02-08 17:26:06.739338", 1, 'AdminDillon', 'Dillon', 'dillonwilliamsail@gmail.com', 1, 1, '2019-02-08 17:25:43', 'Williams');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$TH14Dm7ojtWQ$ArXT7OjsyiZ5Qxpr3Z8mFIp7Hh10m0qhDh0vtjsG4Dk=', "2019-02-08 17:29:12", 0,'cust1', 'User', 'exampleUser@gmail.com', 0, 1, '2019-02-08 17:28:14', 'One');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$aFwSrAL7i2fp$n+f+gG9Rx37PDzYT7E2v6WMUHPXmUKPWdQjOywBfW3o=', "2019-02-08 17:49:01", 0, 'cust2', 'User', 'user2@gmail.com', 0, 1, '2019-02-08 17:46:56', 'Two');
INSERT INTO auth_user VALUES (null, 'pbkdf2_sha256$120000$wuZz8vSAxYxr$GXNEva0KNibqZnHkIvlcF0ie4ikjqrCMr2GA+wuDwPA=', "2019-02-08 17:50:31", 0, 'cust3', 'User', 'user3@gmail.com', 0, 1, '2019-02-08 17:50:04', 'Three');

INSERT INTO website_producttype VALUES (null, "Electronics", null);
INSERT INTO website_producttype VALUES (null, "Appliances", null);
INSERT INTO website_producttype VALUES (null, "Furniture", null);

INSERT INTO website_customer VALUES (null, '123 Sesame Street', '615-938-3032', null, 1);
INSERT INTO website_customer VALUES (null, '4444 magnolia Street', '901-858-0122', null, 2);
INSERT INTO website_customer VALUES (null, '615 Acorn Avenue', '422-758-2311', null, 3);

INSERT INTO website_order VALUES (null, 0, null, 1, 1);
INSERT INTO website_order VALUES (null, 0, null, 2, 2);
INSERT INTO website_order VALUES (null, 0, null, 3, 3);

INSERT INTO website_paymenttype VALUES (null, 'Visa Debit Card', 9384750384761023, null, 1);
INSERT INTO website_paymenttype VALUES (null, 'Amex Credit Card', 1058395877349245, null, 2);
INSERT INTO website_paymenttype VALUES (null, 'Mastercard Platinum', 9983632319577443, null, 3);

INSERT INTO website_product VALUES (null, "Computer", "2014 Macbook Pro: Mint condition (SSD, 256GB, i7 core)", 1500, 1, null, 1, 1);
INSERT INTO website_product VALUES (null, "Refridgerator", "2017 Samsung Smart Refridgerator: never used!", 1200, 1, null, 2, 2);
INSERT INTO website_product VALUES (null, "Office Chairs", "Standard black office chairs with mesh backing", 50, 6, null, 3, 3);

INSERT INTO website_productorder VALUES (null, null, 1, 1);
INSERT INTO website_productorder VALUES (null, null, 2, 2);
INSERT INTO website_productorder VALUES (null, null, 3, 3);