import random

class MovementSt(object):
    def __init__(self):
        self.Situation = {'Motionsensor': rand(), 'Recording': rand()}

def rand():
    return random.randint(0, 1)

class ReflexAgent(MovementSt):

    def __init__(self, MovementSt):
        print("Movement:" + str(MovementSt.Situation))

        while True:
            Movement = rand()
            print("Movement: ", Movement)
            while Movement == 1:
                print("Motion detected.")
                if MovementSt.Situation['Motionsensor'] == 1 and MovementSt.Situation['Recording'] == 1:
                    print("Recording continues.")
                elif MovementSt.Situation['Motionsensor'] == 1 and MovementSt.Situation['Recording'] == 0:
                    print("Recording started.")
                elif MovementSt.Situation['Motionsensor'] == 0 and MovementSt.Situation['Recording'] == 1:
                    print("Motion detected and recording in progress.")
                elif MovementSt.Situation['Motionsensor'] == 0 and MovementSt.Situation['Recording'] == 0:
                    print("Motion detected and Recording started.")
                while True:
                    Movementt = rand()
                    while Movementt==1:
                        print("Movement: ", Movementt)
                        print("Motion continues. Recording continues.")
                        Movementt = rand()
                        break
                    while Movementt==0:
                        print("Movement: ", Movementt)
                        print("No motion at the moment. Recording stopped.")
                        break
                    if Movementt == 1:
                        continue
                    break
                break

            while Movement==0:
                if MovementSt.Situation['Motionsensor'] == 1 and MovementSt.Situation['Recording'] == 1:
                    print("No Motion right now.")
                    print("Recording stopped.")
                    break
                elif MovementSt.Situation['Motionsensor'] == 1 and MovementSt.Situation['Recording'] == 0:
                    print("No motion at the moment. Sensor is stopping.")
                    break
                elif MovementSt.Situation['Motionsensor'] == 0 and MovementSt.Situation['Recording'] == 1:
                    print("No motion at the moment. Recording stopped.")
                    break
                elif MovementSt.Situation['Motionsensor'] == 0 and MovementSt.Situation['Recording'] == 0:
                    print("No motion and no record.")
                    break
            break

env = MovementSt()
recording = ReflexAgent(env)