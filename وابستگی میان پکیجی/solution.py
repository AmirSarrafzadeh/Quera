def sort_dependencies(packages, package_name, order=None):
    if order is None:
        order = []
    if package_name in packages.keys():
        for requirement in packages[package_name]:
            if requirement not in order:
                sort_dependencies(packages, requirement, order)

        if package_name not in order:
            order.append(package_name)

    return order[:-1]









