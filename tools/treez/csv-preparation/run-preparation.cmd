@echo off
setlocal
echo Treez / METRC export preparation
set /p "input_file=Full path to workbook (without quotes): "
set /p "period_start=Start date (YYYY-MM-DD): "
set /p "period_end=End date (YYYY-MM-DD): "
set /p "run_folder=New output folder path (without quotes): "
py "%~dp0prepare_exports.py" --workbook "%input_file%" --output "%run_folder%" --start "%period_start%" --end "%period_end%"
if errorlevel 1 (
  echo Preparation failed. Do not refresh from this output. Send the error to technical support.
) else (
  echo Review manifest.json and preparation_issues.csv before using the output.
)
pause
