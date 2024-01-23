import random
from rich.console import Console
from rich.table import Table


class Dice:
  def __init__(self):
      self.faces = {
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0
    }
      self.table = Table(title="Cube", expand=True)

  def roll(self):
    self.count = 0
    while self.count < 1000:
      random_val = random.random()
      if (0 < random_val < 1/6 ):
        self.faces['1'] += 1
      elif (1/6 < random_val < 2/6 ):
        self.faces['2'] += 1 
      elif (2/6 < random_val < 3/6 ):
        self.faces['3'] += 1
      elif (3/6 < random_val < 4/6):
        self.faces['4'] += 1
      elif (4/6 < random_val < 5/6):
        self.faces['5'] += 1
      elif (5/6 < random_val < 1):
        self.faces['6'] += 1
      self.count += 1
    self._display()

  def _display(self):
    self.table.add_column("Faces", justify="center", style="blue", no_wrap=True)
    self.table.add_column("Frequency",justify="center", style="yellow")
    self.table.add_column("Percentage", justify="center", style="green")

    for key in self.faces:
      self.table.add_row(str(key), str(self.faces[key]), f'{(self.faces[key] /self.count)*100 : .2f} %')

    self.table.add_row('Total', str(self.count), f'{100: .2f} %')

    console = Console()
    console.print(self.table)



if __name__=="__main__":
    dir = Dice()
    dir.roll()

  