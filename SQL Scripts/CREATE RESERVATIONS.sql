DROP TABLE IF EXISTS RESERVATIONS;

CREATE TABLE RESERVATIONS (
    RESERVATION_ID VARCHAR(36) PRIMARY KEY,    -- Primary key for the reservation
    USER_ID VARCHAR(50) NOT NULL,              -- Foreign key referencing the users table
    BUSINESS_ID VARCHAR(50) NOT NULL,          -- Foreign key referencing the restaurants table
    SLOT TIMESTAMP NOT NULL,                   -- Reservation date and time
    NUMBER_OF_PEOPLE INTEGER NOT NULL,         -- Number of people for the reservation
    STATUS VARCHAR(10) NOT NULL CHECK (status IN ('CONFIRMED', 'REJECTED')) -- Reservation status
);