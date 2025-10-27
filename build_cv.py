import subprocess
import os
import sys

def build_latex_cv():
    """Compile LaTeX CV to PDF"""
    print("Building CV from LaTeX...")
    
    tex_file = "cv.tex"
    
    if not os.path.exists(tex_file):
        print(f"Error: {tex_file} not found!")
        sys.exit(1)
    
    try:
        print("Running pdflatex (first pass)...")
        result1 = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], 
                      check=True, capture_output=True, text=True)
        
        print("Running pdflatex (second pass for references)...")
        result2 = subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_file], 
                      check=True, capture_output=True, text=True)
        
        # Cleanup auxiliary files
        for ext in ['.aux', '.log', '.out']:
            aux_file = tex_file.replace('.tex', ext)
            if os.path.exists(aux_file):
                os.remove(aux_file)
        
        print("\n✓ CV successfully built: cv.pdf")
        
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error compiling LaTeX:")
        print(e.stderr if e.stderr else e.stdout)
        print("\nCheck the .log file for details.")
        sys.exit(1)
    except FileNotFoundError:
        print("\n✗ Error: pdflatex not found.")
        print("\nPlease install MiKTeX:")
        print("  1. Download from: https://miktex.org/download")
        print("  2. Run the installer")
        print("  3. Choose 'Install missing packages on-the-fly: Yes'")
        print("  4. Restart your terminal")
        sys.exit(1)

if __name__ == "__main__":
    build_latex_cv()