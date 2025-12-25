# berry-donut
Exploring berry combinations to produce Donut in Pokémon Legends: Z-A: Mega Dimensions.

This project explores berry combinations used to produce **Donut** in *Pokémon Legends: Z-A*.

Rather than trying to define a single “best” combination, this project
is designed as an exploratory space — helping users understand how
different berries interact.

---

## Scope

- Focused on **berry combination logic**
- Designed to scale to **millions of combinations**
- The full generated dataset is **not included** in this repository

---

## Data Generation

To explore all possible berry combinations, this project generates
a large dataset on your **local computer**.

This process is **CPU-intensive** and may take some time to complete.
High CPU usage during generation is **normal and expected**.

### Estimated generation time

Actual time depends on your computer’s performance:

- **Low-end systems**  
  (older CPUs, low core count, HDD storage):  
  about **1.5 – 3 hours**

- **Mid-range systems**  
  (modern consumer CPUs, SSD storage):  
  about **30 – 90 minutes**

- **High-end systems**  
  (high core count CPUs, fast NVMe storage):  
  about **15 – 40 minutes**

These values are estimates. Performance may vary depending on hardware,
storage speed, available memory, and current system load.

---

## One-time Process

The data generation step is designed to be done **only once**.

After the Parquet files are created, they can be reused for filtering
and analysis without generating them again.

You only need to regenerate the dataset if the underlying generation
logic changes.

---

## Data Folder Usage

You are free to choose where the generated Parquet files are stored.
However, both the **generator** and the **filtering tools** must point
to the **same data folder**.

As long as both tools reference the same folder, the exact location
does not matter.

---

## Status

This project is currently in an early, exploratory stage.
Structure, tooling, and documentation may evolve over time.
