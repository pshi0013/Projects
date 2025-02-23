--*****PLEASE ENTER YOUR DETAILS BELOW*****
--T2-tsa-select.sql

--Student ID: 33475881
--Student Name: Peichun Shih
--Unit Code: FIT9132
--Applied Class No: A03

/* Comments for your marker:

*/

/*2(a)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer
SELECT
    town_id,
    town_name,
    poi_type_id,
    poi_type_descr,
    COUNT(poi_type_id) AS poi_count
FROM
         tsa.town
    JOIN tsa.point_of_interest
    USING ( town_id )
    JOIN tsa.poi_type
    USING ( poi_type_id )
GROUP BY
    town_id,
    town_name,
    poi_type_id,
    poi_type_descr
HAVING
    COUNT(poi_type_id) > 1
ORDER BY
    town_id,
    poi_type_descr,
    poi_type_id;

/*2(b)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

/*SELECT
    member_id,
    member_gname || ' '
                    || member_fname AS member_name,
    resort_id,
    resort_name,
    (
        SELECT
            MAX(number_of_recommendation)
        FROM
            (
                SELECT
                    COUNT(member_id_recby) AS number_of_recommendation
                FROM
                    tsa.member
                GROUP BY
                    member_id_recby
            )
    )               AS number_of_recommendation

FROM
         tsa.member
    JOIN tsa.resort
    USING ( resort_id )
WHERE
    member_id IN (
        SELECT
            member_id_recby
        FROM
            tsa.member
        GROUP BY
            member_id_recby
        HAVING
            COUNT(member_id_recby) = (
                SELECT
                    MAX(number_of_recommendation)
                FROM
                    (
                        SELECT
                            COUNT(member_id_recby) AS number_of_recommendation
                        FROM
                            tsa.member
                        GROUP BY
                            member_id_recby
                    )
            )
    )

ORDER BY
    resort_id,
    member_id; */

SELECT
    m2.member_id,
    m2.member_gname
    || ' '
    || m2.member_fname        AS member_name,
    r.resort_id,
    r.resort_name,
    COUNT(m1.member_id_recby) AS number_of_recommendations
FROM
         tsa.member m1
    JOIN tsa.member m2
    ON m1.member_id_recby = m2.member_id
    JOIN tsa.resort r
    ON m2.resort_id = r.resort_id
GROUP BY
    m2.member_id,
    m2.member_gname,
    m2.member_fname,
    r.resort_id,
    r.resort_name
HAVING
    COUNT(m1.member_id_recby) = (
        SELECT
            MAX(recommendation_count)
        FROM
            (
                SELECT
                    COUNT(member_id_recby) AS recommendation_count
                FROM
                    tsa.member
                GROUP BY
                    member_id_recby
            )
    )
ORDER BY
    r.resort_id,
    m2.member_id;
    

/*2(c)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT
    *
FROM
    tsa.point_of_interest p
    FULL OUTER JOIN tsa.review            r
    ON r.poi_id = p.poi_id;

SELECT
    p.poi_id,
    p.poi_name,
    nvl(to_char(MAX(r.review_rating),
                '9'),
        'NR') AS max_rating,
    nvl(to_char(MIN(r.review_rating),
                '9'),
        'NR') AS min_rating,
    nvl(to_char(AVG(r.review_rating),
                '9.9'),
        'NR') AS avg_rating /**/

FROM
    tsa.point_of_interest p
    FULL OUTER JOIN tsa.review            r
    ON r.poi_id = p.poi_id
GROUP BY
    p.poi_id,
    p.poi_name
ORDER BY
    p.poi_id;

/*2(d)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer

SELECT
    p.poi_name,
    pt.poi_type_descr,
    t.town_name,
    lpad('Lat: '
         || to_char(t.town_lat, '999.999999')
         || ' Long: '
         || to_char(t.town_long, '999.999999'),
         35,
         ' ')                   AS town_location,
    to_char(COUNT(r.review_id)) AS reviews_completed,
    CASE
        WHEN COUNT(r.review_id) > 0 THEN
            to_char(COUNT(r.review_id) /(
                SELECT
                    COUNT(*)
                FROM
                    tsa.review
            ) * 100,
                    '90.99')
            || '%'
        ELSE
            'No reviews completed'
    END                         AS percent_of_reviews
FROM
         tsa.point_of_interest p
    NATURAL JOIN tsa.poi_type pt
    LEFT OUTER JOIN tsa.town     t
    ON t.town_id = p.town_id
    LEFT OUTER JOIN tsa.review   r
    ON p.poi_id = r.poi_id
GROUP BY
    p.poi_name,
    pt.poi_type_descr,
    t.town_name,
    t.town_lat,
    t.town_long
ORDER BY
    town_name,
    COUNT(r.review_id) DESC,
    p.poi_name;

/*2(e)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer







/*2(f)*/
-- PLEASE PLACE REQUIRED SQL STATEMENT FOR THIS PART HERE
-- ENSURE that your query is formatted and has a semicolon
-- (;) at the end of this answer