Feature: OrangeHRM Login
  @sanity
  Scenario: Login to OrangeHRM with valid parameter
    Given I launch Chrome browser
    When I open OrangeHRM homepage
    And Enter username "Admin" and password "admin123"
    And Click on Login button
    Then User must successfully login to the Dashboard Page

  # Scenario Outline is used to pass multiple parameter and repeat the execution
  # Scenario Outline is always followed by Examples section
  @regression
   Scenario Outline: Login to OrangeHRM with Multiple parameter
    Given I launch Chrome browser
    When I open OrangeHRM homepage
    And Enter username "<username>" and password "<password>"
    And Click on Login button
    Then User must successfully login to the Dashboard Page

    Examples:
     | username | password |
     | Admin    | admin123 |
     | admin123 | admin    |
     | adminXYZ | admin123 |
     | admin    | adminXYZ |
