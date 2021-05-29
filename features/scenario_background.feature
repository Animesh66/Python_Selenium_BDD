Feature: OrangeHRM Loin

  # All comment steps are included in Background section
  Background: Common Steps
    Given I launch browser
    When I open application
    And Enter valid username and password
    And click on login

  Scenario: Login to HRM Application
    Then User must login to the Dashboard page

   Scenario: Search User
     When navigate to search page
     Then Search page should be displayed

    Scenario: Advanced User Search
      When navigate to advanced search page
      Then advanced search page should be displayed