from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Resume.html")

@app.route("/projects")
def project():
    return render_template("projects.html")

@app.route("/fizzbuzz")
def fizz():
    return render_template("fizzbuzz.html")

@app.route("/Combinations")
def Combinations():
    return render_template("Combinations.html")

@app.route('/Combinations', methods=['POST'])
def data():
    import Combinations
    if request.form['butt']:
        allowed = "xy+-0123456789"
        formula = str(request.form["equation"])
        exp = str(request.form["exponent"])
        for i in formula:
            if i not in allowed:
                return render_template("Combinations.html", Result = "double check your equation")
        try:
            exp = int(exp)
        except:
            return render_template("Combinations.html", Result = "double check your exponent")
        solution = Combinations.binomialExpansion(formula, exp)
        return render_template("Combinations.html", Result = solution,n=exp,expression = formula)
    return render_template("Combinations.html")

@app.route("/affine")
def affine():
    return render_template("affine.html")

@app.route('/affine', methods=['POST'])
def affine_data():
    import Affine
    if request.form['butt'] == "Encrypt":
        text = str(request.form["etext"])
        a = str(request.form["ea"])
        b = str(request.form["eb"])
        try:
            a = int(a)
            b = int(b)
        except:
            return render_template("affine.html", Result = "Only use integers for a and b")
        solution = Affine.affine(text, a,b)
        if Affine.extendedEucledian(a, 94)[0] != 1:
            solution = "Can't be decrypted, but here's the encryption anyways: " + solution
            return render_template("affine.html", Result = solution, eaInt = a, ebInt =b)
        
        return render_template("affine.html", Result = solution, eaInt =a, ebInt =b)
    if request.form['butt'] == "Decrypt":
        text = str(request.form["dtext"])
        a = str(request.form["da"])
        b = str(request.form["db"])
        try:
            a = int(a)
            b = int(b)
        except:
            return render_template("affine.html", dResult = "Only use integers for a and b")
        solution = Affine.dAffine(text, a,b)
        return render_template("affine.html", dResult = solution, daInt = a, dbInt= b)


@app.route("/ModularExponentiation")
def ModEx():
    return render_template("ModularExponentiation.html")

@app.route('/ModularExponentiation', methods=['POST'])
def mod_data():
    from RSA import encryptDecrypt
    a = str(request.form["a"])
    b = str(request.form["b"])
    n = str(request.form["n"])
    try:
        a = int(a)
        b = int(b)
        n = int(n)
    except:
        return render_template("ModularExponentiation.html", Result = "Only use integers")
    solution = encryptDecrypt(a,b,n)
    return render_template("ModularExponentiation.html", Result = solution, constant = a, exponent=b, modn=n)

@app.route("/Ciphers")
def Ciphers():
    return render_template("RSAcalculator.html")
    
@app.route('/Ciphers', methods=['POST'])
def request_data():
    import RSA
    if request.form['butt'] == 'Encrypt':
        allowed = "abcdefghijklmnopqrstuvwxyz"
        messages = str(request.form['m']).lower()
        try:
            exp = int(request.form['e'])
            modn = int(request.form['n'])
        except:
            return render_template("RSAcalculator.html", encrypted = "Letters aren't allowed for the exponents and mod n")
        for i in messages:
            if i not in allowed:
                return render_template("RSAcalculator.html", encrypted ="OnlyUseLetters" )
        messageEncrypt = RSA.convertToNumbers(messages)
        check = RSA.splitCheckAndSend(messageEncrypt, exp, modn)
        encrypted = ''
        for i in range(0, len(check)):
            encrypted += f"{check[i]},"
        return render_template("RSAcalculator.html", message = messages, exponent = exp, modN = modn, encrypted = encrypted[:-1])
    
    elif request.form['butt'] == "Decrypt":
        allowed = "0123456789"
        number = str(request.form['nums']).split(',')
        exponent = str(request.form['de'])
        modn = str(request.form['dn'])
        converted = ""
        try:
            exp = int(exponent)
            modn = int(modn)
        except:
            return render_template("RSAcalculator.html", decrypted ="LettersAreNotAllowed" )
        for i in number:
            try:
                num = int(i)
            except:
                return render_template("RSAcalculator.html", decrypted ="LettersAreNotAllowed" )
            decryption = RSA.encryptDecrypt(num,exp,modn)
            dString = RSA.convertToCharacters(decryption)
            converted += dString
        return render_template("RSAcalculator.html", decrypted = converted)
            
    elif request.form['butt'] == "Check":
        p = str(request.form['p'])
        q = str(request.form['q'])
        e = str(request.form['relative'])
        try:
            p = int(p)
            q = int(q)
            e = int(e)
        except:
            return render_template("RSAcalculator.html", relativeD ="LettersAreNotAllowed")
        d = RSA.getD(p,q,e)
        print(RSA.getD(p,q,e))
        print(d)
        if d == -1:
            return render_template("RSAcalculator.html", relativeD ="ChooseAnotherE" )
        
        return render_template("RSAcalculator.html", relativeD =d, checkN = p*q, relativePrime = e)

