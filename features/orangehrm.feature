Feature:  OrangeHRM Logo

  Scenario: Logo present on OrangeHRM homepage
    Given launch Chrome browser
    When open orangeHRM homepage
    Then Verify that the logo present on the page
    And close the browser