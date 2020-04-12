import random
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
repeatOn = False
while repeatOn == False:
  INIT_CAT_POPULATION = 300
  ADOPTABLE_CAT_PERCENTAGE = 0.33
  CAT_REPRODUCTION_RATE = 3
  CAT_REPRODUCTION_KITTEN_PRODUCTION = 4
  KITTEN_MORTALITY_RATE = 0.75
  NUMBER_OF_LITTERS_PER_YEAR = 3
  CAT_POPULATION = 0
  FERAL_CAT_MORTALITY_RATE = 0.5
  UPDATED_CAT_POPULATION = 0
  TNR_RATE_OF_EFFECTIVENESS = 0.18 
  ypoints = []
# sources http://www.saveacat.org/feral-kittens.html, 
# http://homeatlastrescue.org/html/aboutcats/feral.html,
# https://www.researchgate.net/publication/320745134_An_Examination_of_an_Iconic_Trap-Neuter-Return_Program_The_Newburyport_Massachusetts_Case_Study
# https://en.wikipedia.org/wiki/Feral_cat
# https://resources.bestfriends.org/article/trap-neuter-return-tnr-success-stories
#https://gizmodo.com/feral-cats-can-destroy-the-environment-1730710563

  class cats:
    # function that predicts how many feral cats will be born into the community (birth rate)
    def catBirth(): 
      global UPDATED_CAT_POPULATION
      FERTILE_CATS = random.randint(0,INIT_CAT_POPULATION)#assumes random number of feral cats are fertile and can have kittens
      x = FERTILE_CATS
      y = (CAT_REPRODUCTION_KITTEN_PRODUCTION * (1- KITTEN_MORTALITY_RATE)) #calculates number of kittens per litter 
      q = CAT_POPULATION
      for z in range(NUMBER_OF_LITTERS_PER_YEAR): #loops based on number of times feral cats reproduce per year
        q += x * y
      p = INIT_CAT_POPULATION + q #updated population
      UPDATED_CAT_POPULATION = p
      catPop = UPDATED_CAT_POPULATION
      return catPop
    # function that predicts how many feral cats will die (death rate)
    def catDeath():
      global UPDATED_CAT_POPULATION
      cats.catBirth()
      x = (FERAL_CAT_MORTALITY_RATE * UPDATED_CAT_POPULATION) #calculates how many cats will survive based on mortality rate
      UPDATED_CAT_POPULATION = x
      catPop = UPDATED_CAT_POPULATION
      return catPop

  class TNR:
    # function that calculates TNR effectiveness over course of 5 years
    def withTNR():
      global ypoints
      cats.catBirth()
      x = cats.catDeath()
      ypoints.append(x)
      for i in range(4): #loop to calculate how effective TNR is based on calculated rate of effectiveness 
        x = x - (x*TNR_RATE_OF_EFFECTIVENESS)
        ypoints.append(x)
      x = np.array([1,2,3,4,5])
      a = ypoints[0]
      b = ypoints[1]
      c = ypoints[2]
      d = ypoints[3]
      e = ypoints[4]
      y = np.array([a,b,c,d,e])
      plt.plot(x,y)
      plt.xlabel("Years")
      plt.ylabel("Total number of feral cats")
      plt.title("Effectiveness of TNR on a Feral Cat Population Over 5 Years")
      plt.show()
    # function that calculates growth of feral cat community without TNR
    def withoutTNR():
      global ypoints
      cats.catBirth()
      x = cats.catDeath()
      ypoints.append(x)
      for i in range(4): #loop to calculate how many feral cats will be born each year
        x = x + x #assumes birth and death rates are constant
        ypoints.append(x)
      x = np.array([1,2,3,4,5])
      a = ypoints[0]
      b = ypoints[1]
      c = ypoints[2]
      d = ypoints[3]
      e = ypoints[4]
      y = np.array([a,b,c,d,e])
      plt.plot(x,y)
      plt.xlabel("Years")
      plt.ylabel("Total number of feral cats")
      plt.title("Feral Cat Population over the course of 5 Years without TNR")
      plt.show()

  print("Welcome to the feral cat simulator")
  print("This simulation will walk you through the effectiveness of TNR as documented by a research study on a community outside of Newburyport, MA.")
  print("Feral cats are considered to be an invasive species and can lead to a lack of biodiversity for communities they effect.")
  print("Run the simulation to see how TNR (trap, neuter, release) helps to reduce a stray cat population over the course of 5 years")
  print("Press 1 to see a visualization without TNR over the course of 5 years")
  print("Press 2 to see a visualization where TNR is used over the course of 5 years")
  str1 = input()
  if str1 == "1":
    TNR.withoutTNR()
  if str1 == "2":
    TNR.withTNR()
  print("Now that you have seen a real world example, you can simulate an example for any population of feral cats. Enter any number below.")
  initialCatPop = int(input())
  #model simulation using algorithms above
  def modelSimulation():
    global initialCatPop
    kitten_prod = 4
    kitten_mortality_rate = 0.75
    catPopulation = 0
    ypointsnew = []
    fertile_cats = random.randint(0,initialCatPop)
    x = fertile_cats
    y = (kitten_prod * (1- kitten_mortality_rate))
    q = catPopulation
    for z in range(3):
      q += x * y
    p = initialCatPop + q
    update_cat_pop = p
    catPop2 = update_cat_pop
    x = (0.5 * update_cat_pop)
    update_cat_pop = x
    catPop2 = update_cat_pop
    x = catPop2
    ypointsnew.append(x)
    for i in range(4):
      x = x - (x*0.18)
      ypointsnew.append(x)
    x = np.array([1,2,3,4,5])
    a = ypointsnew[0]
    b = ypointsnew[1]
    c = ypointsnew[2]
    d = ypointsnew[3]
    e = ypointsnew[4]
    y = np.array([a,b,c,d,e])
    plt.plot(x,y)
    plt.xlabel("Years")
    plt.ylabel("Total number of feral cats")
    plt.title("Effectiveness of TNR on a Feral Cat Population Over 5 Years")
    plt.show()
  modelSimulation()
  print("Would you like to run the simulation again? Answer Y or N")
  str2 = input()
  if str2 == "Y":
    repeatOn = False
  if str2 == "N":
    repeatOn = True
