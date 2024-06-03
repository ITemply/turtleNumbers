global lastNumber
lastNumber = 0

class movement():
  def getPosition(self, t):
    return {'x': t.xcor(), 'y': t.ycor()}
  
  def setPosition(self, t, position):
    t.goto(position['x'], position['y'])
    
  def setOffset(self, t, position):
    t.goto(t.xcor() + position['x'], t.ycor() + position['y'])
  
  def moveSpace(self, t):
    t.penup()
    t.goto(t.xcor() + 25, t.ycor())

  def moveBold(self, t):
    t.penup()
    t.goto(t.xcor() + 75, t.ycor())
  
  def moveBack(self, t):
    t.penup()
    t.goto(t.xcor() - 25, t.ycor())

  def moveBackSpace(self, t):
    t.penup()
    t.goto(t.xcor() - 75, t.ycor())

  def moveBackNumber(self, t):
    t.penup()
    t.goto(t.xcor() - 50, t.ycor())

  def moveEnter(self, t):
    t.penup()
    t.goto(t.xcor(), t.ycor() - 125)

  def moveUp(self, t):
    t.penup()
    t.goto(t.xcor(), t.ycor() + 125)
    
  def penPositon(self, t, position):
    t.penup()
    if position == 'left':
      t.setheading(90)
      t.goto(t.xcor() - 190, t.ycor())
    elif position == 'farLeft':
      t.setheading(90)
      t.goto(t.xcor() - 350, t.ycor())
    elif position == 'right':
      t.setheading(90)
      t.goto(t.xcor() + 190, t.ycor())
    elif position == 'farRight':
      t.setheading(90)
      t.goto(t.xcor() + 350, t.ycor())
    elif position == 'center':
      t.home()
    else:
      return exit('Invalid Position: Position must be \'left\' or \'right\'')

class tnumbers:
  def one(self, t):
    global lastNumber
    lastNumber = 1
    t.setheading(90)
    t.pendown()
    t.forward(100)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def two(self, t):
    global lastNumber
    lastNumber = 2
    t.setheading(0)
    t.pendown()
    t.forward(50)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.forward(50)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def three(self, t):
    global lastNumber
    lastNumber = 3
    t.setheading(90)
    t.pendown()
    t.setheading(0)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.forward(50)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def four(self, t):
    global lastNumber
    lastNumber = 4
    t.penup()
    t.setheading(0)
    t.forward(50)
    t.pendown()
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(90)
    t.forward(-50)
    t.setheading(0)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.penup()
    t.goto(t.xcor() + 50, t.ycor() - 100)
  
  def five(self, t):
    global lastNumber
    lastNumber = 5
    t.setheading(0)
    t.pendown()
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def six(self, t):
    global lastNumber
    lastNumber = 6
    t.setheading(0)
    t.pendown()
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    t.forward(-50)
    t.setheading(90)
    t.forward(-100)
    t.penup()
    t.goto(t.xcor()+ 50, t.ycor())
  
  def seven(self, t):
    global lastNumber
    lastNumber = 7
    t.penup()
    t.setheading(0)
    t.forward(50)
    t.pendown()
    t.setheading(90)
    t.forward(100)
    t.setheading(0)
    t.forward(-50)
    t.penup()
    t.goto(t.xcor() + 50, t.ycor() - 100)
  
  def eight(self, t):
    global lastNumber
    lastNumber = 8
    t.setheading(0)
    t.pendown()
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    t.forward(-50)
    t.setheading(90)
    t.forward(-100)
    t.goto(t.xcor() + 50, t.ycor())
    t.forward(100)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def nine(self, t):
    global lastNumber
    lastNumber = 9
    t.penup()
    t.setheading(0)
    t.forward(50)
    t.pendown()
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(-50)
    t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(90)
    t.forward(-50)
    t.setheading(0)
    t.forward(-50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.forward(50)
    t.penup()
    t.goto(t.xcor(), t.ycor() - 100)
  
  def zero(self, t):
    global lastNumber
    lastNumber = 0
    t.setheading(90)
    t.pendown()
    t.forward(100)
    t.setheading(0)
    t.forward(50)
    t.setheading(90)
    t.forward(-100)
    t.setheading(0)
    t.forward(-50)
    t.penup()
    t.goto(t.xcor() + 50, t.ycor())

def renderNumbers(t, number):
  tnums = tnumbers()
  move = movement()
  numbers = list(str(number))
  for inumber in range(len(numbers)):
    newNum = numbers[inumber]
    if newNum == '1':
      tnums.one(t)
    elif newNum == '2':
      tnums.two(t)
    elif newNum == '3':
      tnums.three(t)
    elif newNum == '4':
      tnums.four(t)
    elif newNum == '5':
      tnums.five(t)
    elif newNum == '6':
      tnums.six(t)
    elif newNum == '7':
      tnums.seven(t)
    elif newNum == '8':
      tnums.eight(t)
    elif newNum == '9':
      tnums.nine(t)
    elif newNum == '0':
      tnums.zero(t)
    move.moveSpace(t)

def renderBold(t, number):
  tnums = tnumbers()
  move = movement()
  numbers = list(str(number))
  for inumber in range(len(numbers)):
    newNum = numbers[inumber]
    if newNum == '1':
      for i in range(5):
        tnums.one(t)
        move.setOffset(t, {'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveSpace(t)
    elif newNum == '2':
      for i in range(5):
        tnums.two(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '3':
      for i in range(5):
        tnums.three(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '4':
      for i in range(5):
        tnums.four(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '5':
      for i in range(5):
        tnums.five(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '6':
      for i in range(5):
        tnums.six(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '7':
      for i in range(5):
        tnums.seven(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '8':
      for i in range(5):
        tnums.eight(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '9':
      for i in range(5):
        tnums.nine(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)
    elif newNum == '0':
      for i in range(5):
        tnums.zero(t)
        move.moveBackNumber(t)
        move.setOffset(t,{'x': 1, 'y': 1})
      move.setOffset(t, {'x': 0, 'y': -5})
      move.moveBold(t)

class clearing:
  def clear(self, t):
    t.clear()
    t.home()

  def eraseNumber(self, t, number):
    if number == 1:
      for i in range(5):
       t.undo()
    elif number == 2:
      for i in range(15):
       t.undo()
    elif number == 3:
      for i in range(16):
        t.undo()
    elif number == 4:
      for i in range(19):
        t.undo()
    elif number == 5:
      for i in range(13):
        t.undo()
    elif number == 6:
      for i in range(16):
       t.undo()
    elif number == 7:
      for i in range(10):
       t.undo()
    elif number == 8:
      for i in range(18):
        t.undo()
    elif number == 9:
      for i in range(21):
        t.undo()
    elif number == 0:
      for i in range(11):
        t.undo()

  def eraseLastNumber(self, t):
    global lastNumber
    number = lastNumber

    if number == 1:
      for i in range(5):
       t.undo()
    elif number == 2:
      for i in range(15):
       t.undo()
    elif number == 3:
      for i in range(16):
        t.undo()
    elif number == 4:
      for i in range(19):
        t.undo()
    elif number == 5:
      for i in range(13):
        t.undo()
    elif number == 6:
      for i in range(16):
       t.undo()
    elif number == 7:
      for i in range(10):
       t.undo()
    elif number == 8:
      for i in range(18):
        t.undo()
    elif number == 9:
      for i in range(21):
        t.undo()
    elif number == 0:
      for i in range(11):
        t.undo()
