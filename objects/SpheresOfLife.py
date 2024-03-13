import json
import os


class Spheres():
    def __init__(self):
        self.read_spheres()

    def read_spheres(self):
        if(os.path.isfile('./data/spheresOfLife.json')):
            self.spheres = json.load(open('./data/spheresOfLife.json', 'r'))
        else:
            self.spheres = {
				"generalSphere" : {"health" : 1, "relationship" : 1, "environment" : 1, "vocation" : 1, "independence" : 1, "self-development" : 1, "brightness of life" : 1, "self-realization" : 1, "spirituality" : 1},
				"healthSphere" : {"self-feeling" : 1, "appearance" : 1, "energy" : 1, "ration" : 1, "sport" : 1, "sleep" : 1},
				"relationshipSphere" : {"communication" : 1, "friends" : 1, "beloved" : 1, "family" : 1},
				"environmentSphere" : {"children" : 1, "relatives" : 1, "collegues" : 1, "friends" : 1, "neigbours" : 1, "acquaintances" : 1},
				"vocationSphere" : {"carier/business" : 1, "hobby" : 1},
				"independenceSphere" : {"incomes" : 1, "expences" : 1, "spending possibility" : 1},
				"selfdevelopmentSphere" : {"learning a new" : 1, "achievement of goals" : 1, "personal growth" : 1},
				"brightnessSphere" : {"refreshment" : 1, "travels" : 1, "impression" : 1},
				"spiritualitySphere" : {"outlook" : 1, "art" : 1, "meaning of life" : 1}
				}
            json.dump(self.spheres, open('./data/spheresOfLife.json', 'w'))

    def save(self):
        json.dump(self.spheres, open('./data/spheresOfLife.json', 'w'))
    
    def change_spheres(self, sphere_name, field_name, value):
        self.spheres[sphere_name][field_name] = value
        self.save()