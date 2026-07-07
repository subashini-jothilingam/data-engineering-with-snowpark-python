#------------------------------------------------------------------------------
# Hands-On Lab: Data Engineering with Snowpark
# Script:       05_fahrenheit_to_celsius_udf/app.py
# Author:       Jeremiah Hansen, Caleb Baechtold
# Last Updated: 1/9/2023
#------------------------------------------------------------------------------

# SNOWFLAKE ADVANTAGE: Snowpark Python programmability
# SNOWFLAKE ADVANTAGE: Python UDFs (with third-party packages)
# SNOWFLAKE ADVANTAGE: SnowCLI (PuPr)

import sys

try:
    from scipy.constants import convert_temperature
except ModuleNotFoundError:
    def convert_temperature(value: float, old_scale: str, new_scale: str) -> float:
        if old_scale == 'F' and new_scale == 'C':
            return (float(value) - 32) * 5 / 9
        raise ValueError(f'Unsupported temperature conversion: {old_scale} -> {new_scale}')


def main(temp_f: float | None = None) -> float:
    if temp_f is None:
        return 0.0
    return convert_temperature(float(temp_f), 'F', 'C')


# For local debugging
# Be aware you may need to type-convert arguments if you add input parameters
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(main(sys.argv[1]))  # type: ignore[arg-type]
    else:
        print(main())  # type: ignore[arg-type]
