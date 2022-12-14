from hero import Hero, StAss, Oleksandr, Svettttikkkkk 
 
hero1 = StAss("StAss", 50, 25, 5, "USP") 
hero2 = Hero("Bogdan", 50, 50, 15, "Laser") 
hero3 = Oleksandr("Oleksandr", 50, 25, 23, "Winer") 
hero4 = Svettttikkkkk("Svettttikkkkk", 50, 15, 3, "Weapon") 
 
 
hero1.print_info() 
hero2.print_info() 
hero3.print_info() 
hero4.print_info() 
 
hero1.fight(hero2)  
hero3.fight(hero2) 
hero4.fight(hero3)