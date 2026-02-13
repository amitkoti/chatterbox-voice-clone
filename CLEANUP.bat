@echo off
REM Voice Cloning System - Cleanup Script
REM Safely removes archive files

echo ==========================================
echo Voice Cloning System - Cleanup
echo ==========================================
echo.
echo This will delete OLD/TEST files from _archive folder
echo Reference audio files will NOT be touched
echo.
pause

echo.
echo Deleting archive folder...
if exist "_archive" (
    rmdir /s /q "_archive"
    echo   Archive folder deleted!
) else (
    echo   Archive folder not found (already clean)
)

echo.
echo Cleanup complete!
echo.
echo Folder is now organized and clean.
echo.
pause
