import subprocess
import sys


def run_step(script_name):
    print(f"\nRunning {script_name}...", flush=True)

    subprocess.run(
        [sys.executable, f"src/{script_name}"],
        check=True
    )


def main():
    print("Starting NYC Transit ETL Pipeline", flush=True)

    run_step("extract.py")
    run_step("transform.py")
    run_step("load.py")

    print("\nETL Pipeline completed successfully!")


if __name__ == "__main__":
    main()
