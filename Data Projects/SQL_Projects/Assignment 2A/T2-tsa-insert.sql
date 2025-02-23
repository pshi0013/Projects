/*****PLEASE ENTER YOUR DETAILS BELOW*****/
--T2-tsa-insert.sql

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

--------------------------------------
--INSERT INTO cabin
--------------------------------------
INSERT INTO cabin VALUES (
    1,
    1,
    4,
    16,
    'I',
    100,
    'The 4-bedroom cabin offers a rustic mountain style with 16 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    1,
    2,
    3,
    12,
    'I',
    100,
    'The 3-bedroom cabin offers a rustic mountain style with 12 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    1,
    3,
    4,
    20,
    'I',
    100,
    'The 4-bedroom cabin offers a rustic mountain style with 20 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    2,
    1,
    2,
    10,
    'C',
    50,
    'The 2-bedroom cabin offers a home for your perfect stay with 10 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    2,
    2,
    4,
    20,
    'C',
    50,
    'The 4-bedroom cabin offers a home for your perfect stay with 20 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    2,
    3,
    1,
    4,
    'I',
    100,
    'The 1-bedroom cabin offers a home for your perfect stay with 4 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    2,
    4,
    3,
    12,
    'I',
    100,
    'The 3-bedroom cabin offers a home for your perfect stay with 12 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    3,
    1,
    3,
    12,
    'I',
    100,
    'The 3-bedroom cabin offers an eacape from busy dailylife with 12 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    3,
    2,
    1,
    6,
    'I',
    100,
    'The 1-bedroom cabin offers an eacape from busy dailylife with 6 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    4,
    1,
    4,
    10,
    'I',
    100,
    'The 4-bedroom cabin offers a cozy stay with 10 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    5,
    1,
    2,
    12,
    'C',
    50,
    'The 2-bedroom cabin offers a warm stay with 12 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    5,
    2,
    2,
    12,
    'C',
    50,
    'The 2-bedroom cabin offers a warm stay with 12 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    6,
    1,
    4,
    16,
    'I',
    100,
    'The 4-bedroom cabin offers a wonderful vacation with 16 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    7,
    1,
    1,
    4,
    'I',
    150,
    'The 1-bedroom cabin offers a private and relaxing stay with 4 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    8,
    1,
    4,
    20,
    'C',
    50,
    'The 4-bedroom cabin offers an awesome vacation with 20 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    9,
    1,
    2,
    10,
    'C',
    50,
    'The 2-bedroom cabin offers a forest view with 10 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    9,
    2,
    4,
    16,
    'I',
    100,
    'The 4-bedroom cabin offers a forest view with 16 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    9,
    3,
    1,
    4,
    'I',
    100,
    'The 1-bedroom cabin offers a forest view with 4 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    10,
    1,
    3,
    18,
    'C',
    50,
    'The 3-bedroom cabin with 18 sleeping capacity.'
);

INSERT INTO cabin VALUES (
    10,
    2,
    4,
    20,
    'C',
    50,
    'The 4-bedroom cabin with 20 sleeping capacity.'
);

--------------------------------------
--INSERT INTO booking
--------------------------------------
INSERT INTO booking VALUES (
    1,
    1,
    1,
    TO_DATE('01/03/2023', 'dd/mm/yyyy'),
    TO_DATE('08/03/2023', 'dd/mm/yyyy'),
    12,
    4,
    700,
    1,
    1
);

INSERT INTO booking VALUES (
    2,
    1,
    1,
    TO_DATE('09/03/2023', 'dd/mm/yyyy'),
    TO_DATE('14/03/2023', 'dd/mm/yyyy'),
    10,
    6,
    500,
    2,
    2
);

INSERT INTO booking VALUES (
    3,
    1,
    1,
    TO_DATE('14/03/2023', 'dd/mm/yyyy'),
    TO_DATE('19/03/2023', 'dd/mm/yyyy'),
    16,
    0,
    500,
    3,
    3
);

INSERT INTO booking VALUES (
    4,
    2,
    1,
    TO_DATE('01/03/2023', 'dd/mm/yyyy'),
    TO_DATE('06/03/2023', 'dd/mm/yyyy'),
    8,
    2,
    250,
    2,
    4
);

