import time
import datetime
import locale

current_time = time.time()
locale.setlocale(locale.LC_ALL, '')

formatted_time = locale.format_string("%.4f", current_time, grouping=True)

print(f"Seconds since January 1, 1970: {formatted_time}  or {current_time:.2e} in scientific notation")


current_date = datetime.datetime.now().strftime("%b %d %Y")
print(current_date)