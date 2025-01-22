def print_models(unprinted_designs, completed_models):
    """Print eache design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design.title()}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("The following models have been printed.")
    for completed_model in completed_models:
        print(completed_model.title())
