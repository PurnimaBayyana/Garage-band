class Band :
  def __init__(self,name,members):
      self.name = name
      self.members = memebers

      def play_solos(self):
        pass

      def create_from_data(data):
        pass

      def __str__(self):
        return self.name
        
      def __repr__():
        pass

      def to_list():
        pass

  if __name__ == "__main__":
    members = []
    band = Band("Testband1",members)
    print (band)

# Defining super class Musician
# it should be abstract
class Musician() :
  def __init__(self,name,instrument):
      self.name = name
      self.instrument= instrument 
      @abstractmethod  
      def play_solo(self):
        pass

class Guitarist(Musician):
  def __init__(self,name,solo = "child class1 output"):
       super().__init(name,"guitor")
       self.solo = solo
  def play_solo(self):
      return self.solo
  
class Bassist(Musician):
  def __init__(self,name,solo = "child class2 output"):
       super().__init(name,"bass")
       self.solo = solo
  def play_solo(self):
      return self.solo

class Drummer(Musician):
  def __init__(self,name,solo = "child class3 output"):
       super().__init(name,"drums")
       self.solo = solo
  def play_solo(self):
      return self.solo







