# RACJ
## R.A.C.J. (Robotic Arm Controlled By Joystick)</br></br>



### Elenco materiali:



 Motori          | Link
---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------
 MG996R (servo motori)       | [Amazon](https://www.amazon.it/gp/product/B07DQJ1JXY/ref=ppx_yo_dt_b_asin_image_o02_s00?ie=UTF8&psc=1)



Driver        | Link
------------|--------------------------------------------------------------------------------------------------------------------------------------------------
IIC-PCA9685 (servo shield) | [Amazon](https://www.amazon.it/gp/product/B07RG9ZTMD/ref=ppx_yo_dt_b_asin_title_o04_s00?ie=UTF8&psc=1)



Alimentatore    | Link 
------------|--------------------------------------------------------------------------------------------------------------------------------------------------
Creato noi utilizzando un vecchio alimentatore di un pc | /

### Idee:
1. Sensori (giroscopio), rappresentazione vituale del braccio tramite un software.
2. Telacamera dietro la pinza per foto (A.I. per riconoscere oggetti).
3. A.I. per giocare a tris.
</br></br>



### Componenti braccio meccanico:
Componenti disegnate del braccio: [link](https://drive.google.com/drive/folders/1HjEIjqocrRrQA5hRc8pm9diKWBKX8TIF?usp=sharing)</br></br>
Materiale:
- Alluminio (macchina a controllo numerico)
- Plastica (stampante 3D)
</br></br>



### Software utile:
- Libreria controller PS4: [Link](https://www.pygame.org/project/5129/7487)
- Libreria servo shield: [Link](https://learn.adafruit.com/16-channel-pwm-servo-driver?view=all)
</br></br>



### Numero motori:
- Spalla (2 motori)                                   servo
- Ruotare tutto il braccio (1 motore)                 servo
- Aprire/Chiudere pinza. (1 motore)                   servo
- Ruotare la pinza. (1 motore)                        servo
</br></br></br>



### Fasi della progettazione
- [ ] Fase 1a: Progettazione componenti (ridisegnare);
- [ ] Fase 1b: Vedere funzionamento servo shield;
- [ ] Fase 2a: Gestione movimenti dei motori;
- [ ] Fase 2b: Progettazione gestione joystick;
