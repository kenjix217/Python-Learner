@echo off
echo ========================================
echo Python AI Tutor - Starting with Backend
echo ========================================
echo.

echo Step 1: Starting Backend Server (port 8000)...
start cmd /k "cd backend && venv\Scripts\activate && python main.py"

timeout /t 3 /nobreak >nul

echo Step 2: Starting Frontend Server (port 3000)...
start cmd /k "cd frontend && python -m http.server 3000"

timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo Servers Started!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo Opening browser...
start http://localhost:3000
echo.
echo Configure AI Tutor in Settings tab!
echo Press any key to stop servers...
pause >nul

taskkill /FI "WINDOWTITLE eq *backend*" /F
taskkill /FI "WINDOWTITLE eq *frontend*" /F




