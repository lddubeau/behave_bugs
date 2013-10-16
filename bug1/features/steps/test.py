
@then("nested")
def step_impl(_context):
    pass

@then("nester")
def step_impl(context):
    context.execute_steps(u"""
    Then nested
    """)

@then("test")
def step_impl(_context):
    pass
