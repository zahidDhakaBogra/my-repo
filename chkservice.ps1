$services=Get-Service
foreach ($service in $services) {
    if ($service.Status -ne 'Running') {
        Write-Output "Service '$($service.Name)' is not running. Current status: $($service.Status)"
    }
  else {
        Write-Output "Service '$($service.Name)' is running."
    }
}
