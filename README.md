# Label Studio Validator

This repository provides a **Python validation script** for checking the quality of **Named Entity Recognition (NER)** and **Relation Extraction (RE)** annotations exported from [Label Studio](https://labelstud.io/).  
It helps detect common issues in annotation data such as:

- **Overlapping entity spans** (two or more labeled tokens covering the same text)
- **Relations without assigned labels**
- **Entity labels including leading or trailing whitespace**

---

## Features

- ✅ Detects overlapping entity spans  
- ✅ Identifies unlabeled relations  
- ✅ Flags entities that accidentally include whitespace at the edges  
- ✅ Prints detailed report with `Inner ID` for each affected annotation  

---

## Example Output

When running the script, you might see results like:

```
Report Inner ID = 378
Overlap found between: [111, 148, 'with another interventional treatment'] and [111, 115, 'with']

Report Inner ID = 1086
There is a relation without a label.

Report Inner ID = 1098
There is a relation without a label.
```

---

## Requirements

- Python 3.7+  
- A valid Label Studio export in JSON format (e.g. `labelstudio_export.json`)

No external libraries are required — only the built-in `json` module is used.

---

## Usage

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/labelstudio-validator.git
   cd labelstudio-validator
   ```

2. Place your Label Studio export file in the same directory (default name: `labelstudio_export.json`).

3. Run the validator script:

   ```bash
   python labelstudio_validator.py
   ```

   On Windows you might need:

   ```bash
   python labelstudio_validator.py
   ```

   On macOS/Linux:

   ```bash
   python3 labelstudio_validator.py
   ```

---

## Output

- If issues are detected, they will be printed in the terminal along with the **Report Inner ID**.  
- If no issues are found, the script will exit silently.

---

## License

This project is released under the **MIT License**. You are free to use, modify, and distribute it.

---

