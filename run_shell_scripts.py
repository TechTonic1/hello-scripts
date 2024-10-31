import subprocess
import os

# Function to execute a shell script
def run_shell_script(script_path):
    if os.path.isfile(script_path) and os.access(script_path, os.X_OK):
        try:
            # Run the shell script
            result = subprocess.run([script_path], capture_output=True, text=True)
            print(f"Output of {script_path}:")
            print(result.stdout)
            print(f"Errors (if any) from {script_path}:")
            print(result.stderr)
        except Exception as e:
            print(f"Error running {script_path}: {str(e)}")
    else:
        print(f"Script {script_path} not found or is not executable.")

# Function to update permissions on a specific file
def update_permissions():
    file_path = "/Users/frankwade/scripts/specific_file.txt"  # Specify the file path
    permissions = "755"  # Specify the permission mode (e.g., 755)

    if os.path.isfile(file_path):
        try:
            # Change permissions of the file
            subprocess.run(['chmod', permissions, file_path])
            print(f"Permissions for {file_path} have been updated to {permissions}.")
        except Exception as e:
            print(f"Error updating permissions for {file_path}: {str(e)}")
    else:
        print(f"File {file_path} does not exist.")

# Define the path where scripts are stored
scripts_path = "/Users/frankwade/scripts"

# Add your shell script names here
shell_scripts = [
    f"{scripts_path}/timescript.sh",
    f"{scripts_path}/helloworld.sh",
    f"{scripts_path}/updatepermission.sh"
    # Add more scripts here if needed
]

# Main execution loop
def main():
    print("Starting to run shell scripts...")

    # Run shell scripts
    for script in shell_scripts:
        print(f"\nRunning: {script}")
        run_shell_script(script)

    # Update permissions
    print("\nUpdating permissions for specific file...")
    update_permissions()

    print("\nAll tasks completed.")

if __name__ == "__main__":
    main()