INSERT INTO booking VALUES (
    5,
    2,
    1,
    TO_DATE('13/03/2023', 'dd/mm/yyyy'),
    TO_DATE('19/03/2023', 'dd/mm/yyyy'),
    6,
    4,
    300,
    1,
    6
);

INSERT INTO booking VALUES (
    6,
    2,
    1,
    TO_DATE('20/03/2023', 'dd/mm/yyyy'),
    TO_DATE('27/03/2023', 'dd/mm/yyyy'),
    6,
    4,
    350,
    3,
    6
);

INSERT INTO booking VALUES (
    7,
    2,
    2,
    TO_DATE('01/03/2023', 'dd/mm/yyyy'),
    TO_DATE('11/03/2023', 'dd/mm/yyyy'),
    16,
    4,
    500,
    4,
    7
);

INSERT INTO booking VALUES (
    8,
    2,
    2,
    TO_DATE('12/03/2023', 'dd/mm/yyyy'),
    TO_DATE('22/03/2023', 'dd/mm/yyyy'),
    20,
    0,
    500,
    5,
    8
);

INSERT INTO booking VALUES (
    9,
    2,
    2,
    TO_DATE('23/03/2023', 'dd/mm/yyyy'),
    TO_DATE('30/03/2023', 'dd/mm/yyyy'),
    10,
    10,
    350,
    6,
    9
);

INSERT INTO booking VALUES (
    10,
    3,
    1,
    TO_DATE('01/04/2023', 'dd/mm/yyyy'),
    TO_DATE('08/04/2023', 'dd/mm/yyyy'),
    8,
    4,
    700,
    7,
    10
);

INSERT INTO booking VALUES (
    11,
    3,
    2,
    TO_DATE('01/04/2023', 'dd/mm/yyyy'),
    TO_DATE('08/04/2023', 'dd/mm/yyyy'),
    6,
    0,
    700,
    8,
    11
);

INSERT INTO booking VALUES (
    12,
    4,
    1,
    TO_DATE('10/04/2023', 'dd/mm/yyyy'),
    TO_DATE('20/04/2023', 'dd/mm/yyyy'),
    6,
    0,
    1000,
    9,
    12
);

INSERT INTO booking VALUES (
    13,
    5,
    1,
    TO_DATE('01/04/2023', 'dd/mm/yyyy'),
    TO_DATE('11/04/2023', 'dd/mm/yyyy'),
    6,
    3,
    500,
    10,
    13
);

INSERT INTO booking VALUES (
    14,
    5,
    2,
    TO_DATE('01/04/2023', 'dd/mm/yyyy'),
    TO_DATE('08/04/2023', 'dd/mm/yyyy'),
    8,
    4,
    350,
    11,
    14
);

INSERT INTO booking VALUES (
    15,
    6,
    1,
    TO_DATE('08/04/2023', 'dd/mm/yyyy'),
    TO_DATE('13/04/2023', 'dd/mm/yyyy'),
    10,
    6,
    500,
    12,
    15
);

INSERT INTO booking VALUES (
    16,
    7,
    1,
    TO_DATE('14/04/2023', 'dd/mm/yyyy'),
    TO_DATE('17/04/2023', 'dd/mm/yyyy'),
    2,
    2,
    450,
    12,
    16
);

INSERT INTO booking VALUES (
    17,
    7,
    1,
    TO_DATE('18/04/2023', 'dd/mm/yyyy'),
    TO_DATE('23/04/2023', 'dd/mm/yyyy'),
    2,
    2,
    750,
    13,
    17
);

INSERT INTO booking VALUES (
    18,
    8,
    1,
    TO_DATE('21/04/2023', 'dd/mm/yyyy'),
    TO_DATE('28/04/2023', 'dd/mm/yyyy'),
    16,
    4,
    350,
    14,
    18
);

INSERT INTO booking VALUES (
    19,
    9,
    2,
    TO_DATE('01/03/2023', 'dd/mm/yyyy'),
    TO_DATE('11/03/2023', 'dd/mm/yyyy'),
    12,
    4,
    1000,
    15,
    1
);

INSERT INTO booking VALUES (
    20,
    10,
    1,
    TO_DATE('12/03/2023', 'dd/mm/yyyy'),
    TO_DATE('22/03/2023', 'dd/mm/yyyy'),
    10,
    8,
    500,
    16,
    2
);

COMMIT;

SELECT
    *
FROM
    cabin;

SELECT
    *
FROM
    booking;