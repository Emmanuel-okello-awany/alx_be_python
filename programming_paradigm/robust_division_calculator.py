
def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        answer = numerator/denominator
        return f"The result from dividing {numerator} by {denominator} is:{answer} "
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    
    except ValueError:
        return "Error: Enter a valid numerical value"
        