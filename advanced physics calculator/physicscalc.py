import math

print("Welcome to Modern physics calculator! Made for you to calculate complex concepts easily!")
print("1. Time and Space" \
" 2. Energy and Momentum" \
" 3. Wave-Particle Duality" \
" 4. Photoelectric Effect" \
" 5. Atomic physics" \
" 6. Nuclear Structure" \
" 7. Nuclear Reactions")
m = input("Choose a valid number: ")

def tas():
    print("what would you like to calculate?" \
    " 1. Time dilation" \
    " 2. Length contraction" \
    " 3. Lorentz factor")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        y = input("proper time interval: ")
        m = input("relative velocity between observers: ")
        try:
            y = float(y)
            m = float(m)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            lll = y/bs
            print("time dilation -", lll)
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        y = input("proper length: ")
        m = input("relative velocity between observer and object: ")
        try:
            y = float(y)
            m = float(m)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            lll = y * bs
            print("Length contraction -", lll)
        except ValueError:
            print("Enter a valid number")
    if n in ["3"]:
        m = input("relative velocity between two observers/frames: ")
        try:
            m = float(m)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            lll = 1/bs
            print("Lorentz factor -", lll)
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def eam():
    print("What would you like to calculate?" \
    " 1. Relativistic energy" \
    " 2. Mass-energy equivalence" \
    " 3. Rest energy" \
    " 4. Kinetic energy" \
    " 5. Total energy-momentum relation" \
    " 6. Relativistic momentum" \
    " 7. Velocity addition ")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        v = input("Rest mass: ")
        m = input("Velocity: ")
        try:
            v = float(v)
            m = float(m)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            nh = v * 299792458
            hp = nh/bs
            print("Relativistiv energy -", hp)
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        m = input("Rest mass: ")
        try:
            m = float(m)
            c = 299792458 * 299792458
            e = m * c
            print("Mass-energy equivalence -", e)
        except ValueError:
            print("Enter a valid number")
    if n in ["3"]:
        m = input("Rest mass: ")
        try:
            m = float(m)
            c = 299792458 * 299792458
            e = m * c
            print("Rest energy -", e)
        except ValueError:
            print("Enter a valid number")
    if n in ["4"]:
        m = input("Velocity: ")
        v = input("Mass: ")
        try:
            m = float(m)
            v = float(v)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            lll = 1/bs
            llll = lll - 1
            vv = v * c2
            nd = llll * vv
            print("Kinetic energy -", nd)
        except ValueError:
            print("Enter a valid number")
    if n in ["5"]:
        m = input("Relativistic momentum: ")
        v = input("Rest mass: ")
        try:
            m = float(m)
            v = float(v)
            c2 = 299792458 * 299792458
            e = v * c2
            e2 = e * e
            p = m * 299792458
            p2 = p * p
            lll = e2 + p2
            print("Total energy-momentum relation -", lll)
        except ValueError:
            print("Enter a valid number")
    if n in ["6"]:
        m = input("Velocity: ")
        v = input("Mass: ")
        try:
            m = float(m)
            v = float(v)
            v2 = m * m
            c2 = 299792458 * 299792458
            vc = v2/c2
            b = 1- vc
            bs = math.sqrt(b)
            lll = 1/bs
            uu = lll * m * v
            print("Relativistic momentum -", uu)
        except ValueError:
            print("Enter a valid number")
    if n in ["7"]:
        b = input("Velocity of an object in one frame: ")
        n = input("Velocity of that frame relative to another: ")
        try:
            b = float(b)
            n = float(n)
            c2 = 299792458 * 299792458
            up = b + n
            d = b*n/c2
            down = 1 + d
            lll = up/down
            print("Velocity addition -", lll)
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def wpd():
    print("what would you like to calculate?" \
    " 1. Photon energy" \
    " 2. De Broglie wavelength")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        c = 299792458
        w = input("Wavelength of a photon: ")
        try: 
            w = float(w)
            b = c/w
            print("Photon energy -", b + "h")
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        v = input("Mass of the particle: ")
        m = input("Velocity of the particle: ")
        try:
            v = float(v)
            m = float(m)
            h = m*v
            hh = 1/h
            print("De Broglie wavelength -", hh + "h")
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def pe():
    print("What would you like to calculate?" \
    " 1. Einstein's equiation(Max kinetic energy)" \
    " 2. Threshold frequency" \
    " 3. Work function")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        v = input("Frequency of the incident light: ")
        w = input("Work function of the material: ")
        try:
            v = float(v)
            w = float(w)
            i = v * (6.626 * (10 ** -34))
            ll = i - w
            print("Maximum Kinetic Energy -", ll)
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        v = input("Work function in the material: ")
        try:
            v = float(v)
            i = v / (6.626 * (10 ** -34))
            print("Threshhold Frequency -", i)
        except ValueError:
            print("Enter a valid number")
    if n in ["3"]:
        v = input("Threshold frequency: ")
        try:
            v = float(v)
            i = v * (6.626 * (10 ** -34))
            print("Work function -", i)
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def ap():
    print("what would you like to calculate?" \
    " 1. Energy transition" \
    " 2. Bohr model energy levels")
    n = input("Choose a valid number: ")
    if n in ["2"]:
        v = input("Atomic number (number of protons in nucleus): ")
        o = input("Principal quantum number: ")
        try:
            v = float(v)
            o = float(o)
            u = 13.6 * v
            p = o ** 2
            ll = u/p
            print("Energy of the electron in level n -", ll)
        except ValueError:
            print("Enter a valid number")
    if n in ["1"]:
        v = input("Energy of the initial (higher) energy level: ")
        o = input("Energy of the final (lower) energy level: ")
        try:
            v = float(v)
            o = float(o)
            i = v - o
            print("Energy difference between two atomic levels -", i)
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def ns():
    print("what would you like to calculate?" \
    " 1. Mass defect" \
    " 2. Binding energy" \
    " 3. Binding energy per nucleon")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        v = input("Atomic number: ")
        j = input("Neutron number: ")
        p = input("Mass of proton: ")
        o = input("Mass of neutron: ")
        u = input("Actual mass of nucleus: ")
        try:
            v = float(v)
            j = float(j)
            p = float(p)
            o = float(o)
            u = float(u)
            kk = v * p
            ko = j * o
            lll = kk + ko - u
            print("Mass Defect -", lll)
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        v = input("Mass Defect: ")
        try:
            v = float(v)
            o = 299792458 * 299792458
            p = v * o
            print("Binding energy -", p)
        except ValueError:
            print("Enter a valid number")
    if n in ["3"]:
        v = input("Binding energy: ")
        p = input("Mass number: ")
        try:
            p = float(p)
            v = float(v)
            vp = v/p
            print("Binding energy per nucleon -", vp)
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

