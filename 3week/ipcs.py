import subprocess

def run_ipcs_m():
    try:
        # Use subprocess.run to execute the 'ipcs -m' command and capture the output
        result = subprocess.run(['ipcs', '-m'], capture_output=True, text=True, check=True)
        print(result.stdout)
        result = subprocess.run(['ipcs', '-q'], capture_output=True, text=True, check=True)
        print(result.stdout)
        result = subprocess.run(['ipcs', '-s'], capture_output=True, text=True, check=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
    except FileNotFoundError:
        print("ipcs command not found. Please ensure it is installed and available in PATH.")

# Execute the function
run_ipcs_m()
