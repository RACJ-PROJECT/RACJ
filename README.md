# RACJ
## R.A.C.J. (Robotic Arm Controlled By Joystick)</br></br>



### Elenco materiali:


- [ ] Motori:

 Nome          | Link
---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------
 MG996R (servo motori)       | [Amazon](https://www.amazon.it/gp/product/B07DQJ1JXY/ref=ppx_yo_dt_b_asin_image_o02_s00?ie=UTF8&psc=1)


- [ ] Driver:

Nome        | Link
------------|--------------------------------------------------------------------------------------------------------------------------------------------------
IIC-PCA9685 (servo shield) | [Amazon](https://www.amazon.it/gp/product/B07RG9ZTMD/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)



- [ ] Alimentatore:

Creato noi utilizzando un vecchio alimentatore di un pc.
</br></br>



### Idee:
1. Sensori (giroscopio), rappresentazione vituale del braccio tramite un software.
2. Telacamera dietro la pinza per foto (A.I. per riconoscere oggetti).
3. A.I. per giocare a tris.
</br></br>



### Componenti braccio meccanico:
Componenti disegnate del braccio:</br>
- [link](https://drive.google.com/drive/folders/1HjEIjqocrRrQA5hRc8pm9diKWBKX8TIF?usp=sharing)</br></br>
Materiale:
- Alluminio (macchina a controllo numerico)
- Plastica (stampante 3D)
</br></br>



### Software utile:
- Libreria controller PS4: [Link](https://pypi.org/project/pyPS4Controller/)
- ROS pagina ufficiale: [Link](https://www.ros.org/)
- ROS: [Link 1](https://www.instructables.com/Getting-Started-with-ROS-Robotic-Operating-Syste/)
- ROS: [Link 2](https://robohub.org/programming-for-robotics-introduction-to-ros/)
- ROS: [Link 3](https://github.com/ros/documentation/tree/master/rosdoc)
</br></br>



### Numero motori:

</br>

- Gomito (limite: angolo)                             servo
- Spalla (limite: angolo)                             servo
- Ruotare tutto il braccio                            servo
- Aprire/Chiudere pinza. (limite: sensore pressione)  servo
- Ruotare la pinza. (no limiti)                       step motor
- Polso (limite: angolo)                              servo
</br></br></br>



### Fasi della progettazione
- [ ] Fase 1a: Progettazione componenti (ridisegnare);
- [ ] Fase 1b: Vedere funzionamento servo shield;
- [ ] Fase 2a: Gestione movimenti dei motori;
- [ ] Fase 2b: Progettazione gestione joystick;
