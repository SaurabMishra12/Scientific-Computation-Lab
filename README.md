# Scientific Computation Lab

Collection of interactive Python scripts for numerical linear algebra and optimization coursework. Each lab is a small, self-contained program that reads input from the terminal and prints results to the console (and, in one case, a plot).

## Repository contents
- `lab_1.py` – Gaussian elimination with partial pivoting on a user-supplied matrix.
- `lab2.py` – LU decomposition (Doolittle) with validation that `A ≈ L @ U`.
- `lab3_svd.py` – Singular Value Decomposition computed from user input via eigen-decomposition.
- `svd_lab4.py` – SVD demonstration on a predefined 3×3 matrix.
- `lab5_steepest_descent.py` – Steepest descent method for solving `Ax = b`, with iteration path plotted using Matplotlib.

## Prerequisites
- Python 3.8+  
- `numpy` for all labs  
- `matplotlib` (only for `lab5_steepest_descent.py`)

Install dependencies in your environment:
```bash
python -m pip install numpy matplotlib
```

## Running the labs
From the repository root:

### 1) Gaussian elimination (lab_1.py)
```bash
python3 lab_1.py
```
Provide the number of rows and columns, then enter each row space-separated. The script performs Gaussian elimination with pivoting and prints the resulting row‑echelon form.

### 2) LU decomposition (lab2.py)
```bash
python3 lab2.py
```
Enter `n` followed by `n` rows of the matrix. The program outputs the `L` and `U` factors and checks that `A = L @ U`.

### 3) SVD from user input (lab3_svd.py)
```bash
python3 lab3_svd.py
```
Enter the matrix dimensions and rows. The script computes `U`, `Σ`, and `Vᵀ` via the eigen-decomposition of `AᵀA`.

### 4) SVD demo (svd_lab4.py)
```bash
python3 svd_lab4.py
```
Uses the hardcoded matrix in the script and prints the rounded diagonalized form for reference.

### 5) Steepest descent with visualization (lab5_steepest_descent.py)
```bash
python3 lab5_steepest_descent.py
```
Provide `A`, `b`, an initial guess `x0`, maximum iterations, and tolerance. The script prints each iterate and plots the iteration path alongside the true solution.

> **Note:** When running on a headless system (no display), set `MPLBACKEND=Agg` before executing `lab5_steepest_descent.py` to save or render the plot without an interactive window.

## Tips
- Inputs are expected to be numeric and space-separated. Invalid shapes will raise errors in the SVD and LU labs.
- For reproducibility, capture the console input/output.
