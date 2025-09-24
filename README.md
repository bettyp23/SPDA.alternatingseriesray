# SPDA.alternatingseriesray
Apply parallel and distributed computing to computational problems and analyze the scalability and efficiency of the solutions.

## Series Selected
**Alternating Harmonic Series of Reciprocal Squares:**

\[
\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n^2}
\]

using **parallel computing** with **Ray**. The computation is divided into **4 chunks**, each processed independently to demonstrate distributed computation.  

The series chosen is the **alternating series of reciprocal squares**, which was **not used in previous lecture examples**.

---
## Requirements
- Python 3.9+
- Ray

## Installation
```bash
pip install -r requirements.txt

## Run
python series_compute.py