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

## How to use the Berry Combination Generator

This generator produces all possible berry combinations
and saves them as Parquet files on your computer.

### Steps:

1. Download the **generator `.exe`** from the repository releases.
2. Run the `.exe` file.
3. Choose a folder where the Parquet files will be saved.
4. Wait for the process to complete.
   - High CPU usage is normal.
   - This process only needs to be done **once**.

5. After generation, use the filter or GUI to explore the dataset.
   Make sure both the generator output and the filter/GUI
   point to the **same folder**.

### Notes

- You can select any folder on your computer for the output.
- Once generated, the Parquet files **do not need to be recreated**.
- Estimated generation time depends on your computer:
  - Low-end: ~1.5–3 hours
  - Mid-range: ~30–90 minutes
  - High-end: ~15–40 minutes

---

## 🔐 Security & Privacy

Berry Donut is designed with user privacy and system safety in mind.

### Local Processing Only
All data generation and filtering processes run **entirely on the user's local machine**.
No data is sent, uploaded, or shared to any external server.

### No Network Access
This application does **not** require an internet connection to operate.
It does not perform:
- Network requests
- Telemetry
- Tracking
- Background communication

### Generated Data
All generated files (e.g. Parquet or Excel exports) are created **locally** in the user-defined folder.
The application does not read or modify files outside its working directory.

### Open Source Transparency
The source code is publicly available so users can verify:
- What the application does
- How data is processed
- That no hidden or malicious behavior exists

If you are building from source or using the provided executable, you remain in full control of your data.

---

## Status

This project is currently in an early, exploratory stage.
Structure, tooling, and documentation may evolve over time.

---

## Credits

- Project concept, development, and documentation: **lunafrost-lab**
- Special thanks to all testers and contributors for feedback
