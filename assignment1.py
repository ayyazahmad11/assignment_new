# Solution Approach:

# Parse each point’s base and value.
# Convert each value to decimal format (base-10).
# Use these decimal values as points to reconstruct the polynomial.
# Apply Lagrange interpolation to determine the polynomial's coefficients.
# Extract the constant term 
# 𝑐
# c (the term with no 
# 𝑥
# x factor) from the polynomial.




import json

def base_to_decimal(value, base):
    """Convert a string `value` from a specified `base` to an integer in decimal format."""
    return int(value, int(base))

def parse_json_points(data):
    """
    Extracts (x, y) points from JSON data after converting values from specified bases to decimal.
    Each point's key is treated as `x` and its value (converted to decimal) as `y`.
    """
    points = {}
    for key, val in data.items():
        if key != "keys":  # Skip the metadata section
            base = val["base"]
            value = val["value"]
            points[int(key)] = base_to_decimal(value, base)
    return points

def calculate_constant_term(points, required_points):
    """
    Apply Lagrange interpolation to approximate the constant term of a polynomial.
    points: dictionary of (x, y) values.
    required_points: the minimum number of points to determine the polynomial (degree + 1).
    """
    x_vals = list(points.keys())
    y_vals = list(points.values())
    constant_term = 0

    for i in range(required_points):
        xi, yi = x_vals[i], y_vals[i]
        basis = 1
        for j in range(required_points):
            if i != j:
                xj = x_vals[j]
                basis *= xi / (xi - xj)  # Lagrange basis polynomial for xi
        constant_term += yi * basis  # Accumulate contribution to constant term

    return constant_term
