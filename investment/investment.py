print("with what parameters would you like to check the quality of your investment?")
print("1. EPS" \
" 2. P/E" \
" 3. Book Value Per Share" \
" 4. P/B" \
" 5. EV")
n = input("pick a number : ")

if n in ["1"]:
    m = input("net income: ")
    s = input("number of average shares outstanding: ")
    try:
        m = float(m)
        s = float(s)
        eps = m/s
        print("EPS = ", eps)
        print("submit valid answers.")
    except ValueError:
        print("Please enter valid numbers only.")

if n in ["2"]:
    m = input("Stock price: ")
    s = input("EPS: ")
    try:
        m = float(m)
        s = float(s)
        pe = m/s
        print("P/E = ", pe)
        if 12 < pe < 18:
            print("P/E has a fair value for a mature company.")
        if 15 < pe < 25:
            print("Reasonable P/E for companies with moderate growth")
        if 20 < pe < 40:
            print("P/E this high is acceptable for growth companies")
        else:
            print("unusual P/E ratio, look for reasons of this phenomenon")
        print("recheck all the given info.")
    except ValueError:
        print("Please enter valid numbers only.")
if n in ["3"]:
    m = input("Shareholders' equity: ")
    s = input("Outstanding shares: ")
    try:
        m = float(m)
        s = float(s)
        bv = m/s
        print("Book value per share:", bv)
        if bv < 1:
            print("Possibly undervalued")
        if 1 <= bv <= 3:
            print("Reasonable Book value, fair value")
        if bv > 3:
            print("growth expectations")
        print("recheck all info")
    except ValueError:
        print("Please enter valid numbers only.")
if n in ["4"]:
    m = input("Stock price: ")
    s = input("Book value per share: ")
    try:
        m = float(m)
        s = float(s)
        pv = m/s
        print("Price to book value = ", pv)
        if 1 < pv < 2:
            print("Slightly undervalued")
        if pv < 1:
            print("Undervalued")
        if 2 < pv < 3:
            print("Solid most common PV")
        if 3 < pv < 5:
            print("Premium valuation requiring strong justification.")
        if 5 < pv < 10:
            print("Needs exceptional growth/return ")
        if pv > 10:
            print("Dont invest if not a high growth tech stock")
    except ValueError:
        print("Please enter valid numbers only.")
if n in ["5"]:
    m = input("Market Cap: ")
    s = input("Total Debt: ")
    j = input("Cash and cash equivalents: ")
    try:
        m = float(m)
        s = float(s)
        j = float(j)
        ev = m + s - j
        print("Enterprise Value: ", ev)
        o = input("Do you want to try EV/Revenue? Y/N: " )
        if o in ["Y", "y", "yes", "Yes"]:
            k = input("Revenue: ")
            try:
                k = float(k)
                t = ev/k
                print("EV/Revenue =", t)
                if t < 2:
                    print("potentially undervalued")
                if 2 <= t <= 6:
                    print("Reasonable")
                if t > 6:
                    print("requires good justification/growth")
            except ValueError:
                print("Please enter valid numbers only.")
        if o in ["n", "N", "no", "No"]:
            print("")
    except ValueError:
        print("Please enter valid numbers only.")
else:
    print("Please enter valid numbers only.")
    


        