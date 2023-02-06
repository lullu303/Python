# 모듈을 실행시키는 예제

import fah_converter    # fah_converter 모듈 import

print("Enter a celsiusvalue: ")
celsius = float(input())
fahrenheit = fah_converter.convert_c_to_f(celsius)
print(f"That's {fahrenheit} degrees Fahrenheit.")