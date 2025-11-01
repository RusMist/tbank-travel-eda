# Описание столбцов

### Техническая информация по заказу
- `order_online_payment_flg` — флаг онлайн-оплаты  
- `client_rk` — идентификатор клиента  
- `order_rk` — идентификатор заказа  
- `order_status_cd` — статус заказа (расшифровка внизу)  
- `order_type_cd` — продукт: авиа / отели  
- `created_dttm` — дата создания заказа  
- `order_item_cnt` — количество позиций в заказе  
- `nominal_price_eur_amt` — сумма заказа в евро  
- `nominal_price_rub_amt` — сумма заказа в рублях  
- `hotel_country` — страна отеля  
- `hotel_city` — город отеля  

---

### Подписки и акции
- `loyalty_program_type_nm` — тип программы лояльности (All Airlines / Black)  
- `bundle_nm` — подписка, применившаяся к оплате (Pro / Premium)  
- `promo_code_discount_amt` — размер скидки по промокоду  
- `loyalty_accrual_rub_amt` — начисление бонусных баллов  

---

### Уведомления и коммуникации
- `suppress_email_flg` — отказ от коммуникаций по почте  
- `suppress_call_flg` — отказ от коммуникаций по телефону  
- `bounce_cd` — код SMTP-ответа (отсутствие кода = успешная отправка)  
- `last_sms_success_flg` — было ли последнее СМС успешным  
- `mobile_phone_operator_nm` — оператор мобильной связи  
- `last_sms_dt` — дата последнего СМС  
- `email_valid_flg` — флаг валидности e-mail  
- `good_email_address_flg` — флаг хорошего адреса  
- `bad_email_address_flg` — флаг плохого адреса  

---

### Даты и время
- `created_dttm` — дата создания заказа  
- `book_start_dttm` — дата заезда (для отелей)  
- `book_end_dttm` — дата выезда (для отелей)  
- `party_first_order_dt` — дата первого заказа у клиента  

---

### Информация о клиенте
- `party_first_order_type_dt` — тип первого заказа (авиа / отели)  
- `month_beginning_balance_rub` — баланс в рублях на начало месяца покупки  
- `monthly_income_amt` — месячный доход  
- `children_cnt` — количество детей  
- `age` — возраст клиента  
- `age_type_cd` — возрастная группа (по 20 лет)  
- `lvn_city_nm` — город проживания  
- `lvn_state_nm` — регион проживания  
- `mobile_phone_operator_nm` — оператор мобильной связи  
- `marital_status_cd` — семейный статус  
- `education_level_cd` — уровень образования  
- `gender_cd` — пол клиента  