def nr():
    print("what would you like to calculate?" \
    " 1. Q-value" \
    " 2. Alpha decay" \
    " 3. Beta decay")
    n = input("Choose a valid number: ")
    if n in ["1"]:
        u = input("Total mass of all reactants: ")
        y = input("Total mass of all products: ")
        try:
            u = float(u)
            y = float(y)
            oo = u - y
            c = 299792458 * 299792458
            ooo = oo * c
            print("Q value -", ooo)
            if ooo > 0:
                print("Exothermic, Energy is released")
            if ooo < 0:
                print("Endothermic, Energy is absorbed")
            else:
                print("Energy is neutral")
        except ValueError:
            print("Enter a valid number")
    if n in ["2"]:
        o = input("Mass of the original (unstable) nucleus: ")
        p = input("Mass of the new nucleus: ")
        u = 4.002603
        c = 299792458 * 299792458
        try:
            o = float(o)
            p = float(p)
            oo = o - p - u
            ooo = oo * c
            print("Alpha Decay -", ooo)
            if ooo > 0:
                print("Energy released → decay happens spontaneously, Stable alpha decay")
            if ooo < 0:
                print("Energy required → decay cannot occur naturally, Forbidden decay")
            else:
                print("Energy is neutral")
        except ValueError:
            print("Enter a valid number")
    if n in ["3"]:
        u = input("Mass of the radioactive atom before decay: ")
        y = input("Mass of the new atom after decay: ")
        try:
            u = float(u)
            y = float(y)
            oo = u - y
            c = 299792458 * 299792458
            ooo = oo * c
            print("Q value -", ooo)
            if ooo > 0:
                print("Energy released")
            if ooo < 0:
                print("Reaction not possible")
            else:
                print("Energy is neutral")
        except ValueError:
            print("Enter a valid number")
    else:
        print("enter a valid number")

if m in ["1"]:
    tas

if m in ["2"]:
    eam

if m in ["3"]:
    wpd

if m in ["4"]:
    pe

if m in ["5"]:
    ap

if m in ["6"]:
    ns

if m in ["7"]:
    nr

