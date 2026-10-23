# Platform setup: Windows 11, Kali Linux, Cloud

## Windows 11
1. Install Python 3.10–3.12 from python.org and check **Add Python to PATH**.
2. Install Java 11 or 17 if using PySpark locally; confirm `java -version`.
3. Open PowerShell in the project directory:
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python -m src.generate_data
   python -m src.visualize
   python -m src.ml_pipeline
   ```
4. If script activation is blocked, use `Set-ExecutionPolicy -Scope Process Bypass` in the current PowerShell window only.

## Kali Linux
```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip default-jdk
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python -m src.generate_data
python -m src.visualize
python -m src.ml_pipeline
```
If the distribution's Java version does not match your Spark build, install a supported Java release and verify `JAVA_HOME`.

## Cloud notebook
- Upload the project ZIP or clone your repository.
- Install dependencies from `requirements.txt`.
- Run `python -m src.generate_data`, then visualization and ML modules.
- Spark may require Java and a runtime restart after installation. For managed Spark platforms, use the platform's documented Spark session instead of forcing a local master.
- Do not upload secrets, private logs, or personal data into public notebooks.
