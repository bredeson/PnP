def combat(self, monster = None): 
	while monster.hp > 0:
		if self.hp <= 0:
			print('You have died to a',monster.name)
			break
		elif monster.hp > 0:
			combat_query=input('[attack], [risky] attack, or [magic]?\n')
			if combat_query == 'attack':
                                new_user_attack = random.randint(1,self.attack)
                                new_mon_attack = random.randint(1,monster.attack)
                                print(combatResponses.combatResponse_player(self.attack, new_user_attack),'You deal',new_user_attack, 'damage to', monster.name)
                                time.sleep(3)
                                monster.hp -= new_user_attack
                                if monster.hp > 0:
                                        print('The',monster.name, 'has', monster.hp, 'health remaining')
                                        time.sleep(3)
                                        self.hp -= new_mon_attack
                                        print(combatResponses.combatResponse_monster(monster.attack, new_mon_attack), monster.name, 'does', new_mon_attack, 'damage. You health is now', self.hp)
                                        time.sleep(3)
                                else:
                                        print('The', monster.name, 'is dead')
                                        break


			if combat_query == 'risky':
				chance = random.randint(1,20)
				min = 0.5*self.attack
				max = 2*self.attack
				new_user_attack = random.randint(min,max)
				if chance > 10:
					print('You hit for', new_user_attack, 'damage')
					monster.hp -= new_user_attack
					if monster.hp > 0:
						print('The',monster.name, 'has', monster.hp, 'health remaining')
						time.sleep(3)
						self.hp -= new_mon_attack
						print(combatResponses.combatResponse_monster(monster.attack, new_mon_attack), monster.name, 'does', new_mon_attack, 'damage. Your health is now', self.hp)
						time.sleep(3)
					else:
						print('The, monster.name, 'is dead')
						break
				else:
					print('You missed!')
					print(combatResponses.combatResponse_monster(monster.attack, new_mon_attack), monster.name, 'does', new_mon_attack, 'damage. Your health is now', self.hp)
					self.hp -= new_mon_attack



			if combat_query = 'magic':
				if self.mana > 0:
					new_user_attack = self.attack
					print('You do magic stuff for', new_user_attack,'damage')
					monster.hp -= new_user_attack
					self.mana -= 1
					print('You have',self.mana,'mana left')
					if monster.hp > 0:
						print('The',monster.name, 'has', monster.hp, 'health remaining')
						time.sleep(3)
						self.hp -=new_mon_attack
						print(combatResponses.combatResponse_monster(monster.attack, new_mon_attack), monster.name, 'does', new_mon_attack, 'damage. Your health is now', self.hp)
						time.sleep(3)
					else:
						print('The, monster.name, 'is dead')
						break
				else:
					print('You have no mana left!')
		else:
			break

