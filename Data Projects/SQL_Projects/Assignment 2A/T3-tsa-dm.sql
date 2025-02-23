--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T3-tsa-dm.sql

--Student ID: 33475881
--Student Name: Peichun Shih
--Unit Code: FIT9132 Introduction to databases - S1 2023
--Applied Class No: A03

/* Comments for your marker:

*/

---**This command shows the outputs of triggers**---
---**Run the command before running the insert statements.**---
---**Do not remove**---
SET SERVEROUTPUT ON
---**end**---

--3(a)

DROP SEQUENCE booking_id_seq;

CREATE SEQUENCE booking_id_seq START WITH 100 INCREMENT BY 10;

SELECT
    *
FROM
    cat;
    
--3(b)
-- checking resort_id of 'Awesome Resort'
SELECT
    resort_id
FROM
         resort
    NATURAL JOIN town
WHERE
        resort_name = 'Awesome Resort'
    AND town_lat = - 17.9644
    AND town_long = 122.2304;

SELECT
    *
FROM
    cabin;

INSERT INTO cabin VALUES (
    4,
    4,
    4,
    10,
    'I',
    220,
    'The new 4-bedroom cabin with 10 sleeping capacity.'
);

SELECT
    *
FROM
    cabin;

COMMIT;

--3(c)
-- checking member_id of Noah Garrard
SELECT
    member_id
FROM
    member
WHERE
        member_no = 2
    AND resort_id = 9;

--checking staff_id of Reeba Wildman
SELECT
    staff_id
FROM
    staff
WHERE
    staff_phone = '0493427245';

SELECT
    *
FROM
    booking;

INSERT INTO booking VALUES (
    booking_id_seq.NEXTVAL,
    4,
    4,
    TO_DATE('26/05/2023', 'dd/mm/yyyy'),
    TO_DATE('28/05/2023', 'dd/mm/yyyy'),
    4,
    4,
    (
        SELECT
            cabin.cabin_points_cost_day
        FROM
            cabin
        WHERE
                resort_id = 4
            AND cabin_no = 4
    ) * ( TO_DATE('28/05/2023', 'dd/mm/yyyy') - TO_DATE('26/05/2023', 'dd/mm/yyyy') )
    ,
    18,
    8
);

SELECT
    *
FROM
    booking;

COMMIT;

--3(d)
SELECT
    *
FROM
    booking;

UPDATE booking
SET
    booking_to = TO_DATE('29/05/2023', 'dd/mm/yyyy'),
    booking_total_points_cost = (
        SELECT
            cabin.cabin_points_cost_day
        FROM
            cabin
        WHERE
                resort_id = 4
            AND cabin_no = 4
    ) * ( TO_DATE('29/05/2023', 'dd/mm/yyyy') - TO_DATE('26/05/2023', 'dd/mm/yyyy') )
WHERE
        resort_id = 4
    AND cabin_no = 4
    AND booking_from = TO_DATE('26/05/2023', 'dd/mm/yyyy');

SELECT
    *
FROM
    booking;

COMMIT;

--3(e)
SELECT
    *
FROM
    booking;

DELETE FROM booking
WHERE
        resort_id = 4
    AND cabin_no = 4;

SELECT
    *
FROM
    booking;

SELECT
    *
FROM
    cabin;

DELETE FROM cabin
WHERE
        resort_id = 4
    AND cabin_no = 4;

SELECT
    *
FROM
    cabin;

COMMIT;