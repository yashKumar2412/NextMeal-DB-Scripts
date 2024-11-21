DROP TABLE IF EXISTS USERS;

CREATE TABLE USERS (
    USER_ID VARCHAR(50) PRIMARY KEY,    -- Unique identifier for the user
    NAME VARCHAR(100),                  -- User's name
    REVIEW_COUNT INTEGER,               -- Number of reviews written by the user
    YELPING_SINCE TIMESTAMP,            -- When the user joined Yelp
    USEFUL INTEGER,                     -- Count of 'useful' votes
    FUNNY INTEGER,                      -- Count of 'funny' votes
    COOL INTEGER                        -- Count of 'cool' votes
);