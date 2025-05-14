Feature: Access management
  As a user of the website
  I want to have an access control
  so that no one can access my profile other than me

  Scenario: Successful Login
    Given I am on the login page
    When I enter valid credentials
    And I click on the login button
    Then I should be redirected to the profile page

  Scenario: Unsuccessful Login with invalid user name
    Given I am on the login page
    When I enter invalid user name
    And I click on the login button
    Then I should see an error message
    And I should see a link to go back to the login page

    Scenario: Unsuccessful Login with invalid password
    Given I am on the login page
    When I enter valid user name
    And I enter invalid password
    And I click on the login button
    Then I should see an error message
    And I should see a link to go back to the login page