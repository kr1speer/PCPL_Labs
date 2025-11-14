Feature: Composite Pattern for Autosalon Management
  As an autosalon manager
  I want to use composite pattern to manage cars and packages
  So that I can handle both individual cars and complex car packages

  Scenario: Create a car part
    Given I have a car part "Колесо" with price 15000
    Then the part price should be 15000
    And the part description should contain "Колесо"

  Scenario: Create a basic car
    Given I have a car "Toyota Corolla" with base price 1800000 and type "sedan"
    Then the car base price should be 1800000
    And the car type should be "sedan"

  Scenario: Add options to car
    Given I have a car "Honda Civic" with base price 2000000 and type "sedan"
    And I have a car part "Климат-контроль" with price 40000
    And I have a car part "Кожаный руль" with price 15000
    When I add "Климат-контроль" to car
    And I add "Кожаный руль" to car
    Then the car total price should be 2055000
    And the car should have 2 options

  Scenario: Create empty car package
    Given I have a car package "Базовый пакет"
    Then the package should be empty
    And the package price should be 0

  Scenario: Add cars to package
    Given I have a car package "Семейные автомобили"
    And I have a car "Toyota Camry" with base price 2500000 and type "sedan"
    And I have a car "Honda CR-V" with base price 3200000 and type "suv"
    When I add "Toyota Camry" to package
    And I add "Honda CR-V" to package
    Then the package should contain 2 cars


  Scenario: Create nested packages
    Given I have a car package "Эконом класс"
    And I have a car "Kia Rio" with base price 1500000 and type "sedan"
    And I have a car package "Премиум класс"
    And I have a car "BMW X5" with base price 6000000 and type "suv"
    And I have a car package "Автосалон"
    When I add "Kia Rio" to "Эконом класс" package
    And I add "BMW X5" to "Премиум класс" package
    And I add "Эконом класс" package to "Автосалон" package
    And I add "Премиум класс" package to "Автосалон" package
    Then "Автосалон" package total price should be 7500000
    And "Автосалон" package should contain 2 sub-packages
