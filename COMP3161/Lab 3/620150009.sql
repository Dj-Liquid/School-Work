CREATE DATABASE IF NOT EXISTS Customer_data;
USE Customer_data;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    AnnualIncome INT,
    SpendingScore INT,
    Profession VARCHAR(100),
    WorkExperience INT,
    FamilySize INT
);
