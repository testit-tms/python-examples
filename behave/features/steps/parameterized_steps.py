from behave import when
from behave import then


@when("Summing {left:d}+{right:d}")
def step_impl(context, left, right):
    context.sum = left + right


@then("Result is {result:d}")
def step_impl(context, result):
    assert context.sum == result
