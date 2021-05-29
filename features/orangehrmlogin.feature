Feature: OrangeHRM Login
  Scenario: Login to OrangeHRM with valid parameter
    Given I launch Chrome browser
    When I open OrangeHRM homepage
    And Enter username "Admin" and password "admin123"
    And Click on Login button
    Then User must successfully login to the Dashboard Page