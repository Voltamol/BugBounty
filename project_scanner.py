# Importing necessary modules:
import os
import subprocess
from pylint import epylint as lint
from fpdf import FPDF

# Creating a function that scans the project folder using Pylint and returns the output as a string:
def scan_project(folder_path):
    pylint_options = '--output-format=parseable'
    (pylint_stdout, _) = lint.py_run(f'{folder_path} {pylint_options}', return_std=True)
    return pylint_stdout.getvalue()

# Creating a function to generate a PDF report based on the scan results
def generate_pdf_report(scan_results, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, scan_results)
    pdf.output(output_path)

# Specifying the project folder and output path:
project_folder = "test_files"
output_file = "reports/lint_report.pdf"

# Calling the functions and generating the report:
"""
calling the scan_project function to get the scan results
and then passing those results to the generate_pdf_report function to generate the PDF report
"""
scan_results = scan_project(project_folder)
generate_pdf_report(scan_results, output_file)
