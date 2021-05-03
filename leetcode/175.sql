-- File: 175.sql
-- Title: Combine Two Tables
-- Difficulty: Easy
-- URL: https://leetcode.com/problems/combine-two-tables/

SELECT FirstName, LastName, City, State 
FROM Person 
LEFT JOIN Address ON Person.PersonId = Address.PersonId
