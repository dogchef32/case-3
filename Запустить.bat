@echo off
cd /d "%~dp0"
python --version >nul 2>&1
if errorlevel 1 (echo Python not found. Install Python and add it to PATH.& pause & exit /b 1)
python -m pip install -r requirements.txt
if errorlevel 1 (echo Error installing dependencies.& pause & exit /b 1)
python manage.py migrate
if errorlevel 1 (echo Database error.& pause & exit /b 1)
echo Open http://127.0.0.1:8000/ in browser
python manage.py runserver
pause
