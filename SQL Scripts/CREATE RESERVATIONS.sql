CREATE TABLE IF NOT EXISTS RESERVATIONS (
    RESERVATION_ID VARCHAR(36) PRIMARY KEY,
    USER_ID VARCHAR(50) NOT NULL,
    BUSINESS_ID VARCHAR(50) NOT NULL,
    SLOT TIMESTAMP NOT NULL,
    NUMBER_OF_PEOPLE INTEGER NOT NULL,
    STATUS VARCHAR(10) NOT NULL CHECK (status IN ('CONFIRMED', 'REJECTED'))
);