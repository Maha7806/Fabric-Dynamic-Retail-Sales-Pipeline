# Fabric-Dynamic-Retail-Sales-Pipeline
End-to-end Microsoft Fabric project demonstrating parameterized pipelines, Dataflow Gen2, Lakehouse architecture, PySpark transformations, and Power BI dashboards.

# Dynamic Retail Sales Processing Pipeline using Microsoft Fabric

## Overview

This project was developed as part of my Data Engineering learning journey using Microsoft Fabric. The objective was to design and implement an end-to-end retail sales data processing solution that demonstrates data ingestion, transformation, orchestration, parameterization, and reporting using Fabric services.

The project processes retail sales data from multiple cities through a single reusable pipeline, showcasing real-world Data Engineering concepts such as Bronze-Silver-Gold architecture, Dataflow Gen2 transformations, PySpark processing, and dynamic pipeline execution using Parameters and Variables.

---

## Project Objectives

- Build a reusable and scalable data pipeline
- Learn Microsoft Fabric Data Factory components
- Understand Dataflow Gen2 transformations
- Implement Bronze-Silver-Gold Lakehouse architecture
- Process data using Spark Notebooks
- Create business-ready datasets for analytics
- Demonstrate the use of Pipeline Parameters and Variables
- Build a Power BI dashboard for business insights

---

## Technologies Used

- Microsoft Fabric
- Fabric Data Factory
- Dataflow Gen2
- Lakehouse
- Apache Spark (PySpark)
- Delta Tables
- Power BI
- SQL

---

# Architecture

```text
Retail Sales CSV Files
            │
            ▼
      Fabric Pipeline
(Parameter Driven Execution)
            │
            ▼
      Bronze Layer
     (Raw Data Storage)
            │
            ▼
      Dataflow Gen2
(Data Cleaning & Validation)
            │
            ▼
      Silver Layer
 (Cleaned Business Data)
            │
            ▼
      Spark Notebook
(Business Transformations)
            │
            ▼
       Gold Layer
 (Analytics Ready Data)
            │
            ▼
      Power BI Dashboard
```

---

# Dataset Information

The project uses retail sales data from four cities:

- Chennai
- Bangalore
- Mumbai
- Delhi

### Dataset Schema

| Column | Description |
|----------|-------------|
| OrderID | Unique Order Identifier |
| CustomerID | Customer Identifier |
| CustomerName | Customer Name |
| ProductID | Product Identifier |
| ProductName | Product Name |
| Category | Product Category |
| Quantity | Number of Units Sold |
| UnitPrice | Price per Unit |
| OrderDate | Date of Purchase |
| City | Sales Location |

---

# Bronze Layer

## Purpose

The Bronze Layer stores raw data exactly as received from source systems.

No transformations are performed at this stage.

### Source

```text
Chennai_Sales.csv
Bangalore_Sales.csv
Mumbai_Sales.csv
Delhi_Sales.csv
```

### Characteristics

- Raw Data
- Contains Null Values
- Contains Duplicate Records
- Quantity stored as String
- Preserves original source data

### Output Table

```text
Bronze_Sales
```

---

# Silver Layer

## Purpose

The Silver Layer is responsible for cleansing and standardizing data.

This transformation is performed using Dataflow Gen2.

### Transformations Performed

#### 1. Remove Null Records

Rows with missing values in important columns such as:

```text
CustomerName
Quantity
```

are removed.

---

#### 2. Remove Duplicate Records

Duplicate OrderIDs are removed to ensure data consistency.

---

#### 3. Data Type Conversion

```text
Quantity
String → Whole Number
```

```text
OrderDate
Text → Date
```

---

#### 4. Revenue Calculation

A new business column is created.

```text
Revenue = Quantity × UnitPrice
```

---

### Output Table

```text
Silver_Sales
```

### Benefits

- Clean and reliable data
- Consistent data types
- Business-ready records
- Improved reporting accuracy

---

# Gold Layer

## Purpose

The Gold Layer contains analytics-ready data designed for reporting and business intelligence.

This transformation is performed using a PySpark Notebook.

### Transformations Performed

#### Add Year

Derived from:

```text
OrderDate
```

Example:

```text
2026
```

---

#### Add Month

Derived from:

```text
OrderDate
```

Example:

```text
January
```

---

#### Create Aggregation Tables

Business summaries are generated for:

- Revenue by City
- Revenue by Category
- Monthly Revenue Trends
- Top Selling Products

---

### Output Tables

```text
Gold_Sales
Gold_SalesSummary
Gold_MonthlyRevenue
Gold_TopProducts
```

### Benefits

- Optimized for Power BI
- Faster reporting
- Business-oriented metrics
- Reduced query complexity

---

# Pipeline Parameters

## Why Parameters?

Without parameters, separate pipelines would be required for each city.

```text
PL_Chennai
PL_Mumbai
PL_Delhi
PL_Bangalore
```

This approach is difficult to maintain and scale.

Parameters allow a single pipeline to process multiple city files dynamically.

---

## Parameters Used

| Parameter | Purpose |
|------------|------------|
| CityName | Identifies which city file to process |
| Environment | Identifies execution environment |

### Example

```text
CityName = Chennai
```

Pipeline dynamically processes:

```text
Chennai_Sales.csv
```

Changing the parameter value automatically processes another city.

```text
CityName = Mumbai
```

Results in:

```text
Mumbai_Sales.csv
```

---

# Pipeline Variables

## Why Variables?

Variables store temporary values during pipeline execution.

They help track progress and dynamically generate file paths.

---

## Variables Used

| Variable | Purpose |
|------------|------------|
| FilePath | Stores dynamically generated source file name |
| LoadStatus | Tracks current pipeline status |
| RowsProcessed | Stores processed row count |

### Example

Pipeline Parameter:

```text
CityName = Chennai
```

Variable Generated:

```text
FilePath = Chennai_Sales.csv
```

This variable is then used by the Copy Activity.

---

# Pipeline Execution Flow

```text
User Input
(CityName Parameter)
         │
         ▼
Set FilePath Variable
         │
         ▼
Copy Activity
         │
         ▼
Bronze Layer
         │
         ▼
Dataflow Gen2
         │
         ▼
Silver Layer
         │
         ▼
Spark Notebook
         │
         ▼
Gold Layer
         │
         ▼
Power BI Dashboard
```

---

# Dashboard Insights

The final Power BI dashboard provides:

### KPI Metrics

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value

### Visualizations

- Revenue by City
- Revenue by Category
- Monthly Revenue Trend
- Top Products Analysis

---

# Key Data Engineering Concepts Demonstrated

- Data Ingestion
- ETL Processing
- Data Cleaning
- Data Transformation
- Lakehouse Architecture
- Bronze-Silver-Gold Design Pattern
- Dataflow Gen2
- PySpark Processing
- Parameterized Pipelines
- Variables and Dynamic Content
- Pipeline Orchestration
- Power BI Analytics

---

# Learning Outcome

This project helped me gain hands-on experience with Microsoft Fabric Data Engineering workloads by building a scalable retail analytics solution. It strengthened my understanding of modern ETL processes, data pipeline orchestration, Lakehouse architecture, and the practical implementation of Parameters and Variables for creating reusable and maintainable data pipelines.

---

## Author

**Mahalekshmi M**

B.Tech Artificial Intelligence & Data Science  
Thangavelu Engineering College (Anna University)

Microsoft Fabric | Data Engineering | Data Analytics | Power BI | PySpark
