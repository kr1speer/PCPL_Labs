Feature: Laboratory Functions Testing
  As a developer
  I want to test laboratory functions
  So that I can ensure they work correctly

  Scenario: Extract single field from dictionaries
    Given a list of dictionaries with goods
    When I extract field "title"
    Then I should get list with titles
      """
      Ковер, Диван для отдыха
      """

  Scenario: Extract multiple fields from dictionaries
    Given a list of dictionaries with goods
    When I extract fields "title" and "price"
    Then the result should contain 3 items

  Scenario: Remove duplicates from numbers
    Given a list with duplicate items
    When I get unique items
    Then I should get list with values
      """
      1, 2, 3
      """
