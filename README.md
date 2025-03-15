# PackageSorting

# Package Sorting Challenge Solution

This solution implements a package sorting system for Thoughtful's robotic automation factory. The system categorizes packages into different stacks based on their dimensions and mass.

## Implementation Details

The solution consists of two main files:
- `package_sorter.py`: Contains the main sorting logic
- `test_package_sorter.py`: Contains comprehensive unit tests

### Sorting Rules

Packages are sorted into three categories:
- **STANDARD**: Normal packages (not bulky or heavy)
- **SPECIAL**: Packages that are either heavy or bulky
- **REJECTED**: Packages that are both heavy and bulky

A package is considered:
- **Bulky** if:
  - Volume ≥ 1,000,000 cm³, OR
  - Any dimension ≥ 150 cm
- **Heavy** if:
  - Mass ≥ 20 kg

## Running the Tests

To run the tests, execute:
```bash
python -m unittest test_package_sorter.py
```

## Usage Example

```python
from package_sorter import sort

# Example usage
result = sort(width=100, height=100, length=100, mass=15)
print(result)  # Output: "SPECIAL" (bulky due to volume)

result = sort(width=50, height=50, length=50, mass=10)
print(result)  # Output: "STANDARD" (normal package)
```
