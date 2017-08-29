# whom?
# "He ain't the youngest - he is the second"
# Calendar with year partially obscured; need a year of the form 1__6 in which Jan 26 is a
# Monday.  This would put Jan 1 as a Thursday (now we apply Gauss' algorithm)

def jan_first_day(year):
    # Uses Gauss' algorithm - days of the week are encoded 0 (Sun) through 6 (Sat)
    # Calculate intermediate quantities
    a = 5 * ((year - 1) % 4)
    b = 4 * ((year - 1) % 100)
    c = 6 * ((year - 1) % 400)
    return (1 + a + b + c) % 7

valid_years = []
# Loop over all years of the form 1__6
for i in range(99):
    year = 1006 + (10*i)
    if jan_first_day(year) == 4: # Thursday - see intro comment
        valid_years.append(year)

print(valid_years) # [1046, 1176, 1226, 1356, 1446, 1576, 1626, 1756, 1846, 1976]

# Get "second youngest"
# Jan 27 1756 ("buy flowers for tomorrow") is Mozart's birthday

# mozart