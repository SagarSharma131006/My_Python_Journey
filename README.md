# 🐍 My Python Journey — 100 Days of Code

> A practical journey from Python fundamentals to Data Analysis and Machine Learning through daily learning, coding, practice, and projects.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![100 Days of Code](https://img.shields.io/badge/100%20Days%20of%20Code-Day%2040%2F100-orange)
![GitHub](https://img.shields.io/badge/GitHub-My%20Python%20Journey-black?logo=github)
![Status](https://img.shields.io/badge/Status-In%20Progress-success)

---

## 📌 About This Repository

This repository documents my **100 Days of Code in Python** journey.

The goal is to build a strong Python foundation and gradually move toward:

- NumPy
- Pandas
- Data Visualization
- Data Analysis
- Machine Learning
- Real-world Projects

Each day includes learning, coding, practice, and documentation.

> **Learn → Understand → Code → Practice → Build → Improve**

---

## 🎯 Learning Roadmap

| Phase | Days | Focus |
|---|---|---|
| 1 | 01–20 | 🐍 Python Fundamentals |
| 2 | 21–30 | 🔢 NumPy |
| 3 | 31–40 | 🐼 Pandas |
| 4 | 41–50 | 📊 Matplotlib + Seaborn |
| 5 | 51–60 | 📈 2 Data Analysis Projects |
| 6 | 61–90 | 🤖 Machine Learning + Scikit-learn |
| 7 | 91–100 | 🚀 2 Machine Learning Projects |

**Complete Flow:** Python → NumPy → Pandas → Data Visualization → Data Analysis → Machine Learning → ML Projects

---

## 🐍 Phase 1 — Python Fundamentals (Days 01–20)

**Status:** ✅ Completed — 20/20 days

Topics covered: Data Types, Variables, Operators, Input & Output, Conditional Statements, Loops, Strings, Lists, Tuples, Sets, Dictionaries, Functions, Recursion, Modules & Packages, Exception Handling, File Handling, Regular Expressions, List Comprehensions, OOP, Iterators & Generators.

### Progress

| Day | Topic | Status |
|---|---|---|
| 01 | Data Types | ✅ |
| 02 | Operators | ✅ |
| 03 | Input & Output | ✅ |
| 04 | Conditional Statements | ✅ |
| 05 | Loops | ✅ |
| 06 | Strings | ✅ |
| 07 | Lists | ✅ |
| 08 | Tuples | ✅ |
| 09 | Sets | ✅ |
| 10 | Dictionaries | ✅ |
| 11 | Functions | ✅ |
| 12 | Recursion | ✅ |
| 13 | Modules & Packages | ✅ |
| 14 | Exception Handling | ✅ |
| 15 | File Handling | ✅ |
| 16 | Regular Expressions | ✅ |
| 17 | List Comprehensions | ✅ |
| 18 | OOP | ✅ |
| 19 | Iterators & Generators | ✅ |
| 20 | Python Mini Project | ✅ |

### 🚀 Day 20 — Student Management System

Built a CLI-based Student Management System featuring:

- Add, view, search, update and delete students
- Student statistics and sorting
- JSON-based data storage
- Input validation and exception handling
- Modular code and Object-Oriented Programming

---

## 🔢 Phase 2 — NumPy (Days 21–30)

**Status:** ✅ Completed — 10/10 days

| Day | Topic | Status |
|---|---|---|
| 21 | NumPy Introduction, Arrays & Indexing | ✅ |
| 22 | Array Operations, Comparisons & Aggregations | ✅ |
| 23 | Array Creation Methods | ✅ |
| 24 | Indexing, Slicing & Reshaping | ✅ |
| 25 | Boolean Indexing & Filtering | ✅ |
| 26 | Sorting, Searching & Unique Values | ✅ |
| 27 | Joining, Splitting, Copy & View | ✅ |
| 28 | Random Number Generation | ✅ |
| 29 | Mathematical Functions & Vectorization | ✅ |
| 30 | Practical NumPy Consolidation | ✅ |

**Key learning:** Array manipulation, indexing, broadcasting, aggregation, Boolean masking, vectorization and random number generation.

---

## 🐼 Phase 3 — Pandas (Days 31–40)

**Status:** ✅ Completed — 10/10 days

Pandas was used to load, clean, transform and analyze structured data.

### Progress

| Day | Topic | Status |
|---|---|---|
| 31 | Pandas Series & Basics | ✅ |
| 32 | DataFrames & Basic Operations | ✅ |
| 33 | Indexing, Selection & Filtering | ✅ |
| 34 | Real-World CSV Inspection & Data Cleaning | ✅ |
| 35 | Missing Values, Data Validation & Clean Dataset | ✅ |
| 36 | GroupBy & Aggregation | ✅ |
| 37 | Merging, Joining & Concatenation | ✅ |
| 38 | Pivot Tables & Crosstab | ✅ |
| 39 | Time Series & DateTime | ✅ |
| 40 | Practical Consolidation & Revision | ✅ |

### 🧹 Real-World Dataset Work

**Dataset:** [Retail Store Sales — Dirty for Data Cleaning (Kaggle)](https://www.kaggle.com/datasets/ahmedmohamed2003/retail-store-sales-dirty-for-data-cleaning)

Worked with a real-world retail transactions dataset and documented the cleaning and analysis process.

| Metric | Result |
|---|---:|
| Raw dataset | 12,575 rows × 11 columns |
| Cleaned dataset | 11,971 rows × 11 columns |
| Missing values after cleaning | 0 |
| Duplicate rows after cleaning | 0 |
| Recovered missing unit prices | 609 |
| Missing item names recovered | 1,213 |
| Unspecified discounts retained as | `Unknown` |
| Price × Quantity validation difference | 0.0 |

The 604 records with missing Quantity or Total Spent could not be reliably recovered and were removed. Unknown discount values were not guessed as `True` or `False`.

### 📊 Pandas Analysis Completed

- Used `groupby()` and aggregation to compare sales, quantity, average sale and transaction counts.
- Used `merge()`, `join()` and `concat()` to combine grouped results and subsets.
- Used `pd.pivot_table()` and `pd.crosstab()` to compare sales by category, location and payment method.
- Converted transaction dates with `pd.to_datetime()` and extracted year, month, day and weekday/month names.
- Filtered transactions by date range and sorted records chronologically.
- Used `resample("ME")` for monthly sales and `resample("D")` for daily sales.
- Identified high- and low-sales periods while accounting for incomplete January 2025 data.

### 📈 Selected Dataset Insights

| Metric | Result |
|---|---:|
| Total sales | 1,552,071.00 |
| Total transactions | 11,971 |
| Total quantity sold | 66,276 |
| Average transaction value | 129.65 |
| Online sales | 791,401 |
| In-store sales | 760,670 |
| Highest-sales category | Butchers — 208,118 |
| Highest transaction-count category | Furniture — 1,525 |
| 2024 transactions | 4,036 |
| 2024 sales | 524,881.00 |
| Highest daily sales | 9 April 2024 — 3,790.50 |

### ✅ Day 40 — Pandas Practical Consolidation

Completed an end-to-end revision notebook using the cleaned Retail Store Sales dataset.

The consolidation included:

- Dataset inspection and descriptive statistics
- Category-wise sales analysis
- Online vs. in-store comparison
- Payment-method analysis
- Monthly sales aggregation
- Category × Location pivot table
- Business summary and final validation

**Final validation results:**

- Rows: 11,971
- Columns: 16
- Missing values: 0
- Duplicate rows: 0
- Maximum sales calculation difference: 0.0
- Location sales totals match the overall total: `True`

**Day 40 takeaway:** Combined Pandas skills into one practical workflow:

> **Inspect → Summarize → Group → Compare → Pivot → Validate → Interpret**

*Note: The dataset ends on 18 January 2025, so January 2025 is a partial month and should not be compared directly with complete months or years.*

---

## 📊 Phase 4 — Matplotlib + Seaborn (Days 41–50)

**Status:** ⏳ Upcoming — starts on Day 41

### Matplotlib

- Line plots
- Bar charts
- Scatter plots
- Histograms and pie charts
- Figure and Axes
- Labels, titles, legends and grids
- Subplots and plot customization

### Seaborn

- Count plots and bar plots
- Histograms and KDE plots
- Box plots and violin plots
- Scatter plots and heatmaps
- Pair plots and categorical plots

**Goal:** Use visualizations to understand distributions, compare categories, find relationships, detect outliers, identify correlations and communicate insights.

> Don't just create a graph. Understand what the graph tells you.

---

## 📈 Phase 5 — Data Analysis Projects (Days 51–60)

After learning NumPy, Pandas, Matplotlib and Seaborn, I will apply them together in **two real-world Data Analysis projects** using two different Kaggle datasets.

**Project workflow:**

Raw Dataset → Understand Data → Inspect Data → Clean Data → Handle Missing Values → Handle Duplicates → Analyze Outliers → Feature Engineering → Analysis → Visualization → Insights

- **Project 01:** End-to-end analysis using the first Kaggle dataset.
- **Project 02:** End-to-end analysis using a second Kaggle dataset.

Both projects will follow a complete analysis workflow rather than being limited to individual library exercises.

**Status:** ⏳ Upcoming

### 🗂️ Dataset Strategy

The two datasets selected for Data Analysis will also be used later for Machine Learning.

Kaggle Dataset → Data Cleaning → EDA → Feature Engineering → Visualization → Prepared Dataset → Machine Learning → Model Training → Evaluation

This will help me understand how real-world data moves from analysis to machine learning.

---

## 🤖 Phase 6 — Machine Learning (Days 61–90)

**Status:** ⏳ Upcoming

### 🧠 ML Fundamentals (Days 61–68)

- AI vs. ML
- Supervised and Unsupervised Learning
- Features and target variables
- Training and testing data
- Train/test split and validation
- Data preprocessing and encoding
- Feature scaling
- Model training and predictions
- Scikit-learn workflow

### 📈 Regression (Days 69–76)

- Regression fundamentals
- Linear, Multiple Linear and Polynomial Regression
- Model training and predictions
- Model comparison
- MAE, MSE, RMSE and R² Score

### 🎯 Classification (Days 77–86)

- Classification fundamentals
- Logistic Regression
- K-Nearest Neighbors
- Decision Trees and Random Forest
- Naive Bayes and SVM
- Accuracy, Precision, Recall and F1 Score
- Confusion Matrix and ROC-AUC

### 🔵 Unsupervised Learning (Days 87–90)

- Clustering
- K-Means and choosing the number of clusters
- Cluster visualization
- DBSCAN
- PCA basics
- Cluster evaluation

**General ML workflow:**

Dataset → Understand Data → Clean Data → Feature Engineering → Preprocessing → Train/Test Split → Model Selection → Training → Prediction → Evaluation → Model Comparison

---

## 🚀 Phase 7 — Machine Learning Projects (Days 91–100)

**Status:** ⏳ Upcoming

The final phase will focus on building two Machine Learning projects using the same datasets prepared during the Data Analysis phase.

- **ML Project 01:** Based on Data Analysis Project 01.
- **ML Project 02:** Based on Data Analysis Project 02.

Each project will include appropriate preprocessing, train/test splitting, model training, evaluation and model comparison. Preprocessing steps that learn from data will be fitted on training data only.

---

## 📂 Repository Structure

```text
My_Python_Journey/
├── README.md
├── Day_01_Data_Types/
├── ...
├── Day_20_Python_Mini_Project/
├── Day_21_NumPy/ ... Day_30_NumPy/
├── Day_31_Pandas/ ... Day_40_Pandas/
├── Day_41_Matplotlib_Seaborn/ ... Day_50_Matplotlib_Seaborn/
├── Day_51_Data_Analysis_Project_01/ ... Day_60_Data_Analysis_Project_02/
├── Day_61_ML_Fundamentals/ ... Day_90_Unsupervised_Learning/
├── Day_91_ML_Project_01/ ... Day_100_ML_Project_02/
└── Projects/
    ├── Python_Mini_Project/
    ├── Data_Analysis_Project_01/
    ├── Data_Analysis_Project_02/
    ├── ML_Project_01/
    └── ML_Project_02/
```

*The exact structure may evolve as the projects become more complex.*

### 📁 Daily Work Format

**Regular learning days:**

```text
Day_XX_Topic/
├── topic.py
└── README.md
```

**Data Analysis / Machine Learning days:**

```text
Day_XX_Topic/
├── notebook.ipynb
└── README.md
```

Daily work may include concepts, code examples, practice questions, exercises, experiments, notes, results and key takeaways.

### 📊 Data Analysis Project Structure

```text
Data_Analysis_Project/
├── dataset/
│   └── raw_dataset.csv
├── notebook/
│   └── data_analysis.ipynb
├── output/
│   └── cleaned_dataset.csv
├── visualizations/
└── README.md
```

### 🤖 Machine Learning Project Structure

```text
ML_Project/
├── dataset/
│   └── cleaned_dataset.csv
├── notebook/
│   └── machine_learning.ipynb
├── models/
├── results/
├── visualizations/
└── README.md
```

---

## 🧠 Learning Approach

**Cycle:** Learn → Understand → Code → Practice → Work With Real Data → Build → Debug → Improve → Document → Commit

The goal is to build actual programming ability instead of simply completing tutorials.

### 💻 Coding Philosophy

1. **Understand Before Memorizing** — Focus on logic and concepts rather than memorizing syntax.
2. **Code Consistently** — Consistency matters more than speed.
3. **Practice What I Learn** — Follow new concepts with coding and practice.
4. **Work With Real Data** — Apply concepts to real-world datasets.
5. **Learn From Errors** — Understand what went wrong, why it happened and how to fix it.
6. **Build Projects** — Connect multiple concepts into practical applications.
7. **Improve Previous Work** — Revisit older code to improve readability, structure, performance or documentation.

### 📝 Commit Convention

Examples:

```text
Day 01: Learn Python Data Types
Day 05: Practice Python Loops
Day 11: Learn Functions
Day 18: Learn OOP
Day 20: Complete Student Management System
Day 21: Start NumPy
Day 31: Start Pandas
Day 40: Complete Pandas Practical Consolidation
Day 41: Start Matplotlib
Day 51: Start Data Analysis Project
Day 61: Start Machine Learning
Day 69: Start Regression
Day 77: Start Classification
Day 87: Start Unsupervised Learning
Day 91: Start ML Project 01
```

---

## 📈 Progress Tracker

| Area | Progress |
|---|---|
| Python Fundamentals | 20 / 20 ✅ |
| Python Mini Project | 1 / 1 ✅ |
| NumPy | 10 / 10 ✅ |
| Pandas | 10 / 10 ✅ |
| Matplotlib + Seaborn | 0 / 10 — Starting Day 41 |
| Data Analysis Projects | 0 / 2 |
| ML Core | 0 / 30 |
| ML Projects | 0 / 2 |

**Current Progress:** 40 / 100 days completed  
**Current Phase:** Pandas — completed (10/10 days)  
**Completed Project:** Student Management System ✅  
**Completed Learning Phases:** Python Fundamentals, NumPy and Pandas  
**Next Phase:** Matplotlib + Seaborn  
**Next Day:** Day 41 — Matplotlib Introduction

---

## 🚀 Projects

| # | Project | Description |
|---|---|---|
| 01 | 🐍 Python Mini Project | Student Management System — a CLI application built using Python fundamentals |
| 02 | 📊 Data Analysis Project 01 | Real-world Kaggle dataset analyzed using NumPy, Pandas, Matplotlib and Seaborn |
| 03 | 📊 Data Analysis Project 02 | A second real-world dataset analyzed using the same workflow |
| 04 | 🤖 ML Project 01 | ML project based on Data Analysis Project 01 using Scikit-learn |
| 05 | 🤖 ML Project 02 | ML project based on Data Analysis Project 02 using Scikit-learn |

---

## 📊 Technology Stack

Python → NumPy → Pandas → Matplotlib → Seaborn → Scikit-learn → Jupyter Notebook → Git & GitHub

*Real-world datasets will primarily be sourced from Kaggle.*

## 🧩 Separate DSA Track

Data Structures and Algorithms is being learned separately in C++. It is maintained in a separate repository and is not part of this Python 100 Days of Code repository.

This repository focuses on:

Python → NumPy → Pandas → Data Visualization → Data Analysis → Machine Learning

---

## 🔥 100-Day Timeline

```text
DAY 01 ───── DAY 20   🐍 Python Fundamentals + 🎓 Python Mini Project
DAY 21 ───── DAY 30   🔢 NumPy
DAY 31 ───── DAY 40   🐼 Pandas
DAY 41 ───── DAY 50   📊 Matplotlib + Seaborn
DAY 51 ───── DAY 60   📈 2 Data Analysis Projects
DAY 61 ───── DAY 68   🧠 ML Fundamentals
DAY 69 ───── DAY 76   📈 Regression
DAY 77 ───── DAY 86   🎯 Classification
DAY 87 ───── DAY 90   🔵 Unsupervised Learning
DAY 91 ───── DAY 100  🤖 2 ML Projects
```

---

## 🎯 What I Want to Achieve by Day 100

- ✅ Strong Python fundamentals
- ✅ Practical NumPy knowledge
- ✅ Practical Pandas knowledge
- ✅ Data cleaning experience
- ⏳ Data visualization skills
- ⏳ Real-world Data Analysis projects
- ⏳ Scikit-learn experience
- ⏳ Regression and classification knowledge
- ⏳ Unsupervised Learning basics
- ⏳ Model evaluation and feature engineering experience
- ✅ 1 Python project
- ⏳ 2 Data Analysis projects
- ⏳ 2 Machine Learning projects
- 🎯 100 days of consistent learning and GitHub contributions

---

## 🌱 What Comes After Day 100?

The current challenge focuses on:

Python → Data Analysis → Machine Learning

After completing the 100 days, I plan to explore advanced areas such as:

Machine Learning → Deep Learning → Neural Networks → CNN → NLP → Transformers → Generative AI → LLMs → RAG → AI Agents

*These topics are outside the current 100-day challenge.*

---

## 📚 Resources

- Official Python Documentation
- NumPy Documentation
- Pandas Documentation
- Matplotlib Documentation
- Seaborn Documentation
- Scikit-learn Documentation
- Kaggle
- Online Courses, Coding Platforms, Books and Tutorials
- Open-source Projects

---

## 🧪 Practice Strategy

**General flow:** Learn Concept → Understand → Write Examples → Solve Practice Questions → Apply on Real Data → Build Project

- **NumPy:** Learn Arrays → Practice Indexing → Practice Operations → Apply on Dataset
- **Pandas:** Learn DataFrames → Load Dataset → Clean Data → Analyze Data
- **Machine Learning:** Learn Algorithm → Train Model → Make Predictions → Evaluate → Compare Models → Build Project

---

## 🔥 Challenges

Not every day will be equally productive. Some concepts may take longer, code may fail, and datasets or models may create unexpected problems.

**The goal is simple:** Keep learning. Keep coding. Keep building. Even a small improvement every day matters.

## 📌 Consistency Rule

The goal is not to be perfect every day. The goal is to keep moving.

Bad Day → Learn Something Small → Write Some Code → Commit → Continue Tomorrow

*A small step is still a step forward.*

---

## ⭐ Why I Created This Repository

I created My Python Journey to document my progress and keep myself accountable. This repository represents what I learned, what I practiced, what I struggled with, what I built, what datasets I worked with, what models I trained, and how my skills improved.

Every file represents something I learned. Every commit represents another step. Every project represents an opportunity to apply that knowledge.

This repository is not about showing that I already know everything. It is about showing that I am continuously learning, practicing, building and improving.

## 🏆 The Rule

**One Day. One Step. One Commit. One Improvement.**

🐍 Learn → 💻 Code → 🧠 Practice → 📊 Analyze → 🤖 Build → 🐛 Debug → 📈 Improve → 📁 Document → 🚀 Commit → 🔁 Repeat

---

## 📌 Repository Status

| Field | Value |
|---|---|
| Challenge | 100 Days of Code in Python |
| Current Day | 40 / 100 |
| Current Phase | Pandas — completed (10 / 10 days) |
| Projects Done | 1 |
| Next Phase | Matplotlib + Seaborn |
| Next Day | Day 41 — Matplotlib Introduction |
| Status | 🚧 In Progress |

---

## 🌟 Final Objective

The main objective of this journey is to transform Python knowledge into practical skills — starting with Python Fundamentals and gradually reaching Data Analysis → Machine Learning → Real-World Projects.

By the end, I want to have not only theoretical knowledge, but also code, projects, datasets, experiments and practical experience that demonstrate my progress.

---

## 🌱 Follow My Journey

This repository will continue to evolve throughout the 100 days.

If you are also learning Python, Data Analysis or Machine Learning, feel free to explore the code and learn along with me.

Thanks for visiting my Python journey! 🐍

> *"The best way to learn programming is to write programs."*
