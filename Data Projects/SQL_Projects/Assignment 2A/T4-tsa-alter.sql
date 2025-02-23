--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T4-tsa-alter.sql

--Student ID: 33475881
--Student Name: Peichun Shih
--Unit Code: FIT9132 Introduction to databases - S1 2023
--Applied Class No: A03

/* Comments for your marker:

*/

--4(a)
DESC cabin;

ALTER TABLE cabin ADD (
    cabin_booking_no NUMBER(4, 0) DEFAULT 0 NOT NULL
);

COMMENT ON COLUMN cabin.cabin_booking_no IS
    'Current number of bookings of the cabin';

DESC cabin;

SELECT
    *
FROM
    cabin;

UPDATE cabin
SET
    cabin_booking_no = (
        SELECT
            COUNT(*)
        FROM
            booking
        WHERE
                cabin.resort_id = booking.resort_id
            AND cabin.cabin_no = booking.cabin_no
    );

SELECT
    *
FROM
    cabin;

COMMIT;

--4(b)
DROP TABLE staff_role CASCADE CONSTRAINTS PURGE;

CREATE TABLE staff_role (
    staff_role_id          CHAR(1) NOT NULL,
    staff_role_name        VARCHAR2(50) NOT NULL,
    staff_role_description VARCHAR2(250) NOT NULL
);

COMMENT ON COLUMN staff_role.staff_role_id IS
    'Staff role identifier';

COMMENT ON COLUMN staff_role.staff_role_name IS
    'The name of the staff role';

COMMENT ON COLUMN staff_role.staff_role_description IS
    'The description of the staff role';

ALTER TABLE staff_role ADD CONSTRAINT staff_role_pk PRIMARY KEY ( staff_role_id );

ALTER TABLE staff_role
    ADD CONSTRAINT chk_staff_role CHECK ( staff_role_id IN ( 'A', 'C', 'M' ) );

DESC staff_role;

INSERT INTO staff_role VALUES (
    'A',
    'Admin',
    'Take bookings, and reply to customer inquiries'
);

INSERT INTO staff_role VALUES (
    'C',
    'Cleaning',
    'Clean cabins and maintain resort''s public area'
);

INSERT INTO staff_role VALUES (
    'M',
    'Marketing',
    'Prepare and present marketing ideas and deliverables.'
);

SELECT
    *
FROM
    staff_role;

SELECT
    *
FROM
    staff;

ALTER TABLE staff ADD (
    staff_role_id CHAR(1) DEFAULT 'A' NOT NULL
);

ALTER TABLE staff ADD (
    CONSTRAINT chk_staff_staff_role_id CHECK ( staff_role_id IN ( 'A', 'C', 'M' ) )
);

ALTER TABLE staff
    ADD CONSTRAINT staff_role_staff FOREIGN KEY ( staff_role_id )
        REFERENCES staff_role ( staff_role_id );

DESC staff;

SELECT
    *
FROM
    staff;

COMMIT;
  
--4(c)
-- drop table statements
DROP TABLE cleaning CASCADE CONSTRAINTS PURGE;

DROP TABLE staff_cleaning CASCADE CONSTRAINTS PURGE;

-- adding CLEANING table
CREATE TABLE cleaning (
    cleaning_no   NUMBER(6) NOT NULL,
    resort_id     NUMBER(4) NOT NULL,
    cabin_no      NUMBER(3) NOT NULL,
    cleaning_date DATE NOT NULL
);

COMMENT ON COLUMN cleaning.cleaning_no IS
    'Surrogate key added to replace CLEANING composite PK';

COMMENT ON COLUMN cleaning.resort_id IS
    'Resort identifier';

COMMENT ON COLUMN cleaning.cabin_no IS
    'Cabin number within the resort';

COMMENT ON COLUMN cleaning.cleaning_date IS
    'Cabin cleaning date';

ALTER TABLE cleaning ADD CONSTRAINT cleaning_pk PRIMARY KEY ( cleaning_no );

ALTER TABLE cleaning
    ADD CONSTRAINT cleaning_uq UNIQUE ( resort_id,
                                        cabin_no,
                                        cleaning_date );

-- adding STAFF_CLEANING table
CREATE TABLE staff_cleaning (
    cleaning_no              NUMBER(6) NOT NULL,
    staff_id                 NUMBER(5) NOT NULL,
    staff_cleaning_starttime DATE NOT NULL,
    staff_cleaning_endtime   DATE NOT NULL
);

COMMENT ON COLUMN staff_cleaning.cleaning_no IS
    'The identifier of Cabin cleaning on a specific date';

COMMENT ON COLUMN staff_cleaning.staff_id IS
    'Staff identifier';

COMMENT ON COLUMN staff_cleaning.staff_cleaning_starttime IS
    'The start time of a specific staff''s cabin cleaning';

COMMENT ON COLUMN staff_cleaning.staff_cleaning_endtime IS
    'The end time of a specific staff''s cabin cleaning';

ALTER TABLE staff_cleaning ADD CONSTRAINT staff_cleaning_pk PRIMARY KEY ( staff_id,
                                                                          cleaning_no
                                                                          );
                                                                          
-- adding FKs
ALTER TABLE cleaning
    ADD CONSTRAINT cabin_cleaning FOREIGN KEY ( resort_id,
                                                cabin_no )
        REFERENCES cabin ( resort_id,
                           cabin_no );

ALTER TABLE staff_cleaning
    ADD CONSTRAINT cleanng_staff_cleaning FOREIGN KEY ( cleaning_no )
        REFERENCES cleaning ( cleaning_no );

ALTER TABLE staff_cleaning
    ADD CONSTRAINT staff_staff_cleaning FOREIGN KEY ( staff_id )
        REFERENCES staff ( staff_id );

DESC cleaning;
DESC staff_cleaning;