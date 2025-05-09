# Big Data

## Q1: True/False

### 1. Concepts & Examples

#### 3Vs:

- **Volume:** Massive data scale (e.g., terabytes to petabytes)
- **Velocity:** Real-time data generation (e.g., sensors, streams)
- **Variety:** Multiple formats (structured, semi-structured, unstructured)

---

- **Classification**: Assigning data to predefined categories.

  - Example: Spam detection (classify emails as "spam" or "not spam").

- **Association Rule Mining**: Discovering relationships between variables in large datasets.

  - Example: Market basket analysis (e.g., customers who buy bread often buy milk).

- **K-means Clustering:** Grouping similar data points into _k_ clusters.

  - Example: Customer segmentation based on purchase behavior.

- **Naive Bayes**: Probabilistic classifier based on Bayes’ Theorem, assuming feature independence.

  - Example: Sentiment analysis (classify text as positive/negative).

- Clustering: Unsupervised grouping of similar data points.
  - Example: Grouping news articles by topics.

---

| Term           | Description                                                          | Example                                  |
| -------------- | -------------------------------------------------------------------- | ---------------------------------------- |
| Classification | Supervised ML technique to assign data to predefined categories      | Email spam detection, Customer Churn     |
| Clustering     | Grouping of similar data without predefined labels                   | Document topic grouping                  |
| Association    | Finds relationships between variables/items in datasets              | Market basket analysis ("milk -> bread") |
| K-Means        | Unsupervised clustering algorithm that partitions data into K groups | Customer segmentation                    |
| Naive Bayes    | Probabilistic classifier based on Bayes Theorem                      | Sentiment analysis                       |


### 2. Naive Bayes Dependency

- Based on **Bayes Theorem**
- Assumes **independent features**
- Uses **prior**, **likelihood**, and **posterior** probabilities

---

## Q2: Multiple Choice

### 1. Big Data Analytics Lifecycle

Extracting insights from large, complex datasets using tools like Hadoop/Spark.

Lifecycle:

- Discovery (Business Domain)
- Data Preparation (ETL, cleaning)
- Model Planning (Choose algorithms,Develop Datasets)
- Model Building (Train/test)
- Communicate Results (Visualizations, Success or Failure)
- Operationalization (Deploy model, Business Intelligence Analyst).

### 2. Hadoop vs ETL

| Feature        | Hadoop                         | Traditional ETL   |
| -------------- | ------------------------------ | ----------------- |
| Storage        | Distributed                    | Centralized       |
| Scalability    | High                           | Medium            |
| Format Support | Structured, Semi, Unstructured | Mainly structured |

### 3. Graph Database Tools

- **Neo4j**
- **JanusGraph**

### 4. Regression

- Predicts continuous values (e.g., temperature, prices)
- Example: Predicting house prices based on square footage

### 5. Hadoop vs Spark

| Feature    | Hadoop       | Spark                    |
| ---------- | ------------ | ------------------------ |
| Processing | Batch (disk) | In-memory                |
| Speed      | Slower       | Faster                   |
| Use Cases  | storage      | ML, streaming, analytics |

### 6. MapReduce Model:

- Map: Breaks input into key-value pairs
- Shuffle/Sort: Groups and sorts data
- Reduce: Aggregates and summarizes results

### 7. Data Storage Options:

• HDFS: Distributed file system
• Data Lakes: Centralized storage of raw data
• Data Warehouses: Structured historical data

### 8. ETL vs ELT/ETLT

- **ETL:** Extract → Transform → Load (data is cleaned before loading)
- **ETLT/ELT:** Extract → Load → Transform (data is loaded in raw form, then processed using big data frameworks like Spark)

---

## Q3: Short Answers

### 1. Classification vs Regression vs Clustering

- **Classification**: Categorizes (e.g., spam, disease yes/no)
- **Regression**: Predicts numeric values (e.g., house prices)
- **Clustering**: No labels (e.g., customer segments).

| Feature | Classification | Regression | Clustering |
| ------- | -------------- | ---------- | ---------- |
| Label   | Yes            | Yes        | No         |
| Output  | Category       | Numeric    | Groups     |

### 2. Data Types

- **Structured**: data that follows rigid schemas (e.g. SQL DBs)
- **Semi-structured**: Dataa that has some organizational properties (XML, JSON)
- **Unstructured**: data which is not organized (Images, videos,Text)

### 3. Classification Types

- **Binary**: 2 classes (yes/no)
- **Multiclass**: >2 (types of disease)
- **Multilabel**: Multiple tags (e.g., social posts)

### 4. Pig vs Hive

- **Apache Hive:** Hive provides a data warehouse infrastructure built on top of Hadoop, enabling data summarization, querying, and analysis of large datasets

  - SQL-like query engine
  - Used for batch processing
  - Language: HiveQL

- **Apache Pig:** Pig is used for the analysis of a large amount of data focused on data flows
  - ETL scripting tool
  - Language: Pig Latin
  - Procedural vs Hive's declarative model

| Feature       | Hive                 | Pig                    |
| ------------- | -------------------- | ---------------------- |
| Language      | SQL-like (HiveQL)    | Dataflow (Pig Latin)   |
| Primary Users | Data Analysts        | Data Engineers         |
| Use Case      | Reporting & Analysis | ETL & Data Preparation |
| Approach      | Declarative          | Procedural             |

### 5. Shuffle/Sort Phase in MapReduce

- Groups and sorts data
- Optimizes reducer efficiency

_The Shuffle and Sort Phase occur in between the Map and Reduce Phases_

<p align="center">
  <img width="460" height="300" src="https://i.sstatic.net/lRpoU.jpg">
</p>

