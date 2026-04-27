$serviceName=Nginx

@service=Get-Service -Name $serviceName 
if ($null -eq $service) {
    Write-Output "Service '$serviceName' is not installed."
} elseif ($service.Status -eq 'Running') {
    Write-Output "Service '$serviceName' is running."
} else {
    Write-Output "Service '$serviceName' is not running."
}
