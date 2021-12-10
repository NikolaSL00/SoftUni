import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):

    def test_hero_initialization(self):
        hero = Hero('username 1', 10, 100, 75)
        self.assertEqual('username 1', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(100, hero.health)
        self.assertEqual(75, hero.damage)

    def test_should_return_proper_str(self):
        hero = Hero('username 1', 10, 100, 75)
        expected = f"Hero {hero.username}: {hero.level} lvl\n" \
                   f"Health: {hero.health}\n" \
                   f"Damage: {hero.damage}\n"
        actual = str(hero)

        self.assertEqual(expected, actual)

    def test_battle__when_hero_tries_to_battle_himself__expect_exception(self):
        hero = Hero('username 1', 10, 100, 75)
        with self.assertRaises(Exception) as context:
            hero.battle(hero)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_tries_to_battle_with_0_or_less_health__expect_exception(self):
        for health in [0, -25]:
            hero = Hero('username 1', 10, health, 75)
            enemy_hero = Hero('username 2', 10, 100, 75)
            with self.assertRaises(Exception) as context:
                hero.battle(enemy_hero)
            self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_tries_to_battle_with_enemy_hero_with_0_or_less_health__expect_exception(self):
        for health in [0, -25]:
            hero = Hero('username 1', 10, 100, 75)
            enemy_hero = Hero('username 2', 10, health, 75)
            with self.assertRaises(Exception) as context:
                hero.battle(enemy_hero)
            self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle_returns_draw_when_both_heroes_dies(self):
        hero = Hero('username 1', 10, 100, 50)
        enemy_hero = Hero('username 2', hero.level, hero.health, hero.damage)

        expected_health = hero.health - enemy_hero.level * enemy_hero.damage

        result = hero.battle(enemy_hero)

        expected_result = 'Draw'

        self.assertEqual(expected_result, result)
        self.assertEqual(expected_health, hero.health)
        self.assertEqual(expected_health, enemy_hero.health)

    def test_battle_when_enemy_is_dead_return_win(self):
        enemy_hero_level, enemy_hero_health, enemy_hero_damage = 1, 100, 75
        hero_level, hero_health, hero_damage = 10, 100, 75

        enemy_hero = Hero('username 1', enemy_hero_level, enemy_hero_health, enemy_hero_damage)
        hero = Hero('username 2', hero_level, hero_health, hero_damage)

        result = hero.battle(enemy_hero)
        expected_result = "You win"

        self.assertEqual(expected_result, result)
        self.assertEqual(hero_level + 1, hero.level)
        self.assertEqual(hero_health - enemy_hero_damage * enemy_hero_level + 5, hero.health)
        self.assertEqual(hero_damage + 5, hero.damage)

    def test_battle_when_enemy_win_return_lose(self):
        enemy_hero_level, enemy_hero_health, enemy_hero_damage = 10, 100, 75
        hero_level, hero_health, hero_damage = 1, 100, 75
        enemy_hero = Hero('username 1', enemy_hero_level, enemy_hero_health, enemy_hero_damage)
        hero = Hero('username 2', hero_level, hero_health, hero_damage)

        result = hero.battle(enemy_hero)
        expected_result = "You lose"

        self.assertEqual(expected_result, result)
        self.assertEqual(enemy_hero_level + 1, enemy_hero.level)
        self.assertEqual(enemy_hero_health - hero_damage * hero_level + 5, enemy_hero.health)
        self.assertEqual(enemy_hero_damage + 5, enemy_hero.damage)


if __name__ == '__main__':
    unittest.main()
