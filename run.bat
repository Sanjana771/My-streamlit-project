@echo off
TITLE VVCE AI Placement Readiness & Skill Gap Analyzer - Launcher
echo ========================================================================
echo   VIDYAVARDHAKA COLLEGE OF ENGINEERING (VVCE), MYSURU
echo   Department of CSE (Artificial Intelligence & Machine Learning)
echo   Mini-Project: AI-Powered Placement Readiness & Skill Gap Analyzer
echo ========================================================================
echo.

cd /d "%~dp0"

:: Check if Anaconda Python exists at C:\ProgramData\anaconda3\python.exe
if exist "C:\ProgramData\anaconda3\python.exe" (
    echo Using Anaconda Python at C:\ProgramData\anaconda3\python.exe...
    "C:\ProgramData\anaconda3\python.exe" -m streamlit run app.py
    goto end
)

:: Check if Anaconda Python exists in user profile
if exist "%USERPROFILE%\anaconda3\python.exe" (
    echo Using Anaconda Python at %USERPROFILE%\anaconda3\python.exe...
    "%USERPROFILE%\anaconda3\python.exe" -m streamlit run app.py
    goto end
)

:: Check if standard python command works
where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo Using system Python...
    python -m streamlit run app.py
    goto end
)

echo [ERROR] Python / Streamlit was not found in standard paths.
echo Please run: "C:\ProgramData\anaconda3\python.exe" -m streamlit run app.py
pause

:end
