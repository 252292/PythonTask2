def genderdef():
  global gender
  gender=str(input('Please Enther the athletes gender \n'))
  print (gender)
  if gender == 'male':
    pass
  elif gender == 'female':
    pass
  else:
    print('Please enter a correct gender')
    genderdef()

def athletenumberdef():
  global athletenumber
  athletenumber=int(input('How many Athetes are participating? \n'))
  print (athletenumber)
  athletenumberdef()

def lanenumber4def():
  global lane1
  global lane2
  global lane3
  global lane4
  lane1 = float(input('Lane number 1s time is:'))
  lane2 = float(input('Lane number 2s time is:'))
  lane3 = float(input('Lane number 3s time is:'))
  lane4 = float(input('Lane number 4s time is:'))
      


  



genderdef()
athletenumberdef()