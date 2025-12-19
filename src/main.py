import subprocess
import sys

SCRIPTS = [
    "01_data_clean.py",
    "02_Extracting_KPIs.py",
    "03_visualizations.py",
    "04_export_for__tableau_dashboard.py",
    "run_rfm_pipeline.py",
    "11_business_insights.py"
]

def run_script(script):
    print(f"\n▶ Running {script} ...")
    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"❌ Error in {script}")
        print(result.stderr)
        sys.exit(1)
    else:
        print(f"✅ Finished {script}")

def main():
    print("🚀 Starting UK Retail Analytics Pipeline")

    for script in SCRIPTS:
        run_script(script)

    print("\n🎉 Pipeline completed successfully")

if __name__ == "__main__":
    main()
