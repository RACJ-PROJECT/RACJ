import time
import pygame
import threading
from adafruit_servokit import ServoKit
 
# Set channels to the number of servo channels on your kit.
# 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
kit = ServoKit(channels=16)

NUM_MOTORS = 5

degree = []

MIN_ANGLE = 0
MAX_ANGLE = 180

DELAY = 0.005
DELAY_SETTAGGIO_MOTORE = 1

NUMERO_GRADI_SINGOLO_MOVIMENTO = 1
motore_altri = 1
gradi_motore_altri = 0

motore_base = 0
gradi_motore_base = 0

limitazioni_angoli = {0: [MIN_ANGLE, MAX_ANGLE], 1: [MIN_ANGLE, MAX_ANGLE], 2: [MIN_ANGLE, MAX_ANGLE], 3: [MIN_ANGLE, MAX_ANGLE], 4: [58, 108]}
tastiPremuti={'on_L3_down': False, 'on_L3_up': False, 'on_R3_right': False, 'on_R3_left': False}


def initMotors():
    for i in range(NUM_MOTORS):
        degree.append((limitazioni_angoli[i])[0])
        if(i != 1 and i != 2):
            kit.servo[i].angle = (limitazioni_angoli[i])[0]
        
        elif(i==1):
            motore_1 = threading.Thread(target=thread_function_motore1, args=(0,))
            motore_2 = threading.Thread(target=thread_function_motore2, args=(180,))
            motore_1.start()
            motore_2.start()
            motore_1.join()
            motore_2.join()
        print("Setaggio motore: "+str(i))
        time.sleep(DELAY_SETTAGGIO_MOTORE)


def thread_function_motore1(n_degree):
    kit.servo[1].angle = n_degree

def thread_function_motore2(n_degree):
    kit.servo[2].angle = n_degree



def runMotors():
    """
    This function send a string with the code of the motor to enable
    and the value of the rotation angle.
    """
    dati = getValori()
    
    controlDegree(dati[1], dati[0])
    controlDegree(dati[3], dati[2])
    kit.servo[dati[0]].angle = degree[dati[0]]
    kit.servo[dati[2]].angle = degree[dati[2]]

    if dati[2] == 1:
        motore_1 = threading.Thread(target=thread_function_motore1, args=(degree[dati[2]],))
        motore_2 = threading.Thread(target=thread_function_motore2, args=(MAX_ANGLE-degree[dati[2]],))
        motore_1.start()
        motore_2.start()
        motore_1.join()
        motore_2.join() 

def controlDegree(diff, i):
    if(degree[i]+diff>=(limitazioni_angoli[i])[0] and degree[i]+diff<=(limitazioni_angoli[i])[1]):
        degree[i] += diff

def control():
    """
    Questa funzione verifica se tutte le levette sono su "FERMO", in modo
    che se premo un pulsante per selezionare i motori verifico che non sia premuto
    anche altro
    """
    lista = list(tastiPremuti.values())
    result = False
    result = all(elem == lista[0] for elem in lista)
    return result

def getValori():
    """
    Questa funzione ritorna i valori dei motori e i gradi di rotazione
    """
    return [motore_base, gradi_motore_base, motore_altri, gradi_motore_altri]


def main():

    global motore_altri
    global gradi_motore_altri
    global motore_base
    global gradi_motore_base
    
    initMotors()

    #initializes pygame
    pygame.init()
    #creates a controller object
    controller = pygame.joystick.Joystick(0)
    #initializes the controller
    controller.init()

    try:
        while True:

            ######################################################################
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.JOYBUTTONDOWN:

                    if controller.get_button(0):
                        if(control()):
                            motore_altri = 1
                        print("X Pressed")
                        print("angolo "+str(degree[1]))

                    elif controller.get_button(2):
                        if(control()):
                            motore_altri = 4  
                        print("Triangle Pressed")
                        print("angolo "+str(degree[4]))

                    elif controller.get_button(3):
                        if(control()):
                            motore_altri = 3
                        print("Square Pressed")
                        print("angolo "+str(degree[3]))


                elif event.type == pygame.JOYBUTTONUP:
                    print("Button Released")

                elif event.type == pygame.JOYAXISMOTION:
                    #print(event.dict, event.joy, event.axis, event.value)

                    # GESTIONE LEVETTA DI SINISTRA

                    # GIU
                    if((event.dict['axis']==1 and int(event.dict['value'])==1) and (tastiPremuti['on_L3_down']==False and tastiPremuti['on_L3_up']==False)):
                        tastiPremuti['on_L3_down'] = True
                        print("on_L3_down")
                        gradi_motore_altri = -NUMERO_GRADI_SINGOLO_MOVIMENTO
                    
                    # SU
                    elif((event.dict['axis']==1 and int(event.dict['value'])==-1) and (tastiPremuti['on_L3_up']==False and tastiPremuti['on_L3_down']==False)):
                        tastiPremuti['on_L3_up'] = True
                        print("on_L3_up")
                        gradi_motore_altri = NUMERO_GRADI_SINGOLO_MOVIMENTO
                    
                    # FERMO
                    elif((event.dict['axis']==1 and int(event.dict['value'])==0) and (tastiPremuti['on_L3_down'] or tastiPremuti['on_L3_up'])):
                        tastiPremuti['on_L3_down'] = False
                        tastiPremuti['on_L3_up'] = False
                        print("on_L3_y_at_rest")
                        gradi_motore_altri = 0
                    
                    # GESTIONE LEVETTA DI DESTRA

                    # DESTRA
                    elif((event.dict['axis']==3 and int(event.dict['value'])==1) and (tastiPremuti['on_R3_right']==False and tastiPremuti['on_R3_left']==False)):
                        tastiPremuti['on_R3_right']=True
                        print('on_R3_right')
                        gradi_motore_base = 3

                    # SINISTRA
                    elif((event.dict['axis']==3 and int(event.dict['value'])==-1) and (tastiPremuti['on_R3_left']==False and tastiPremuti['on_R3_right']==False)):
                        tastiPremuti['on_R3_left']=True
                        print('on_R3_left')
                        gradi_motore_base = -3
                    
                    # FERMO
                    elif((event.dict['axis']==3 and int(event.dict['value'])==0) and (tastiPremuti['on_R3_right'] or tastiPremuti['on_R3_left'])):
                        tastiPremuti['on_R3_right'] = False
                        tastiPremuti['on_R3_left'] = False
                        print("on_R3_x_at_rest")
                        gradi_motore_base = 0

            ######################################################################

            runMotors()

            #time.sleep(DELAY)
    
    except KeyboardInterrupt:
        print('\nExit program.\n')
        controller.quit()
        pygame.quit()

if __name__ == '__main__':
    main()
 
