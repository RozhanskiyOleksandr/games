from time import sleep 
 
class Hero(): 
    def __init__(self, name, health, armor, demage, weapon): 
        self.name = name 
        self.health = health 
        self.armor = armor 
        self.demage = demage 
        self.weapon = weapon 
 
    def attack(self, enemy): 
        print("Attack!! ", self.name, "attack", enemy.name) 
        sleep(2) 
        print("Hit!") 
        sleep(2) 
        enemy.armor = enemy.armor - self.demage 
        if enemy.armor < 0: 
            enemy.health = enemy.health + enemy.armor 
            enemy.armor = 0 
        print(enemy.name, "armor is", enemy.armor, "and", enemy.health) 
        sleep(2) 
 
    def print_info(self): 
        print("New hero", self.name) 
        sleep(2) 
        print("Health", self.health) 
        sleep(2) 
        print("Armor", self.armor) 
        sleep(2) 
        print("Weapon", self.weapon) 
        sleep(2) 
 
    def fight(self, enemy): 
        while self.health >= 0 or enemy.health >= 0: 
            if enemy.health <= 0: 
                print(enemy.name, "felt in battle") 
                sleep(2) 
                break 
            if self.health <= 0: 
                print(self.name, "felt in battle") 
                sleep(2) 
                break 
            if enemy.health >= 0: 
                self.attack(enemy) 
            if self.health >= 0: 
                enemy.attack(self) 
         
class StAss(Hero): 
    def __init__(self, name, health, armor, demage, weapon): 
        super().__init__(name, health, armor, demage, weapon) 
 
    def print_info(self): 
        print("З лісу вибігає дикий герой StAss") 
        sleep(2) 
        print("StAss health is", self.health, "and armor is ", self.armor) 
        sleep(2) 
        print("Він поки біг впав і загубив свою зброю") 
        sleep(2) 
         
class Oleksandr(Hero): 
    def __init__(self, name, health, armor, demage, weapon): 
        super().__init__(name, health, armor, demage, weapon) 
         
    def print_info(self): 
        print('Oleksandr:Мій дідусь воювавн на 2 світовій, і мені передались його сили.') 
        sleep(2) 
        print("Oleksandr:Мені потрібно всіх вбити.", self.health, "and armor is ", self.armor) 
        sleep(2) 
        print("Oleksandr:Мені потрібна допомога!")
        sleep(2) 
         
class Svettttikkkkk(Hero): 
    def __init__(self, name, health, armor, demage, weapon): 
        super().__init__(name, health, armor, demage, weapon) 
         
    def attack(self, enemy): 
        print("Oleksandr:Доможи!!", self.name, "health", enemy.name) 
        sleep(2) 
        print("Oleksandr:Аптечку!") 
        sleep(2) 
        enemy.armor = enemy.armor - self.health 
        if enemy.armor < 0: 
            enemy.health = enemy.health + enemy.armor 
            enemy.armor = 0 
        print(enemy.name, "armor is", enemy.armor, "and", enemy.health) 
        sleep(2) 
         
    def fight(self, enemy): 
        while self.health >= 0 or enemy.health >= 0: 
            if enemy.health <= 0: 
                print(enemy.name, "not cured, Game Over!") 
                sleep(2) 
                break 
            if self.health <= 0: 
                print(self.name, "Cured") 
                sleep(2) 
                break 
            if enemy.health >= 0: 
                self.attack(enemy) 
            if self.health >= 0: 
                enemy.attack(self) 
         
    def print_info(self): 
        print('Svettttikkkkk:Я знала твого діда ти справжній монстр!') 
        sleep(2)  
        print("Oleksandr attack is", self.demage, "and armor is ", self.armor) 
        sleep(2) 
        print("Svettttikkkkk:Я тебе врятую!") 
        sleep(2)