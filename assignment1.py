# Solution Approach:


# Parse Input from JSON File: Read the polynomial points from a separate JSON file, where each point has its x value as the key, and y value in a specific base.

# Decode Values: Convert each y value to base-10 using the provided base.

# Polynomial Interpolation: Use the decoded points to find the polynomial’s constant term 
# 𝑐
# c. We’ll use Lagrange interpolation because it’s straightforward and efficient for our purpose.



import json

def convert_base_to_decimal(value, base):
    """
    Converts a value from a specified base to its decimal form.
    
    Args:
        value (str): The base-encoded value as a string.
        base (int): The base in which the value is represented.
    
    Returns:
        int: Decimal integer representation of the value.
    """
    return int(value, int(base))

def extract_points_from_json(file_path):
    """
    Reads JSON data and converts encoded points (x, y) into decimal pairs.
    
    Args:
        file_path (str): Path to the JSON file.
    
    Returns:
        dict: Points with decimal x and y values.
        int: Total number of points (n).
        int: Minimum number of points required (k).
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    n = data["keys"]["n"]
    k = data["keys"]["k"]
    points = {}
    
    for key, val in data.items():
        if key != "keys":
            x = int(key)
            base = val["base"]
            value = val["value"]
            y = convert_base_to_decimal(value, base)  # Convert y to decimal
            points[x] = y
    
    return points, n, k

def find_constant_term_using_lagrange(points, k):
    """
    Determines the constant term of a polynomial using Lagrange interpolation.
    
    Args:
        points (dict): Dictionary with x and y values in decimal.
        k (int): Minimum points required for the interpolation.
    
    Returns:
        float: The constant term of the polynomial.
    """
    x_vals = list(points.keys())[:k]
    y_vals = list(points.values())[:k]
    constant_term = 0.0

    for i in range(k):
        xi, yi = x_vals[i], y_vals[i]
        basis_poly = 1.0
        for j in range(k):
            if i != j:
                xj = x_vals[j]
                basis_poly *= xi / (xi - xj)
        
        constant_term += yi * basis_poly  # Accumulate to get the constant term

    return constant_term

def main():
    # Load points and other values for each test case
    points_1, n1, k1 = extract_points_from_json('testcase1.json')
    points_2, n2, k2 = extract_points_from_json('testcase2.json')
    
    # Calculate constant term (c) for each test case
    constant_term_1 = find_constant_term_using_lagrange(points_1, k1)
    constant_term_2 = find_constant_term_using_lagrange(points_2, k2)
    
    print("Constant term (c) for Test Case 1:", constant_term_1)
    print("Constant term (c) for Test Case 2:", constant_term_2)

if __name__ == "__main__":
    main()

