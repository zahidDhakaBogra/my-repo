function Ping-Host {
    param (
        $OptionalParameters
    )
    Test-Connection $OptionalParameters
}
Ping-Host google.com 


