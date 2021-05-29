Feature: OrangeHRM Loin

  Background: Common Steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

   Scenario: Search User
     Then Search page should be displayed

    Scenario: Advanced User Search
      Then advanced search page should be displayed