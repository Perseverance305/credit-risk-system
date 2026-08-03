# Credit Risk System

> **A production-inspired South African credit risk, affordability, loan pricing and IFRS 9 simulation platform built with Python.**

## Overview

The **Credit Risk System** is a modular banking platform that simulates how financial institutions evaluate loan applications, assess credit risk, price loans, and estimate expected credit losses under **IFRS 9**.

The project is designed to bridge the gap between accounting, banking, data engineering, machine learning, and software engineering by implementing realistic banking workflows in a clean, extensible software architecture.

Rather than focusing solely on machine learning, the system models the complete lending lifecycle—from customer onboarding and affordability assessment to credit risk modelling and loan pricing.

---

# Objectives

This project aims to:

* Build a production-inspired banking application using modern software engineering practices.
* Simulate South African lending and affordability assessments.
* Implement modular, object-oriented Python architecture.
* Demonstrate Git and GitHub best practices through incremental development.
* Integrate data engineering and machine learning into a realistic financial system.
* Implement IFRS 9 Expected Credit Loss (ECL) concepts using Probability of Default (PD), Loss Given Default (LGD), and Exposure at Default (EAD).
* Provide a portfolio-quality project demonstrating professional software development.

---

# Planned Features

## Customer Management

* Customer profiles
* Employment information
* Financial profiles
* Assets and investments
* Bank account information

---

## Loan Management

* Loan applications
* Loan products
* Loan purposes
* Loan terms
* Loan repayment schedules

---

## Affordability Assessment

* Disposable income calculation
* Debt-to-Income (DTI)
* Payment-to-Income (PTI)
* Affordability decision engine
* Lending policy validation

---

## Credit Risk Assessment

* Credit bureau integration (simulation)
* Credit score analysis
* Probability of Default (PD)
* Risk grading
* Decision support

---

## Loan Pricing

* Base interest rate
* Risk-based pricing
* Customer risk premium
* Expected return calculations

---

## IFRS 9 Expected Credit Loss

* Probability of Default (PD)
* Loss Given Default (LGD)
* Exposure at Default (EAD)
* Stage 1, Stage 2 and Stage 3 impairment
* Lifetime Expected Credit Loss calculations

---

## Data Engineering

* PostgreSQL database
* ETL pipelines
* Data validation
* Feature engineering
* Data quality checks

---

## Machine Learning

* Credit default prediction
* Feature engineering
* Model evaluation
* Model monitoring
* Explainable predictions

---

## API

* FastAPI REST API
* Customer endpoints
* Loan endpoints
* Credit assessment endpoints
* Pricing endpoints

---

## Dashboard

* Streamlit web application
* Customer dashboard
* Loan assessment dashboard
* Credit risk dashboard
* Portfolio analytics

---

# Technology Stack

| Category             | Technology             |
| -------------------- | ---------------------- |
| Programming Language | Python                 |
| Version Control      | Git & GitHub           |
| Database             | PostgreSQL             |
| API Framework        | FastAPI                |
| Dashboard            | Streamlit              |
| Containerization     | Docker                 |
| Data Analysis        | Pandas, NumPy          |
| Machine Learning     | Scikit-learn           |
| ORM                  | SQLAlchemy *(planned)* |
| Testing              | Pytest *(planned)*     |

---

# Project Structure

```text
credit-risk-system/

├── app/
│   ├── config/
│   ├── models/
│   ├── services/
│   └── __init__.py
│
├── scripts/
├── tests/                 # Planned
├── docs/                  # Planned
├── data/                  # Planned
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

# Current Progress

## Completed

* Git repository initialized
* Project architecture established
* Customer domain model
* Loan application model
* Lending policy configuration
* Affordability result model
* Affordability service scaffold
* Initial testing framework

## In Progress

* Affordability Engine
* Repayment calculator
* Lending decision logic

## Planned

* PostgreSQL integration
* FastAPI API
* Docker containerization
* Machine Learning credit scoring
* IFRS 9 Expected Credit Loss engine
* Streamlit dashboard
* Cloud deployment

---

# Software Engineering Principles

This project follows modern software engineering practices, including:

* Object-Oriented Programming (OOP)
* Separation of Concerns
* Single Responsibility Principle (SRP)
* Modular architecture
* Incremental Git commits
* Test-driven development principles
* Clean code practices

---

# Future Roadmap

* Customer onboarding workflow
* Affordability assessment engine
* Credit bureau simulation
* Probability of Default model
* Loan pricing engine
* IFRS 9 Expected Credit Loss
* PostgreSQL persistence layer
* REST API
* Docker deployment
* Continuous Integration (GitHub Actions)
* Interactive Streamlit dashboard
* Cloud deployment

---

# Learning Goals

This project is being developed as a comprehensive learning platform to strengthen practical skills in:

* Software Engineering
* Banking Systems
* Accounting and IFRS
* Credit Risk Modelling
* Machine Learning
* Data Engineering
* Database Design
* API Development
* Docker
* Git & GitHub

---

# Contributing

This repository is currently a personal portfolio project. Suggestions, feedback, and discussions are welcome through GitHub Issues.

---

# License

This project is released under the MIT License.

---

## Author

**Mogau Maphanga**

Bachelor of Accounting Science (Final Year)

Financial Data Practitioner

Building production-inspired financial technology systems that combine accounting, software engineering, data engineering, and machine learning.
