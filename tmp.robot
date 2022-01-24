*** Settings ***
Library     SeleniumLibrary     run_on_failure=None

*** Tasks ***
Login as user
    Open Browser     https://google.com    ff  service_log_path=${{os.path.devnull}}
    # Input text    id:user-name    ${USERNAME}
    # Input text    id:password     ${PASSWORD}