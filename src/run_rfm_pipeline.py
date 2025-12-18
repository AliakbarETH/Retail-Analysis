import subprocess
import sys

scripts = [
    "05_rfm_segmentation.py",
    "06_rfm_visuals.py",
    "07_clv_simple.py",
    "08_cohort_retention.py",
    "09_market_basket.py",
    "10_forecast_revenue.py"
]

for script in scripts:
    print(f"\n▶ Running {script} ...")
    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"❌ Error running {script}. Stopping pipeline.")
        break
    else:
        print(f"✅ Finished {script}")
