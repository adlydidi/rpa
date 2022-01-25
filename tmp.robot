*** Settings ***
Library     SeleniumLibrary     run_on_failure=None

*** Tasks ***
Login as user
    Open Browser     ${urlname}   ff  service_log_path=${{os.path.devnull}}
    # Input text    id:user-name    ${USERNAME}
    # Input text    id:password     ${PASSWORD}