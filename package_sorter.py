def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into different stacks based on their dimensions and mass.
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
    
    Returns:
        str: The stack where the package should be placed (STANDARD, SPECIAL, or REJECTED)
    """
    # Calculate if package is bulky based on volume or dimensions
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    is_heavy = mass >= 20
    
    # Using ternary operator for final decision
    return "REJECTED" if (is_bulky and is_heavy) else "SPECIAL" if (is_bulky or is_heavy) else "STANDARD"
