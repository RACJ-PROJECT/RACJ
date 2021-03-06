# RACJ
## R.A.C.J. (Robotic Arm Controlled By Joystick)</br></br>



### Elenco materiali:


- [ ] Motori:

 Nome          | Link
---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------
 LDX 227       | [Amazon](https://www.amazon.it/LewanSoul-LDX-227-Standard-Digital-Bearing/dp/B077TXLWZS )
 17HS19-2004S1 | [Amazon](https://www.amazon.it/NEMA-17HS19-2004S1-Motore-passo-passostampante/dp/B07P464BSX/ref=sr_1_2?dchild=1&keywords=17HS19-2004S1&qid=1610703387&sr=8-2)


- [ ] Driver:

Nome        | Link
------------|--------------------------------------------------------------------------------------------------------------------------------------------------
IIC-PCA9685 | [Amazon](https://www.amazon.it/ARCELI-Interfaccia-IIC-PCA9685-arduino-Raspberry/dp/B07RG9ZTMD/ref=asc_df_B07RG9ZTMD/?tag=googshopit-21&linkCode=df0&hvadid=459269273979&hvpos=&hvnetw=g&hvrand=17037251313190546924&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=20543&hvtargid=pla-926730742055&psc=1)
TB6600      | [Amazon](https://www.amazon.it/Scheda-controller-passo-passo-COVVY-segmenti/dp/B07SBZ9SM5/ref=sr_1_8?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=TB6600&qid=1610703473&s=industrial&sr=1-8)
Servo Driver HAT | [KUBII](https://www.kubii.it/schede-espansione-fotocamere-raspberry-pi/2750-servo-driver-hat-614961955844.html?search_query=sunfounder+55g+servo+driver+servo&results=158)



- [ ] Alimentatore:

Link: [Amazon](https://www.amazon.it/gp/product/B07TC2LFRL/ref=ox_sc_saved_title_5?smid=A6FTR3WNTF6EM&psc=1)
</br></br>



### Idee:
1. Sensori (giroscopio), rappresentazione vituale del braccio tramite un software.
2. Telacamera dietro la pinza per foto (A.I. per riconoscere oggetti).
3. A.I. per giocare a tris.
</br></br>



### Componenti braccio meccanico:
Le componenti vanno ridisegnate per permettere maggiore manovrabilità. </br>
- [link](https://www.thingiverse.com/thing:3327968)</br></br>
Materiale:
- Plastica (stampante 3D)
</br></br>



### Documentazione stampante 3D:
- [Link 1](https://www.prusa3d.it/prusaslicer/)</br>
- [Link 2](https://www.prusa3d.it/driver/)
</br></br>



### Software utile:
- Libreria controller PS4: [Link](https://pypi.org/project/pyPS4Controller/)
- ROS pagina ufficiale: [Link](https://www.ros.org/)
- ROS: [Link 1](https://www.instructables.com/Getting-Started-with-ROS-Robotic-Operating-Syste/)
- ROS: [Link 2](https://robohub.org/programming-for-robotics-introduction-to-ros/)
- ROS: [Link 3](https://github.com/ros/documentation/tree/master/rosdoc)
</br></br>



### Numero motori:

Durante la fase 1 per testare la pinza si può usare una calamita. </br></br>

- Gomito (limite: angolo)                             servo
- Spalla (limite: angolo)                             servo
- Ruotare tutto il braccio (no limiti)                step motor
- Aprire/Chiudere pinza. (limite: sensore pressione)  servo
- Ruotare la pinza. (no limiti)                       step motor
- Polso (limite: angolo)                              servo
</br></br></br>



### Fasi della progettazione
- [ ] Fase 1a: Progettazione componenti (ridisegnare);
- [ ] Fase 1b: Vedere funzionamento di R.O.S.;
- [ ] Fase 2a: Gestione movimenti dei motori;
- [ ] Fase 2b: Progettazione gestione joystick;


### Link drive con cartella dei progetti 
 [link](https://drive.google.com/drive/folders/1HjEIjqocrRrQA5hRc8pm9diKWBKX8TIF?usp=sharing)

