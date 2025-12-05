# goit-algo-hw-03

## How to Run

### Task 1: Recursive File Organizer
Recursively copies files from a source directory and organizes them by file extension.

```bash
python task1.py <input_dir> [output_dir]
```

**Arguments:**
- `input_dir` - source directory (required)
- `output_dir` - destination directory (optional, default: `dist`)

**Examples:**
```bash
python task1.py input_test/
python task1.py input_test/ my_output/
```

---

### Task 2: Koch Snowflake
Draws a Koch snowflake fractal using turtle graphics.

```bash
python task2.py [order]
```

**Arguments:**
- `order` - recursion level for the fractal (optional, default: 3). Higher values create more detailed fractals.

**Examples:**
```bash
python task2.py          # Uses default order of 3
python task2.py 0        # Draws a simple triangle
python task2.py 2        # Draws a less detailed snowflake
python task2.py 4        # Draws a more detailed snowflake
```