### 6. Association Rules

Association rules are if-then patterns that reveal relationships between seemingly unrelated data in large datasets. 

- #### Apriori Algorithm:

Measuring Association Strength by:

1. **Support**: The fraction of transactions containing both A and B. 
  -  Indicates how common the rule is in the dataset. *Higher support means the association occurs more frequently.*
2. **Confidence**: The likelihood of B occurring when A occurs. 
  - Measures the reliability of the inference made by the rule *Higher confidence indicates stronger association.*
3. **Lift**: How much more likely A and B occur together than expected if they were independent 
  -  Measures how far from independence the rule is *Lift > 1 indicates positive correlation.*


### 7. Clustering vs Classification

| Feature | Clustering   | Classification |
| ------- | ------------ | -------------- |
| Type    | Unsupervised | Supervised     |
| Labels  | No           | Yes            |

### 8. Spark vs Hadoop

| Feature  | Spark         | Hadoop     |
| -------- | ------------- | ---------- |
| Memory   | In-memory     | Disk-based |
| Speed    | Fast          | Slower     |
| Use Case | ML, streaming | Batch jobs |

### 9.Parallel Databases vs. MapReduce

Feature Parallel Databases MapReduce
| Feature | Parallel Databases | MapReduce |
| -------- | ------------- | ---------- |
Data Structure | Structured (SQL) | Structured + Unstructured
Processing | Model Query-driven | Distributed Computation
Performance | High for structured data | Efficient for large-scale analytics


---

## Q4: Long Answers

### 1. Big Data Analytics Life Cycle

**1. Discovery**

involves discovery, where the team learns the business domain and frames the problem.

Key Activities:

- Define the business problem (e.g., fraud detection, customer churn).
- Identify data sources (e.g., databases, IoT, web logs, APIs).

**2. Data Preparation (ETL / ETLT)**

In this phase focuses on data preparation, including setting up the analytic sandbox and performing ETLT

Tasks:
- Establish Analytic Sandbox
- Data Wrangling/Cleaning (handle nulls, duplicates)
- Pattern Visualization

**3. Model Planning**

In Phase 3, the team focuses on Data Exploration and Variable Selection, Model Selection, and using Common tools for Model Planning Phase.

Tasks:

- Select model type (classification, clustering, regression)
- Choose evaluation metrics (accuracy, RMSE, etc.)
- Visualize data patterns using EDA (exploratory data analysis)

**4. Model Building**

In this phase, we do Dataset Creation and train and test models using prepared data.

Tasks:

- Dataset Creation
- Model Development
- Model Execution
- Model Validation

**5. Communicating Results**

This step focuses on presenting findings to stakeholders in a clear and actionable way.

Deliverables:

- Success Evaluation
- Result Validation
- Presentation Preparation (charts, heatmaps)

**6. Operationalization**

Operationalize, the team communicates the benefits of the project more broadly and sets up a pilot project to deploy the work in a controlled way before broadening the work to a full enterprise or ecosystem of users.

- Model Deployment
- Documentation

### 2. Hospital Dataset Example

**Dataset**: `PatientID, Age, Symptoms, Diagnosis, AdmissionDate, HospitalLocation`

**2.1 Data Cleaning**:

- Remove duplicates
- Handle nulls
- Normalize columns (e.g., date format)

**2.2 Clustering & Classification**:

- **Clustering**: K-Means (group patients by symptom severity)
- **Classification**: Naive Bayes (predict diagnosis)

**2.3 Prediction**:

- Predict disease severity or re-admission risk

### 3. Ministry of Tourism Example

#### Example of the ministry of tourism that found anonymity on visitors and unusual pattern data what tool can help with this issue and what algorithms or models are used for this issue and provide advice to solve this issue and how to mitigate the issue to be scalable enough and how to mitigate fault tolerance

**Problem**: Detect unusual visitor patterns and mitigate fault tolerance

**Tools**:

- Apache Kafka (real-time anomaly detection).
- Apache Flink Used for (real-time analytics).
- HDFS replication and Spark Streaming (Scalability/Fault Tolerance).

**Algorithms**: Anomaly detection to identify unusual visitor patterns (Isolation Forest, DBSCAN)

**Advice**:

- Use fault-tolerant distributed systems
- Automate anomaly alerts
- Ensure scalability using distributed storage system (hadoop) of cloud infrastructure

## Q5: SQL Task

### Example Table: `Orders`

```sql
Orders(OrderID, CustomerID, CustomerName, OrderAmount, OrderDate)
```

### Query: Top 5 Customers by Order Count

#### Single table:

The COUNT() function returns the number of rows that matches a specified criterion.

```sql
SELECT
    CustomerID,
    CustomerName,
    COUNT(OrderID)
FROM
    Orders
GROUP BY
    CustomerID
ORDER BY
    OrderCount DESC
LIMIT 5; -- select only 5 rows
```

### Query: Top 5 Customers by Order Amount

The SUM() function returns the sum of all the values

```sql
SELECT
    CustomerID,
    CustomerName,
    SUM(OrderAmount)
FROM
    Orders
GROUP BY
    CustomerID
ORDER BY
    TotalSpent DESC
LIMIT 5;
```

#### Multi tables:

**Tables:**

- **Customers** (_CustomerID_, Name)
- **Orders** (OrderID, _CustomerID_, Amount)
- **Products** (ProductID, Name, Price)

**Query: Top 5 Customers by Order Amount**

```sql
SELECT Customers.CustomerID, Customers.Name, SUM(Orders.Amount) as TotalSpent
FROM Customers JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
GROUP BY Customers.CustomerID
ORDER BY TotalSpent DESC
LIMIT 5;
```
