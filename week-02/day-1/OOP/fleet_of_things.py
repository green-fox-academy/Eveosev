from fleet import Fleet
from thing import Thing

fleet = Fleet()
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

thing1 = Thing('Get milk')
thing1.__str__()

thing2 = Thing('Remove the obstacles')
thing2.__str__()

thing3 = Thing('Stand up')
thing3.complete()
thing3.__str__

thing4 = Thing('Eat Lunch')
thing4.complete()
thing4.__str__()

fleet.add(thing1)
fleet.add(thing2)
fleet.add(thing3)
fleet.add(thing4)
fleet.__str__()

print(fleet)
