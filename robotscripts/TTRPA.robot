*** Settings ***
Documentation  Basic Search Function
Library  SeleniumLibrary

*** Variables ***
${Username}  CRMUSER
${Password}  Welcome01
${CRMReference}  BLAZ937504323932
${DebitAccount}  7703222477101
${DebitValueDate}
${DebitCurrency}  MVR
${OrderingCustomer1}  ADAM IRUFAAN
${BeneficiaryInstitution1}  AACGECE1XXX
${BeneficiaryAccountNo}  3333333
${Beneficiary1}  contact with SWIFT and COR SWIFT,
${Beneficiary2}  Beneficiary address
${CreditCurrency}  USD
${Beneficiary3}  dd
${Beneficiary4}
${CreditAmount}  30.00
${RemittanceInformation1}  /RFB/Family Support and Savings
${RemittanceInformation2}  /INV/ teat
${DescriptionCode}  13.01.00
${CreditAccount}  7730000006055
${ChargesFor}  Beneficiary
${CreditValueDate}
${Sector}  Individuals
${PurposeofSale}  Education
${TTtype}
${ACUMechanism}  No
${SwiftCharge}  0.00
${ComissionAmount}  0.00
${CorrespondenceBankCharge}  0.00
${ACUCharges}  0.00
${SWIFTM103SentTo1}
${SendertoReceiverInfo1}
${SWIFTM103SentTo2}
${SWIFTM103SentTo3}
${SWIFTM103SentTo4}
${SendertoReceiverInfo2}
${SendertoReceiverInfo3}
${SendertoReceiverInfo4}
${RemittanceInformation3}  xx
${RemittanceInformation4}
${calculatedCurrencies}  MVR
${regulatoryReporting1}
${DollarSupportApprove}  No
${USDFundingAmount}  15
${OrderingCustomer2}  .BML, , ,
${OrderingCustomer3}  ee
${OrderingCustomer4}  dd
${IDorPPNumber}  A153627
${chargesFromMVRAcc}  7703222477101
${dollarSupportRequired}  Yes
${dollarSupportType}  Partial
${concessionalCustomer}  No
${OrderingCustomerName}  ADAM IRUFAAN


*** Test Cases ***
Verify Basic Search Function of EBAY
    [documentation]  this test case verifies basic search
    [tags]  functional

    Run Login

    Open MT103plus Menu

    Tester

    Fill TT Details






*** Keywords ***

Run Login
    Open Browser  https://t24r19-upnr-app.bml.com.mv:8444/BrowserWeb/servlet/BrowserServlet  edge
    Input Text  //*[@id="signOnName"]  CRMUSER
    Input Password  //*[@id="password"]  Welcome01
    Click Button  //*[@id="sign-in"]
    Page Should Contain  Sign Off

Open MT103plus Menu
    Select Frame  //frame[contains(@id,'menu')]
    Click Element  //span[text()="Payment Services"]
    Click Element  //span[text()="Input Inward / Outward Payments"]
    Click Element  //a[text()='Swift Transfer with MT103+ ']
    Switch Window  NEW
    Maximize Browser Window
    Wait Until Page Contains  Outward Remittance  60 seconds

