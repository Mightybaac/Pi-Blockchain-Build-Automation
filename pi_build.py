import os
import subprocess

def build_pi_project(build_dir="build"):
    try:
        # Clone the repository
        subprocess.run(["git", "clone", "https://github.com/pidiscovery/pi.git"])
        print("Repository cloned successfully.")

        # Navigate to the cloned repository
        os.chdir("pi")

        # Update submodules
        subprocess.run(["git", "submodule", "update", "--init", "--recursive"])
        print("Submodules updated successfully.")

        # Create the build directory
        os.makedirs(build_dir, exist_ok=True)
        os.chdir(build_dir)
        print(f"Build directory '{os.getcwd()}' created.")

        # Run cmake
        subprocess.run(["cmake", ".."])
        print("CMake configuration completed successfully.")

        # Build the project
        subprocess.run(["make"])
        print("Build completed successfully!")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    build_dir = input("Enter the build directory path (press Enter for default 'build'): ").strip()
    if not build_dir:
        build_dir = "build"

    print("Building the Pi blockchain project...")
    build_pi_project(build_dir)

if __name__ == "__main__":
    main()
