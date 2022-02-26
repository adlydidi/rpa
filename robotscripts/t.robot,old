*** Settings ***
Documentation               This is just an example
Metadata                    VERSION     1.0
Library                     SeleniumLibrary
Suite Setup                 Start Browser
Suite Teardown              Close Browser

*** Variables ***
${SERVER}                   http://www.google.com
${BROWSER}                  chrome

*** Keywords ***
Start Browser
    [Documentation]         Start firefox browser on selenium grid
    Open Browser            ${SERVER}   ${BROWSER}   None  http://selenium-hub:4444/wd/hub

*** Test Cases ***
Check page title
    [Documentation]         Check the page title
    Title Should Be         Google
