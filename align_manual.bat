@echo off
REM Manual MUSCLE alignment script for Windows users

REM Update this path if MUSCLE is installed somewhere else
set MUSCLE_PATH="C:\Program Files\muscle\muscle.exe"

REM Input and output paths
set INPUT_FILE="data\example_large.fa"
set OUTPUT_FILE="output\aligned_sequences.fasta"

%MUSCLE_PATH% -in %INPUT_FILE% -out %OUTPUT_FILE%

echo Alignment complete! Output saved to %OUTPUT_FILE%
pause
