#check if a python module is installed on the local machine

import importlib.util
import sys

# For illustrative purposes.
package_name = 'imageio'

spec = importlib.util.find_spec(package_name)
if spec is None:
    print(package_name +" is not installed")
