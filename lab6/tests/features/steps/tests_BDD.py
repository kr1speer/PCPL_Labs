from behave import given, when, then
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from composite import CarPart, Car, CarPackage, CarType

car_parts = {}
cars = {}
packages = {}
current_package = None

@given('I have a car part "{name}" with price {price}')
def step_create_car_part(context, name, price):
    car_parts[name] = CarPart(name, float(price))

@given('I have a car "{model}" with base price {price} and type "{car_type}"')
def step_create_car(context, model, price, car_type):
    cars[model] = Car(model, float(price), CarType[car_type.upper()])

@given('I have a car package "{name}"')
def step_create_car_package(context, name):
    packages[name] = CarPackage(name)
    context.current_package = packages[name]

@when('I add "{part_name}" to car')
def step_add_part_to_car(context, part_name):
    current_car = list(cars.values())[-1]
    current_car.add_option(car_parts[part_name])

@when('I add "{car_name}" to package')
def step_add_car_to_package(context, car_name):
    if hasattr(context, 'current_package') and context.current_package:
        current_package = context.current_package
    else:
        current_package = list(packages.values())[-1]
    current_package.add(cars[car_name])
    context.current_package = current_package

@when('I add "{car_name}" to "{package_name}" package')
def step_add_car_to_specific_package(context, car_name, package_name):
    packages[package_name].add(cars[car_name])
    context.current_package = packages[package_name]

@when('I add "{source_package}" package to "{target_package}" package')
def step_add_package_to_package(context, source_package, target_package):
    packages[target_package].add(packages[source_package])
    context.current_package = packages[target_package]

@then('the part price should be {expected_price}')
def step_check_part_price(context, expected_price):
    part_name = list(car_parts.keys())[-1]
    actual_price = car_parts[part_name].get_price()
    assert actual_price == float(expected_price), f"Expected {expected_price}, got {actual_price}"

@then('the part description should contain "{text}"')
def step_check_part_description(context, text):
    part_name = list(car_parts.keys())[-1]
    description = car_parts[part_name].get_description()
    assert text in description, f"Text '{text}' not found in: {description}"

@then('the car base price should be {expected_price}')
def step_check_car_base_price(context, expected_price):
    car_model = list(cars.keys())[-1]
    actual_price = cars[car_model].base_price
    assert actual_price == float(expected_price), f"Expected {expected_price}, got {actual_price}"

@then('the car type should be "{expected_type}"')
def step_check_car_type(context, expected_type):
    car_model = list(cars.keys())[-1]
    actual_type = cars[car_model].car_type.value
    assert actual_type == expected_type.lower(), f"Expected {expected_type}, got {actual_type}"

@then('the car total price should be {expected_price}')
def step_check_car_total_price(context, expected_price):
    car_model = list(cars.keys())[-1]
    actual_price = cars[car_model].get_price()
    assert actual_price == float(expected_price), f"Expected {expected_price}, got {actual_price}"

@then('the car should have {count} options')
def step_check_car_options_count(context, count):
    car_model = list(cars.keys())[-1]
    actual_count = len(cars[car_model].options)
    assert actual_count == int(count), f"Expected {count} options, got {actual_count}"

@then('the package should be empty')
def step_check_package_empty(context):
    package = context.current_package if hasattr(context, 'current_package') else list(packages.values())[-1]
    assert len(package.children) == 0, f"Package is not empty, contains {len(package.children)} items"

@then('the package price should be {expected_price}')
def step_check_package_price(context, expected_price):
    package = context.current_package if hasattr(context, 'current_package') else list(packages.values())[-1]
    actual_price = package.get_price()
    assert actual_price == float(expected_price), f"Expected {expected_price}, got {actual_price}"

@then('the package should contain {count} cars')
def step_check_package_car_count(context, count):
    package = context.current_package if hasattr(context, 'current_package') else list(packages.values())[-1]
    actual_count = len(package.children)
    assert actual_count == int(count), f"Expected {count} cars, got {actual_count}"

@then('"{package_name}" package total price should be {expected_price}')
def step_check_specific_package_price(context, package_name, expected_price):
    actual_price = packages[package_name].get_price()
    assert actual_price == float(expected_price), f"Expected {expected_price}, got {actual_price}"

@then('"{package_name}" package should contain {count} sub-packages')
def step_check_package_subpackages_count(context, package_name, count):
    package = packages[package_name]
    # Считаем только дочерние пакеты (не автомобили)
    subpackages_count = sum(1 for child in package.children if isinstance(child, CarPackage))
    assert subpackages_count == int(count), f"Expected {count} sub-packages, got {subpackages_count}"
