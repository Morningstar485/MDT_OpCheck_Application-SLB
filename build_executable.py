import os
import sys
import shutil
import subprocess
from pathlib import Path

def build_executable():
    print("Building executable for SLB MDT OpCheck Application...")
    
    # Get the current directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create a build directory
    build_dir = os.path.join(base_dir, "build")
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)
    os.makedirs(build_dir)
    
    # Create a dist directory
    dist_dir = os.path.join(base_dir, "dist")
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    os.makedirs(dist_dir)
    
    # Define resource directories to include
    resource_dirs = ["Icons", "SFTs", "Reports"]
    
    # Create the PyInstaller command
    cmd = [
        "pyinstaller",
        "--name=MDT_OpCheck_Application",
        "--windowed",  # For a GUI application with no console
        "--onefile",   # Create a single executable
        "--clean",     # Clean PyInstaller cache before building
        "--log-level=INFO",
        f"--distpath={dist_dir}",
        f"--workpath={build_dir}",
        "--icon=Icons/SLB_Logo.png",  # Set the application icon
    ]
    
    # Add resource directories as additional data
    for resource_dir in resource_dirs:
        dir_path = os.path.join(base_dir, resource_dir)
        if os.path.exists(dir_path):
            # Add each file in the directory as a data file
            for root, _, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, base_dir)
                    destination = os.path.dirname(relative_path)
                    cmd.append(f"--add-data={relative_path}{os.pathsep}{destination}")
    
    # Add any individual files that might be needed
    additional_files = ["Images.qrc"]
    for file in additional_files:
        file_path = os.path.join(base_dir, file)
        if os.path.exists(file_path):
            cmd.append(f"--add-data={file}{os.pathsep}.")
    
    # Add the main script
    cmd.append(os.path.join(base_dir, "main.py"))
    
    # Run PyInstaller
    print("Running PyInstaller with the following command:")
    print(" ".join(cmd))
    
    try:
        subprocess.run(cmd, check=True)
        print("\nBuild completed successfully!")
        print(f"Executable created at: {os.path.join(dist_dir, 'MDT_OpCheck_Application.exe')}")
        
        # Optional: Create a simple batch file to run the executable
        batch_path = os.path.join(dist_dir, "Run_MDT_OpCheck.bat")
        with open(batch_path, "w") as batch_file:
            batch_file.write(f'@echo off\nstart "" "{os.path.join(os.path.dirname(batch_path), "MDT_OpCheck_Application.exe")}"\n')
        
        print(f"Batch file created at: {batch_path}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error building executable: {e}")
        return False
    
    return True

if __name__ == "__main__":
    # Ensure PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("PyInstaller is not installed. Installing now...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
    
    # Build the executable
    success = build_executable()
    
    if success:
        print("\nExecutable build process completed. You can distribute the .exe file along with any external resources.")
    else:
        print("\nExecutable build process failed. Please check the errors above.")