@app.route('/ImperialMetricConversion')
def unitConversion():
    return render_template('output.html')

def convert_is(miles):
    yards = float(miles)*1760
    feet = yards*3
    inches = feet*12
    return [yards, feet, inches]

def convert_ms(miles):
    kilometer = float(miles)*1.609344
    meter = kilometer*1000
    centimeter = meter*100
    return [kilometer, meter, centimeter]

@app.route('/ImperialMetricConversion', methods=['POST'])
def unitData():
    old_data = [str(request.form[f'text{i}']) for i in range(1,8)]

    if request.form['butt'] == 'Convert IS':
        conversions_is = convert_is(old_data[0])
        return render_template('output.html', miles=old_data[0], yards=conversions_is[0], feet=conversions_is[1],
                                              inches=conversions_is[2], kilometers=old_data[-3], meters=old_data[-2], centimeters=old_data[-1])
    elif request.form['butt'] == 'Clear IS':
        return render_template('output.html', miles=old_data[0], yards='', feet='', inches='',
                                              kilometers=old_data[-3], meters=old_data[-2], centimeters=old_data[-1])
    elif request.form['butt'] == 'Convert ME':
        conversions_ms = convert_ms(old_data[0])
        return render_template('output.html', miles=old_data[0], yards=old_data[1], feet=old_data[2], inches=old_data[3],
                                              kilometers=conversions_ms[0], meters=conversions_ms[1], centimeters=conversions_ms[2])
    elif request.form['butt'] == 'Clear ME':
        return render_template('output.html', miles=old_data[0], yards=old_data[1], feet=old_data[2], inches=old_data[3],
                                              kilometers='', meters='', centimeters='')
    elif request.form['butt'] == 'Clear ALL':
        return render_template('output.html', miles='', yards='', feet='', inches='',
                                              kilometers='', meters='', centimeters='')

@app.route('/VectorCalculator')
def matrixManipulation():
    return render_template("VectorCalculator.html")

@app.route('/VectorCalculator', methods=['POST'])
def matrixData():
    import VectorCalculator as vc
    if request.form["butt"] == "Submit":
        fpoint = str(request.form["first"])
        spoint = str(request.form["second"])
        tpoint = str(request.form["third"])
        fourthp = str(request.form["fourth"])
        vector1 = vc.checks(fpoint,spoint)
        vector2 = vc.checks(tpoint,fourthp)
        if (type(vector1) == str) or (type(vector2) == str):
            return render_template("VectorCalculator.html", product1 = vector1, product2 = vector2)
        vpoints = [vector1, vector2]
        M1 = vc.Matrix(vector1)
        M2 = vc.Matrix(vector2)
        p1 = M1.matrix_product(M2)
        p2 = M2.matrix_product(M1)
        cp1 = M1.characteristic_polynomial()
        cp2 = M2.characteristic_polynomial()
        i1= M1.inverse()
        i2 = M2.inverse()
        t1= M1.trace()
        t2 = M2.trace()
        d1 = M1.determinant()
        d2= M2.determinant()
        plus = M1+M2
        minus = M1-M2
        multiply = M1*M2
        return render_template("VectorCalculator.html", vectorPoints = f"({vpoints[0]}),({vpoints[1]})", product1 = p1, product2 = p2, polynomial1 = cp1, polynomial2 = cp2, inverse1 = i1, inverse2 = i2, trace1= t1, trace2 = t2, det1 = d1, det2 = d2, add = plus, sub = minus)

if __name__ == '__main__':
    app.run()