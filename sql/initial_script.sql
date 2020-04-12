CREATE TABLE IF NOT EXISTS Classifieds (
  id VARCHAR(30) DEFAULT '',
  customer_id VARCHAR(30) DEFAULT '',
  created_at VARCHAR(30) DEFAULT '',
  text VARCHAR(400) DEFAULT '',
  ad_type VARCHAR(30) DEFAULT '',
  price DECIMAL( 7,3 ) DEFAULT 0.0,
  currency VARCHAR(30) DEFAULT '',
  payment_type VARCHAR(30) DEFAULT '',
  payment_cost DECIMAL( 7,3 ) DEFAULT 0.0
);

CREATE TABLE IF NOT EXISTS Margin_info (
  discriminator VARCHAR(20),
  type VARCHAR(20),
  from_timestamp VARCHAR(30),
  to_timestamp VARCHAR(30),
  margin DECIMAL( 7,3 ));
