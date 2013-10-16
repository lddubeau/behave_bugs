def after_scenario(_context, scenario):
    import sys
    sys.__stderr__.write(repr(sys.stderr) + "\n")
    if scenario.name != "test":
        raise Exception("Q")
