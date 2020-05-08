from pythonic_garage_band.garageBand import Musician,Guitarist,Bassist,Drummer

def test_guitarist():
  result1 = Guitarist ("James")
  assert result1.name == "James"
  assert result1.instrument == "guitor"
  assert result1.play_solo() == "child class1 output"

def test_bassist():
  result2 = Bassist ("Tony")
  assert result2.name == "Tony"
  assert result2.instrument == "bass"
  assert result2.play_solo() == "child class2 output"

def test_drummer():
  result3 = drummer("Jhony")
  assert result3.name == "Jhony"
  assert result3.instrument == "drum"
  assert result3.play_solo() == "child class3 output"
 