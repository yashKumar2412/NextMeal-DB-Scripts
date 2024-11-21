DROP TABLE IF EXISTS RESTAURANTS;

CREATE TABLE RESTAURANTS (
    BUSINESS_ID VARCHAR(50) PRIMARY KEY,     -- Unique identifier for the business
    NAME VARCHAR(255),                       -- Business name
    ADDRESS VARCHAR(255),                    -- Business address
    CITY VARCHAR(100),                       -- City
    STATE CHAR(2),                           -- State abbreviation
    POSTAL_CODE VARCHAR(20),                 -- Postal/ZIP code
    LATITUDE DOUBLE PRECISION,               -- Latitude (geographical coordinate)
    LONGITUDE DOUBLE PRECISION,              -- Longitude (geographical coordinate)
    STARS NUMERIC(2, 1),                     -- Star rating (e.g., 4.0)
    REVIEW_COUNT INTEGER,                    -- Number of reviews
    IS_OPEN SMALLINT,                        -- Whether the business is open (1 for open, 0 for closed)
    ATTRIBUTES JSONB,                        -- Attributes stored as JSONB for flexibility
    CATEGORIES TEXT,                         -- Categories (comma-separated)
    HOURS JSONB                              -- Operating hours stored as JSONB
);