def Is_Leap_Year(year):
    """Input Your Number and check is it Leap Year"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    try:
        year = int(input("Enter Your Year: "))
        if Is_Leap_Year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        print("❌ Invalid input! Please enter a numeric year (e.g., 2024).")

if __name__ == '__main__':
    main()
