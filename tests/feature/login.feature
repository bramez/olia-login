Feature: Access management
  As a user of the website
  I want to have an access control
  so that no one can access my profile other than me

  Scenario: Successful Login
    Given I am on the login page
    When I enter valid credentials
    And I click on the login button
    Then I should be redirected to the profile page

#  Scenario: Unsuccessful Login
#    Given I am on the login page
#    When I enter invalid credentials
#    And I click on the login button
#    Then I should see an error message
#    And I should remain on the login page