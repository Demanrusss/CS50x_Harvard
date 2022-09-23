-- Keep a log of any SQL queries you execute as you solve the mystery.
-- Firstly we have to get a description of the crime
SELECT description
FROM crime_scene_reports
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND street = 'Humphrey Street';
-- Time of crime - 10:15am, mentioned place - bakery, witnesses - 3, date - the same. Littering - 16:36

-- Look through the interviews to find names and transcripts
SELECT name, transcript
FROM interviews
WHERE year = 2021
  AND month = 7
  AND day = 28;
-- Wow! Quite good transcripts
-- 1) Time - within 10 minutes after theft, place bakery car parking
-- 2) Time - early in the morning, witness - Eugene, place - Leggett Street, what - ATM: withdraw cash
-- 3) What - phone call, duration - less than 1 minute, date - the same
-- 4) What - earliest flight, when - tomorrow, addition - other person bought a ticket

-- So let's take some information from log book
SELECT id, license_plate, activity, minute
FROM bakery_security_logs
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND hour = 10
  AND minute BETWEEN 15 AND 25;
-- Hm... 8 plates. Now, Ruth told that it was only one person. So we might have had only four: 5P2BI95, 4328GD8, G412CB7 and L93JTIZ
-- We have to correct our selection

-- ATM:cash
SELECT id, account_number, amount
FROM atm_transactions
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND atm_location = 'Leggett Street'
  AND transaction_type = 'withdraw';
-- We have got 8 account numbers. Nothing much :-|

-- Let's see what we have from the call
SELECT id, caller, receiver, duration
FROM phone_calls
WHERE year = 2021
  AND month = 7
  AND day = 28
  AND duration < 60;
-- Ok, that's better. We cannot say that the call was only one, so we do not exclude doubles like (499) 555-9472

-- Lastly, we will see the flights from the airport
SELECT f.id, a.city, f.hour, f.minute
FROM flights AS f, airports AS a
WHERE year = 2021
  AND month = 7
  AND day = 29
  AND f.destination_airport_id = a.id
  AND f.origin_airport_id = (SELECT id
                           FROM airports
                           WHERE city = 'Fiftyville')
ORDER BY hour;
-- Well, only 5 cities

-- We can combine logs and people
SELECT logs.id, logs.license_plate, logs.activity, logs.minute, p.name
FROM bakery_security_logs AS logs
INNER JOIN people AS p
ON logs.license_plate = p.license_plate
WHERE logs.year = 2021
  AND logs.month = 7
  AND logs.day = 28
  AND logs.hour = 10
  AND logs.minute BETWEEN 15 AND 25;
-- OK, names are Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey

-- Let us combine calls and people
SELECT ph.id, ph.caller, ph.receiver, ph.duration, p.name
FROM phone_calls AS ph
INNER JOIN people AS p
ON ph.caller = p.phone_number
WHERE ph.year = 2021
  AND ph.month = 7
  AND ph.day = 28
  AND ph.duration < 60;
-- Names are Sofia, Kelsey, Bruce, Taylor, Diana, Carina, Kenny, Benista
-- From two table we are able to notice the mathes. Here they are: Bruce, Sofia, Diana, Kelsey
-- Only four. Great!

-- Next, let us look at atm, bank account
SELECT atm.id, atm.account_number, atm.amount, p.name
FROM atm_transactions AS atm, bank_accounts AS bank, people AS p
WHERE atm.year = 2021
  AND atm.month = 7
  AND atm.day = 28
  AND atm.atm_location = 'Leggett Street'
  AND atm.transaction_type = 'withdraw'
  AND atm.account_number = bank.account_number
  AND bank.person_id = p.id;
-- Now according to the previous results (Bruce, Sofia, Diana, Kelsey) we can get another matches: Bruce and Diana
-- Excellent! Only two persons!

-- Hense, we have to check the flights
SELECT p.name
FROM passengers AS pass, people AS p
WHERE pass.flight_id IN (36, 43, 23)
  AND pass.passport_number IN (SELECT people.passport_number
                               FROM people
                               WHERE people.name IN ('Diana', 'Bruce'))
  AND pass.passport_number = p.passport_number;
-- The thief is Bruce

-- So, to define other information is not a difficult job
--City - New York City
--Tthief’s accomplice
SELECT people.name
FROM people
WHERE people.phone_number = '(375) 555-8161';
-- It is Robin