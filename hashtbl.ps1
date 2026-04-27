$users =@{
    "user1" = "password1"
    "user2" = "password2"
    "user3" = "password3"
    "user4" = @{
        "firstName" = "John"
        "lastName"  = "Doe"
        }
        "user5" = @{ "firstName" = "Jane"
        "lastName"="Smith"
        "age"="30"
        "city"="New York"
        "email"="jane@gmail.com"    
       }
}

$users.GetEnumerator()


