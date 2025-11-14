from behave import given, when, then
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))

from lab_python_fp.field import field
from lab_python_fp.unique import Unique


@given('a list of dictionaries with goods')
def step_given_list_of_dicts(context):
    context.goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
        {'title': None, 'price': 1000}
    ]

@given('a list with duplicate items')
def step_given_list_with_duplicates(context):
    context.data = [1, 1, 2, 2, 3, 3, 1, 2, 3]

@given('a list with case sensitive strings')
def step_given_case_sensitive_strings(context):
    context.data = ['a', 'A', 'b', 'B', 'a', 'A']

@when('I extract field "{field_name}"')
def step_when_extract_single_field(context, field_name):
    context.result = list(field(context.goods, field_name))

@when('I extract fields "{field1}" and "{field2}"')
def step_when_extract_multiple_fields(context, field1, field2):
    context.result = list(field(context.goods, field1, field2))

@when('I get unique items')
def step_when_get_unique_items(context):
    context.result = list(Unique(context.data))

@when('I get unique items ignoring case')
def step_when_get_unique_ignore_case(context):
    context.result = list(Unique(context.data, ignore_case=True))

@then('I should get list with values')
def step_then_should_get_list(context):
    expected = context.text.strip().split(', ')
    expected = [int(x) if x.isdigit() else x for x in expected]
    assert context.result == expected, f"Expected {expected}, got {context.result}"

@then('I should get list with titles')
def step_then_should_get_titles(context):
    expected = context.text.strip().split(', ')
    assert context.result == expected, f"Expected {expected}, got {context.result}"

@then('the result should contain {count:d} items')
def step_then_result_should_contain_count(context, count):
    assert len(context.result) == count, f"Expected {count} items, got {len(context.result)}"

@then('the result should not contain duplicates')
def step_then_no_duplicates(context):
    seen = set()
    for item in context.result:
        key = item.lower() if isinstance(item, str) else item
        assert key not in seen, f"Duplicate found: {item}"
        seen.add(key)
