*** Settings ***
Library    RPA.Browser.Selenium

*** Tasks ***
Login as user
    Open available Browser    https://example.com
    # Input text    id:user-name    ${USERNAME}
    # Input text    id:password     ${PASSWORD}