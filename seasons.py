import sys
from datetime import date
import inflect


def main():
    day=input("Date of Birth: ")
    y,m,d=validate(day)
    print(time(y,m,d))

    
def time(y,m,d):
    dob=date(y,m,d)
    today=date.today()
    t=today-dob
    t=t.total_seconds()
    time_minutes=round(t/60)
    p=inflect.engine()
    words=p.number_to_words(time_minutes)
    words= words.replace(" and ", " ")
    return f"{words} minutes"


def validate(dt):
    try:
        year,month,day=dt.strip().split("-")
        year,month,day=int(year),int(month),int(day)
        if 0<=year<=9999 and 1<=month<=12 and 1<=day<=31:
            return (year,month,day)
        else:
            sys.exit("Invalid date")
    except ValueError:
        sys.exit("Invalid date")


if __name__=="__main__":
    main()