Fill TT Details
    IF  len('${chargesFromMVRAcc}')>0
        Input Text  //*[@id="fieldName:DEBIT.ACCT.NO"]  ${chargesFromMVRAcc}
        Press Keys	//*[@id="fieldName:DEBIT.ACCT.NO"]	RETURN
    ELSE
        Input Text  //*[@id="fieldName:DEBIT.ACCT.NO"]  ${DebitAccount}
        Press Keys	//*[@id="fieldName:DEBIT.ACCT.NO"]	RETURN
    END
    Wait Until Element Is Not Visible  //*[@id="processingPage"]/p[text()='Your request is being processed.']  60 seconds

    Input Text  //*[@id="fieldName:DEBIT.CURRENCY"]  ${DebitCurrency}

    Input Text  //*[@id="fieldName:ORDERING.CUST:1"]  ${OrderingCustomer1}

    IF  len('${OrderingCustomer2}')>0
        Click Element At Coordinates  //a[text()="Ordering Customer.1"]  103  0
        Input Text  //*[@id="fieldName:ORDERING.CUST:2"]  ${OrderingCustomer2}
    END
    IF  len('${OrderingCustomer3}')>0
        Click Element At Coordinates  //a[text()="Ordering Customer.2"]  103  0
        Input Text  //*[@id="fieldName:ORDERING.CUST:3"]  ${OrderingCustomer3}
    END
    IF  len('${OrderingCustomer4}')>0
        Click Element At Coordinates  //a[text()="Ordering Customer.3"]  103  0
        Input Text  //*[@id="fieldName:ORDERING.CUST:4"]  ${OrderingCustomer4}
    END


    Input Text  //*[@id="fieldName:ACCT.WITH.BANK:1"]  SW-${BeneficiaryInstitution1}
    Input Text  //*[@id="fieldName:BEN.ACCT.NO"]  ${BeneficiaryAccountNo}


    IF  len('${Beneficiary1}')>0
        Input Text  //*[@id="fieldName:BEN.CUSTOMER:1"]  ${Beneficiary1}
    END

    IF  len('${Beneficiary2}')>0
        Click Element At Coordinates  //a[text()="Beneficiary.1"]  125  0
        Input Text  //*[@id="fieldName:BEN.CUSTOMER:2"]  ${Beneficiary2}
    END

    IF  len('${Beneficiary3}')>0
        Click Element At Coordinates  //a[text()="Beneficiary.2"]  125  0
        Input Text  //*[@id="fieldName:BEN.CUSTOMER:3"]  ${Beneficiary3}
    END

    IF  len('${Beneficiary4}')>0
        Click Element At Coordinates  //a[text()="Beneficiary.3"]  125  0
        Input Text  //*[@id="fieldName:BEN.CUSTOMER:4"]  ${Beneficiary4}
    END

    Input Text  //*[@id="fieldName:CREDIT.CURRENCY"]  ${CreditCurrency}
    Input Text  //*[@id="fieldName:CREDIT.AMOUNT"]  ${CreditAmount}
    Input Text  //*[@id="fieldName:PAYMENT.DETAILS:1"]  ${RemittanceInformation1}

    IF  len('${RemittanceInformation2}')>0
        Click Element At Coordinates  //a[text()="Remittance Information.1"]  88  0
        Input Text  //*[@id="fieldName:PAYMENT.DETAILS:2"]  ${RemittanceInformation2}
    END

    IF  len('${RemittanceInformation3}')>0
        Click Element At Coordinates  //a[text()="Remittance Information.2"]  88  0
        Input Text  //*[@id="fieldName:PAYMENT.DETAILS:3"]  ${RemittanceInformation3}
    END

    IF  len('${RemittanceInformation4}')>0
        Click Element At Coordinates  //a[text()="Remittance Information.3"]  88  0
        Input Text  //*[@id="fieldName:PAYMENT.DETAILS:4"]  ${RemittanceInformation4}
    END

    Input Text  //*[@id="fieldName:MMA.DESC.CODE"]  ${DescriptionCode}
    Input Text  //*[@id="fieldName:CREDIT.ACCT.NO"]  ${CreditAccount}
    Press Keys	//*[@id="fieldName:CREDIT.ACCT.NO"]	RETURN
    Wait Until Element Is Not Visible  //*[@id="processingPage"]/p[text()='Your request is being processed.']  60 seconds


    IF  '${CreditCurrency}'!='USD'
        Click Element  //*[@dropfield="fieldName:CUSTOMER.SPREAD"]
        Wait Until Page Contains  ${calculatedCurrencies} MARGIN  60 seconds
        Click Element  //td[contains(text(),'${calculatedCurrencies}')]
        Wait Until Element Is Not Visible  //*[@id="processingPage"]/p[text()='Your request is being processed.']  60 seconds
    END


    Input Text  //*[@id="fieldName:CREDIT.VALUE.DATE"]  ${CreditValueDate}
    Input Text  //*[@id="fieldName:EXTERNAL.REF"]  ${CRMReference}

    IF  '${ChargesFor}'=='Beneficiary'
        Select Radio Button  radio:tab1:BEN.OUR.CHARGES  SHA
    ELSE IF  '${ChargesFor}'=='Remitter'
        Select Radio Button  radio:tab1:BEN.OUR.CHARGES  OUR
    END

    Select Radio Button  radio:tab1:COMMISSION.CODE  DEBIT PLUS CHARGES

    IF  '${concessionalCustomer}'=='Yes'
        Input Text  //*[@id="fieldName:COMMISSION.AMT:1"]  ${calculatedCurrencies} ${ComissionAmount}
        Input Text  //*[@id="fieldName:COMMISSION.AMT:2"]  ${calculatedCurrencies} ${SwiftCharge}
    END

    IF  '${ChargesFor}'=='Remitter'
        Click Element At Coordinates  //a[text()="Commission Type.2"]  85  0
        Input Text  //*[@id="fieldName:COMMISSION.TYPE:3"]  SFTFGNBKUSD
        Input Text  //*[@id="fieldName:COMMISSION.AMT:3"]  ${calculatedCurrencies} ${CorrespondenceBankCharge}
        Select From List By Value  //*[@id="fieldName:COMMISSION.FOR:3"]  SENDER
    END

    IF  '${concessionalCustomer}'=='Yes'

        IF  '${SwiftCharge}' == '0.00'
            Click Element At Coordinates  //a[text()="Commission Type.2"]  106  0
        END

        IF  '${ComissionAmount}' == '0.00'
            Click Element At Coordinates  //a[text()="Commission Type.1"]  106  0
        END

    END

        IF  len('${chargesFromMVRAcc}') > 0
        Input Text  //*[@id="fieldName:CHARGES.ACCT.NO"]  ${chargesFromMVRAcc}
    END

Tester
    Sleep  6 seconds

96th step

    Sleep  6000 seconds

#//*[@id="fieldName:CHARGES.ACCT.NO"]


#    Run Keyword If len('${chargesFromMVRAcc}')>0  Input Text  //*[@id="fieldName:DEBIT.ACCT.NO"]  ${chargesFromMVRAcc}
#    ... ELSE Input Text  //*[@id="fieldName:DEBIT.ACCT.NO"]  ${DebitAccount}

#Input Text  //*[@id="fieldName:DEBIT.ACCT.NO"]  ${chargesFromMVRAcc}