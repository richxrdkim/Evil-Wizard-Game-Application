import random

# Base Character Class


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health
        self.block_next = False  # For abilities like Paladin's shield or Archer's evade

    def attack(self, opponent):
        # Randomized damage ±5
        damage = random.randint(self.attack_power - 5, self.attack_power + 5)
        if opponent.block_next:
            print(f"{opponent.name} blocks the attack!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} attacks {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 10
        self.health += heal_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} heals for {heal_amount} health! Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior Class

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)

    def power_attack(self, opponent):
        damage = self.attack_power * 2
        if opponent.block_next:
            print(f"{opponent.name} blocks the POWER ATTACK!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} performs a POWER ATTACK for {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")

    def battle_cry(self):
        boost = 5
        self.attack_power += boost
        print(f"{self.name} shouts a battle cry! Attack Power increased by {boost} for the rest of the fight.")


# Mage Class

class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def cast_spell(self, opponent):
        damage = self.attack_power + 15
        if opponent.block_next:
            print(f"{opponent.name} resists the spell!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} casts a devastating spell for {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")

    def mana_shield(self):
        self.block_next = True
        print(
            f"{self.name} conjures a magical barrier! The next attack will be blocked.")


# Archer Class

class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=20)

    def quick_shot(self, opponent):
        total_damage = self.attack_power * 2
        if opponent.block_next:
            print(f"{opponent.name} evades the first arrow but is hit by the second!")
            opponent.health -= self.attack_power
        else:
            opponent.health -= total_damage
        print(f"{self.name} fires two quick arrows for {total_damage} total damage!")
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.name} has been defeated!")

    def evade(self):
        self.block_next = True
        print(f"{self.name} prepares to evade the next attack!")


# Paladin Class

class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=160, attack_power=20)

    def holy_strike(self, opponent):
        damage = self.attack_power + 10
        if opponent.block_next:
            print(f"{opponent.name} blocks the holy strike!")
            opponent.block_next = False
        else:
            opponent.health -= damage
            print(f"{self.name} smites {opponent.name} for {damage} damage!")
            if opponent.health <= 0:
                opponent.health = 0
                print(f"{opponent.name} has been defeated!")

    def divine_shield(self):
        self.block_next = True
        print(f"{self.name} raises a divine shield! The next attack will be blocked.")


# Evil Wizard Class

class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        regen_amount = 5
        self.health += regen_amount
        if self.health > self.max_health:
            self.health = self.max_health
        print(f"{self.name} regenerates {regen_amount} health! Current health: {self.health}/{self.max_health}")


# Character Creation

def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name = input("Enter your character's name: ")

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


# Battle Function

def battle(player, wizard):
    while wizard.health > 0 and player.health > 0:
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Use Special Ability 1")
        print("3. Use Special Ability 2")
        print("4. Heal")
        print("5. View Stats")

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(wizard)
        elif choice == '2':
            if isinstance(player, Warrior):
                player.power_attack(wizard)
            elif isinstance(player, Mage):
                player.cast_spell(wizard)
            elif isinstance(player, Archer):
                player.quick_shot(wizard)
            elif isinstance(player, Paladin):
                player.holy_strike(wizard)
        elif choice == '3':
            if isinstance(player, Warrior):
                player.battle_cry()
            elif isinstance(player, Mage):
                player.mana_shield()
            elif isinstance(player, Archer):
                player.evade()
            elif isinstance(player, Paladin):
                player.divine_shield()
        elif choice == '4':
            player.heal()
        elif choice == '5':
            player.display_stats()
            wizard.display_stats()
        else:
            print("Invalid choice. Try again.")
            continue

        # Wizard's turn
        if wizard.health > 0:
            wizard.regenerate()
            wizard.attack(player)

        # Check defeat
        if player.health <= 0:
            player.health = 0
            print(f"{player.name} has been defeated!")
            break

    # Victory
    if wizard.health <= 0:
        print(
            f"\n🎉 Victory! The wizard {wizard.name} has been defeated by {player.name}! 🎉")


# Main Game

def main():
    player = create_character()
    wizard = EvilWizard("The Dark Wizard")
    battle(player, wizard)


if __name__ == "__main__":
    main()
