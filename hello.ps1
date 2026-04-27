# My First PowerShell Script 
Write-Host "=== My First PowerShell Script ===" -ForegroundColor Cyan 
$computerName = $env:COMPUTERNAME 
$userName = $env:USERNAME 
$currentTime = Get-Date 
Write-Host "Computer Name: $computerName" -ForegroundColor Green 
Write-Host "User Name: $userName" -ForegroundColor Yellow 
Write-Host "Current Time: $currentTime" -ForegroundColor Magenta 
Write-Host "`nFiles in current directory:" -ForegroundColor Cyan 
Get-ChildItem | Select-Object -First 5 | Format-Table Name, Length, LastWriteTime 

$test = "Testing"
Write-Host "`n$test" -ForegroundColor White
