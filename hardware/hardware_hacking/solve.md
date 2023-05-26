# Hardware hacking

On sait que l'on travaille sur le processeur STM32WL55, on va dont chercher sa [documentation](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiKhLfz2JD_AhVHUKQEHQqeDTkQFnoECA4QAQ&url=https%3A%2F%2Fwww.st.com%2Fresource%2Fen%2Freference_manual%2Frm0453-stm32wl5x-advanced-armbased-32bit-mcus-with-subghz-radio-solution-stmicroelectronics.pdf&usg=AOvVaw2iPz075oOfNAFHu0jPiSVl)

Dans la section `Memory organisation`, on trouve que la configuration de l'USART 1 est entre les addresses 0x40013800 et  0x40013BFF

Dans la section USART, on trouve que le registre USART_BRR à l'offset 0x0C es responsable de la vitesse du lien 
