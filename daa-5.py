import random 
import streamlit as st
  
comparison_count = 0  # Global counter 
  
def min_max_dc(arr, low, high): 
    global comparison_count 
    # Base case: single element 
    if low == high: 
        return arr[low], arr[low] 
    # Base case: two elements 
    if high == low + 1: 
        comparison_count += 1 
        if arr[low] < arr[high]: 
            return arr[low], arr[high] 
        return arr[high], arr[low] 
  
    # Divide 
    mid = (low + high) // 2 
    lmin, lmax = min_max_dc(arr, low, mid) 
    rmin, rmax = min_max_dc(arr, mid + 1, high) 
  
    # Conquer: combine with 2 comparisons 
    comparison_count += 1 
    overall_min = lmin if lmin < rmin else rmin 
    comparison_count += 1 
    overall_max = lmax if lmax > rmax else rmax 
    return overall_min, overall_max 
  
def min_max_naive(arr): 
    mn, mx = arr[0], arr[0] 
    comps = 0 
    for x in arr[1:]: 
        comps += 1 
        if x < mn: mn = x 
        comps += 1 
        if x > mx: mx = x 
    return mn, mx, comps 
  
# -------------------- Streamlit UI --------------------

st.title("Min and Max using Divide and Conquer")

st.write("Click the button below to find the minimum and maximum elements using Divide and Conquer.")

if st.button("Run Algorithm"):

    # --- Demonstration on small array ---
    arr = [3, 1, 7, 4, 9, 2, 8, 5, 6, 0]

    comparison_count = 0
    mn, mx = min_max_dc(arr, 0, len(arr) - 1)
    dc_comps = comparison_count
    _, _, naive_comps = min_max_naive(arr)

    st.subheader("Results")

    st.write(f"Array : {arr}")
    st.success(f"Minimum Element : {mn}")
    st.success(f"Maximum Element : {mx}")
    st.write(f"Divide & Conquer Comparisons : {dc_comps}")
    st.write(f"Naive Comparisons : {naive_comps}")

    st.subheader("Performance Analysis")

    result = []

    for size in [10, 100, 1000, 10000]:

        arr = [random.randint(1, 10000) for _ in range(size)]

        comparison_count = 0

        mn, mx = min_max_dc(arr, 0, len(arr) - 1)
        dc = comparison_count

        _, _, naive = min_max_naive(arr)

        formula = 3 * size // 2 - 2

        result.append({
            "Array Size": size,
            "D&C Comparisons": dc,
            "Naive Comparisons": naive,
            "Formula (3n/2 - 2)": formula
        })

    st.table(result)