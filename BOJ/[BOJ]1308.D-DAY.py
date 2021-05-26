def main():
  total_day = 0
  for year in range(year1,year2 + 1):
    if year == year1:
      month_d = 29 if month1 == 2 and not year_check(year1) else month_day[str(month1)]
      total_day += (month_d - day1)
      total_day+=(month_total(year,month1+1,12))
      pass
    elif year == year2:
      total_day += day2
      total_day += month_total(year,1,month2-1)
      pass
    else:
      if year_check(year):
        total_day += 365
      else: total_day += 366
  return total_day

def month_total(year,start_month,end_month):
  if start_month >= end_month: return 0
  return_value = 0
  for m in range(start_month,end_month+1):
    m_day = 29 if m == 2 and not year_check(year) else month_day[str(m)]
    return_value += m_day
  return return_value

def same_year():
  if month1 == month2:
    return day2-day1

  total_d_day = 0

  for month in range(month1+1,month2+1):
    if month == month1:
      total_month = month_day[str(month)]
      if month == 2 and not year_check(year1):
        total_month = 29
      total_d_day += (total_month-day1)
    elif month == month2:
      total_d_day += day2
    else:
      total_month = month_day[str(month)]
      if month == 2 and not year_check(year1):
        total_month = 29
      total_d_day += total_month
  return total_d_day

def year_check(year):
  if year % 4 == 0:
    return False
  elif year % 100 == 0:
    return True
  elif year % 400 == 0:
    return False
  return True

if __name__ == "__main__":
  month_day = {
    '1':31, '2':28, '3':31,
    '4':30, '5':31, '6':30,
    '7':31, '8':31, '9':30,
    '10':31,'11':30,'12':31
  }
  year1, month1, day1 = map(int,input().split())
  year2, month2, day2 = map(int, input().split())
  result = 0
  if year2-year1 > 1000 or (year2-year1 == 1000 and ((month1==month2 and day1 <= day2) or (month2>month1))):
    result = 'gg'
  elif year1 == year2:
    result = same_year()
  else:
    result = main()

  if result == 'gg':print('gg')
  else:
    print(f'D-{result}')